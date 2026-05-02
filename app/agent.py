from agno.agent import Agent
from agno.models.nvidia import Nvidia
from agno.knowledge import Knowledge
from agno.knowledge.embedder.sentence_transformer import SentenceTransformerEmbedder
from agno.vectordb.chroma import ChromaDb, SearchType
from agno.tools.csv_toolkit import CsvTools
from agno.tools.google.gmail import GmailTools
from dotenv import load_dotenv
import os

load_dotenv()

csv_tools = CsvTools(csvs=['data/raw/amazon.csv'])

knowledge = Knowledge(
    vector_db=ChromaDb(
        collection="data",
        path="data/chromadb",
        persistent_client=True,
        search_type=SearchType.hybrid,
        embedder=SentenceTransformerEmbedder(id="sentence-transformers/all-MiniLM-L6-v2")
    )
)

knowledge.insert(path='data/raw/', skip_if_exists=True)

data_analysis_agent = Agent(
    name="Data Analysis & Email Agent",
    model=Nvidia(id="z-ai/glm4.7"),
    tools=[
        csv_tools,
        GmailTools(credentials_path='credentials/credentials.json', port=8080)
    ],  
    instructions=[
        "You are an expert Data Analyst.",
        "You must analyze the data using the provided tools.",
        "Limit your analysis to a maximum of 3 queries.",
        "After gathering insights, create a concise report.",
        f"Immediately email the report to {os.getenv('EMAIL_ADDRESS')} using the `send_email` tool.",
        "CRITICAL: You MUST actually call the `send_email` tool. Do not just output text saying that you sent it.",
        "Do not overthink or overcomplicate the report."
    ],
    search_knowledge=True,
    knowledge=knowledge,
    debug_mode=True,
)