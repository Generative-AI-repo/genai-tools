from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()
agent = create_agent(model="groq:llama-3.3-70b-versatile",tools=[], system_prompt="You are a helpful assistant",
                     checkpointer=checkpointer)

config = {"configurable": {"thread_id":"1"}}
response = agent.invoke({
    "messages":[{
        "role" :"user",
        "content" : "who is Dhoni?"
    }]},
    config
)

print(response)

response = agent.invoke({
    "messages":[{
        "role" :"user",
        "content" : "when was he born?"
    }]},
    config
)

print(response)
