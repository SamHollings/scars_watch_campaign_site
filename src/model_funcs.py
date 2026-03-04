from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import AIMessage, HumanMessage, SystemMessage
import dotenv

def gemini_model():
    dotenv.load_dotenv()
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=1.0,  # Gemini 3.0+ defaults to 1.0
        max_tokens=None,
        timeout=None,
        max_retries=2,
    # other params...
    )

    return model