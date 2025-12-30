import os
from dotenv import load_dotenv
from langchain.agents import create_agent
import asyncio
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def get_weather(city: str) -> str:
   """Get weather for a given city."""
   return f"It's always sunny in {city}!"

def add_file():
    """Create a new file if not exists"""
    try:
        with open("ai_file.txt", "x") as f:
            f.write("This file is new.")
            print("file was created")
    except FileExistsError:
        print("File already exists, did not overwrite.")

def add_folder():
    """Create a folder if not exists"""
    os.mkdir("ai_folder")

def delete_file(file_path:str):
    """Delete a file if exists"""
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    else:
        print(f"File not found: {file_path}")

def delete_folder(folder_name:str):
    """Delete folder if exists"""
    try:
        os.rmdir(folder_name)
        print("{folder_name} got deleted.")
    except OSError as e:
        print(f"Error deleting folder: {e}")

agent = create_agent(model = "groq:llama-3.3-70b-versatile",
tools=[add_file,add_folder,delete_file,delete_folder],
system_prompt="You are a helpful assistant")

response = agent.invoke({"messages":[{
    "role" : "user",
    "content":"delete the given file ai_file.txt"
}]})

print(response)