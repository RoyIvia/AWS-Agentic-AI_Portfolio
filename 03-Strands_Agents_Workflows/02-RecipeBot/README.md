# RecipeBot — Task-Specific Strands Agent

I built a task-specific AI agent called **RecipeBot**.
The agent helps users find recipes and answer cooking-related
questions.

RecipeBot uses a **web search tool** to retrieve information from
the internet and combine it with the reasoning capabilities of
the language model.

## Key Components

RecipeBot consists of three main components:

### Model
Claude Sonnet running on Amazon Bedrock.

### Tool
A custom `websearch` tool implemented using the DuckDuckGo search API.

### Prompt
A system prompt defining the behavior of the cooking assistant.

<img width="3584" height="1705" alt="image" src="https://github.com/user-attachments/assets/801c7d58-ecde-464a-aaeb-c960914b822d" />

---

## Running the Agent

Install dependencies:
```python
pip install strands-agents strands-agents-tools duckduckgo-search
```
Run the agent:

```python
python recipe_agent.py
```
