import streamlit as st
import speech_recognition as sr
import pyttsx3

from agents.planner import planner_agent
from agents.researcher import researcher_agent
from agents.analyst import analyst_agent
from agents.writer import writer_agent

# =====================================
# PAGE SETTINGS
# =====================================

st.set_page_config(
    page_title="AI Research Studio",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =====================================
# SESSION
# =====================================

if "history" not in st.session_state:
    st.session_state.history = []

# =====================================
# VOICE FUNCTIONS
# =====================================

import platform
import speech_recognition as sr
import pyttsx3


def speak_text(text):

    if platform.system() != "Windows":

        st.info("🔊 Voice reading works only on Windows.")
        return

    try:

        engine = pyttsx3.init()

        engine.setProperty("rate", 170)

        engine.say(text)

        engine.runAndWait()

    except Exception:

        st.warning("Voice engine is unavailable.")


def listen_voice():

    recognizer = sr.Recognizer()

    try:

        with sr.Microphone() as source:

            st.info("🎤 Speak Now...")

            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(source)

        return recognizer.recognize_google(audio)

    except Exception:

        st.warning("Voice input is unavailable.")

        return ""
# =====================================
# READ REPORT
# =====================================

def read_complete_report():

    text=""

    if "plan" in st.session_state:

        text += "Research Plan\n\n"

        text += st.session_state.plan

        text += "\n\n"

    if "research" in st.session_state:

        text += "Research Results\n\n"

        if isinstance(st.session_state.research,list):

            text += "\n".join(st.session_state.research)

        else:

            text += str(st.session_state.research)

        text += "\n\n"

    if "analysis" in st.session_state:

        text += "Analysis\n\n"

        text += st.session_state.analysis

        text += "\n\n"

    if "report" in st.session_state:

        text += "Final Report\n\n"

        text += st.session_state.report

    if text:

        speak_text(text)

    else:

        st.warning("Generate a report first.")
# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.stApp{
background:radial-gradient(circle at top,#1d1638,#0d1018 60%,#090909);
}

.block-container{
max-width:1100px;
padding-top:35px;
}

.hero{
font-size:68px;
font-weight:900;
line-height:1.1;
background:linear-gradient(90deg,#b388ff,#40c4ff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.subtitle{
color:#9CA3AF;
font-size:18px;
margin-top:-10px;
margin-bottom:30px;
}

.badge{
display:inline-block;
padding:8px 18px;
margin:5px;
border-radius:25px;
background:#1c1b34;
border:1px solid #7c3aed;
color:white;
font-size:15px;
font-weight:bold;
}

.card{
background:#111827;
border:1px solid #262f42;
padding:25px;
border-radius:22px;
margin-top:20px;
box-shadow:0px 10px 35px rgba(0,0,0,.35);
}

.result-card{
background:#151823;
padding:25px;
border-radius:18px;
border:1px solid #343a46;
color:white;
line-height:1.8;
font-size:16px;
margin-top:10px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# HERO
# =====================================

st.markdown("""
<div class="hero">
🤖 AI-Powered Multi-Agent Research Assistant
</div>

<div class="subtitle">
Autonomous research pipeline powered by five specialized AI agents
</div>

<div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:20px;margin-bottom:25px;">

<div class="badge">🧭 Planner</div>

<div class="badge">🔍 Researcher</div>

<div class="badge">📊 Analyst</div>

<div class="badge">✍ Writer</div>

<div class="badge">✅ Fact Checker</div>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# =====================================
# INPUT
# =====================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("💬 Ask Anything")

col1,col2=st.columns([5,1])

with col1:

    topic=st.text_input(
        "",
        placeholder="Type your research topic...",
        label_visibility="collapsed"
    )

with col2:

    if st.button("🎤 Voice"):

        voice=listen_voice()

        if voice:

            topic=voice

            st.success(voice)

st.write("")

st.subheader("📁 Upload File")

uploaded_file=st.file_uploader(
    "",
    type=["pdf","txt","docx"],
    label_visibility="collapsed"
)

st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# GENERATE REPORT
# =====================================

topic = topic.strip()

if topic:

    progress = st.progress(0)

    status = st.empty()

    with st.spinner("🤖 AI Agents are Working..."):

        status.info("🧭 Planner Agent...")
        progress.progress(20)

        plan = planner_agent(topic)

        status.info("🔍 Researcher Agent...")
        progress.progress(40)

        research = researcher_agent(topic)

        status.info("📊 Analyst Agent...")
        progress.progress(70)

        analysis = analyst_agent(topic, research)

        status.info("✍️ Writer Agent...")
        progress.progress(90)

        report = writer_agent(topic, analysis)

        progress.progress(100)

    status.success("✅ Research Completed Successfully!")

    st.session_state.plan = plan
    st.session_state.research = research
    st.session_state.analysis = analysis
    st.session_state.report = report

    if topic not in st.session_state.history:

        st.session_state.history.append(topic)

# =====================================
# RESULTS
# =====================================

if "report" in st.session_state:

    st.write("")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "🧭 Plan",
            "🌐 Research",
            "📊 Analysis",
            "📄 Final Report"
        ]
    )

    with tab1:

        st.markdown(f"""
        <div class="result-card">
        {st.session_state.plan}
        </div>
        """, unsafe_allow_html=True)

    with tab2:

        st.markdown(f"""
        <div class="result-card">
        {st.session_state.research}
        </div>
        """, unsafe_allow_html=True)

    with tab3:

        st.markdown(f"""
        <div class="result-card">
        {st.session_state.analysis}
        </div>
        """, unsafe_allow_html=True)

    with tab4:

        st.markdown(f"""
        <div class="result-card">
        {st.session_state.report}
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        col1, col2 = st.columns(2)

        with col1:

            st.download_button(
                "⬇ Download Report",
                st.session_state.report,
                file_name="research_report.txt",
                mime="text/plain",
                use_container_width=True
            )

        with col2:

           if platform.system() == "Windows":

              if st.button(
                 "🔊 Read Report",
                 key="read_report",
                 use_container_width=True
         ):

                 read_complete_report()

           else:

            st.info("🔊 Voice feature works only on Windows.")
# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.title("🤖 AI Dashboard")

    st.markdown("---")

    st.metric("📄 Reports", len(st.session_state.history))
    st.metric("🤖 AI Agents", "5")
    st.metric("⚡ Version", "9.0")

    st.markdown("---")

    st.subheader("📚 Research History")

    if st.session_state.history:

        for item in reversed(st.session_state.history):

            st.write("•", item)

    else:

        st.write("No History")

    st.markdown("---")

    st.success("🟢 System Online")

# =====================================
# FOOTER
# =====================================

st.write("")
st.write("")

st.divider()

st.caption("🚀 Professional AI Research Platform")

st.caption("👨‍💻 Built by Rushi | Version 9.0")