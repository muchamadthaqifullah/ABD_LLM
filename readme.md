# Code Writer - GitHub README.md
## Introduction
Welcome to the Code Writer! This Streamlit application integrates with Google's Generative AI to provide a powerful and user-friendly platform for generating code in various programming languages. Whether you're a seasoned developer or a beginner, Code Writer simplifies the process of coding by transforming your ideas into code snippets.

## Features
Multiple Programming Languages: Choose from Python, Go, JavaScript, or TypeScript.
User-Friendly Interface: A simple and intuitive Streamlit sidebar for input.
Customizable Prompts: Specify what you want to code, and Code Writer will generate the corresponding script.
Advanced AI Integration: Utilizes Google's Generative AI to ensure high-quality code generation.
## How to Use
Select a Programming Language: Use the dropdown in the sidebar to choose your preferred language.
Enter Your Prompt: In the text input field, describe what you want to code.
Generate Code: Click the 'Generate' button to produce the code based on your prompt.
View the Result: The generated code will be displayed on the main screen.
## Installation
To run Code Writer, you need to install Streamlit and set up the Google Generative AI API:

    pip install streamlit

    pip install google.generativeai

Set up your API key as per Google's Generative AI documentation and include it in the application (api.py file).

## Usage Example
    import streamlit as st
    import google.generativeai as genai
    from api import api

    # Configure the API key
    genai.configure(api_key=api)

    # Set default parameters
    defaults = {
        'model': 'models/text-bison-001',
        'temperature': 0.25,
        'candidate_count': 1,
        'top_k': 40,
        'top_p': 0.95,
    }

    st.title('Code Writer')
    st.write('You can ask me to code anything')
    final_response = None

    # Creating a side panel for inputs
    with st.sidebar:
        st.write("## Code Generator Settings")
        programming_language = st.selectbox("Choose the programming language:", 
                                        ["Python", "Go", "JavaScript", "TypeScript"])
        prompt = st.text_input("What do you want to code?")
        if st.button('Generate'):
            formatted_prompt = f"Write a {programming_language.lower()} code about {prompt}"
            response = genai.generate_text(
                **defaults,
                prompt=formatted_prompt
            )
            final_response = response
    if final_response != None:
        st.write(final_response.result)
## Support
For any queries or support, please open an issue on the project's GitHub repository.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

# Enjoy coding with Code Writer! 🚀





