import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = headers)

    formatted_response = json.loads(response.text)

    response_dict = {
        "anger": formatted_response["emotionPredictions"][0]['emotion']["anger"],
        "disgust": formatted_response["emotionPredictions"][0]['emotion']["disgust"],
        "fear": formatted_response["emotionPredictions"][0]['emotion']["fear"],
        "joy": formatted_response["emotionPredictions"][0]['emotion']["joy"],
        "sadness": formatted_response["emotionPredictions"][0]['emotion']["sadness"]
    }

    dominant_emotion_score = 0
    for emotion in response_dict:
        if response_dict[emotion] > dominant_emotion_score:
            dominant_emotion_score = response_dict[emotion]
            dominant_emotion = emotion

    response_dict['dominant_emotion'] = dominant_emotion

    return response_dict
