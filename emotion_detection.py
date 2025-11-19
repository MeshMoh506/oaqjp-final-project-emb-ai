import requests
import json

def emotion_detector(text_to_analyse):
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = { "raw_document": { "text": text_to_analyse } }
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(URL, json=myobj, headers=Headers)
    result = json.loads(response.text)
    
    # Extract emotions dictionary
    emotions = result["emotionPredictions"][0]["emotion"]
    
    # Filter only required emotions
    required_emotions = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"]
    }
    
    # Find dominant emotion (highest score)
    dominant_emotion = max(required_emotions, key=required_emotions.get)
    
    # Add dominant emotion to dictionary
    required_emotions["dominant_emotion"] = dominant_emotion
    
    return required_emotions
