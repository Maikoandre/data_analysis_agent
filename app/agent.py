from agno.agent import Agent
from agno.models.nvidia import Nvidia
from agno.knowledge import Knowledge
from agno.knowledge.embedder.sentence_transformer import SentenceTransformerEmbedder
from agno.vectordb.chroma import ChromaDb, SearchType
from agno.tools.csv_toolkit import CsvTools
from agno.tools.google.gmail import GmailTools
from agno.team.team import Team
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

analyst_agent = Agent(
    name="Data Analysis Agent",
    model=Nvidia(id="z-ai/glm4.7"),
    tools=[csv_tools],  
    instructions=[
        "You are a data analysis agent.",
        "You have access to tools to analyze the data.",
        "Limit your analysis to a maximum of 3 queries. Do not get stuck in a loop.",
        "Always answer the user's questions based on the analysis.",
        "Generate a report and use the tools to send it to the user by using the Gmail tool."
    ],
    search_knowledge=True,
    knowledge=knowledge,
)

gmail_agent = Agent(
    name="Gmail Agent",
    model=Nvidia(id="qwen/qwen3.5-122b-a10b"),
    tools=[GmailTools(credentials_path='credentials/credentials.json', port=8080)],
    description="You are an expert Gmail Agent that can read, draft, send and label emails using Gmail.",
    instructions=[
        "Based on user query, you can read, draft, send and label emails using Gmail.",
        "While showing email contents, you can summarize the email contents, extract key details and dates.",
        "Show the email contents in a structured markdown format.",
        "Attachments can be added to the email",
        "When you need to modify an email, make sure to find its message_id and thread_id in order to do modification operations.",
    ],
)

data_analysis_team = Team(
    name="Data Analysis Team",
    model=Nvidia(id="qwen/qwen3.5-122b-a10b"),
    members=[analyst_agent, gmail_agent],
    instructions=[
        "You are a central agent that can coordinate between different agents.",
        "You have access to tools to analyze the data.",
        "Limit your analysis to a maximum of 3 queries.",
        "Always answer the user's questions based on the analysis.",
        "Generate a report and use the tools to send it to the user by using the Gmail tool.",
        f"Always send an email to {os.getenv('EMAIL_ADDRESS')} with the report."
    ],
    search_knowledge=True,
    knowledge=knowledge,
)