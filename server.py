from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# Route for the homepage (renders index.html)
@app.route("/")
def index():
    return render_template("index.html")

# Route for emotion detection
@app.route("/emotionDetector")
def emotionDetector():
    # Get text from request
    text_to_analyse = request.args.get("textToAnalyze")
    
    # Call emotion detector function
    result = emotion_detector(text_to_analyse)
    
    # Format response string
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
