import streamlit as st
import pdfplumber
import re
import io

# Set page config
st.set_page_config(page_title="Text Summarizer", layout="wide", page_icon="📝")

# Load custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📝 Text Summarizer")

# Sidebar
with st.sidebar:
    st.markdown("""
    ## About
    A powerful text summarization tool that helps you quickly extract key information from long texts.

    ## Features
    - Real-time summarization
    - File upload support
    - Multiple output formats

    ## Version
    1.0.0

    ## Source Code
    [GitHub Repository](https://github.com/meetchauhan1/text-summarizer)

    ---
    Powered by Streamlit and AI Summarization
    """)

# Session state defaults
if 'current_text' not in st.session_state:
    st.session_state.current_text = ""
if 'word_count' not in st.session_state:
    st.session_state.word_count = 0
if 'text_updated_from_file' not in st.session_state:
    st.session_state.text_updated_from_file = False

# File uploader
uploaded_file = st.file_uploader("Upload .txt or .pdf file", type=['txt', 'pdf'])

# File processing logic
if uploaded_file:
    try:
        if uploaded_file.type == "text/plain":
            content = uploaded_file.read().decode("utf-8")
        elif uploaded_file.type == "application/pdf":
            with pdfplumber.open(io.BytesIO(uploaded_file.getvalue())) as pdf:
                content = ' '.join([page.extract_text() or "" for page in pdf.pages])
        else:
            content = ""

        # Clean and store
        content = ' '.join(content.split())
        st.session_state.current_text = content
        st.session_state.word_count = len(content.split())
        st.session_state.text_updated_from_file = True

    except Exception as e:
        st.error(f"Failed to read file: {e}")
        st.session_state.current_text = ""
        st.session_state.word_count = 0
        st.session_state.text_updated_from_file = False

# If updated from file, don't override textarea on next rerun
if st.session_state.text_updated_from_file:
    text_input = st.text_area("Enter text to summarize:", value=st.session_state.current_text, height=200)
    st.session_state.text_updated_from_file = False  # Reset after displaying once
else:
    text_input = st.text_area("Enter text to summarize:", height=200)

# Update session state when user types manually
if text_input != st.session_state.current_text:
    st.session_state.current_text = text_input
    st.session_state.word_count = len(text_input.split())

# Analytics
st.markdown(f"""
<div style="background-color:#fff5e6;padding:16px;border-left:4px solid #ffb347;border-radius:8px">
<h3 style='color:#e67e22;'>📊 Text Analytics</h3>
<p><strong>Words:</strong> {st.session_state.word_count}</p>
</div>
""", unsafe_allow_html=True)

# Summary controls
summary_length = st.slider("Summary Length (%)", 10, 100, 50, step=10)
st.markdown("#### Output Format", unsafe_allow_html=True)
format_options = st.radio("Choose format", ["Plain Text", "Bullet Points", "Numbered List"], horizontal=True, label_visibility="collapsed")

# Summarizer function
def summarize_text(text, ratio, bullet_points=False, numbered_list=False):
    text = re.sub(r'\s+', ' ', text.strip())
    sentences = re.split(r'(?<=[.!?]) +', text)
    total = len(sentences)
    keep = max(1, int(total * ratio / 100))
    selected = sentences[:keep]

    if bullet_points:
        return "• " + "\n• ".join(selected)
    elif numbered_list:
        return "\n".join(f"{i+1}. {s}" for i, s in enumerate(selected))
    else:
        return " ".join(selected)

# Summarize
if st.button("Summarize"):
    if st.session_state.current_text.strip():
        summary = summarize_text(
            st.session_state.current_text,
            summary_length,
            bullet_points=(format_options == "Bullet Points"),
            numbered_list=(format_options == "Numbered List")
        )
        st.markdown("### Summary")
        st.code(summary)

        st.download_button("📥 Download Summary", data=summary, file_name="summary.txt", mime="text/plain")
    else:
        st.warning("Please enter or upload text to summarize.")
