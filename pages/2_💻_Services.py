import streamlit as st
from streamlit_option_menu import option_menu
from files import Sentiment_analysis as analyzer
from files import Grammar_Checker as checker
from files import Text_Summarization as summarizer
from files import Text_Generator as generator

st.set_page_config(page_title="Services", layout="wide", initial_sidebar_state="collapsed", page_icon='💻')

selected = option_menu(
    menu_title=None,
    options=["Sentiment","Text Generator","Summarization","Grammar"],
    icons=["bar-chart-line", "card-text", "body-text", "alphabet-uppercase"],
    default_index=0,
    orientation="horizontal"
)

def Textgenerator():
    st.title("Text Generator")
    col1, col2 = st.columns([2,1])
    with col1:
        st.subheader("Generator")

        with st.form(key='text_gen_form'):
            raw_text = st.text_area("Type Here", height=200)
            num = st.number_input("Enter the number of words to be generated: ", min_value=5)
            submit_text = st.form_submit_button(label = 'Submit')
    with col2:
        if submit_text:
            st.subheader("Output")
            if(raw_text!="" and num>=5):
                with st.spinner("Generating"):
                    response = generator.generate(raw_text, num)
                    if(len(response)>0):
                        st.write(response)
            else:
                st.write("Enter some text for text generation")

def sentiment():
    st.title("Sentiment Analyzer")
    col1, col2 = st.columns([2,1])
    with col1:
        st.subheader("Emotion Detection")

        with st.form(key='emotion_clf_form'):
            raw_text = st.text_area("Type Here", height=250)
            submit_text = st.form_submit_button(label = 'Submit')

    with col2:
        if submit_text:
            st.subheader("Output")
            
            if(raw_text!=""):
                prediction = analyzer.predict_emotions(raw_text)
                probability = analyzer.get_prediction_proba(raw_text)

                colx,coly =st.columns(2)
                with colx:
                    st.success("Original Text")
                    st.write(raw_text)
                    st.success("Prediction Probability")
                    st.write(probability)

                with coly:
                    st.success("Prediction")
                    emoji_icon = analyzer.emotions_emoji_dict[prediction]
                    st.write("{}:{}".format(prediction,emoji_icon))
            else:
                st.write("Enter Some Text for Sentiment Analysis")

def summarization():
    st.title("Text Summarizer")
    col1, col2 = st.columns([2.5,1.5])
    with col1:
        st.subheader("Summarization")

        with st.form(key='text_summarizer'):
            text = st.text_area("Type Here", height=250)
            submit = st.form_submit_button(label="Submit")
    
    with col2:
        if(submit):
            st.subheader("Summarized Output")
            if(text!=""):
                result = summarizer.textsumarization(text)
                if(result!=""):
                    st.write(result)
                else:
                    st.write("Provide a bigger text")
            else:
                st.write("Enter some Text for Summarization")

def grammar():
    st.title("Grammar Analyzer")
    col1, col2 = st.columns([2,1])
    with col1:
        st.subheader("Grammar Checker & Corrector")

        with st.form(key='grammar_checker'):
            text = st.text_area("Type Here", height=250)
            submit = st.form_submit_button(label="Submit")
    
    with col2:
        if(submit):
            st.subheader("Grammar Checking Results")
            if(text!=""):
                with st.status('Checking'):
                    st.write(checker.check_grammar(text))
                st.subheader("Corrected Grammar")
                st.write(checker.correct_grammar(text))
            else:
                st.write("Enter Some Text for Grammar Analysis")

if(selected=="Text Generator"):
    Textgenerator()

elif(selected=="Sentiment"):
    sentiment()

elif selected=="Summarization":
    summarization()

elif(selected=="Grammar"):
    grammar()

