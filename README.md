# Text to Speech Conversion App

### This project is a Text to Speech (TTS) conversion application built using Streamlit and Azure Cognitive Services. The application takes user input (text), converts it into speech using Azure's TTS service, and plays the audio directly in the browser.

---

## Live URL of project:

You can check my project here: https://multilingual-text-to-speech-converter.streamlit.app/

![image](https://github.com/user-attachments/assets/c7f762c0-8144-41e0-a91a-cb44766b4418)

![image](https://github.com/user-attachments/assets/299bbd42-d194-40c5-b137-048d82335837)

## 🚀Features

-**Real-time Text to Speech Conversion:** Input any text and hear it spoken out loud.
-**Customizable Voices:** Choose from a variety of voices available via Azure Cognitive Services.
-**Adjustable Speech Speed:** Control the speed of the speech output.
-**In-browser Audio Playback:** Listen to the converted speech directly in the browser without downloading files.

---

## ⚙️Technologies Used

-**Streamlit:** A fast, easy-to-use web framework for building data apps in Python.
-**Azure Cognitive Services (Speech SDK):** Used for converting text to speech using cloud-based services.
-**Python:** Backend logic for handling TTS requests and managing the app.

---

## 🫴🏻Setup and Installation

### Prerequisites:

-Python 3.7+
-Azure account with access to Cognitive Services.
-Azure Speech API key and region.

### Installation Steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/text-to-speech-app.git
    cd text-to-speech-app
    ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   -On MacOS:
   
      ```bash
      source venv/bin/activate
      ```

   -On Windows:

       ```bash
       venv/Scripts/activate
       ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   pip install -r requirements.txt
   ```
---

## 👤Usage

1. Enter the text you want to convert to speech in the input box.
2. Select a voice from the dropdown menu.
3. Adjust the speech speed (optional).
4. Click the "Convert" button.
5. The app will synthesize the speech and play the audio directly in the browser.

--- 

## File structure

  ```bash
    text-to-speech-app/
    │
    ├── trial1.py            # Main Streamlit application
    ├── README.md            # Project documentation
    ├── requirements.txt     # Python dependencies
    ├── .env                 # Azure API credentials
    └── .gitignore           # Files to ignore in Git
  ```

---

## Azure Setup

To use Azure Cognitive Services for Text to Speech, you'll need:

1. A Microsoft Azure account.
2. Create a Speech resource in Azure and obtain the API key and region.
3. Add the API key and region to the .env file as shown above.
4. Dependencies
5. The required dependencies are listed in requirements.txt. Some of the main libraries include:

-azure-cognitiveservices-speech
-streamlit
-python-dotenv

### You can install them using:

  ```bash
    pip install -r requirements.txt
  ```

---

## Future Enhancements

1. Add more customization options for speech (e.g., pitch, volume).
2. Support for multiple languages.
3. Integration with other TTS services for comparison.

---

## Contributing

Feel free to open issues or submit pull requests if you'd like to contribute!

---

## License

This project is licensed under the MIT License.

