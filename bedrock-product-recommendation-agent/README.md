# Bedrock Product Recommendation Agent

This project demonstrates how to build an **AI-powered product recommendation chatbot using Amazon Bedrock Agents**. The chatbot interacts with users, understands their shopping needs, and recommends products by calling backend APIs and accessing structured knowledge.

The system uses a **serverless architecture** combining Amazon Bedrock, AWS Lambda, DynamoDB, Amazon S3, and Knowledge Bases to create an intelligent multi-agent e-commerce assistant.

This project is part of my **AWS Agentic AI Portfolio**, where I explore how AI agents can orchestrate cloud services to perform complex tasks.

---

# Project Architecture

The application follows a **serverless AI agent architecture**.


<img width="895" height="298" alt="Product_Reccomendation_Architecture" src="https://github.com/user-attachments/assets/6bb0e915-2ac4-4794-8d52-4ff893a1d2dd" />

Core flow:

1. User interacts with the chatbot.
2. **Amazon Bedrock Agent** interprets the request.
3. The agent decides whether to:
   - Call an **API via AWS Lambda**
   - Query a **Knowledge Base**
4. Lambda retrieves or updates data in **DynamoDB**.
5. The agent returns a contextual response to the user.

---

# Architecture Components

### Amazon Bedrock Agents
Acts as the **AI reasoning layer** that decides which tools or APIs to call based on the conversation.

### AWS Lambda
Executes backend business logic such as:
- retrieving products
- updating carts
- processing requests

### Amazon DynamoDB
Stores structured data including:

- product catalog
- cart information
- recommendation data

### Amazon S3
Stores unstructured files used for knowledge retrieval.

### Knowledge Bases for Amazon Bedrock
Provides contextual information such as **gift wrapping policies**.

---

# Features Implemented

This project progressively builds a full AI shopping assistant.

| Feature | Description |
|------|------|
| Product discovery | AI agent retrieves products from DynamoDB |
| Cart management | Users can add and update items in cart |
| Personalized recommendations | Uses Amazon Personalize |
| Knowledge-based responses | Gift wrapping policies via Bedrock Knowledge Base |
| Multi-agent collaboration | Multiple agents coordinate tasks |

---
```
# Project Structure

AWS-Agentic-AI_Portfolio
│
└── bedrock-product-recommendation-agent
│
├── 00-Create_agent
│ └── README.md
│
├── 01-Update_cart
│ └── README.md
│
├── 02-Personalise_Recommendation
│ └── README.md
│
├── 03-Gift-Wrapping_Knowledge-base
│ └── README.md
│
├── 04-Multi-Agent_Collaboration
│ └── README.md
│
└── README.md
```

Each module documents the **step-by-step implementation** and the infrastructure used.

---

# Infrastructure Deployment

The workshop infrastructure is deployed using **AWS CloudFormation**.

Resources created include:

- DynamoDB product tables
- API endpoints
- Lambda functions
- supporting IAM roles

Deployment takes approximately **5–10 minutes**.

---

# Technologies Used

- Amazon Bedrock Agents
- AWS Lambda
- Amazon DynamoDB
- Amazon S3
- Knowledge Bases for Bedrock
- Amazon Personalize
- AWS CloudFormation

---

# Skills Demonstrated

This project demonstrates practical experience with:

- AI Agents on AWS
- Serverless architecture
- API orchestration with AI
- Knowledge-based AI responses
- Multi-agent systems
- AI-driven product recommendation systems

---

# Example Interaction

User:

> I'm looking for a gift for my sister's birthday.

Agent:

1. Asks clarifying questions
2. Identifies product category
3. Calls product API
4. Returns recommended items

---

# Learning Objectives

Through this project I explored:

- Designing **AI agents that interact with cloud services**
- Integrating **LLMs with APIs**
- Building **multi-agent AI systems**
- Combining **structured and unstructured data retrieval**

---

# Workshop Reference

Implementation is based on the AWS workshop:

https://catalog.workshops.aws/e-commerce-in-a-bot/en-US/getting-started

---

# Author

**Roy Ivia**
Cloud & DevOps Engineer  
AWS | Kubernetes | AI Agents
