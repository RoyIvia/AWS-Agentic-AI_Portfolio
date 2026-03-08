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
