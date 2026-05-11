import socket

# Force IPv4 to prevent httplib2 timeout on IPv6 networks
old_getaddrinfo = socket.getaddrinfo
def new_getaddrinfo(*args, **kwargs):
    responses = old_getaddrinfo(*args, **kwargs)
    return [response for response in responses if response[0] == socket.AF_INET]
socket.getaddrinfo = new_getaddrinfo
socket.setdefaulttimeout(30)

from app.agent import data_analysis_agent

def main():
    data_analysis_agent.print_response(
        "Analyze the amazon dataset, create a dashboard and send me the dashboard and a report via email.",
        stream=True
    )

if __name__ == "__main__":
    main()
