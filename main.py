from app.agent import data_analysis_team

def main():
    data_analysis_team.print_response(
        "Analyze the amazon dataset and send me a report.",
        stream=True
    )

if __name__ == "__main__":
    main()
