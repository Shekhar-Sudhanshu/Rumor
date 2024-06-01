import os
import joblib

current = os.getcwd()
model_path = os.path.join(current, "models", "emotion_classifier_pipeline .pkl")


pipe_lr = joblib.load(open(model_path,"rb"))

def predict_emotions(docx):
    results = pipe_lr.predict([docx])
    return results[0]

def get_prediction_proba(docx):
    results = pipe_lr.predict_proba([docx])
    return results

emotions_emoji_dict = {"anger":"😠", "disgust":"🤮", "fear":"😨", "happy":"😁", "joy":"😂","neutral":"😐","sadness":"😭","shame":"😣","surprise":"🙀"}