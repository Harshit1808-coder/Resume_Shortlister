import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Shortlist Desk", page_icon="📋", layout="wide")

model = joblib.load("models/resume_model.pkl")

# ---------------------------------------------------------------- styling
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Instrument+Sans:wght@400;600&display=swap');

:root{
  --base:#070b24; --tint:rgba(10,15,52,.46);
  --edge:rgba(255,255,255,.34); --txt:#ffffff; --mute:rgba(226,232,255,.86);
  --yes:#62f7cc; --no:#ff8fab;
}
html,body,.stApp{font-family:'Instrument Sans',sans-serif;}
.stApp{background:var(--base);}
.stApp, .stApp p, .stApp label, .stApp span, .stApp li{color:var(--txt);}
#MainMenu,footer,header{visibility:hidden;}
.block-container{position:relative;z-index:1;max-width:1120px;padding-top:2.4rem;padding-bottom:5rem;}

/* ---------- flowing background ---------- */
.flow{position:fixed;inset:0;overflow:hidden;pointer-events:none;z-index:0;}
.flow i{position:absolute;border-radius:50%;filter:blur(80px);opacity:.6;will-change:transform;}
.flow i:nth-child(1){width:46vw;height:46vw;left:-8vw;top:-10vw;background:#2f54eb;animation:d1 22s ease-in-out infinite alternate;}
.flow i:nth-child(2){width:38vw;height:38vw;right:-6vw;top:8vh;background:#7a3cff;animation:d2 26s ease-in-out infinite alternate;}
.flow i:nth-child(3){width:42vw;height:42vw;left:22vw;bottom:-18vw;background:#0e9aa7;animation:d3 30s ease-in-out infinite alternate;}
.flow i:nth-child(4){width:26vw;height:26vw;right:14vw;bottom:6vh;background:#ff7a59;opacity:.32;animation:d4 24s ease-in-out infinite alternate;}
@keyframes d1{to{transform:translate(28vw,22vh) scale(1.15)}}
@keyframes d2{to{transform:translate(-30vw,30vh) scale(.85)}}
@keyframes d3{to{transform:translate(-24vw,-26vh) scale(1.2)}}
@keyframes d4{to{transform:translate(-18vw,-30vh) scale(1.3)}}
.flow:after{content:"";position:absolute;inset:0;
  background:radial-gradient(ellipse at 50% 20%,transparent 25%,rgba(7,11,36,.78) 100%);}

/* ---------- glass ---------- */
.glass,div[data-testid="stVerticalBlockBorderWrapper"]{
  position:relative;background:linear-gradient(135deg,rgba(255,255,255,.20),rgba(255,255,255,.05) 60%),var(--tint);
  backdrop-filter:blur(26px) saturate(180%);-webkit-backdrop-filter:blur(26px) saturate(180%);
  border:1px solid var(--edge)!important;border-radius:28px!important;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.55),inset 0 -1px 0 rgba(255,255,255,.08),0 24px 60px -24px rgba(3,6,30,.7);}
div[data-testid="stVerticalBlockBorderWrapper"]{padding:1.2rem 1.4rem;}

/* ---------- hero (one orchestrated entrance) ---------- */
.hero{padding:3.2rem 0 2.2rem;text-align:center;}
.badge{display:inline-flex;align-items:center;gap:.55rem;padding:.45rem 1rem;border-radius:999px;font-size:.9rem;
  animation:rise .8s .05s both;}
.badge b{width:9px;height:9px;border-radius:50%;background:var(--yes);box-shadow:0 0 0 0 rgba(76,242,192,.7);animation:ping 2s infinite;}
.hero h1{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:clamp(2.8rem,7.5vw,5.6rem);
  letter-spacing:-.04em;line-height:.98;margin:1.3rem auto .9rem;max-width:13ch;
  animation:rise .9s .2s both;text-shadow:0 4px 30px rgba(4,8,40,.7);}
.hero p.lead{font-size:1.2rem;color:var(--mute);max-width:44ch;margin:0 auto 1.8rem;animation:rise .9s .35s both;}
.cta{display:inline-block;padding:.95rem 2rem;border-radius:999px;font-family:'Bricolage Grotesque',sans-serif;
  font-weight:800;font-size:1.05rem;color:#070b24!important;text-decoration:none;background:#fff;
  box-shadow:0 10px 30px -8px rgba(255,255,255,.55);animation:rise .9s .5s both;transition:transform .2s,box-shadow .2s;}
.cta:hover{transform:translateY(-3px) scale(1.03);box-shadow:0 16px 40px -8px rgba(255,255,255,.7);}
.stats{display:flex;justify-content:center;gap:1rem;flex-wrap:wrap;margin-top:2.6rem;}
.stat{padding:1rem 1.5rem;border-radius:22px;text-align:left;animation:rise .9s both,bob 7s ease-in-out infinite;}
.stat:nth-child(1){animation-delay:.65s,0s}.stat:nth-child(2){animation-delay:.8s,1.2s}.stat:nth-child(3){animation-delay:.95s,2.4s}
.stat strong{display:block;font-family:'Bricolage Grotesque',sans-serif;font-size:1.7rem;font-weight:800;}
.stat span{color:var(--mute);font-size:.88rem;}
@keyframes rise{from{opacity:0;transform:translateY(26px);filter:blur(8px)}to{opacity:1;transform:none;filter:none}}
@keyframes bob{50%{transform:translateY(-8px)}}
@keyframes ping{70%{box-shadow:0 0 0 10px rgba(76,242,192,0)}100%{box-shadow:0 0 0 0 rgba(76,242,192,0)}}

/* ---------- how it works ---------- */
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:1rem;margin:1.5rem 0 3.2rem;}
.step{padding:1.4rem 1.5rem;transition:transform .25s,background .25s;}
.step:hover{transform:translateY(-5px);}
.step h4{font-family:'Bricolage Grotesque',sans-serif;font-size:1.15rem;margin:.6rem 0 .3rem;}
.step p{margin:0;color:var(--mute);font-size:.95rem;}
.ico{width:46px;height:46px;border-radius:14px;display:grid;place-items:center;font-size:1.4rem;
  background:linear-gradient(145deg,rgba(255,255,255,.38),rgba(255,255,255,.08));box-shadow:inset 0 1px 0 rgba(255,255,255,.6);}
h2.sec{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:2.1rem;letter-spacing:-.02em;margin:0 0 .3rem;}
p.sec{color:var(--mute);margin:0 0 1.4rem;}

/* ---------- widgets ---------- */
div[data-testid="stSlider"] [role="slider"]{background:#fff;border:0;box-shadow:0 3px 12px rgba(0,0,0,.4);}
div[data-testid="stSlider"] div[data-baseweb="slider"]>div>div{background:rgba(255,255,255,.38);}
div[data-testid="stSlider"] div[data-testid="stThumbValue"],div[data-testid="stSlider"] [data-testid="stTickBarMin"],
div[data-testid="stSlider"] [data-testid="stTickBarMax"]{color:#fff;}
div[data-baseweb="select"]>div{background:rgba(7,11,36,.55)!important;border:1px solid var(--edge)!important;border-radius:14px!important;}
div[data-baseweb="select"] *{color:#fff!important;}
div[data-baseweb="popover"] ul{background:#10174a!important;}
div[data-baseweb="popover"] li{color:#fff!important;}
div.stButton>button{width:100%;border:1px solid rgba(255,255,255,.5);border-radius:999px;padding:.9rem 1rem;color:#fff;
  font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:1.05rem;
  background:linear-gradient(135deg,#3a57f5,#8a3df0);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.6),0 14px 34px -10px rgba(110,80,255,.9);transition:transform .2s,filter .2s;}
div.stButton>button:hover{transform:translateY(-2px) scale(1.01);filter:brightness(1.12);color:#fff;border-color:#fff;}
div.stButton>button:active{transform:scale(.97);}
div.stButton>button:focus-visible{outline:3px solid #fff;outline-offset:3px;}

/* ---------- result card ---------- */
.file{padding:1.5rem 1.7rem 1.7rem;min-height:420px;scroll-margin-top:1rem;}
.file h3{font-family:'Bricolage Grotesque',sans-serif;font-weight:500;font-size:1.15rem;margin:0 0 .9rem;}
.verdict{display:flex;align-items:center;gap:1.4rem;padding:1.2rem 1.4rem;border-radius:22px;border:1.5px solid;
  margin-bottom:1.2rem;animation:rise .3s both;}
.verdict.yes{background:linear-gradient(135deg,rgba(98,247,204,.26),rgba(98,247,204,.06)),rgba(4,30,36,.62);border-color:rgba(98,247,204,.8);
  box-shadow:0 0 60px -16px rgba(98,247,204,.7),inset 0 1px 0 rgba(255,255,255,.4);}
.verdict.no{background:linear-gradient(135deg,rgba(255,143,171,.26),rgba(255,143,171,.06)),rgba(40,8,28,.62);border-color:rgba(255,143,171,.8);
  box-shadow:0 0 60px -16px rgba(255,143,171,.7),inset 0 1px 0 rgba(255,255,255,.4);}
.vlabel{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:clamp(1.9rem,4.2vw,2.6rem);
  line-height:1;letter-spacing:-.02em;animation:pop .35s cubic-bezier(.2,1.7,.4,1) both;}
.verdict.yes .vlabel{color:var(--yes);} .verdict.no .vlabel{color:var(--no);}
.note{color:var(--txt);opacity:.92;font-size:.95rem;margin-top:.5rem;max-width:32ch;}
.ring{width:124px;height:124px;flex:none;}
.ring .arc{animation:fill .8s cubic-bezier(.2,.8,.2,1) both;}
@keyframes fill{from{stroke-dashoffset:var(--c)}}
@property --n{syntax:'<integer>';initial-value:0;inherits:false;}
.pct{--n:0;counter-reset:n var(--n);animation:count .8s cubic-bezier(.2,.8,.2,1) forwards;
  font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:26px;fill:#fff;}
.pct:after{content:counter(n)"%";}
@keyframes count{to{--n:var(--to)}}
@keyframes pop{from{transform:scale(.6);opacity:0}to{transform:none;opacity:1}}
.stale{padding:.55rem .9rem;border-radius:12px;background:rgba(70,45,0,.55);border:1px solid rgba(255,205,110,.8);color:#ffe9b8;
  font-size:.9rem;margin-bottom:.9rem;}
.cmp{margin:.55rem 0;}
.cl{display:flex;justify-content:space-between;font-size:.92rem;margin-bottom:.25rem;}
.cl em{font-style:normal;color:var(--mute);margin-left:.5rem;}
.bar{position:relative;height:8px;border-radius:99px;background:rgba(255,255,255,.22);}
.fill{height:100%;border-radius:99px;background:linear-gradient(90deg,#5de0ff,#b794ff);animation:grow .7s ease-out both;}
@keyframes grow{from{width:0}}
.tick{position:absolute;top:-4px;width:2px;height:16px;background:#fff;border-radius:2px;}
.edu{display:flex;justify-content:space-between;font-size:.92rem;margin:.2rem 0 .7rem;}
.legend{color:var(--mute);font-size:.8rem;margin-top:.8rem;}
.waiting{color:var(--mute);margin-top:3.2rem;text-align:center;}

@media (prefers-reduced-motion:reduce){*{animation-duration:.01s!important;animation-iteration-count:1!important;transition:none!important;}}
</style>

<div class="flow"><i></i><i></i><i></i><i></i></div>

<section class="hero">
  <div class="badge glass"><b></b>Model ready</div>
  <h1>Find the right hire in seconds</h1>
  <p class="lead">Enter a candidate's experience, skills and projects. Shortlist Desk tells you if they make the cut, and how confident it is.</p>
  <a class="cta" href="#screen">Start screening</a>
  <div class="stats">
    <div class="stat glass"><strong>30,000</strong><span>resumes learned from</span></div>
    <div class="stat glass"><strong>6</strong><span>signals per candidate</span></div>
    <div class="stat glass"><strong>&lt; 1 sec</strong><span>to get a verdict</span></div>
  </div>
</section>

<div class="steps">
  <div class="step glass"><div class="ico">🧾</div><h4>Add the details</h4><p>Experience, skills match, education, projects, GitHub activity and resume length.</p></div>
  <div class="step glass"><div class="ico">🧠</div><h4>Model scores it</h4><p>Your trained pipeline turns those six signals into a shortlisting probability.</p></div>
  <div class="step glass"><div class="ico">✅</div><h4>See the verdict</h4><p>A clear shortlisted or not shortlisted result with a confidence ring.</p></div>
</div>

<div id="screen"></div>
<h2 class="sec">Screen a candidate</h2>
<p class="sec">Move the sliders, then press the button.</p>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------- tool
AVG = {  # dataset averages and maxima, used for the comparison bars
    "years_experience": ("Experience", 7.5, 15, " yrs"),
    "skills_match_score": ("Skills match", 73.7, 100, "%"),
    "project_count": ("Projects", 10.6, 25, ""),
    "github_activity": ("GitHub activity", 325, 842, ""),
    "resume_length": ("Resume length", 573, 900, " words"),
}

left, right = st.columns([1.05, 1], gap="large")

with left:
    with st.container(border=True):
        years_experience = st.slider("Years of experience", 0, 30, 2)
        skills_match_score = st.slider("Skills match score", 0.0, 100.0, 70.0, step=0.5)
        education_level = st.selectbox("Education level", ["High School", "Bachelors", "Masters", "PhD"], index=1)
        c1, c2 = st.columns(2)
        with c1:
            project_count = st.slider("Projects", 0, 30, 5)
        with c2:
            github_activity = st.slider("GitHub activity", 0, 1000, 200, step=10)
        resume_length = st.slider("Resume length (words)", 100, 1000, 500, step=10)
        run = st.button("Screen candidate")

inputs = {
    "years_experience": years_experience,
    "skills_match_score": skills_match_score,
    "education_level": education_level,
    "project_count": project_count,
    "resume_length": resume_length,
    "github_activity": github_activity,
}

if run:
    candidate = pd.DataFrame({k: [v] for k, v in inputs.items()})
    st.session_state.result = {
        "inputs": dict(inputs),
        "pred": int(model.predict(candidate)[0]),
        "prob": float(model.predict_proba(candidate)[0][1]),
    }
    r = st.session_state.result
    st.toast(f"{'Shortlisted' if r['pred'] == 1 else 'Not shortlisted'} - {round(r['prob'] * 100)}%",
             icon="✅" if r["pred"] == 1 else "⚠️")

res = st.session_state.get("result")

with right:
    if res:
        ok = res["pred"] == 1
        prob = res["prob"]
        pct = round(prob * 100)
        cls, label = ("yes", "Shortlisted") if ok else ("no", "Not shortlisted")
        colour = "#62f7cc" if ok else "#ff8fab"
        circ = 2 * 3.14159 * 54
        offset = circ * (1 - prob)
        note = (
            f"The model gives this candidate a {pct}% chance. Strong enough to move forward."
            if ok
            else f"The model gives this candidate a {pct}% chance. A higher skills match or more projects would help most."
        )
        stale = (
            '<div class="stale">Inputs changed since this result. Press Screen candidate to update.</div>'
            if res["inputs"] != inputs
            else ""
        )
        verdict = f"""
        <div class="verdict {cls}">
          <svg class="ring" viewBox="0 0 128 128" role="img" aria-label="Probability {pct} percent">
            <circle cx="64" cy="64" r="54" fill="none" stroke="rgba(255,255,255,.24)" stroke-width="12"/>
            <circle class="arc" cx="64" cy="64" r="54" fill="none" stroke="{colour}" stroke-width="12"
              stroke-linecap="round" stroke-dasharray="{circ:.1f}" stroke-dashoffset="{offset:.1f}"
              style="--c:{circ:.1f}" transform="rotate(-90 64 64)"/>
            <text class="pct" style="--to:{pct}" x="64" y="73" text-anchor="middle"></text>
          </svg>
          <div><div class="vlabel">{label}</div><div class="note">{note}</div></div>
        </div>"""
        bars = ""
        for key, (name, avg, mx, unit) in AVG.items():
            v = res["inputs"][key]
            w = min(v / mx * 100, 100)
            a = min(avg / mx * 100, 100)
            bars += (
                f'<div class="cmp"><div class="cl"><span>{name}</span><span>{v:g}{unit}<em>avg {avg:g}</em></span></div>'
                f'<div class="bar"><div class="fill" style="width:{w:.0f}%"></div><div class="tick" style="left:{a:.0f}%"></div></div></div>'
            )
        edu = f'<div class="edu"><span>Education</span><span>{res["inputs"]["education_level"]}</span></div>'
        body = (
            f"{stale}{verdict}{edu}{bars}"
            '<div class="legend">White tick marks the average candidate in the training data.</div>'
        )
    else:
        body = '<div class="waiting">Your result will appear here.</div>'

    st.markdown(f'<div id="result" class="file glass"><h3>Result</h3>{body}</div>', unsafe_allow_html=True)

if run:  # bring the result into view straight away, even on small screens
    import time
    import streamlit.components.v1 as components

    components.html(
        f"<script>/*{time.time()}*/setTimeout(()=>{{const e=window.parent.document.getElementById('result');"
        "if(e)e.scrollIntoView({behavior:'smooth',block:'center'});},120);</script>",
        height=0,
    )