# Gift Wrapping Knowledge Base – Retrieval Augmented Generation (RAG)

This section documents the integration of a **Knowledge Base using Amazon Bedrock** to enhance the Product Recommendation Agent with **gift wrapping suggestions**.

After implementing product recommendations, cart functionality, and personalized suggestions, the next step was to enable the agent to provide **gift wrapping ideas based on the products selected by the user**.

This capability introduces **Retrieval-Augmented Generation (RAG)** into the architecture. Instead of relying solely on the foundation model’s knowledge, the agent retrieves contextual information from a **knowledge base built from documents stored in Amazon S3**.

By integrating a knowledge base, the agent is able to provide **more contextual and relevant responses** based on external information sources.

The implementation follows the AWS workshop:

https://catalog.workshops.aws/e-commerce-in-a-bot/en-US/getting-started

However, this documentation reflects **my own deployment and configuration process within my AWS environment**.

---

# Architecture Overview

The architecture now expands to include **Knowledge Bases for Amazon Bedrock**, allowing the agent to retrieve information from documents before generating responses.

The updated architecture flow becomes:

User  
↓  
Amazon Bedrock Agent  
↓  
Knowledge Base Retrieval  
↓  
Amazon S3 Data Source  
↓  
Foundation Model Response  

In this stage, the agent retrieves **gift wrapping ideas from the knowledge base** and incorporates them into its response when users ask for gift wrapping suggestions.

---

# Infrastructure Components Used

The knowledge base integration relies on several AWS services.

---

## Amazon Bedrock Knowledge Bases

Knowledge Bases for Amazon Bedrock provide a **fully managed solution for implementing Retrieval-Augmented Generation (RAG)**.

The service handles:

- Data ingestion
- Vector indexing
- Semantic search
- Retrieval augmentation

This eliminates the need to manually build custom vector databases or retrieval pipelines.

---

## Amazon S3

The knowledge base retrieves its source data from an **Amazon S3 bucket** that contains a text file with gift wrapping suggestions.

Example document used:

```
Gift-wrapping.txt
```

This document contains multiple wrapping ideas categorized by **occasion, gift type, and recipient**.

The content is automatically indexed and converted into embeddings during the knowledge base synchronization process.

---

# Deploying the Knowledge Base

In my AWS environment, the Knowledge Base was deployed using a **CloudFormation template provided by the workshop**.

This template provisions the resources required for the Bedrock Knowledge Base.

---

## Step 1 — Launch the CloudFormation Stack

Navigate to:

```
AWS Console → CloudFormation
```

Choose:

```
Create Stack
```

Then upload the template provided by the workshop.

When prompted for the stack name, use:

```
BedrockKB
```

After submitting the stack, AWS deploys the resources required for the knowledge base.

---

# Knowledge Base Resources Created

The CloudFormation template provisions the following components.

---

## Knowledge Base

```
GiftWrappingKnowledgeBase
```

This knowledge base contains the indexed data used by the Bedrock Agent to retrieve wrapping ideas.

---

## Data Source

```
GiftWrappingDataSource
```

This data source connects the knowledge base to the **Amazon S3 bucket containing the gift wrapping document**.

---

# Synchronizing the Knowledge Base

Once the stack deployment was completed, the data source had to be synchronized so the knowledge base could ingest the document.

Steps performed:

1. Navigate to **Amazon Bedrock → Knowledge Bases**
2. Open the knowledge base:

```
GiftWrappingKnowledgeBase
```

3. Locate the data source:

```
GiftWrappingDataSource
```

4. Select **Sync**

During synchronization, the following processes occur:

- The document is retrieved from S3
- Text is split into smaller chunks
- Embeddings are generated
- Vectors are stored in the Bedrock retrieval index

After synchronization, the **Sync History** section confirms successful ingestion.

---

# Updating the Bedrock Agent

After the knowledge base was synchronized, the next step was to update the **ProductRecommendationAgent** so it could retrieve gift wrapping ideas when needed.

Steps performed:

1. Navigate to:

```
Amazon Bedrock → Agents
```

2. Open:

```
ProductRecommendationAgent
```

3. Select:

```
Edit in Agent Builder
```

---

# Updating Agent Instructions

The agent instruction prompt was updated to include guidance on when and how to retrieve gift wrapping suggestions.

The updated instructions included the following section:

```
Before the end of the conversation ask the user if they want you to suggest gift wrapping ideas for the products in the cart, and get the wrapping ideas based on the gift wrapping knowledge base.
```

This ensures that the agent proactively suggests wrapping ideas after assisting with product selection and cart management.

---

# Adding the Knowledge Base to the Agent

To allow the agent to retrieve information from the knowledge base, I attached it directly within the agent configuration.

Steps performed:

1. In **Agent Builder**, navigate to the **Knowledge Bases** section
2. Choose **Add Knowledge Base**
3. Select:

```
GiftWrappingKnowledgeBase
```

4. Configure the action group type as:

```
Define with API Schemas
```

---

# Knowledge Base Instructions for the Agent

The following instructions were added to guide how the agent should use the knowledge base.

```
This is a gift wrapping knowledge base for ideas on how to wrap gifts based on the gift details the occasion and its recipient.
```

These instructions provide context to the agent so it understands **when to retrieve information from the knowledge base**.

---

# Preparing the Agent

After adding the knowledge base integration, the agent was updated and prepared.

Steps performed:

1. Select **Save**
2. Choose **Prepare**

Preparing the agent compiles the configuration and enables the updated capabilities.

---

# Testing the Knowledge Base Integration

The updated agent was tested using the **Bedrock Agent testing interface**.

Example interaction:

User:

```
Can you suggest wrapping ideas for the perfume gift?
```

Agent workflow:

1. Detect the user's request for gift wrapping ideas
2. Query the **GiftWrappingKnowledgeBase**
3. Retrieve relevant wrapping suggestions
4. Generate a contextual response

Example response:

```
Here are some gift wrapping ideas for this item:

- Elegant wrapping paper with a satin ribbon
- Minimalist kraft paper with dried flowers
- A decorative gift box with tissue lining

Would you like help adding a greeting card as well?
```

---

# Observing Retrieval Behavior

Using the **Show Trace** feature during testing makes it possible to observe how the agent performs knowledge retrieval.

The trace reveals:

- The query sent to the knowledge base
- The document chunks retrieved from S3
- The context injected into the prompt
- The final response generated by the foundation model

This demonstrates the **Retrieval-Augmented Generation workflow** in practice.

---

# Outcome

At the end of this stage, the Product Recommendation Agent gained the ability to retrieve contextual information from a **Knowledge Base using Amazon Bedrock**.

Key outcomes include:

- Successful deployment of a Bedrock Knowledge Base
- Integration of an S3 data source for document retrieval
- Implementation of Retrieval-Augmented Generation (RAG)
- Dynamic gift wrapping suggestions generated from external knowledge

This stage significantly improves the intelligence of the chatbot by enabling it to **augment responses with external data rather than relying solely on the foundation model’s internal knowledge**.
