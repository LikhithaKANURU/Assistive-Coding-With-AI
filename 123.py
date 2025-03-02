import streamlit as st
import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
import threading

# Assign the API key (USE ENV VARIABLES IN PRODUCTION)
GOOGLE_API_KEY = ""  # Replace with your actual API key

# Configure the Gemini API
try:
    if GOOGLE_API_KEY:
        genai.configure(api_key=GOOGLE_API_KEY)
        try:
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
        except Exception as e:
            st.error(f"Model Listing Error: {e}")
            model = None
    else:
        st.error("No API key provided.")
        model = None
except Exception as e:
    st.error(f"Configuration Error: {e}")
    model = None


def speak(text):
    """Speaks the given text using the text-to-speech engine."""
    def speak_thread(text):
        try:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            st.error(f"TTS Error: {e}")

    thread = threading.Thread(target=speak_thread, args=(text,))
    thread.start()


def listen():
    """Captures speech input and converts it to text using SpeechRecognition."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please speak now.")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Could not understand the speech."
        except sr.RequestError:
            return "Speech Recognition service error."
        except Exception as e:
            return f"Error: {str(e)}"


def generate_code_from_description(description, language="python"):
    """Generates code from a description using Gemini."""
    if model is None:
        return "Gemini API is not configured."

    prompt = f"Write a {language} function based on the following description:\n\n{description}\n\n# Code:"
    try:
        response = model.generate_content(
            prompt, generation_config=genai.GenerationConfig(temperature=0.2, max_output_tokens=150)
        )
        return response.text.strip() if response.text else "Error: Gemini API returned an empty response."
    except Exception as e:
        return f"Error generating code: {str(e)}"


def get_gemini_comment(code_line, language="python"):
    """Generates an inline comment for a given line of code using Gemini."""
    if model is None:
        return ""

    # Construct the prompt for Gemini
    prompt = (
        f"Add a brief inline comment to the following {language} code snippet, "
        f"explaining what it does:\n\n{code_line}\n\n# Comment:"
    )

    try:
        response = model.generate_content(
            prompt, generation_config=genai.GenerationConfig(temperature=0.3, max_output_tokens=50)
        )
        return response.text.strip() if response.text else ""
    except Exception as e:
        return f"Error generating comment: {str(e)}"


def add_inline_comments(code, language="python"):
    """Adds inline comments to the given code using Gemini."""
    if model is None:
        return "Gemini API is not configured."

    comment_lines = []
    for line in code.splitlines():
        comment = get_gemini_comment(line, language)  # Fetch comment using Gemini
        if comment:
            # Choose the correct comment syntax for different languages
            if language.lower() in ["c", "c++", "java", "javascript", "go", "rust", "php", "swift", "typescript"]:
                comment_prefix = "//"  # Single-line comment syntax
            elif language.lower() in ["python", "ruby"]:
                comment_prefix = "#"  # Hash-style comments
            else:
                comment_prefix = "#"  # Default to Python style

            comment_lines.append(f"{line} {comment_prefix} {comment}")
        else:
            comment_lines.append(line)

    return "\n".join(comment_lines)



def explain_code(code, language="python"):
    """Explains the given code using Gemini and speaks the explanation."""
    if model is None:
        st.error("Gemini API is not configured.")
        return

    prompt = (
        f"Explain the following {language} code in a simple and clear manner, "
        f"focusing on its logic and purpose:\n\n{code}\n\n# Explanation:"
    )

    try:
        response = model.generate_content(
            prompt, generation_config=genai.GenerationConfig(temperature=0.3, max_output_tokens=150)
        )
        if response.text:
            explanation = response.text.strip()
            st.info(explanation)  # Display the explanation
            speak(explanation)  # Speak the explanation
        else:
            st.error("Error: Gemini API returned an empty response for code explanation.")
    except Exception as e:
        st.error(f"Error generating code explanation: {str(e)}")


def main():
    st.title("Code Generator & Comment Assistant")
    language = st.selectbox("Select Programming Language:", [
        "python", "javascript", "java", "c", "c++", "ruby", "go", "swift", "html", "css", "php", "rust", "typescript"
    ])
    action = st.radio("Choose Action:", ["Generate Code", "Add Comments & Explain Code"])

    # Text input with speech-to-text feature
    input_text = st.text_area("Input (Code or Description):", height=150)
    listen_button = st.button("🎤 Listen to Speech")

    if listen_button:
        speech_text = listen()
        if speech_text:
            st.session_state.input_text = speech_text  # Store speech text in session state
            st.text_area("Recognized Speech:", speech_text, height=100)
            input_text = speech_text
            output_text = generate_code_from_description(input_text, language)
            st.code(output_text, language=language)
            st.session_state.output_text = output_text
            speak(st.session_state.output_text)


    if action == "Generate Code":
        request_code_button = st.button("Request Code")
        read_code_button = st.button("Read Code")

        if request_code_button:
            if not input_text:
                st.warning("Please enter a description.")
            else:
                output_text = generate_code_from_description(input_text, language)
                st.session_state.generated_code = output_text
                st.code(output_text, language=language)

        if read_code_button and "generated_code" in st.session_state:
            speak(st.session_state.generated_code)
            output_text = generate_code_from_description(input_text, language)
            st.session_state.generated_code = output_text
            st.code(output_text, language=language)

    elif action == "Add Comments & Explain Code":
        col1, col2 = st.columns([0.8, 0.2])
        
        with col1:
            perform_action_button = st.button("Add Comments")
        
        with col2:
            explain_button = st.button("Explain Code")

        if not input_text:
            st.warning("Please enter some code.")
        else:
            if perform_action_button:
                commented_code = add_inline_comments(input_text, language)
                st.code(commented_code, language=language)

            if explain_button:
                explain_code(input_text, language)


if __name__ == "__main__":
    main()
