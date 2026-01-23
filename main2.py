from typing import Dict

from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()
from langchain.agents import create_agent

class RecipeResponse(BaseModel):
    title: str
    ingredients: Dict[str, str]
    instructions: Dict[str, str]

agent = create_agent("groq:llama-3.3-70b-versatile", tools=[], response_format=RecipeResponse)
config = {"configurable" : {"thread_id" : "1"}}
response = agent.invoke({"messages": [{"role": "user", "content": "Give step by step instructions of max 5 steps of South-Indian sambar recipe"}]},
   config )



print("------------------------------")
print(response["structured_response"].title)


print("------------------------------")
print(response["structured_response"].ingredients)

print("------------------------------")
print(response["structured_response"].instructions)