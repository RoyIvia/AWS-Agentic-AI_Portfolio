# Cart Management – Updating the Agent with Cart Functionality

This section documents the implementation of **cart management functionality** for the Product Recommendation Agent using **Amazon Bedrock Agents and AWS Lambda APIs**.

After the initial agent was able to recommend products, the next step was to allow users to **add items to a shopping cart and retrieve cart contents during the conversation**.

This stage extends the agent's capabilities from **product discovery** to **basic e-commerce interaction**, allowing users to manage items they intend to purchase.

The implementation leverages backend APIs that were provisioned earlier through **AWS CloudFormation**, specifically Lambda functions and DynamoDB tables responsible for cart storage.

This documentation reflects **the steps I performed in my AWS environment** while integrating cart actions into the Bedrock agent.

---

# Architecture Overview

The cart functionality introduces additional interactions between the Bedrock Agent and backend APIs.

The updated architecture flow becomes:

User  
↓  
Amazon Bedrock Agent  
↓  
Action Group (Cart API)  
↓  
AWS Lambda  
↓  
DynamoDB Cart Table  

The **Cart Table in DynamoDB** stores items associated with each user session.

The agent interacts with two backend APIs:

- **AddToCartFunction**
- **GetCartFunction**

These APIs allow the agent to persist and retrieve cart data during the conversation.

---

# Infrastructure Components Used

The cart functionality relies on infrastructure already deployed during the CloudFormation setup.

## DynamoDB

### Cart Table

Stores cart items associated with each user.

Example attributes include:

- userId
- productId
- productName
- quantity

This table enables the agent to maintain cart state across multiple interactions.

---

## AWS Lambda Functions

The following Lambda functions were used during this stage.

| Function | Purpose |
|--------|--------|
| AddToCartFunction | Adds a selected product to the user's cart |
| GetCartFunction | Retrieves all items currently in the cart |

These Lambda functions serve as backend APIs that the Bedrock Agent can invoke.

---

## API Gateway

API Gateway exposes HTTP endpoints that connect the Bedrock Agent’s **Action Groups** to the Lambda functions.

This creates a secure integration layer between the AI agent and backend services.

---

# Updating the Agent Instructions

To enable cart interactions, I updated the **Agent Instruction Prompt** in the Bedrock Agent configuration.

The updated instructions guide the agent to:

1. Ask the user whether they want to add recommended products to their cart
2. Collect the user’s email to use as a **user ID**
3. Call the **AddToCart API**
4. Retrieve cart contents using the **GetCart API**
5. Display cart items back to the user

Updated instruction snippet:

```
After recommending products ask the user if they want to add any products to the cart,
then use the add to cart API to add it.

Ask the user about his email and use it as user id and use it along the whole conversation
and in any cart API calls.

Reply to the user with the user id after first cart addition to be used in later additions.

After adding an item to the cart, retrieve the cart items from the get cart API
and display it to the user.

The user can ask about the items in the cart at any time,
use the get cart api to answer that.
```

These instructions ensure that the agent consistently follows the correct workflow when handling cart actions.

---

# Configuring the Cart Action Group

To allow the agent to interact with the cart APIs, I configured an **Action Group** within the Bedrock Agent.

The action group connects the agent to the Lambda functions through an **OpenAPI schema**.

Steps performed:

1. Open the **Agent Builder** in Amazon Bedrock
2. Navigate to **Action Groups**
3. Create or update the existing Action Group
4. Attach the Lambda functions:
   - AddToCartFunction
   - GetCartFunction
5. Upload or configure the **API schema**
6. Map request parameters such as:
   - userId
   - productId
   - quantity

Once configured, the agent can invoke these APIs automatically when the conversation requires cart actions.

---

# Testing the Cart Workflow

After updating the instructions and action group configuration, I prepared the agent and tested the functionality using the **Bedrock testing interface**.

Example interaction:

User:

```
I need a birthday gift for my sister
```

Agent:

Recommends products retrieved from the product API.

User:

```
Add the perfume to the cart
```

Agent workflow:

1. Requests the user’s email
2. Uses the email as the **user ID**
3. Calls the **AddToCart API**
4. Confirms the addition
5. Calls the **GetCart API**
6. Displays the updated cart contents

Example response:

```
The item has been added to your cart.

Current cart items:
- Luxury Perfume
```

This confirms that the agent successfully executed backend API calls and maintained cart state.

---

# Observing Agent Behavior

Using the **Show trace** feature in the Bedrock testing interface made it possible to observe how the agent determines when to call the cart APIs.

The trace shows:

- The reasoning behind the decision to add an item to the cart
- The parameters passed to the AddToCart API
- The retrieval of cart items using the GetCart API

This visibility is useful when debugging or validating the agent’s reasoning and action execution.

---

# Outcome

At the end of this stage, the Product Recommendation Agent was successfully extended with cart functionality.

Key outcomes include:

- Integration of cart APIs with the Bedrock Agent
- Ability for users to add recommended products to a cart
- Retrieval and display of cart contents during conversation
- Persistent cart storage using DynamoDB

This stage transforms the system from a **simple recommendation agent** into a more interactive **shopping assistant capable of managing user selections**.
