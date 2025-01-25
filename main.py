from prompts import context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.gemini import Gemini
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

llm = Gemini(
    model="models/gemini-1.5-flash", api_key="AIzaSyC3qdktWjzcP3tMGGKzpP3EEJVv53N9sRY"
)

agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)
