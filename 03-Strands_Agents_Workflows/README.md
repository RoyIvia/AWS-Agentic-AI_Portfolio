# Building AI Agents with Strands SDK


This project documents the process of building an AI agent using the **Strands Agents SDK**, an open-source framework designed for developing intelligent agents powered by large language models (LLMs). Strands enables developers to build agents that can reason, plan tasks, and interact with tools or external services in order to complete complex workflows.

A Strands agent is built around three core components:

* **Model** – the LLM responsible for reasoning and decision making
* **Prompt** – instructions that define the agent’s role and behavior
* **Tools** – functions or services the agent can use to perform actions

Together, these components allow the agent to move beyond simple text generation and perform meaningful operations such as retrieving data, executing logic, or interacting with external systems.

---

## The Agentic Loop

Strands agents operate through an **agentic loop**, where the model continuously evaluates the task and determines the next action required to complete it.

The loop typically follows this pattern:

```
User Request
     ↓
Agent receives instruction
     ↓
Model reasons about the task
     ↓
Model selects a tool (if required)
     ↓
Tool executes and returns results
     ↓
Model evaluates results and produces a final response
```

<img width="648" height="328" alt="agentic_loop" src="https://github.com/user-attachments/assets/3acba136-29c3-45b2-a278-42d4fad621d8" />

This dynamic decision-making process allows the agent to autonomously plan and execute multi-step tasks.


---

## Development Environment on AWS

To implement the agent, the development environment was launched using **Amazon SageMaker AI Studio**, AWS’s managed environment for machine learning and AI development.

SageMaker Studio provides a fully managed workspace that includes:

* scalable compute resources
* integrated development tools
* persistent storage for project artifacts
* seamless integration with other AWS services

Using SageMaker eliminates the need to manually provision infrastructure while providing an environment optimized for AI development.

---

## Launching SageMaker AI Studio

After logging into the AWS Console, the development environment was launched by navigating to **Amazon SageMaker AI** and opening **SageMaker Studio**.

A user profile within the SageMaker domain provides access to Studio applications and resources. Once the profile is selected, the Studio interface launches in a new browser tab, providing access to the development workspace.


<img width="1728" height="992" alt="Sagemaker_studio" src="https://github.com/user-attachments/assets/fd5dbdd9-7403-4172-aca0-7d6c40793153" />


---

## Using JupyterLab as the Development IDE

Within SageMaker Studio, the project environment was created using **JupyterLab**.

JupyterLab is a web-based IDE designed for interactive computing and data workflows. It provides an environment for:

* writing and executing Python code
* running notebooks
* installing dependencies
* experimenting with agent behavior

In SageMaker, each application runs inside a **space**, which manages the compute and storage resources required by the application. Once the JupyterLab space is launched, the environment becomes available for development and experimentation.

<img width="1728" height="992" alt="jupyterLab" src="https://github.com/user-attachments/assets/7c9a0781-6c43-42df-aaed-632662bc5cfd" />


This setup provides a practical environment for iteratively building and testing the Strands agent.

