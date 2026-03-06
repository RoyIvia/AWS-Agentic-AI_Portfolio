# Bedrock Product Recommendation Agent

This project demonstrates how to build an **AI-powered product recommendation chatbot using Amazon Bedrock Agents**. The chatbot interacts with users, understands their shopping needs, and recommends products by calling backend APIs and accessing structured knowledge.

The system uses a **serverless architecture** combining Amazon Bedrock, AWS Lambda, DynamoDB, Amazon S3, and Knowledge Bases to create an intelligent multi-agent e-commerce assistant.

This project is part of my **AWS Agentic AI Portfolio**, where I explore how AI agents can orchestrate cloud services to perform complex tasks.

---

# Project Architecture

The application follows a **serverless AI agent architecture**.

User → Amazon Bedrock Agent → Lambda Functions → DynamoDB  
                                          ↓  
                             Knowledge Base (S3)
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

# Project Structure
