import streamlit as st

# Dark theme colors (default)
DARK_THEME = {
    "background": "#1e1e2f",
    "text": "#ffffff",
    "box": "#2d2d44",
    "primary_accent": "#00c2ff",
    "secondary_accent": "#ff7f50",
    "button_hover": "#3e3e5a"
}

theme = DARK_THEME

# Inject CSS for full page and components styling
st.markdown(f"""
    <style>
        /* Page background and text */
        body, .css-18e3th9 {{
            background-color: {theme['background']} !important;
            color: {theme['text']} !important;
        }}

        /* Input boxes and select boxes */
        .stTextInput>div>div>input, .stSelectbox>div>div>div>div {{
            background-color: {theme['box']} !important;
            color: {theme['text']} !important;
        }}

        /* Buttons */
        .stButton>button {{
            background-color: {theme['primary_accent']} !important;
            color: {theme['text']} !important;
            border: none;
        }}
        .stButton>button:hover {{
            background-color: {theme['button_hover']} !important;
            color: {theme['text']} !important;
        }}

        /* Success message box */
        .stAlert-success {{
            background-color: {theme['box']} !important;
            color: {theme['text']} !important;
            border-radius: 5px;
            padding: 10px;
        }}

        /* Title and headers */
        h1, h2, h3, h4, h5, h6 {{
            color: {theme['primary_accent']} !important;
        }}

        /* Chatbot icon and text container */
        #chatbot-icon-container {{
            position: fixed;
            top: 20px;
            right: 20px;
            display: flex;
            align-items: center;
            cursor: pointer;
            z-index: 1000;
            user-select: none;
            animation: pulse 2s infinite;
            color: {theme['primary_accent']};
        }}
        #chatbot-icon-container:hover {{
            color: {theme['secondary_accent']};
        }}
        #chatbot-icon {{
            font-size: 64px;
            margin-right: 10px;
        }}
        #chatbot-text {{
            font-size: 18px;
            font-weight: bold;
            white-space: nowrap;
            opacity: 0;
            transition: opacity 0.3s ease;
            pointer-events: none;
        }}
        #chatbot-icon-container:hover #chatbot-text {{
            opacity: 1;
            pointer-events: auto;
        }}

        /* Pulse animation */
        @keyframes pulse {{
            0% {{ transform: scale(1); }}
            50% {{ transform: scale(1.1); }}
            100% {{ transform: scale(1); }}
        }}

        /* Chatbot popup container */
        #chatbot-popup {{
            position: fixed;
            bottom: 80px;
            right: 20px;
            width: 320px;
            height: 400px;
            background-color: {theme['box']};
            color: {theme['text']};
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            padding: 10px;
            z-index: 1001;
            display: none;
            flex-direction: column;
        }}

        /* Show popup */
        #chatbot-popup.show {{
            display: flex;
        }}

        /* Popup header */
        #chatbot-popup-header {{
            font-weight: bold;
            font-size: 1.2em;
            margin-bottom: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        /* Close button */
        #chatbot-popup-close {{
            cursor: pointer;
            font-size: 1.2em;
            color: {theme['primary_accent']};
        }}
        #chatbot-popup-close:hover {{
            color: {theme['secondary_accent']};
        }}

        /* Chat messages */
        #chatbot-messages {{
            flex-grow: 1;
            overflow-y: auto;
            background-color: {theme['background']};
            padding: 8px;
            border-radius: 5px;
            margin-bottom: 10px;
        }}

        /* Input area */
        #chatbot-input {{
            display: flex;
        }}
        #chatbot-input input[type="text"] {{
            flex-grow: 1;
            padding: 6px;
            border-radius: 5px 0 0 5px;
            border: 1px solid {theme['primary_accent']};
            outline: none;
            color: {theme['text']};
            background-color: {theme['box']};
        }}
        #chatbot-input button {{
            padding: 6px 12px;
            border-radius: 0 5px 5px 0;
            border: none;
            background-color: {theme['primary_accent']};
            color: white;
            cursor: pointer;
        }}
        #chatbot-input button:hover {{
            background-color: {theme['secondary_accent']};
        }}
    </style>
""", unsafe_allow_html=True)

# App UI
st.title("LearnLoop - Study Companion for Class 10–12")
st.write("Welcome! Select your class and subject to begin.")

selected_class = st.selectbox("Select your class", ["10th", "11th", "12th"], key="class_select")

if selected_class == "10th":
    subjects = ["Maths", "Science"]
else:
    subjects = ["Maths", "Physics", "Chemistry", "Biology"]

selected_subject = st.selectbox("Select your subject", subjects, key="subject_select")

st.success(f"Showing content for Class {selected_class} - {selected_subject}")

# Chatbot icon and popup HTML with minimal JS for toggle
st.markdown("""
<div id="chatbot-icon-container" title="mitra chatbot" role="button" tabindex="0" aria-label="Open mitra chatbot">
    <div id="chatbot-icon">🤖</div>
    <div id="chatbot-text">Hey!! here is your mitra</div>
</div>

<div id="chatbot-popup" role="dialog" aria-modal="true" aria-labelledby="chatbot-popup-header">
    <div id="chatbot-popup-header">
        mitra
        <span id="chatbot-popup-close" role="button" tabindex="0" aria-label="Close chatbot popup">&times;</span>
    </div>
    <div id="chatbot-messages">
        <p>Welcome to mitra! How can I help you?</p>
    </div>
    <div id="chatbot-input">
        <input type="text" id="chatbot-text" placeholder="Type your message..." />
        <button id="chatbot-send">Send</button>
    </div>
</div>

<script>
const icon = window.parent.document.getElementById('chatbot-icon');
const popup = window.parent.document.getElementById('chatbot-popup');
const closeBtn = window.parent.document.getElementById('chatbot-popup-close');

if(icon && popup && closeBtn) {
    icon.addEventListener('click', () => {
        popup.classList.toggle('show');
    });
    closeBtn.addEventListener('click', () => {
        popup.classList.remove('show');
    });
}
</script>
""", unsafe_allow_html=True)