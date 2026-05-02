from agno.tools.google.gmail import GmailTools
import traceback
import socket

# Force IPv4
old_getaddrinfo = socket.getaddrinfo
def new_getaddrinfo(*args, **kwargs):
    responses = old_getaddrinfo(*args, **kwargs)
    return [response for response in responses if response[0] == socket.AF_INET]
socket.getaddrinfo = new_getaddrinfo
socket.setdefaulttimeout(15)

try:
    tools = GmailTools(credentials_path='credentials/credentials.json', port=8080)
    tools._auth()
    tools.service = tools._build_service()
    
    message = tools._create_message(["maikosousa.tech@gmail.com"], "Test", "Test message")
    print("Created message, sending...")
    res = tools.service.users().messages().send(userId="me", body=message).execute()
    print("Result:", res)
except Exception as e:
    print("Exception!")
    traceback.print_exc()
