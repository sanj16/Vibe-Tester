# Vibe-Tester

## Overview

This project utilizes speech recognition and sentiment analysis to determine the sentiment of spoken words based on the tone of voice rather than the actual content. It employs the Google Speech Recognition API and the VADER sentiment analysis tool to provide insights into the emotional tone of the user's speech.

## Key Features

- **Speech Recognition:** The application captures audio input through a microphone using the SpeechRecognition library. The Google Speech Recognition API is then employed to convert spoken words into text.

- **Sentiment Analysis:** The VADER sentiment analysis tool assesses the emotional tone of the spoken text. It provides a compound sentiment score along with a corresponding message and image representation.

- **User Feedback:** The application displays a sentiment analysis result, including the compound sentiment score, a descriptive message, and an associated image reflecting the detected sentiment.

## Key Terms

- **Speech Recognition:** The process of converting spoken language into written text.

- **Sentiment Analysis:** The computational process of determining the emotional tone conveyed in a piece of text, often used to understand attitudes, opinions, and sentiments expressed by individuals.

- **VADER Sentiment Analysis:** A pre-trained model specifically designed for sentiment analysis that considers both the polarity and intensity of sentiments.

- **Compound Sentiment Score:** A numerical score provided by VADER, representing the overall sentiment of the text. Positive values indicate positive sentiments, negative values indicate negative sentiments, and values around zero suggest neutrality.

- **Tone of Voice:** The pitch, intonation, and rhythm of spoken words, which convey emotional nuances beyond the literal meaning of the words.

## Usage

1. Ensure you have the required dependencies installed. You can install them using the following:
    ```
    pip install tk vaderSentiment SpeechRecognition Pillow
    ```

2. Run the script by executing the provided Python code.

3. Click the "Analyze Sentiment" button to start the sentiment analysis process.

4. Speak into the microphone, and the application will analyze the sentiment based on the tone of your voice.

## Note

This project focuses on evaluating the emotional tone of speech rather than the semantic content. Keep in mind that the accuracy of sentiment analysis may vary based on factors such as background noise and individual speaking styles.

Feel free to experiment with different speech inputs and observe how the application interprets various tones of voice.

**Disclaimer:** This project relies on external APIs, and users are responsible for adhering to the terms and conditions of those services.

## Dependencies

- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [vaderSentiment](https://github.com/cjhutto/vaderSentiment)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [Pillow](https://python-pillow.org/)

