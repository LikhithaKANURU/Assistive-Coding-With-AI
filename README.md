# AI-Powered Code Generator & Comment Assistant

## 📌 Overview
This project is an AI-powered coding assistant that helps developers generate code, add inline comments, and explain code snippets using Google Gemini AI. It also supports speech-to-text input and text-to-speech output for a hands-free coding experience.

## 🚀 Features
- **Code Generation**: Generate code from natural language descriptions.
- **Inline Comments**: Automatically add comments to explain code.
- **Code Explanation**: Understand the logic and purpose of code with AI-generated explanations.
- **Speech-to-Text Input**: Speak your code description instead of typing.
- **Text-to-Speech Output**: Listen to generated code and explanations.
- **Supports Multiple Languages**: Python, JavaScript, Java, C, C++, Ruby, Go, Swift, HTML, CSS, PHP, Rust, TypeScript.

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Backend AI**: Google Gemini AI
- **Speech Processing**: SpeechRecognition & Pyttsx3
- **Language Support**: Python

## 📂 Installation & Setup
### Prerequisites
- Python 3.8+
- A Google Gemini AI API key

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ai-code-assistant.git
   cd ai-code-assistant
   ```

2. **Create a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up API Key**:
   - Replace `GOOGLE_API_KEY` in `app.py` with your actual Gemini API key.
   - Or set it as an environment variable:
     ```bash
     export GOOGLE_API_KEY='your_api_key_here'  # Windows: set GOOGLE_API_KEY=your_api_key_here
     ```

5. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

## 🎥 Demo Video
[![Watch the demo](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

If your video is hosted on Google Drive, ensure the correct format:
- Use a direct Google Drive embed link:
  ```
  https://drive.google.com/file/d/YOUR_VIDEO_ID/preview
  ```
  Example:
  ```
  [Watch the Demo](https://drive.google.com/file/d/1QHltFWSL1sNRQeHwm4Uk2fUNss_E1pzd/preview)
  ```

## 📌 Usage Guide
1. Select the programming language.
2. Choose between generating code or adding comments & explanations.
3. Provide input via text or speech.
4. View and listen to AI-generated responses.
5. Copy, modify, and use the generated code in your projects.

## 🏆 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## 🐟 License
This project is licensed under the MIT License.

## 🙌 Acknowledgments
- Google Gemini AI for powering code generation.
- Streamlit for the interactive UI.
- SpeechRecognition & Pyttsx3 for speech processing.

---
Enjoy coding with AI! 🚀

