# Restaurant Booking Assistant

**Strands Agents + Amazon Bedrock + AWS Knowledge Base + DynamoDB**

## Overview

In this project, I built a **restaurant booking assistant agent** using the **Strands Agents SDK** integrated with several AWS services. The goal was to demonstrate how an AI agent can combine **LLM reasoning, retrieval (RAG), and transactional operations** to perform real-world tasks through natural language.

The assistant can:

* answer restaurant-related questions
* retrieve restaurant information from a knowledge base
* create reservations
* retrieve booking details
* delete reservations

The system combines **Amazon Bedrock LLMs**, **Bedrock Knowledge Bases**, **OpenSearch Serverless**, **Amazon S3**, and **Amazon DynamoDB** into a single agent workflow.

---

# Architecture

<img width="3863" height="2429" alt="image" src="https://github.com/user-attachments/assets/fc815337-64c8-47a2-89b3-379490aa5283" />


The architecture separates the **agent runtime environment** from the **cloud services it interacts with**.

### Local Environment

The Strands Agent runs locally (or in SageMaker Studio) and orchestrates the entire agent workflow.

### AWS Cloud

The agent invokes AWS services for reasoning, retrieval, and persistence.

---

# System Workflow

The overall interaction flow is:

```
User
  │
  ▼
Restaurant Assistant Agent (Strands)
  │
  ├── Amazon Bedrock LLM (Claude Sonnet)
  │
  ├── Retrieval Tool
  │       └── Bedrock Knowledge Base
  │             └── OpenSearch Serverless
  │                   └── S3 Document Store
  │
  └── Booking Tools
          └── DynamoDB Reservation Database
```

The agent interprets the user's request, retrieves context if necessary, executes tools, and produces a final response.

---

# Key Components

## 1. Strands Agent Runtime

The **Strands Agent** acts as the orchestrator of the system.

It performs:

* prompt interpretation
* reasoning using the LLM
* tool selection
* tool execution
* response generation

The agent runs in the environment where it is created (local machine or SageMaker Studio).

---

# 2. Amazon Bedrock LLM

The agent uses **Anthropic Claude Sonnet 4.5** hosted in Amazon Bedrock.

The model is responsible for:

* interpreting natural language requests
* deciding when to use tools
* generating responses
* orchestrating the agentic loop

Example configuration:

```python
from strands.models import BedrockModel

model = BedrockModel(
    model_id="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    additional_request_fields={
        "thinking": {"type": "disabled"}
    }
)
```

---

# 3. Retrieval Layer (Knowledge Base)

To provide contextual restaurant information, the agent uses a **Bedrock Knowledge Base**.

The retrieval pipeline works as follows:

```
User Question
      ↓
retrieve() tool
      ↓
Bedrock Knowledge Base
      ↓
OpenSearch Serverless Vector Index
      ↓
S3 Document Store
      ↓
Relevant Context
```

This architecture implements **Retrieval-Augmented Generation (RAG)**.

---

# 4. Amazon OpenSearch Serverless

OpenSearch Serverless acts as the **vector index** for the knowledge base.

It stores embeddings generated from the restaurant documents and enables semantic search during retrieval.

---

# 5. Amazon S3

Amazon S3 stores the **documents that form the knowledge base**.

These documents contain information such as:

* restaurant descriptions
* menus
* locations
* cuisine types

The knowledge base ingests these documents and indexes them for retrieval.

---

# 6. Amazon DynamoDB

DynamoDB stores **restaurant reservation records**.

It acts as the transactional database for the booking system.

Example stored attributes:

```
booking_id
restaurant_name
date
hour
guest_name
num_guests
```

---

# Agent Tools

To interact with AWS services, the agent uses several tools.

### Retrieval Tool

```
retrieve()
```

Retrieves relevant restaurant information from the knowledge base.

---

### Booking Tools

```
create_booking()
get_booking_details()
delete_booking()
```

These tools interact with DynamoDB to manage reservations.

---

### Utility Tool

```
current_time()
```

Provides time context to the agent when handling reservations.

---

# Tool Implementation Approaches

Strands supports three different ways of implementing tools.

### 1. Decorator Approach

Functions are converted into tools using the `@tool` decorator.

Example:

```python
from strands import tool

@tool
def delete_booking(booking_id: str, restaurant_name: str):
    ...
```

Best suited for:

* quick prototypes
* simple tools
* Python-only environments

---

### 2. TOOL_SPEC Approach

Tools are defined through a structured schema.

Example:

```
TOOL_SPEC = {
   "name": "create_booking",
   "inputSchema": {...}
}
```

Best suited for:

* complex tools
* strict validation
* multi-model compatibility

---

### 3. Standalone Tool Modules

Tools can also be implemented in separate files and imported into the agent.

This is the approach used in this project to keep the system modular.

---

# Infrastructure Deployment

Before running the agent, the required AWS infrastructure must be created.

A deployment script provisions the necessary components.

```
# agent knowledge base
echo "deploying knowledge base ..."
python prereqs/knowledge_base.py --mode create

# agent dynamodb
echo "deploying DynamoDB ..."
python prereqs/dynamodb.py --mode create
```

Run the script with:

```
sh deploy_prereqs.sh
```

This creates:

* Bedrock Knowledge Base
* OpenSearch index
* DynamoDB reservation table
* required parameters in SSM Parameter Store

---

# Agent Initialization

After the infrastructure is deployed, the agent loads configuration from **AWS Systems Manager Parameter Store**.

Example:

```python
kb_name = "restaurant-assistant"

dynamodb = boto3.resource("dynamodb")
ssm_client = boto3.client("ssm")

table_name = ssm_client.get_parameter(
    Name=f"{kb_name}-table-name"
)

table = dynamodb.Table(table_name["Parameter"]["Value"])
```

This allows the agent to dynamically locate the resources it needs.

---

# Creating the Agent

Once the model and tools are defined, the agent is created.

```python
agent = Agent(
    model=model,
    system_prompt=system_prompt,
    tools=[
        retrieve,
        current_time,
        get_booking_details,
        create_booking,
        delete_booking
    ]
)
```

---

# Invoking the Agent

The agent can now respond to natural language queries.

Example:

```python
agent("Hi, where can I eat in San Francisco?")
```

Example booking request:

```
Book a table for 4 people at Italian Bistro tomorrow at 7 PM
```

The agent will:

1. retrieve restaurant information if necessary
2. generate a reservation
3. store the booking in DynamoDB
4. return a confirmation message

---

# Monitoring Agent Behavior

Strands Agents automatically track runtime metrics and conversation history.

### Conversation History

```
agent.messages
```

Stores:

* user messages
* assistant responses
* tool calls
* tool results

---

### Metrics Captured

The SDK automatically records:

* token usage
* latency
* execution time
* tool invocation counts
* reasoning loop cycles

These metrics help evaluate and optimize agent performance.

---

# Project Outcome

By the end of this project, the restaurant booking assistant was capable of:

* understanding natural language requests
* retrieving restaurant information through RAG
* creating and managing reservations
* interacting with AWS services through agent tools

This project demonstrates how **AI agents can combine LLM reasoning, knowledge retrieval, and transactional systems to build practical real-world applications**.

---

# Technologies Used

* **Strands Agents SDK**
* **Amazon Bedrock**
* **Anthropic Claude Sonnet**
* **Amazon Bedrock Knowledge Base**
* **Amazon OpenSearch Serverless**
* **Amazon S3**
* **Amazon DynamoDB**
* **Python**
