import streamlit as st

# Dark theme colors (similar to main page)
DARK_THEME = {
    "background": "#1e1e2f",
    "text": "#ffffff",
    "box": "#2d2d44",
    "primary_accent": "#00c2ff",
    "secondary_accent": "#ff7f50",
    "button_hover": "#3e3e5a"
}

theme = DARK_THEME

# Inject CSS for chatbot page styling similar to main page
st.markdown(f"""
    <style>
        body, .css-18e3th9 {{
            background-color: {theme['background']} !important;
            color: {theme['text']} !important;
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }}
        .chatbot-container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            box-sizing: border-box;
            height: 90vh;
            display: flex;
            flex-direction: column;
        }}
        .chatbot-messages {{
            flex-grow: 1;
            background-color: {theme['box']};
            border-radius: 10px;
            padding: 20px;
            overflow-y: auto;
            margin-bottom: 10px;
            color: {theme['text']};
            font-family: Arial, sans-serif;
            font-size: 16px;
        }}
        .chatbot-input-area {{
            display: flex;
            align-items: center;
        }}
        .chatbot-input {{
            flex-grow: 1;
            padding: 10px;
            border-radius: 20px 0 0 20px;
            border: none;
            outline: none;
            font-size: 16px;
            background-color: {theme['box']};
            color: {theme['text']};
        }}
        .chatbot-ask-button {{
            padding: 10px 20px;
            border-radius: 0 20px 20px 0;
            border: none;
            background-color: {theme['primary_accent']};
            color: white;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }}
        .chatbot-ask-button:hover {{
            background-color: {theme['secondary_accent']};
        }}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="chatbot-container">', unsafe_allow_html=True)

st.markdown('<div class="chatbot-messages">', unsafe_allow_html=True)
st.write("Welcome to mitra! How can I help you?")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="chatbot-input-area">', unsafe_allow_html=True)
user_input = st.text_input("", placeholder="Ask anything", key="chatbot_input", label_visibility="collapsed")
ask_button = st.button("Ask", key="chatbot_ask_button")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
