"""Generates post battle fluff based on the ongoing story and sides 
invovled in our battles.

Contents:
- access to ongoing story google docs document
    - intially contents of this could simply be put into a text file, but eventually we want to be able to read and write to a google doc
- use this as background context then, take in battle info and generate post battle fluff
    - intially the whole document could be dumped into the prompt, 
    - but eventually will want to bring only the relevant sections of the story into the prompt - e.g. RAG
- save this fluff back into the ongoing story document
- some sort of front end, to display the ongoing story
- a trigger mechanism - such that when a battle report is submitted, the fluff is generated, added to the story document and displauyued on the front end

Assets:
- txt file to store the story
- battle report submission file
- model pipeline to generate fluff
- prompt template
- front end to display story and receive submissions
- trigger mechanism to run the model pipeline when a battle report is submitted

"""

import streamlit as st
from langchain.messages import AIMessage, HumanMessage, SystemMessage
import model_funcs
import prompts
import streamlit_utils
import retrieval

DEBUG_MODE = True

st.title("Warhammer 40k Story Generator")

st.write("This is a work in progress. The goal of this project is to generate post battle fluff based on the ongoing story and sides involved in our battles.")

# need to add a system prompt to the beginning of the conversation, to set the context for the model. This should only be added once, at the beginning of the conversation, and not on every message.

system_message = prompts.system_message
ai_message = prompts.ai_message

if "messages" not in st.session_state:
    st.session_state.messages = [system_message, ai_message]

streamlit_utils.display_messages()

from langchain.messages import AIMessage, HumanMessage, SystemMessage

# get new input
input_text = st.chat_input("Ask me anything about the ongoing story, or submit a battle report to generate post-battle fluff.")

if DEBUG_MODE:
    import pprint
    pprint.pp(st.session_state.messages)

#prompt_template = f"""{input_text}"""

user_message = dict(role="user", content=input_text)

if user_message['content']:
    # Add user message to history
    st.session_state.messages.append(user_message)

    # Show user message
    with st.chat_message("user"):
        st.write(user_message["content"])

    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.write("🤔 Thinking...")
    
        try:

            model = model_funcs.gemini_model()

            response = model.invoke(st.session_state.messages + [HumanMessage(content=(f"The relevant history is: {retrieval.extract_relevant_history(input_text)}"))])
            response_text = response.content

            print(response_text)

        except Exception as e:
            response_text = "Error generating response."
            st.error(str(e))

        placeholder.write(response_text)

        st.session_state.messages.append({"role": "assistant", "content": response_text})

    st.rerun()

