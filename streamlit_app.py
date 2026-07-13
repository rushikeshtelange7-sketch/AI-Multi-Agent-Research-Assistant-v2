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
# VERSION 10.5 PREMIUM CSS
# =====================================

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.stApp{

background:
radial-gradient(circle at top,#2E1065 0%,#111827 45%,#05070D 100%);

color:white;

}

.block-container{

max-width:1450px;

padding-top:30px;

padding-left:50px;

padding-right:50px;

}

.hero{

font-size:72px;

font-weight:900;

line-height:1.05;

background:linear-gradient(90deg,#B388FF,#7C4DFF,#42A5F5,#40C4FF);

-webkit-background-clip:text;

-webkit-text-fill-color:transparent;

margin-bottom:10px;

}

.subtitle{

font-size:21px;

color:#BFC7D5;

margin-bottom:35px;

}

/* ---------------------------- */
/* AGENTS */
/* ---------------------------- */

.agents-row{

display:flex;

justify-content:flex-start;

align-items:center;

gap:18px;

flex-wrap:nowrap;

overflow-x:auto;

margin-top:25px;

margin-bottom:35px;

padding-bottom:10px;

}

.agent-card{

display:flex;

align-items:center;

justify-content:center;

min-width:190px;

height:68px;

border-radius:22px;

background:rgba(255,255,255,.06);

border:1px solid rgba(124,77,255,.7);

backdrop-filter:blur(20px);

font-size:20px;

font-weight:700;

color:white;

transition:.35s;

cursor:pointer;

box-shadow:0 0 18px rgba(124,77,255,.18);

}

.agent-card:hover{

transform:translateY(-5px);

border:1px solid #40C4FF;

box-shadow:0 0 35px rgba(64,196,255,.45);

}

/* ---------------------------- */
/* SEARCH */
/* ---------------------------- */

.search-card{

background:rgba(18,24,42,.85);

padding:18px;

border-radius:22px;

border:1px solid rgba(120,120,255,.18);

backdrop-filter:blur(20px);

box-shadow:0 0 35px rgba(70,120,255,.15);

margin-top:25px;

}

/* ---------------------------- */
/* RESULT */
/* ---------------------------- */

.result-card{

background:rgba(255,255,255,.05);

border-radius:22px;

padding:28px;

border:1px solid rgba(255,255,255,.12);

backdrop-filter:blur(25px);

box-shadow:0 10px 30px rgba(0,0,0,.25);

margin-top:15px;

line-height:1.8;

font-size:17px;

}

/* ---------------------------- */
/* DASHBOARD */
/* ---------------------------- */

.dashboard{

background:rgba(255,255,255,.05);

border:1px solid rgba(255,255,255,.08);

border-radius:20px;

padding:16px;

width:100%;

min-height:140px;

backdrop-filter:blur(18px);

box-shadow:0 6px 18px rgba(0,0,0,.20);

transition:all .3s ease;

}

.dashboard:hover{

transform:translateY(-3px);

box-shadow:0 0 22px rgba(64,196,255,.30);

}

.metric{

font-size:30px;

font-weight:800;

color:#4FC3F7;

margin-top:8px;

margin-bottom:4px;

line-height:1.1;

}

.label{

font-size:13px;

color:#BFC7D5;

margin-bottom:10px;

}

.glow{

box-shadow:0 0 20px rgba(64,196,255,.15);

}

.dashboard h2{

font-size:22px;

font-weight:700;

margin-bottom:12px;

}

.dashboard h3{

font-size:18px;

font-weight:600;

margin-bottom:10px;

}

/* ---------------------------- */
/* BUTTONS */
/* ---------------------------- */

.stButton>button{

height:48px;

border-radius:14px;

font-size:16px;

font-weight:700;

background:linear-gradient(90deg,#7C4DFF,#42A5F5);

border:none;

color:white;

transition:.3s;

}

.stButton>button:hover{

transform:translateY(-2px);

box-shadow:0 0 18px rgba(64,196,255,.40);

}

/* ---------------------------- */
/* INPUT */
/* ---------------------------- */

.stTextInput input{

background:#171E32 !important;

border:1px solid #344267 !important;

border-radius:18px !important;

height:62px !important;

font-size:18px !important;

padding-left:55px !important;

color:white !important;

box-shadow:none !important;

}

.stTextInput input:focus{

border:1px solid #7C4DFF !important;

box-shadow:0 0 18px rgba(124,77,255,.40) !important;

}

/* ---------------------------- */
/* FILE */
/* ---------------------------- */

[data-testid="stFileUploader"]{

border-radius:20px;

background:#161C29;

padding:15px;

}

/* ---------------------------- */
/* TABS */
/* ---------------------------- */

.stTabs [data-baseweb="tab"]{

font-size:17px;

font-weight:700;

padding:15px;

}

.stTabs [aria-selected="true"]{

color:#42A5F5;

}

/* ---------------------------- */
/* SCROLL */
/* ---------------------------- */

::-webkit-scrollbar{

height:8px;

width:8px;

}

::-webkit-scrollbar-thumb{

background:#7C4DFF;

border-radius:20px;

}

</style>
""", unsafe_allow_html=True)
# =====================================
# HERO
# =====================================

left, right = st.columns([4, 1])

with left:

    st.markdown("""
<div class="hero">

🤖 AI-Powered Multi-Agent<br>
Research Assistant

</div>

<div class="subtitle">

Autonomous Research Platform Powered by AI Agents

</div>

<div class="agents-row">

<div class="agent-card">
🧭 Planner
</div>

<div class="agent-card">
🌐 Researcher
</div>

<div class="agent-card">
📊 Analyst
</div>

<div class="agent-card">
📝 Writer
</div>

<div class="agent-card">
✅ Fact Checker
</div>

</div>

""", unsafe_allow_html=True)

with right:

    st.markdown("""

<div class="dashboard glow">

<h3 style="margin:0;color:white;">
📊 Dashboard
</h3>

<div style="margin-top:20px;">

<div style="display:flex;justify-content:space-between;margin-bottom:12px;">
<span style="color:#BFC7D5;">AI Agents</span>
<b style="color:#40C4FF;">5</b>
</div>

<div style="display:flex;justify-content:space-between;margin-bottom:12px;">
<span style="color:#BFC7D5;">Model</span>
<b style="color:#40C4FF;">Groq</b>
</div>

<div style="display:flex;justify-content:space-between;margin-bottom:12px;">
<span style="color:#BFC7D5;">Status</span>
<b style="color:#00E676;">🟢 Online</b>
</div>

<div style="display:flex;justify-content:space-between;">
<span style="color:#BFC7D5;">Version</span>
<b style="color:#40C4FF;">v10.0</b>
</div>

</div>

</div>

""", unsafe_allow_html=True)
st.write("")

# =====================================
# VERSION 10 STATS
# =====================================

st.write("")

c1,c2,c3,c4=st.columns(4)

with c1:

    st.markdown("""

<div class="dashboard glow">

<h2>📄 Reports</h2>

<h1 style="color:#59C3FF;">{}</h1>

</div>

""".format(len(st.session_state.history)),unsafe_allow_html=True)

with c2:

    st.markdown("""

<div class="dashboard glow">

<h2>🤖 AI Agents</h2>

<h1 style="color:#7C4DFF;">5</h1>

</div>

""",unsafe_allow_html=True)

with c3:

    st.markdown("""

<div class="dashboard glow">

<h2>🧠 Model</h2>

<h3 style="color:#4FC3F7;">Groq Llama 3.3</h3>

</div>

""",unsafe_allow_html=True)

with c4:

    st.markdown("""

<div class="dashboard glow">

<h2>🟢 Status</h2>

<h2 style="color:#00E676;">ONLINE</h2>

</div>

""",unsafe_allow_html=True)

st.write("")

# =====================================
# VERSION 10 INPUT
# =====================================

st.markdown('<div class="search-card">', unsafe_allow_html=True)

st.subheader("🔍 AI Research")

topic = st.text_input(
    "",
    placeholder="Enter your research topic and press Enter...",
    label_visibility="collapsed"
)

st.write("")

uploaded_file = st.file_uploader(
    "",
    type=["pdf", "txt", "docx"],
    label_visibility="collapsed"
)

if st.button("🎤 Voice"):

    voice_text = listen_voice()

    if voice_text:

        topic = voice_text

        st.success(f"🎤 {voice_text}")

st.markdown("</div>", unsafe_allow_html=True)
# =====================================
# VERSION 10 GENERATE REPORT
# =====================================

if topic.strip():

    topic = topic.strip()

    progress = st.progress(0)

    status = st.empty()

    with st.spinner("🤖 AI Agents are Working..."):

        status.info("🧭 Planner Agent")
        progress.progress(20)

        plan = planner_agent(topic)

        status.info("🌐 Researcher Agent")
        progress.progress(40)

        research = researcher_agent(topic)

        status.info("📊 Analyst Agent")
        progress.progress(70)

        analysis = analyst_agent(topic, research)

        status.info("📝 Writer Agent")
        progress.progress(90)

        report = writer_agent(topic, analysis)

        progress.progress(100)

    status.success("✅ Research Completed")

    st.session_state.plan = plan
    st.session_state.research = research
    st.session_state.analysis = analysis
    st.session_state.report = report

    if topic not in st.session_state.history:

        st.session_state.history.append(topic)
# =====================================
# VERSION 10 RESULTS
# =====================================

if "report" in st.session_state:

    st.write("")

    st.markdown("## 📑 Research Results")

    tab1, tab2, tab3, tab4 = st.tabs(

        [

            "🧭 Research Plan",

            "🌐 Web Research",

            "📊 AI Analysis",

            "📄 Final Report"

        ]

    )

    with tab1:

        st.markdown(

            f"""

<div class="result-card">

<h3>🧭 Research Plan</h3>

{st.session_state.plan}

</div>

""",

            unsafe_allow_html=True

        )

    with tab2:

        st.markdown(

            f"""

<div class="result-card">

<h3>🌐 Web Research</h3>

{st.session_state.research}

</div>

""",

            unsafe_allow_html=True

        )

    with tab3:

        st.markdown(

            f"""

<div class="result-card">

<h3>📊 AI Analysis</h3>

{st.session_state.analysis}

</div>

""",

            unsafe_allow_html=True

        )

    with tab4:

        st.markdown(

            f"""

<div class="result-card">

<h3>📄 Final Report</h3>

{st.session_state.report}

</div>

""",

            unsafe_allow_html=True

        )

        st.write("")
 # =====================================
# DOWNLOAD & READ REPORT
# =====================================

if "report" in st.session_state:

    c1, c2 = st.columns(2)

    with c1:

        st.download_button(

            label="⬇ Download Report",

            data=st.session_state.report,

            file_name="Research_Report.txt",

            mime="text/plain",

            use_container_width=True

        )

    with c2:

        if platform.system() == "Windows":

            if st.button(

                "🔊 Read Report",

                key="read_report",

                use_container_width=True

            ):

                read_complete_report()

        else:

            st.info("🔊 Voice works only on Windows.")
# =====================================
# VERSION 10 SIDEBAR
# =====================================

with st.sidebar:

    st.title("🚀 AI Dashboard")

    st.markdown("---")

    col1,col2=st.columns(2)

    with col1:

        st.metric(

            "📄 Reports",

            len(st.session_state.history)

        )

    with col2:

        st.metric(

            "🤖 Agents",

            "5"

        )

    st.metric(

        "🧠 Model",

        "Groq Llama 3.3"

    )

    st.metric(

        "⚡ Version",

        "10.0"

    )

    st.success("🟢 System Online")

    st.markdown("---")

    st.subheader("📚 Recent Research")

    if st.session_state.history:

        for item in reversed(st.session_state.history):

            st.markdown(

                f"""

<div class="result-card">

📄 {item}

</div>

""",

                unsafe_allow_html=True

            )

    else:

        st.info("No Research Yet")

    st.markdown("---")

    st.caption("👨‍💻 Developed by Rushi")

    st.caption("🤖 AI Research Studio")
# =====================================
# VERSION 10 FOOTER
# =====================================

st.write("")
st.write("")

st.divider()

col1,col2,col3 = st.columns(3)

with col1:

    st.caption("🚀 AI Research Studio")

with col2:

    st.caption("Version 10.0")

with col3:

    st.caption("👨‍💻 Developed by Rushi")