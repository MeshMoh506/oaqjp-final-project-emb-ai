"""
Flask server for Emotion Detection application.
Provides a web interface and API endpoint to analyze emotions in text.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the homepage with the input form.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def emotionDetector():
    """
    Handle emotion detection requests.
    Accepts text input via query parameter 'textToAnalyze',
    calls the emotion_detector function, and returns formatted results.
    """
    text_to_analyse = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyse)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
