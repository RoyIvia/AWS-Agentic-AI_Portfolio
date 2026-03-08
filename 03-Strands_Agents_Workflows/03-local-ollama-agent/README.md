# Running Strands Agents Locally with Ollama

## Overview

In this step, the agent was configured to run using **Ollama**, an open-source framework for running large language models locally. Unlike previous steps where the agent invoked models through **Amazon Bedrock**, Ollama enables the agent to operate entirely on the local machine.

This approach is useful when building applications that require:

* **privacy-focused processing**
* **offline execution**
* **zero API costs**
* **local experimentation with open-source models**

With Ollama, the model runs locally while the Strands agent orchestrates the agentic loop and tool execution.

---

# Architecture

In this configuration, both the **agent runtime** and the **LLM** run locally.

<img width="1454" height="778" alt="image" src="https://github.com/user-attachments/assets/91ff4b34-416f-4342-a46c-4b870be42df7" />


This architecture differs from the earlier Bedrock-based setup where the model ran in the AWS cloud.

---

# Key Benefits of Using Ollama

Using Ollama provides several advantages when developing AI agents locally:

**Privacy**

All inference happens on the local machine. No prompts or data are sent to external APIs.

**No API Costs**

Since the model runs locally, there are no token-based usage costs.

**Offline Capability**

Agents can operate without an internet connection once the model has been downloaded.

**Customization**

Local models can be fine-tuned or replaced depending on the use case.

---

# Prerequisites

Before running the agent locally, the following setup was completed:

### Install Ollama

Ollama was installed by following the official installation guide:

```
https://ollama.com/download
```

### Download a Model

A local model was downloaded using:

```bash
ollama pull llama3.2:latest
```

### Start the Ollama Server

The Ollama runtime was started with:

```bash
ollama serve
```

The server exposes the model through a local endpoint.

```
http://localhost:11434
```

---

# Configuring the Ollama Model

After installing and starting Ollama, the model was configured inside the Strands agent environment.

### Implementation

```python
from strands.models.ollama import OllamaModel

ollama_model = OllamaModel(
    model_id="llama3.2:latest",
    host="http://localhost:11434",
    params={
        "max_tokens": 2048,
        "temperature": 0.7,
        "top_p": 0.9,
        "stream": True,
    },
)
```

### Explanation

This configuration defines how the Strands agent interacts with the Ollama model.

* **model_id** specifies the downloaded Ollama model
* **host** points to the local Ollama server
* **temperature** controls randomness in responses
* **top_p** adjusts nucleus sampling
* **max_tokens** limits response length

---

# Creating the Agent

Once the model configuration is complete, the agent can be created using the local Ollama model.

```python
local_agent = Agent(
    system_prompt=system_prompt,
    model=ollama_model,
    tools=[file_read, file_write, list_directory],
)
```

In this configuration:

* the **LLM runs locally**
* the **agent manages tool orchestration**
* tools enable interaction with the local system

---

# Example Local Tools

To demonstrate local capabilities, several file system tools can be implemented.

```python
@tool
def file_read(file_path: str) -> str:
    """Read a file and return its content."""
```

```python
@tool
def file_write(file_path: str, content: str) -> str:
    """Write content to a file."""
```

```python
@tool
def list_directory(directory_path: str = ".") -> str:
    """List files and directories in the specified path."""
```

These tools allow the agent to perform operations directly on the local machine.

---

# Interacting with the Agent

Once the agent is initialized, it can execute tasks using the local model.

Example interactions include:

```python
local_agent("Show me the files in the current directory")
```

```python
local_agent("Create a file called 'sample.txt' with the content 'This is a test file created by my Ollama agent.'")
```

```python
local_agent("Read the file 'document.txt' and summarize it in 5 bullet points.")
```

The agent uses the **Ollama model for reasoning** and **tools for performing system actions**.

---

# Result

At the end of this step, the Strands agent was successfully configured to run using a **local LLM through Ollama**.

This setup demonstrates how Strands can operate with both:

* **cloud-hosted models (Amazon Bedrock)**
* **locally hosted models (Ollama)**

This flexibility allows developers to choose the deployment model that best fits their application's requirements.
