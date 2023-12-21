import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyCq-IpiBOK3xU6plRQkD0dXBHgXCWL-eZY")

# Set default parameters for text summarization
defaults = {
    'model': 'models/text-bison-001',  # Replace with a supported text summarizer model
    'temperature': 0.25,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
}

st.title('Text Summarizer')
st.write('You can ask me to summarize any text')
final_response = None

# Creating a side panel for inputs
with st.sidebar:
    st.write("## Text Summarizer Settings")
    # Create a text input for the text to be summarized
    text_to_summarize = st.text_area("Enter the text to be summarized:")
    # When the 'Summarize' button is pressed, generate the summary
    if st.button('Summarize'):
        # Include the language in the prompt
        formatted_prompt = f"Write a code summary in English: {text_to_summarize}"
        response = genai.generate_text(
            **defaults,
            prompt=formatted_prompt
        )
        final_response = response

if final_response is not None:
    st.write(final_response.result)
