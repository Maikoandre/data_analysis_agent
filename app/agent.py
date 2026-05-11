from agno.agent import Agent
from agno.models.nvidia import Nvidia
from agno.knowledge import Knowledge
from agno.knowledge.embedder.sentence_transformer import SentenceTransformerEmbedder
from agno.vectordb.chroma import ChromaDb, SearchType
from agno.tools.csv_toolkit import CsvTools
from agno.tools.google.gmail import GmailTools
from dotenv import load_dotenv
import os
from app.pdf_generator import generate_pdf_report
from agno.tools.python import PythonTools

load_dotenv()

csv_tools = CsvTools(csvs=['data/raw/amazon.csv'])

knowledge = Knowledge(
    vector_db=ChromaDb(
        collection="data",
        path="db/chromadb",
        persistent_client=True,
        search_type=SearchType.hybrid,
        embedder=SentenceTransformerEmbedder(id="sentence-transformers/all-MiniLM-L6-v2")
    )
)

knowledge.insert(path='data/raw/', skip_if_exists=True)

current_dir = os.path.dirname(os.path.abspath(__file__))
instructions_path = os.path.join(current_dir, "instructions.md")

data_analysis_agent = Agent(
    name="Data Analyst",
    description="Advanced data analytics agent that generates charts and provides actionable insights.",
    model=Nvidia(id="z-ai/glm4.7"),
    tools=[
        csv_tools,
        generate_pdf_report,
        GmailTools(credentials_path='credentials/credentials.json', port=8080),
        PythonTools()
    ],  
    instructions=instructions_path,
    search_knowledge=True,
    knowledge=knowledge,
    debug_mode=True,
)