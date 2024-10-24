import streamlit as st
from dotenv import load_dotenv
import os
import azure.cognitiveservices.speech as speech_sdk
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Streamlit page configuration
st.set_page_config(
    page_title="Text-to-Speech Converter",
    page_icon="🗣️",  # Emoji for the icon
    layout="centered",     # Options: "centered" or "wide"
    initial_sidebar_state="expanded",  # Options: "auto", "expanded", "collapsed"
)

# Load environment variables
load_dotenv()

# Azure Speech SDK configurations
speech_key = os.getenv("SPEECH_KEY")
speech_region = os.getenv("SPEECH_REGION")
speech_endpoint = os.getenv("ENDPOINT")
language_key = os.getenv("AI_SERVICE_KEY")
language_endpoint = os.getenv("AI_SERVICE_ENDPOINT")

# Initialize Speech SDK configuration
speech_config = speech_sdk.SpeechConfig(subscription=speech_key, region=speech_region)

# Language and voice mapping
language_voices = {
    "English (US)": ["en-US-JennyNeural", "en-US-GuyNeural"],
    "Spanish (Spain)": ["es-ES-ElviraNeural", "es-ES-AlvaroNeural"],
    "French (France)": ["fr-FR-DeniseNeural", "fr-FR-HenriNeural"],
    "German (Germany)": ["de-DE-KatjaNeural", "de-DE-ConradNeural"],
    "Hindi (India)": ["hi-IN-SwaraNeural", "hi-IN-MadhurNeural"],
    "Tamil (India)": ["ta-IN-PallaviNeural"],
    "Telugu (India)": ["te-IN-MohanNeural"],
    "Kannada (India)": ["kn-IN-GaganNeural"],
    "Gujarati (India)": ["gu-IN-DhwaniNeural"],
    "Assamese (India)": ["as-IN-JintiNeural"],
    "Rajasthani (India, using Hindi TTS)": ["hi-IN-MadhurNeural"],  # Rajasthani mapped to Hindi
    "Malwi (India, using Hindi TTS)": ["hi-IN-MadhurNeural"],       # Malwi mapped to Hindi
    "Haryanvi (India, using Hindi TTS)": ["hi-IN-SwaraNeural"],      # Haryanvi mapped to Hindi
    "Bengali (India)": ["bn-IN-BashkarNeural"],
    "Punjabi (India)": ["pa-IN-JagtarNeural"],
    "Marathi (India)": ["mr-IN-AarohiNeural"]
}

# Custom CSS for a modern look
st.markdown(
    """
    <style>
    .main {
        background-color: #433878;
        padding: 0px;
        border-radius: 0px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stButton > button {
        border: 1px solid #3498db;
        background-color: #CB80AB;
        color: white;
        padding: 8px 16px;
        font-size: 16px;
        border-radius: 10px;
    }
    .stButton > button:hover {
        background-color: #E6D9A2;
    }
    .sidebar .sidebar-content {
        background-color: #1abc9c;
        color: white;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Function to synthesize speech with chosen options
def speak_out(input_text, voice, speed=1.0):
    try:
        sample_rate=44110
        # Set voice
        speech_config.speech_synthesis_voice_name = voice
        
        # Use an audio file output
        # audio_output = speech_sdk.audio.AudioOutputConfig(filename="output_audio.wav")
        synthesizer = speech_sdk.SpeechSynthesizer(speech_config=speech_config)
        # st.audio("output_audio.wav", sample_rate=sample_rate)
        
        # Synthesize speech
        speech_synthesis_result = synthesizer.speak_text_async(input_text).get()
        
        # Check the result
        if speech_synthesis_result.reason == speech_sdk.ResultReason.SynthesizingAudioCompleted:
            st.success("Speech synthesis completed!")
            # Convert the synthesized audio result to a playable format
            audio_stream = io.BytesIO(result.audio_data)
            st.audio(audio_stream, format='audio/wav')
            
        elif speech_synthesis_result.reason == speech_sdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            st.error(f"Error during speech synthesis: {cancellation_details.reason} - {cancellation_details.error_details}")
        
    except Exception as e:
        st.error(f"Error during speech synthesis: {str(e)}")


# Function to display text input
def enter_text():
    return st.text_area("Enter your text here:", height=200)

# Function to select language and voice
def language_voice_selector():
    language = st.selectbox("Select Language", options=list(language_voices.keys()))
    voice = st.selectbox("Select Voice", options=language_voices[language])
    return language, voice

# Function to handle multiple pages
def multi_page_app():
    st.sidebar.title("🌐 Navigation")
    page = st.sidebar.radio("Choose a Language", options=["Home", "English", "Spanish", "French", "German", "Hindi", "Tamil", "Kannada", "Telugu", "Gujarati", "Marathi", "Assamese", "Rajasthani", "Malwi", "Haryanvi", "Bengali", "Punjabi"])
    
    if page == "Home":
        st.title("🌍Multilingual Text-to-Speech Converter🌍");
        st.write("")
        st.write("""
            This application allows you to convert text to speech in multiple languages.
            Choose a language from the sidebar to explore the features for that language.
        """)
        st.image("home_img.jpg", use_column_width=True)
        
    elif page == "English":
        st.title("🇺🇸 English Text-to-Speech Converter")
        process_language_page("English (US)")
    
    elif page == "Spanish":
        st.title("🇪🇸 🤖 Spanish Text-to-Speech Converter")
        process_language_page("Spanish (Spain)")
    
    elif page == "French":
        st.title("🇫🇷 🤖 French Text-to-Speech Converter")
        process_language_page("French (France)")
    
    elif page == "German":
        st.title("🇩🇪 🤖 German Text-to-Speech Converter")
        process_language_page("German (Germany)")
    
    elif page == "Hindi":
        st.title("🇮🇳 🤖 Hindi Text-to-Speech Converter")
        process_language_page("Hindi (India)")
        
    elif page == "Tamil":
        st.title("🇮🇳 🤖 Tamil Text-to-Speech Converter")
        process_language_page("Tamil (India)")
        
    elif page == "Telugu":
        st.title("🇮🇳 🤖 Telugu Text-to-Speech Converter")
        process_language_page("Telugu (India)")
        
    elif page == "Kannada":
        st.title("🇮🇳 🤖 Kannada Text-to-Speech Converter")
        process_language_page("Kannada (India)")
        
    elif page == "Gujarati":
        st.title("🇮🇳 🤖 Gujarati Text-to-Speech Converter")
        process_language_page("Gujarati (India)")
        
    elif page == "Assamese":
        st.title("🇮🇳 🤖 Assamese Text-to-Speech Converter")
        process_language_page("Assamese (India)")

    elif page == "Rajasthani":
        st.title("🇮🇳 🤖 Rajasthani Text-to-Speech Converter")
        process_language_page("Rajasthani (India, using Hindi TTS)")
    
    elif page == "Malwi":
        st.title("🇮🇳 🤖 Malwi Text-to-Speech Converter")
        process_language_page("Malwi (India, using Hindi TTS)")
        
    elif page == "Haryanvi":
        st.title("🇮🇳 🤖 Haryanvi Text-to-Speech Converter")
        process_language_page("Haryanvi (India, using Hindi TTS)")
        
    elif page == "Bengali":
        st.title("🇮🇳 🤖 Bengali Text-to-Speech Converter")
        process_language_page("Bengali (India)")
        
    elif page == "Punjabi":
        st.title("🇮🇳 🤖 Punjabi Text-to-Speech Converter")
        process_language_page("Punjabi (India)")
        
    elif page == "Marathi":
        st.title("🇮🇳 🤖 Marathi Text-to-Speech Converter")
        process_language_page("Marathi (India)")

# Function to handle the core features per language
def process_language_page(language_key):
    language, voice = language_key, st.selectbox("Select Voice", options=language_voices[language_key])
    text_input = enter_text()
    
    # Speech speed control
    speed = st.slider("Adjust Speech Speed", min_value=0.5, max_value=2.0, step=0.1, value=1.0)
    
    # Text summarization and sentiment analysis
    if st.checkbox("Enable Text Summarization"):
        summary_text = summarize_text(text_input)
        st.write(summary_text)
        st.success("Text summarized successfully!")
    
    if st.checkbox("Perform Sentiment Analysis"):
        sentiment = analyze_sentiment(text_input)
        st.info(f"Sentiment of the text: {sentiment}")
    
    # Speak out the text
    if st.button("Convert to Speech"):
        if text_input:
            speak_out(text_input, voice, speed)
        else:
            st.warning("Please enter some text.")

# Text summarization (simple example, can be extended)
def summarize_text(text):
    # Placeholder summarization logic
    return text[:200] + "..." if len(text) > 200 else text

# Sentiment analysis (simple example, can be extended)
def analyze_sentiment(text):
    client = TextAnalyticsClient(endpoint=language_endpoint, credential=AzureKeyCredential(language_key))
    documents = [text]
    response = client.analyze_sentiment(documents=documents)[0]
    return response.sentiment

# Main app function
if __name__ == "__main__":
    # st.set_page_config("Multilingual TTS🗣️")
    st.markdown('<div class="main">', unsafe_allow_html=True)
    
    multi_page_app()  # Start the multi-page app
    st.markdown('</div>', unsafe_allow_html=True)
