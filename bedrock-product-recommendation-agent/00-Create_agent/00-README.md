# Product Recommendation Agent – Initial Setup


This section documents the **initial creation of the Product Recommendation Agent** using **Amazon Bedrock Agents** as part of my **AWS Agentic AI Portfolio**.

The objective of this stage was to build the **core AI agent** capable of recommending gift products through a conversational interface.

The agent gathers information from the user such as:

- Gender of the gift recipient
- Occasion
- Product category

Using these inputs, the agent retrieves relevant products through an **API backed by AWS Lambda and DynamoDB**.

At this stage, the system establishes the **foundation architecture** that will later be expanded with:

- Cart management
- Personalized recommendations
- Retrieval-Augmented Generation (RAG) using a knowledge base
- Multi-agent collaboration

This implementation follows the AWS workshop:

https://catalog.workshops.aws/e-commerce-in-a-bot/en-US/getting-started

However, the documentation here reflects **my own implementation and deployment process in my AWS environment**.

---

# Architecture Overview

The base system architecture created in this stage consists of the following AWS services:

- **Amazon Bedrock Agents**
- **AWS Lambda**
- **Amazon DynamoDB**
- **Amazon API Gateway**
- **AWS CloudFormation**

The agent interacts with backend APIs to retrieve product data.

```
User
 ↓
Amazon Bedrock Agent
 ↓
Action Group (Products API)
 ↓
AWS Lambda
 ↓
DynamoDB Product Table
```

This architecture allows the AI agent to remain **stateless and lightweight**, while the backend infrastructure handles data retrieval and business logic.

---

# Infrastructure Provisioning

The backend infrastructure required for the agent was provisioned using **AWS CloudFormation**.

Using CloudFormation allowed the environment to be deployed in a **reproducible and automated way**, ensuring all required services were created consistently.

---

# Deploying the Infrastructure

To replicate this environment in my own AWS account, I deployed the CloudFormation stack provided in the workshop.

## Step 1 — Open CloudFormation

Navigate to:

```
AWS Console → CloudFormation
```

Select:

```
Create Stack
```

Then choose:

```
With new resources (standard)
```

---

## Step 2 — Upload the Template

Upload the CloudFormation template provided by the workshop.

This template provisions all the backend resources required by the AI agent.

Once the template is uploaded, proceed with the stack creation.

---

# Resources Created by CloudFormation

The CloudFormation stack provisions the following infrastructure components.

---

## DynamoDB Tables

### Product Table

Stores the product catalog used by the agent to recommend items.

Attributes include:

- Product name
- Description
- Category
- Gender
- Occasion

### Cart Table

Stores cart information associated with each user session.

This table will be used later when implementing cart functionality.

---

## Lambda Functions

The stack deploys several Lambda functions that serve as the backend APIs for the agent.

| Function | Purpose |
|--------|--------|
| GetProductsFunction | Retrieves product catalog data |
| AddToCartFunction | Adds items to a user cart |
| GetCartFunction | Retrieves cart contents |
| GetPersonalizeRecommendationFunction | Simulates Amazon Personalize recommendations |

At this stage, the agent primarily interacts with **GetProductsFunction**.

---

## API Gateway

API Gateway exposes endpoints that allow the **Bedrock Agent Action Groups** to call the Lambda functions.

This creates a **secure integration layer** between the AI agent and the backend services.

---

# Creating the Amazon Bedrock Agent

After the infrastructure was deployed, I created the conversational agent using **Amazon Bedrock Agents**.

Navigate to:

```
AWS Console → Amazon Bedrock
```

Open:

```
Agents
```

Select:

```
Create Agent
```

---

# Agent Configuration

The agent was configured with the following parameters.

| Setting | Value |
|------|------|
| Agent Name | ProductRecommendationAgent |
| Foundation Model | Claude Sonnet |
| Agent Type | Conversational AI Agent |
| Action Groups | Product API |

The selected model (**Claude Sonnet**) was chosen due to its strong reasoning capabilities and suitability for conversational applications.


<img width="810" height="715" alt="image" src="https://github.com/user-attachments/assets/51c36ce0-8f84-4c3a-9a1e-d396a1f36fa5" />


---

# Agent Instruction Prompt

The agent’s reasoning behavior was defined using the following instruction prompt.

```
you are a product recommendations agent for gift products, the user is trying to buy a gift for someone and you are trying to help identify the best products based on the filters in the action groups, ask questions to identify at least one of the input filters, gender, category or occasion.
do not recommend any products that are not retrieved from the products API.
do not ask about the gender if it is obvious from the user input already.
Always start by getting the full list of products from the API so you can know the proper filter values to be used in the API parameters.
always use a single value for each filter field, and adhere to the filtration values based on the first API call.
And never tell the user about the API and its details.
```

These instructions guide how the agent interacts with users and determines which API calls to trigger.

---

# Action Group Configuration

To allow the agent to retrieve products dynamically, I configured an **Action Group** connected to the product API.

The action group enables the agent to invoke backend Lambda functions using a defined **OpenAPI schema**.

Key configuration steps included:

- Selecting the Lambda function responsible for retrieving products
- Defining the API schema
- Mapping parameters between the agent and the API

This integration enables the agent to fetch real product data instead of generating generic responses.

---

# Testing the Agent

Once the agent configuration was completed, the agent was **prepared and tested using the Bedrock testing interface**.

Example interaction:

User input:

```
I need a birthday gift
```

Agent workflow:

1. Identify the occasion as **birthday**
2. Retrieve available products from the API
3. Apply the appropriate filter
4. Recommend matching products

The agent was able to successfully retrieve and present product recommendations.

---



This folder contains screenshots documenting the implementation process, including:

- Agent creation interface
- Agent instruction configuration
- Action group setup
- Test conversations with the agent

These screenshots illustrate the exact configuration steps taken during deployment.

---

# Outcome

At the end of this stage, the following components were successfully implemented:

- Amazon Bedrock Agent deployed
- Product catalog backend provisioned
- API integration between Bedrock and Lambda
- Conversational product recommendations

This stage establishes the **core AI agent framework** that subsequent stages build upon.

---

# Next Stage

The next phase introduces **shopping cart functionality**, allowing the agent to:

- Add items to a cart
- Retrieve cart contents
- Track user sessions using email as an identifier

See the next section:

```
01-Update_cart
```

---

# Author

**Roy Ivia**


