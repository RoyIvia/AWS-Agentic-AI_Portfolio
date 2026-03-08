## Installing the Strands SDK

The first step in building the agent was installing the **Strands Agents SDK**, which provides the framework required to create and run AI agents.

The installation was performed using `pip` inside the development environment.

```python
pip install strands-agents strands-agents-tools
```

This command installs two packages:

* **strands-agents** — the core SDK used to create and manage AI agents
* **strands-agents-tools** — a library containing built-in tools that agents can use to perform tasks

Installing these dependencies prepares the environment for building and running Strands-based agents within the Python runtime.


## Creating the First Agent

The next step was to create a **basic Strands agent**. This verifies that the SDK is correctly installed and that the agent can communicate with the configured model provider.

### Implementation

```python
from strands import Agent

# Initialize your agent
agent = Agent(
    system_prompt="You are a helpful assistant that provides concise responses."
)

# Send a message to the agent
response = agent("Hello! What can you do?")
print(response)
```

### Explanation

This implementation performs the following steps:

1. **Import the Agent class**

   The `Agent` class from the Strands SDK provides the core functionality for building and managing agents.

2. **Initialize the agent**

   An agent instance is created and configured with a **system prompt**.
   The system prompt defines the role and behavior of the agent.

3. **Send a user request**

   A prompt is sent to the agent. The agent forwards the request to the configured model provider.

4. **Generate a response**

   The language model processes the request and returns a generated response, which is printed to the console.

At this stage, the agent operates as a **basic conversational interface powered by an LLM**. 

# Configuring the Model Provider

The next step was configuring the agent to use a specific Amazon Bedrock model rather than relying on the default configuration.

In this case, the agent was configured to use Claude Sonnet 4.5 through Amazon Bedrock.

Implementation
```python
import warnings
warnings.filterwarnings(action="ignore", message=r"datetime.datetime.utcnow")

from strands import Agent

# Initialize your agent
agent = Agent(
    model="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    system_prompt="You are a helpful assistant that provides concise responses."
)

# Send a message to the agent
response = agent("Hello! Tell me a joke.")
```
## Explanation:


<img width="1103" height="194" alt="image" src="https://github.com/user-attachments/assets/7547c134-620e-4694-a214-17a70033a788" />



This implementation introduces two key changes:

1. Suppressing runtime warnings

A warning filter is applied to suppress deprecation warnings related to datetime.utcnow.
This keeps the notebook output clean during execution.

2. Explicit model configuration

Instead of relying on the SDK default, the agent is explicitly configured to use the Bedrock model:

us.anthropic.claude-sonnet-4-5-20250929-v1:0

This ensures the agent always invokes the specified model.


