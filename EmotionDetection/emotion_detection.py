import requests ,json

def emotion_detector(text_to_analyze):

    url="https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}    
    myobj={ "raw_document": { "text": text_to_analyze } }
    response=requests.post(url,json=myobj,headers=headers)
    formatted_response=json.loads(response.text)
    for data in formatted_response['emotionPredictions']:
        for k, v in data.items():

            max_key=max(v,key=v.get)
            
            v['dominant_emotion']=max_key    
            return v     