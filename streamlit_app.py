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
    layout="centered"
)

# =====================================
# SESSION
# =====================================

if "history" not in st.session_state:
    st.session_state.history = []

# =====================================
# VOICE FUNCTIONS
# =====================================

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()


def listen_voice():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)
    except:
        return ""

# =====================================
# READ COMPLETE REPORT
# =====================================

def read_complete_report():

    text = ""

    if "plan" in st.session_state:
        text += "Research Plan\n\n"
        text += st.session_state.plan + "\n\n"

    if "research" in st.session_state:

        text += "Research Results\n\n"

        if isinstance(st.session_state.research, list):
            text += "\n".join(st.session_state.research)
        else:
            text += str(st.session_state.research)

        text += "\n\n"

    if "analysis" in st.session_state:
        text += "Analysis\n\n"
        text += st.session_state.analysis + "\n\n"

    if "report" in st.session_state:
        text += "Final Report\n\n"
        text += st.session_state.report

    if text:
        speak_text(text)
    else:
        st.warning("Please generate a report first.")

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.stApp{
background:linear-gradient(135deg,#0b1120,#111827,#1e293b);
}

.block-container{
max-width:1100px;
padding-top:30px;
}

.hero{
font-size:58px;
font-weight:900;
background:linear-gradient(90deg,#a855f7,#38bdf8);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
line-height:1.1;
}

.subtitle{
font-size:18px;
color:#94a3b8;
margin-top:-8px;
margin-bottom:25px;
}

.badge{
display:inline-block;
padding:10px 18px;
margin-right:10px;
margin-top:8px;
border-radius:25px;
background:#1e293b;
border:1px solid #6366f1;
color:white;
font-size:15px;
font-weight:bold;
}

.card{
background:#111827;
padding:25px;
border-radius:20px;
border:1px solid #334155;
margin-top:20px;
box-shadow:0 0 20px rgba(0,0,0,.35);
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
""", unsafe_allow_html=True)

st.markdown("""
<div>
<span class="badge">🧭 Planner</span>
<span class="badge">🔍 Researcher</span>
<span class="badge">📊 Analyst</span>
<span class="badge">✍ Writer</span>
<span class="badge">✅ Fact Checker</span>
</div>
""", unsafe_allow_html=True)

st.write("")

# =====================================
# INPUT
# =====================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("💬 Ask Anything")

col1, col2 = st.columns([5,1])

with col1:

    topic = st.text_input(
        "",
        placeholder="Type your research topic...",
        label_visibility="collapsed"
    )

with col2:

    if st.button("🎤 Voice"):

        voice = listen_voice()

        if voice:
            topic = voice

st.write("")

st.subheader("📁 Upload Document")

uploaded_file = st.file_uploader(
    "",
    type=["pdf","txt","docx"],
    label_visibility="collapsed"
)

st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# =====================================
# GENERATE REPORT
# =====================================

topic = topic.strip()

if topic != "":

    progress = st.progress(0)

    status = st.empty()

    with st.spinner("🤖 AI Agents are researching..."):

        status.info("🧭 Planner Agent Working...")
        progress.progress(20)
        plan = planner_agent(topic)

        status.info("🔍 Researcher Agent Working...")
        progress.progress(40)
        research = researcher_agent(topic)

        status.info("📊 Analyst Agent Working...")
        progress.progress(70)
        analysis = analyst_agent(topic, research)

        status.info("✍ Writer Agent Working...")
        progress.progress(90)
        report = writer_agent(topic, analysis)

        progress.progress(100)

    status.success("✅ Report Generated Successfully!")

    st.session_state.plan = plan
    st.session_state.research = research
    st.session_state.analysis = analysis
    st.session_state.report = report

    if topic not in st.session_state.history:
        st.session_state.history.append(topic)

# =====================================
# RESULTS
# =====================================

    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 Plan",
        "🌐 Research",
        "📊 Analysis",
        "📄 Final Report"
    ])

    with tab1:

        st.markdown(plan)

    with tab2:

        if isinstance(research, list):
            for item in research:
                st.write("•", item)
        else:
            st.write(research)

    with tab3:

        st.markdown(analysis)

    with tab4:

        st.markdown(report)

        st.write("")

        col1, col2 = st.columns(2)

        with col1:

            st.download_button(
                "⬇ Download Report",
                report,
                file_name=f"{topic}.txt",
                mime="text/plain",
                use_container_width=True
            )

        with col2:

            if st.button(
                "🔊 Read Report",
                use_container_width=True
            ):
                read_complete_report()

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.title("🤖 AI Dashboard")

    st.metric("📄 Reports", len(st.session_state.history))
    st.metric("🤖 AI Agents", "5")
    st.metric("⚡ Version", "9.0")

    st.markdown("---")

    st.subheader("📚 History")

    if st.session_state.history:

        for item in reversed(st.session_state.history):
            st.write("•", item)

    else:
        st.write("No history")

    st.markdown("---")

    st.success("🟢 System Online")

# =====================================
# FOOTER
# =====================================

st.divider()

st.caption("🚀 Professional AI Research Platform")

st.caption("👨‍💻 Built by Rushi | Version 9.0")