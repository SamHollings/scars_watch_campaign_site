

def extract_relevant_history(input_text: str) -> str:
    """Extract the relevant parts of the history text based on the input text."""
    # This is a placeholder implementation. You can replace this with a more sophisticated method, such as using RAG or a similarity search.
    history_text = ""
    try:
        with open("data/ongoing_story.txt", "r") as f:
            history_text = f.read()
            #print("History text loaded successfully.")
    except FileNotFoundError:
        history_text = "No ongoing story yet."
    return history_text