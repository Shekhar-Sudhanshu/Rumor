import streamlit as st
import speech_recognition as sr
import pyttsx3
import datetime


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def wish():
    time = datetime.datetime.now()
    hour = time.hour
    response = ""
    if(hour>=0 and hour<12):
        response+="Good Morning"
        print(hour)
    if (hour>=12 and hour<17):
        response+="Good Afternoon"
        print(hour)
    if(hour>=17 and hour<24):
        response+="Good Evening"
        print(hour)
    return response

def listen(placeholder):
    st.session_state.terminal = 1
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Removing noise")
        if(st.session_state.terminal!=0):
            placeholder.info("Removing noise")

        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Speak now")

        if(st.session_state.terminal!=0):
            placeholder.success("Speak now 🎙️")

        audio = r.listen(source)
        output = ""

        try:
            myText = r.recognize_google(audio, language="en-IN")
            myText = myText.lower()
            output+=myText
            print(f"Did you say {myText}")

            if(st.session_state.terminal!=0):
                placeholder.success(f"Did you say {myText}")
        except:
            if(st.session_state.terminal!=0):
                placeholder.error("Couldn't Listen")
         
        st.session_state.terminal = 0
        return output

def user_chat(text):
    with st.chat_message("user"):
        st.markdown(text)

def bot_chat(text):
    if(text=="introduce"):
        text = "introduce yourself"
    if(text=="what you offer" or text=="services"):
        text = "what do you offer"
    if(text=="sleep now"):
        text = "sleep"

    responses = {"introduce yourself":"Hello! I am Rumor, an NLP assistant bot! We offer several content related services.",
                  "what do you offer":"We offer: Text Generation, Text Summarization, Sentiment Analysis, Grammar Checker. What would you like to choose?",
                  "exit":"Ok! Thank you!",
                  "bye":"Ok! Bye.",
                  "sleep":"Ok! Good night",
                  "nothing":"Okay"}
    
    if(text in responses):
        with st.chat_message("ai"):
            st.markdown(responses[text])
        speak(responses[text])
    else:
        with st.chat_message("ai"):
            st.markdown(text)
        speak(text)