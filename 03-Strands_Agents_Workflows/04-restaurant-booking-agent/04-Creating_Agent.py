#Defining agent underlying model:

model = BedrockModel(
    model_id="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    additional_request_fields={
        "thinking": {
            "type": "disabled"
        }
    },
)

#Constructing the agent with previously defined and imported custom tools:

agent = Agent(
    model=model,
    system_prompt=system_prompt,
    tools=[retrieve, current_time, get_booking_details, create_booking, delete_booking],
)


#invoking the agent with sample prompt:

results = agent("Hi, where can I eat in San Francisco?")



