import os
from langchain.agents import create_agent
from tools import tools, execute_tool
import json

os.environ["GOOGLE_API_KEY"] = ""

agent = create_agent(
    model="google_genai:gemini-2.5-flash",
    tools=tools,
    system_prompt="You are a helpful assistant",
)

def process_query(query):
    result = agent.invoke(
        {"messages": [{"role": "user", "content": query}]}
    )
    print(result)
    response_message = result["messages"][-1]
    
    if hasattr(response_message, "tool_calls") and response_message.tool_calls:
        tool_call = response_message.tool_calls[0]
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        result = execute_tool(tool_name, tool_args)
        
    return result

if __name__ == "__main__":
    info = process_query("give information about this paper 2412.05997v3")
    print(info)
