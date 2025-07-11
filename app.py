import streamlit as st
from utils.helpers import load_formulas

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

# Inject CSS for full page and components styling and hide sidebar globally
st.markdown(f"""
    <style>
        /* Hide Streamlit sidebar globally */
        [data-testid="stSidebar"] {{
            display: none;
        }}
        /* Expand main content to full width */
        [data-testid="stAppViewContainer"] {{
            margin-left: 0px;
            width: 100%;
        }}
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

# App UI with navigation and page switching

if 'page' not in st.session_state:
    st.session_state.page = 'selection'

if 'selected_class' not in st.session_state:
    st.session_state.selected_class = None

if 'selected_subject' not in st.session_state:
    st.session_state.selected_subject = None

if 'selected_topic' not in st.session_state:
    st.session_state.selected_topic = None

def show_selection_page():
    st.title("LearnLoop - Study Companion for Class 10–12")
    st.write("Welcome! Select your class and subject to begin.")

    selected_class = st.selectbox("Select your class", ["10th", "11th", "12th"], key="class_select")

    if selected_class == "10th":
        subjects = ["Maths", "Science"]
    else:
        subjects = ["Maths", "Physics", "Chemistry", "Biology"]

    selected_subject = st.selectbox("Select your subject", subjects, key="subject_select")

    if st.button("Enter"):
        st.session_state.selected_class = selected_class
        st.session_state.selected_subject = selected_subject
        st.session_state.page = 'formulas'
        st.session_state.selected_topic = None

def show_formulas_page():
    st.title(f"Formulas for Class {st.session_state.selected_class} - {st.session_state.selected_subject}")

    # Example topics per subject - this can be extended or loaded dynamically
    topics_map = {
        "Maths": ["Algebra", "Geometry", "Trigonometry"],
        "Science": ["Physics Basics", "Chemistry Basics"],
        "Physics": ["Mechanics", "Optics", "Thermodynamics"],
        "Chemistry": ["Organic", "Inorganic", "Physical"],
        "Biology": ["Botany", "Zoology"]
    }

    topics = topics_map.get(st.session_state.selected_subject, [])

    # Sidebar for topics
    selected_topic = st.sidebar.radio("Select Topic", topics, index=0 if topics else -1)

    st.session_state.selected_topic = selected_topic

    # Load formulas for selected class and subject
    class_map = {
        "10th": "10",
        "11th": "11",
        "12th": "12"
    }
    class_level = class_map.get(st.session_state.selected_class, "10")

    formulas = load_formulas(class_level, st.session_state.selected_subject)

    st.subheader(f"📘 Formulas for {selected_topic}")

    # For demonstration, show all formulas (in real case, filter by topic)
    for name, formula in formulas.items():
        st.markdown(f"{name}: {formula}")

    if st.button("Back"):
        st.session_state.page = 'selection'
        st.session_state.selected_class = None
        st.session_state.selected_subject = None
        st.session_state.selected_topic = None

if st.session_state.page == 'selection':
    show_selection_page()
elif st.session_state.page == 'formulas':
    show_formulas_page()

# Chatbot icon that opens chatbot page in new tab
st.markdown("""
<style>
    #chatbot-icon-container {
        position: fixed;
        top: 20px;
        right: 20px;
        display: flex;
        align-items: center;
        cursor: pointer;
        z-index: 1000;
        user-select: none;
        animation: pulse 2s infinite;
        color: #00c2ff;
    }
    #chatbot-icon-container:hover {
        color: #ff7f50;
    }
    #chatbot-icon {
        font-size: 64px;
        margin-right: 10px;
    }
    #chatbot-text {
        font-size: 18px;
        font-weight: bold;
        white-space: nowrap;
        opacity: 0;
        transition: opacity 0.3s ease;
        pointer-events: none;
    }
    #chatbot-icon-container:hover #chatbot-text {
        opacity: 1;
        pointer-events: auto;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
</style>

<a id="chatbot-icon-container" href="/chatbot_page" target="_blank" title="mitra chatbot" role="button" tabindex="0" aria-label="Open mitra chatbot" style="text-decoration:none; color: inherit;">
    <div id="chatbot-icon">🤖</div>
    <div id="chatbot-text">Hey!! here is your mitra</div>
</a>
""", unsafe_allow_html=True)
