import streamlit as st
from files import Text_Summarization as summarizer
from files import Sentiment_analysis as analyzer
from files import Grammar_Checker as checker
from files import voice_bot as voice
from files import Text_Generator as generator


st.set_page_config(page_title="Rumor", layout="wide", initial_sidebar_state="collapsed", page_icon='🤖')

if "voice" not in st.session_state:
    st.session_state.voice = "False"
if "terminal" not in st.session_state:
        st.session_state.terminal = 0

def toggle_voice():
    if(st.session_state.voice=="True"):
        voice.speak("Disabling Voice")
        st.session_state.voice="False"
    else:
        st.session_state.voice = "True"
        wish = voice.wish()
        voice.speak(f"{wish}!")

def speakitOut(response):
    voice.speak(f"Output Generated: {response}")
    

if st.session_state.get('voice_request'):
    st.session_state.voice = "True"
    wish = voice.wish()
    voice.speak(f"{wish}!")

if st.session_state.get('disable_voice'):
    st.session_state.voice = "False"


def speakout(text):
    if st.session_state.get("speak"):
        voice.speak(text)
    

def operation(text, key):
    if(key=="checker"):
        return checker.check_grammar(text)


col1, col2 = st.columns([2,1], gap="large")
with col1:
    with(st.container(border=True, height=640)):
        st.title("Rumor")
        st.text_area(label="Choices" ,value="1: Text Generation\n2: Text Summarization\n3: Sentiment Analysis\n4: Grammar Checker", height=120)

        colx, coly = st.columns([0.15,0.85])
        with colx:
            st.button("Enable Voice" if st.session_state.voice=="False" else "Disable Voice", on_click=toggle_voice)
                
        with coly:
            st.write("")
            st.text("Voice Enabled" if st.session_state.voice=="True" else "")
        
        choice = st.selectbox("Select your choice", (0,1,2,3,4))
        text = st.text_area("Enter your text", height=130)
        
        button = st.button("Generate", type="primary", use_container_width=True, help="Click to generate")
        
with col2:
    if(button):
        if(choice==0):
            with st.container(border=True):
                st.write("Select a valid choice")
                if(st.session_state.voice=="True"):
                    voice.speak("Select a valid choice")

        if(choice==1):
            st.subheader("Generated Output")
            if(text!=""):
                with st.spinner("Generating"):
                    response = generator.generate(text, 100)
                if(response):
                    with st.container(height=570, border=False):
                        st.write(response)

                if(response and st.session_state.voice=="True"):
                    voice.speak(f"Response Generated")
            else:
                st.write("Enter some Text for Generation")
                if(st.session_state.voice=="True"):
                        voice.speak("Enter some Text for Generation")

        if(choice==2):
            st.subheader("Summarized Output")
            if(text!=""):
                output = summarizer.textsumarization(text)
                with st.container(height=570, border=False):
                    st.write(output)
                if(st.session_state.voice=="True"):
                    voice.speak("Text Summarized")
                    
                    
            else:
                st.write("Enter some Text for Summarization")
                if(st.session_state.voice=="True"):
                        voice.speak("Enter some Text for Summarization")
            
        
        if(choice==3):
            st.subheader("Predicted Analysis")
            if(text!=""):
                col1,col2 =st.columns(2)

                prediction = analyzer.predict_emotions(text)
                probability = analyzer.get_prediction_proba(text)

                if(prediction):
                    with col1:
                        st.success("Original Text")
                        st.write(text)

                    with col2:
                        st.success("Prediction")
                        emoji_icon = analyzer.emotions_emoji_dict[prediction]
                        st.write("{}:{}".format(prediction,emoji_icon))
                    
                    st.success("Prediction Probability")
                    st.write(probability)

                    if(st.session_state.voice=="True"):
                        voice.speak(f"Sentiment Analysis for the entered text is {prediction}")

            else:
                st.write("Enter Some Text for Sentiment Analysis")
                if(st.session_state.voice=="True"):
                    voice.speak("Enter Some Text for Sentiment Analysis")
                
        
        if(choice==4):
            st.subheader("Grammar Checking Results")
            if(text!=""):
                result = checker.check_grammar(text)
                st.write(result)
                st.subheader("Original Text")
                st.write(text)
                if(st.session_state.voice=="True"):
                    voice.speak(result)
            else:
                st.write("Enter Some Text for Grammar Analysis")
                if(st.session_state.voice=="True"):
                    voice.speak("Enter Some Text for Grammar Analysis")
