import requests  # Import the requests library to handle HTTP requests
import json  # Import the json library to handle JSON data

def emotion_detector(text_to_analyze):  # Define a function named emotion_detector that takes a string input (text_to_analyze)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = {"raw_document": {"text": text_to_analyze}}  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json=myobj, headers=header)  # Send a POST request to the API with the text and headers

    # Convert the response text into a dictionary
    response_dict = json.loads(response.text)

    # Extract the relevant emotions and their scores from the correct path
    emotions = response_dict.get('emotionPredictions', [])[0].get('emotion', {})

    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)

    # Determine the dominant emotion
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return the required output format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
