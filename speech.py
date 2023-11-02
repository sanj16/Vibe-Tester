import tkinter as tk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
from PIL import Image, ImageTk

recognizer = sr.Recognizer()

def analyze_sentiment():
    global recognizer

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recorded_audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(recorded_audio, language='en-US')

        analyser = SentimentIntensityAnalyzer()
        v = analyser.polarity_scores(text)
        compound_value = v['compound']

        if compound_value > 0.5:
            message = "You passed the vibe check"
            img_path = "happyy.png"
        elif compound_value < -0.5:
            message = "Your sadness is infectious fr"
            img_path = "sad.jpeg"
        else:
            message = "Your indecisive tone is getting on my nerves"
            img_path = "neutral.jpeg"

        img = Image.open(img_path)
        img = img.resize((100, 100), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img

        sentiment_result = f"Compound: {compound_value}\n{message}"
        result_label.config(text=sentiment_result)

        print(f"Positive: {v['pos']}, Negative: {v['neg']}, Neutral: {v['neu']}")

    except sr.UnknownValueError:
        sentiment_result = "Google Speech Recognition could not understand audio"
        result_label.config(text=sentiment_result)
    except sr.RequestError as e:
        sentiment_result = f"Could not request results from Google Speech Recognition service; {e}"
        result_label.config(text=sentiment_result)
    except Exception as ex:
        sentiment_result = f"{ex}"
        result_label.config(text=sentiment_result)

# Create the GUI window
root = tk.Tk()
root.title("Sentiment Analysis")
root.geometry("400x450")

# Configure background color
root.configure(bg='#a5cf61')

result_label = tk.Label(root, text="", bg='#a5cf61', font=("Helvetica", 11))  # Increased text size
result_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)  # Centered position

# Create a label to display an image
image_label = tk.Label(root, bg='#a5cf61')
image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create a button to trigger sentiment analysis
analyze_button = tk.Button(root, text="Analyze Sentiment", command=analyze_sentiment, bg="#315726",fg="white", font=("Helvetica", 10))
analyze_button.pack(side=tk.BOTTOM, anchor=tk.S, pady=50)

root.mainloop()
