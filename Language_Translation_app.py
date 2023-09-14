import streamlit as st
from transformers import pipeline
st.subheader('Solomon Kibon')
# Create a Streamlit app
st.title("Language Translation App")
st.write('Supported languages in this application include English (en), Spanish (es), French (fr), German (de), Italian (it), Portuguese (pt), Dutch (nl), Russian (ru), Chinese (zh), Japanese (ja), Korean (ko), and Arabic (ar).')
# Input text box for user to enter text
user_input = st.text_area("Enter text:")

# Language selection
source_lang = st.selectbox("Select source language:", ["en", "es", "fr", "de", "it", "pt", "nl", "ru", "zh", "ja", "ko", "ar"])
target_lang = st.selectbox("Select target language:", ["en", "es", "fr", "de", "it", "pt", "nl", "ru", "zh", "ja", "ko", "ar"])

# Translation function
def translate_text(text, source_lang, target_lang):
    translator = pipeline("translation", model=f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}")
    translation = translator(text)
    return translation[0]['translation_text']

if st.button("Translate"):
    if user_input:
        if source_lang != target_lang:
            translated_text = translate_text(user_input, source_lang, target_lang)
            st.success(f"Translated text ({source_lang} to {target_lang}):")
            st.write(translated_text)
        else:
            st.warning("Source and target languages are the same. Please choose different languages.")
    else:
        st.warning("Please enter text to translate.")
