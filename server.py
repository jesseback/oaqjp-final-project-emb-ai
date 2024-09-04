"""
This module initiates the application of emotion detection
to be executed over the Flask channel and deployed on
localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Receive text from the HTTP request and run emotion detection
    on it using the emotion_detector() function.
    The output returned shows the emotion scores and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Invalid input! Please provide text to analyze.", 400

    # Run the emotion detection function
    response = emotion_detector(text_to_analyze)

    # Format the response as requested
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return formatted_response

@app.route("/")
def render_index_page():
    """
    Render the main application page over the Flask channel.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Execute the Flask app and deploy it on localhost:5000
    app.run(host="0.0.0.0", port=5000)