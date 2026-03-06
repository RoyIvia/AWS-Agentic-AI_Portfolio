# 00 – Create Product Recommendation Agent

In this section, we create the **foundation of the AI shopping assistant** using Amazon Bedrock Agents.

The agent is responsible for:
- interacting with users
- asking clarifying questions
- retrieving product recommendations
- orchestrating backend APIs

This step establishes the **core reasoning engine** of the application.

---

# Objective

The objective of this module is to:

- Create an Amazon Bedrock Agent
- Configure the agent instructions
- Connect the agent to backend APIs
- Enable product discovery functionality

---

# Infrastructure Required

The following AWS resources are required:

| Resource | Purpose |
|--------|--------|
| Amazon Bedrock | Hosts the AI Agent |
| AWS Lambda | Executes API business logic |
| Amazon DynamoDB | Stores product catalog |
| AWS CloudFormation | Deploys backend infrastructure |
| IAM Roles | Grants permissions to the agent |

---

# Implementation Steps

## Step 1 – Deploy Backend Infrastructure

The backend services are deployed using **AWS CloudFormation** which creates:

- DynamoDB product tables
- Lambda functions
- API endpoints
- IAM roles

Deployment takes approximately **5–10 minutes**.

---

## Step 2 – Create the Bedrock Agent

Navigate to:

AWS Console → Amazon Bedrock → Agents → Create Agent

Configure the following:

Agent Name  
ProductRecommendationAgent

Foundation Model  
Claude / Amazon Titan (depending on workshop configuration)

---

## Step 3 – Configure Agent Instructions

Provide instructions that guide how the agent interacts with users.

Example instruction:

You are a helpful e-commerce assistant.
Ask questions to understand the user's needs and recommend suitable products.
Use the available APIs to retrieve products when enough information is gathered.



---

## Step 4 – Configure Action Group

The agent requires **actions** to interact with backend services.

Actions allow the agent to call APIs via Lambda functions.

Configured action:

Product Recommendation API

---

# Agent Configuration

The agent is configured with:

- Natural language instructions
- API integration via Lambda
- structured response generation

This allows the agent to translate **user intent into API calls**.

---

# Testing the Agent

Once deployed, the agent can be tested using the **Bedrock Agent Test Console**.

Example conversation:

User:

> I'm looking for a birthday gift for my sister.

Agent:

- asks clarifying questions
- identifies product category
- retrieves recommendations

---

# Key Takeaways

- Amazon Bedrock Agents can orchestrate backend services
- Natural language instructions define agent behavior
- APIs extend the capabilities of AI agents

