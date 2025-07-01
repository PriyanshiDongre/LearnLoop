import streamlit as st

# Dark theme colors (same as main page)
DARK_THEME = {
    "background": "#000000",
    "text": "#ffffff",
    "box": "#000000",
    "primary_accent": "#00c2ff",
    "secondary_accent": "#ff7f50",
    "button_hover": "#3e3e5a"
}

theme = DARK_THEME

# Inject CSS for chatbot page styling to match main page and hide sidebar
st.markdown(f"""
    <style>
        /* Hide Streamlit sidebar */
        [data-testid="stSidebar"] {{
            display: none;
        }}
        /* Expand main content to full width */
        [data-testid="stAppViewContainer"] {{
            margin-left: 0px;
            width: 100%;
            height: 100vh;
            display: flex;
            flex-direction: column;
            background-color: {theme['background']} !important;
            color: {theme['text']} !important;
            font-family: Arial, sans-serif;
        }}
        body, .css-18e3th9 {{
            margin: 0;
            padding: 0;
            height: 100%;
            display: flex;
            flex-direction: column;
            background-color: {theme['background']} !important;
            color: {theme['text']} !important;
            font-family: Arial, sans-serif;
        }}
        .chatbot-container {{
            flex-grow: 1;
            overflow-y: auto;
            max-width: 700px;
            margin: 20px auto 0 auto;
            padding: 20px;
            box-sizing: border-box;
            background-color: {theme['box']};
            border-radius: 10px;
            box-shadow: none;
            color: {theme['text']};
            font-size: 16px;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }}
        .chatbot-header {{
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
            color: {theme['primary_accent']};
        }}
        .chatbot-input-area {{
            position: fixed;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
            max-width: 700px;
            background-color: {theme['box']};
            padding: 10px 20px;
            box-sizing: border-box;
            display: flex;
            align-items: center;
            border-top: none;
            border-radius: 0 0 10px 10px;
            box-shadow: none;
        }}
        .chatbot-input {{
            flex-grow: 1;
            padding: 12px;
            font-size: 16px;
            border-radius: 8px 0 0 8px;
            border: none;
            outline: none;
            color: {theme['text']};
            background-color: {theme['background']};
            box-sizing: border-box;
            border: 1px solid {theme['primary_accent']};
        }}
        .chatbot-ask-button {{
            padding: 12px 24px;
            font-size: 16px;
            border-radius: 0 8px 8px 0;
            border: none;
            background-color: {theme['primary_accent']};
            color: white;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s ease;
            margin-left: 5px;
        }}
        .chatbot-ask-button:hover {{
            background-color: {theme['button_hover']};
        }}
    </style>
""", unsafe_allow_html=True)

# Chatbot UI layout
st.markdown('<div class="chatbot-container">', unsafe_allow_html=True)

st.markdown('<div class="chatbot-header">Mitra Chatbot</div>', unsafe_allow_html=True)

# Placeholder for chat messages (empty for now)
st.markdown('<div style="flex-grow:1;"></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="chatbot-input-area">', unsafe_allow_html=True)
user_input = st.text_input("", placeholder="Type your question here...", key="chatbot_input", label_visibility="collapsed", help="Type your question here")
ask_button = st.button("Ask", key="chatbot_ask_button")
st.markdown('</div>', unsafe_allow_html=True)
