import asyncio
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

async def run_agent():
    client = MultiServerMCPClient(
        {
            "github": {
                "command": "npx",
                "args": [
                    "-y",
                    "@modelcontextprotocol/server-github"
                ],
                "env": {
                    "GITHUB_PERSONAL_ACCESS_TOKEN": GITHUB_TOKEN
                },
                "transport": "stdio"
            }
        }
    )
    tools = await client.get_tools()
    agent = create_agent("groq:llama-3.3-70b-versatile", tools,system_prompt="You are a helpful assistant")
    response = await agent.ainvoke({
        "messages" : [{
            "role" : "user",
            "content" : "create a directory Binarysearch and place binary search program in BinarySearch.java file under initialBranch of msiva06/AtoZDSA repository "
        }]
    })
    last_msg = response["messages"][-1]
    print(last_msg.content)

if __name__ == "__main__":
    asyncio.run(run_agent())


