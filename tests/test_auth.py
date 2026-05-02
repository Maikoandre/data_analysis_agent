from agno.tools.gmail import GmailTools
import traceback

print("Testing Gmail authentication...")
try:
    tools = GmailTools(credentials_path='credentials/credentials.json', port=8080)
    tools._auth()
    print("Authentication successful! token.json should be created.")
except Exception as e:
    print(f"Error during authentication: {e}")
    traceback.print_exc()
