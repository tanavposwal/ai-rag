import os
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.agent import ReActAgent
from llama_index.llms import Ollama
from pdf import india_engine, deforestation_engine

tools = [
    note_engine,
    QueryEngineTool(
        query_engine=deforestation_engine,
        metadata=ToolMetadata(
            name="india_data",
            description="this gives detailed information about climate in india the country",
        ),
    ),
    QueryEngineTool(
        query_engine=india_engine,
        metadata=ToolMetadata(
            name="deforestation_data",
            description="this gives detailed information about deforestation",
        ),
    ),
]

llm = Ollama(model="llama3.2:3b", temperature=0)  # Add this line

agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)
