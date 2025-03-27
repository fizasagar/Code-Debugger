import streamlit as st

# Custom CSS for theme colors
st.markdown("""
    <style>
        body {
            background-color: #a7d1f9;
            color: #1d248a;
        }
        .stApp {
            background-color: #a7d1f9;
        }
        .stButton>button {
            background-color: #3674B5;
            color: white;
        }
        .stTextInput>div>div>input {
            border-color: #4138f3;
        }
    </style>
""", unsafe_allow_html=True)

st.title("AI-Powered Code Debugger 🛠️")
st.write("This app helps you debug Python code with AI assistance.")

code = st.text_area("Paste your Python code here:")
if st.button("Debug Code"):
    st.success("This is where debugging output will appear!")  # Placeholder
