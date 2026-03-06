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


