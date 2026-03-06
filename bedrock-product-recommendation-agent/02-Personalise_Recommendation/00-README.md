# Personalized Recommendations – Integrating Product Personalization

This section documents the integration of **personalized product recommendations** into the Product Recommendation Agent using **Amazon Bedrock Agents and a recommendation API powered by AWS Lambda**.

After enabling users to add products to a cart, the next enhancement was to introduce **recommendations based on user behavior and purchase patterns**. This functionality simulates the behavior of recommendation systems used by modern e-commerce platforms.

The agent is now able to suggest **additional products that other customers commonly purchase together** with items the user has already added to their cart.

This stage builds upon the previous architecture by introducing a **Personalization API** that the Bedrock Agent can invoke before confirming cart additions.

The implementation follows the AWS workshop:

https://catalog.workshops.aws/e-commerce-in-a-bot/en-US/getting-started

However, this documentation reflects **my own implementation and testing process within my AWS environment**.

---

# Architecture Overview

With the addition of personalized recommendations, the architecture now includes an additional API interaction before completing the cart addition process.

The updated interaction flow becomes:

User  
↓  
Amazon Bedrock Agent  
↓  
Action Group (Recommendation API)  
↓  
AWS Lambda  
↓  
Recommendation Engine Logic  

The agent retrieves recommendations **based on products already selected by the user**.

These recommendations are presented as **“customers who bought this item also bought…”** suggestions.

---

# Infrastructure Components Used

The personalized recommendation functionality relies on backend resources that were already provisioned through the initial CloudFormation deployment.

---

## AWS Lambda

### GetPersonalizeRecommendationFunction

This Lambda function generates product recommendations related to a specific product.

The function simulates a **product co-purchase recommendation model**, returning items that are commonly bought alongside the selected product.

The agent calls this function **before confirming a cart addition**, allowing it to suggest complementary products to the user.

---

## API Gateway

API Gateway exposes the endpoint that allows the Bedrock Agent to invoke the **GetPersonalizeRecommendationFunction**.

This ensures the AI agent can retrieve recommendations dynamically through an **Action Group integration**.

---

# Updating the Agent Instructions

To enable this capability, the **Agent Instruction Prompt** was updated so that the agent retrieves personalized recommendations before finalizing a cart addition.

The instructions guide the agent to:

1. Detect when a user wants to add a product to their cart  
2. Retrieve related product recommendations using the personalization API  
3. Suggest these products to the user before confirming the cart addition  

Instruction snippet added to the agent configuration:

```
before item addition to the cart, use the get personalize recommendation API to get products other customer has bought based on the product that you just added to the cart.

recommend that to the user by telling them that other customers also bought this along with the product that you just added and ask if they want to also add it to the cart as well.
```

This prompt ensures that the agent consistently performs a **recommendation check** before confirming cart updates.

---

# Configuring the Personalization Action Group

To allow the Bedrock Agent to call the personalization API, I configured an **Action Group** connected to the recommendation Lambda function.

Steps performed:

1. Open **Amazon Bedrock → Agents**
2. Select the **ProductRecommendationAgent**
3. Navigate to **Agent Builder**
4. Open the **Action Groups section**
5. Add the recommendation API integration

The action group configuration included:

- Selecting the **GetPersonalizeRecommendationFunction**
- Uploading the API schema that defines the endpoint
- Mapping request parameters such as:
  - productId
  - userId

Once configured, the agent could automatically trigger the recommendation API during conversation flow.

---

# Testing the Personalization Workflow

After updating the instructions and configuring the action group, I prepared the agent and tested the new functionality using the **Bedrock Agent testing interface**.

Example interaction:

User:

```
Add the luxury perfume to my cart
```

Agent workflow:

1. Detect intent to add the product to the cart  
2. Call the **GetPersonalizeRecommendation API**  
3. Retrieve related product suggestions  
4. Present these recommendations to the user  

Example agent response:

```
Other customers who purchased this item also bought:

- Scented Candle
- Luxury Gift Box

Would you like to add any of these to your cart as well?
```

If the user agrees, the agent proceeds to call the **AddToCart API**.

---

# Observing Agent Decision Logic

Using the **Show trace** feature in the Bedrock testing interface allows inspection of the agent’s reasoning process.

The trace reveals:

- How the agent interprets the user's intent
- The decision to call the personalization API
- The parameters passed to the Lambda function
- The recommended products returned by the backend service

This trace provides useful insight into how **agent reasoning combines user input with backend services** to generate contextual recommendations.

---

# Outcome

At the end of this stage, the Product Recommendation Agent was enhanced with **personalized recommendation capabilities**.

Key outcomes include:

- Integration of a product recommendation API with the Bedrock Agent
- Dynamic suggestions of complementary products
- Improved conversational shopping experience
- Simulation of a recommendation system similar to those used in modern e-commerce platforms

This stage moves the system closer to a **fully intelligent shopping assistant**, capable of not only recommending products but also suggesting **contextually relevant add-on items**.
