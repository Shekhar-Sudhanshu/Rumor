import streamlit as st
from files import voice_bot as voice
from files import Text_Generator as generator
from files import Text_Summarization as summarizer
from files import Sentiment_analysis as analyzer
from files import Grammar_Checker as checker

st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_icon='🎙️')

if "terminal" not in st.session_state:
    st.session_state.terminal = 0
if "visit" not in st.session_state:
        st.session_state.visit = 0
if "input_option" not in st.session_state:
     st.session_state.input_option = "disable"
if "key" not in st.session_state:
    st.session_state.key = ""


def operations(key, text):
    if(text!=""):
        if(key=="text generation"):
            placeholder.info("Generating")
            with st.spinner():
                st.write(generator.generate(text, 100))
            placeholder.success("Generated")
            voice.speak(f"Content Generated on the topic {text}")
        elif(key=="text summarization"):
            placeholder.info("Summarizing")
            st.write(summarizer.textsumarization(text))
            placeholder.success("Summarized")
            voice.speak("Text Summarized")
        elif(key=="sentiment analysis"):
            placeholder.info("Analyzing")
            col1,col2 =st.columns(2)
            prediction = analyzer.predict_emotions(text)
            probability = analyzer.get_prediction_proba(text)

            if(prediction):
                placeholder.success("Generated")
                with col1:
                    st.success("Original Text")
                    st.write(text)

                with col2:
                    st.success("Prediction")
                    emoji_icon = analyzer.emotions_emoji_dict[prediction]
                    st.write("{}:{}".format(prediction,emoji_icon))
                
                st.success("Prediction Probability")
                st.write(probability)

                voice.speak(f"Sentiment Analysis for the text {text} is {prediction}")

        elif(key=="grammar checker"):
            placeholder.info("Checking")
            with st.status("Checking"):
                result = checker.check_grammar(text)
                st.write(result)
            placeholder.success("Generated  ")
            voice.speak(result)
    else:
        placeholder.error("Invalid")
            
        voice.speak("Invalid")



with st.form(key="voice_form", border=False):
    col1, col2, col3 = st.columns([0.25,0.6,0.3], gap="large")
    with col1:
        st.header("Terminal", divider=True)
        placeholder = st.empty()

        if(st.session_state.terminal == 0):
            placeholder.info("None")

        with st.expander("Utility Commands", expanded=True):
            st.text("Introduce yourself -\nTo introduce")
            st.divider()
            st.text("What do you offer -\nTo know about services")
            st.divider()
            st.text("Exit -\nTo exit")

        
                            
    with col3:
        st.header("Output", divider=True)

       
        text = st.text_area(label="Input here")
        submit = st.form_submit_button("Done!")
        if(submit):
            operations(st.session_state.key, text)



    with col2:
        st.divider()
        st.title("🤖 Rumor - Voice Bot")
        with st.container(height=520):
            if(st.session_state.visit==0):
                wish = voice.wish()
                msg = wish + "! How can I help you?"
                voice.bot_chat(msg)
                st.session_state.visit=1
                
            while(True):
                command = voice.listen(placeholder)
                command = command.lower()
                if(command==""):
                    continue
                elif(command==None):
                    continue
                elif(command=="text generation" or command=="sentiment analysis" or command=="text summarization" 
                     or command=="text summarisation" or command=="grammar checker"):
                    voice.user_chat(command)
                    voice.bot_chat("Ok! Enter the text in the Input here option")
                    
                    
                    st.session_state.key = command


                elif(command=="exit" or command=="sleep" or command=="bye"):
                        voice.user_chat(command)
                        voice.bot_chat(command)
                        break
                elif(command!=""):
                    voice.user_chat(command)
                    voice.bot_chat(command)