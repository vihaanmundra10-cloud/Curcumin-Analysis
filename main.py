import random
import math
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# ─── PAGE CONFIG ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Curcumin NRT Simulator",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── CUSTOM CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=DM+Serif+Display:ital@0;1&display=swap');

*, *::before, *::after { box-sizing: border-box; }

:root {
    --bg:        #0D1117;
    --surface:   #161B22;
    --surface2:  #1E2530;
    --border:    #2A3244;
    --red:       #E53E3E;
    --red-soft:  #FC8181;
    --teal:      #2DD4BF;
    --teal-soft: #99F6E4;
    --teal-glow: rgba(45, 212, 191, 0.12);
    --text:      #E2E8F0;
    --muted:     #718096;
    --label:     #A0AEC0;
    --white:     #FFFFFF;
    --gold:      #F6AD55;
}

.stApp, [data-testid="stAppViewContainer"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Inter', sans-serif !important;
}
[data-testid="stHeader"]     { background: transparent !important; }
[data-testid="stToolbar"]    { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }

[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
}

.main .block-container {
    padding: 2rem 3rem 4rem !important;
    max-width: 1100px !important;
}

/* ── Hero ── */
.hero {
    background: linear-gradient(135deg, #0a1a0f 0%, #0f1a2a 100%);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 3rem 3.5rem;
    margin-bottom: 2.5rem;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '🌿';
    position: absolute;
    right: 3rem;
    top: 50%;
    transform: translateY(-50%);
    font-size: 7rem;
    opacity: 0.10;
    filter: grayscale(1);
}
.hero-eyebrow {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--teal);
    margin-bottom: 0.75rem;
}
.hero h1 {
    font-family: 'DM Serif Display', serif !important;
    font-size: 2.4rem !important;
    font-weight: 400 !important;
    line-height: 1.2 !important;
    color: var(--white) !important;
    margin: 0 0 1rem !important;
    max-width: 620px;
}
.hero h1 em { font-style: italic; color: var(--teal-soft); }
.hero-sub {
    font-size: 0.92rem;
    color: var(--label);
    line-height: 1.7;
    max-width: 560px;
}
.author-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 100px;
    padding: 0.35rem 1rem;
    font-size: 0.78rem;
    color: var(--label);
    margin-bottom: 2rem;
}
.author-badge span { color: var(--teal); font-weight: 600; }

/* ── Section headers ── */
.section-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin: 2.5rem 0 1.25rem;
}
.section-header-line { flex: 1; height: 1px; background: var(--border); }
.section-title {
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--muted);
    white-space: nowrap;
}

/* ── Paper card ── */
.paper-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 2.5rem 3rem;
    margin-bottom: 1.5rem;
}
.paper-section-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.15rem;
    color: var(--teal-soft);
    margin: 2rem 0 0.75rem;
    padding-bottom: 0.4rem;
    border-bottom: 1px solid var(--border);
}
.paper-section-title:first-child { margin-top: 0; }
.paper-body {
    font-size: 0.88rem;
    color: var(--label);
    line-height: 1.85;
}
.paper-body p { margin: 0 0 1rem; }

/* References */
.ref-list {
    font-size: 0.78rem;
    color: var(--muted);
    line-height: 1.8;
    padding-left: 1.2rem;
}
.ref-list li { margin-bottom: 0.4rem; }
.ref-list a  { color: var(--teal); text-decoration: none; }
.ref-list a:hover { text-decoration: underline; }

/* ── Simulation card ── */
.sim-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 2rem;
    margin-top: 1rem;
}
.sim-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.3rem;
    color: var(--white);
    margin-bottom: 0.4rem;
}
.sim-desc {
    font-size: 0.82rem;
    color: var(--muted);
    margin-bottom: 1.5rem;
    line-height: 1.6;
}

/* ── Data tables ── */
[data-testid="stDataFrame"] {
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    overflow: hidden !important;
}
[data-testid="stDataFrame"] table { background: var(--surface) !important; color: var(--text) !important; }
[data-testid="stDataFrame"] th {
    background: var(--surface2) !important;
    color: var(--teal) !important;
    font-size: 0.72rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
    border-bottom: 1px solid var(--border) !important;
}
[data-testid="stDataFrame"] td {
    border-color: var(--border) !important;
    color: var(--label) !important;
    font-size: 0.82rem !important;
}

/* ── Caution box ── */
.caution {
    background: var(--surface2);
    border-left: 3px solid var(--gold);
    border-radius: 0 8px 8px 0;
    padding: 0.9rem 1.25rem;
    font-size: 0.8rem;
    color: var(--muted);
    margin: 2rem 0;
    line-height: 1.6;
}
.caution strong { color: var(--gold); }

/* ── Metric cards ── */
.metric-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin: 1.25rem 0 2rem;
}
.metric-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    position: relative;
    overflow: hidden;
}
.metric-card::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    border-radius: 12px 12px 0 0;
}
.metric-card.red::after  { background: var(--red); }
.metric-card.teal::after { background: var(--teal); }
.metric-card.gold::after { background: var(--gold); }
.metric-label {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 0.5rem;
}
.metric-value { font-size: 1.9rem; font-weight: 700; color: var(--white); line-height: 1; }
.metric-sub   { font-size: 0.75rem; color: var(--muted); margin-top: 0.3rem; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--muted); }

p, .stMarkdown p { color: var(--label) !important; font-size: 0.88rem !important; line-height: 1.7 !important; }
</style>
""", unsafe_allow_html=True)

# ─── MATPLOTLIB DARK THEME ───────────────────────────────────────────────────────
plt.rcParams.update({
    'figure.facecolor':  '#161B22',
    'axes.facecolor':    '#161B22',
    'axes.edgecolor':    '#2A3244',
    'axes.labelcolor':   '#A0AEC0',
    'axes.titlecolor':   '#E2E8F0',
    'xtick.color':       '#718096',
    'ytick.color':       '#718096',
    'text.color':        '#E2E8F0',
    'grid.color':        '#2A3244',
    'grid.alpha':        0.5,
    'axes.spines.top':   False,
    'axes.spines.right': False,
    'font.family':       'sans-serif',
    'legend.facecolor':  '#1E2530',
    'legend.edgecolor':  '#2A3244',
})

# ─── HERO ────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="author-badge">
    <span>Vihaan Rajesh Mundra</span> · Cardiovascular Research
</div>
<div class="hero">
    <div class="hero-eyebrow">Conceptual Simulation · Monte Carlo Model · CAD Risk Index</div>
    <h1>A Conceptual Model of <em>Curcumin Infused</em> Nicotine Therapy</h1>
    <p class="hero-sub">
        Predicting cardiovascular damage across four patient groups — regular smokers, 
        non-smokers, smokers on standard NRT, and smokers on curcumin-infused NRT — 
        simulated over a 12-month period using a stochastic risk index model.
    </p>
</div>
""", unsafe_allow_html=True)

# ─── KEY STATS ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="metric-grid">
    <div class="metric-card teal">
        <div class="metric-label">Simulation Groups</div>
        <div class="metric-value">4</div>
        <div class="metric-sub">Smoker, Non-smoker, NRT, Curcumin NRT</div>
    </div>
    <div class="metric-card gold">
        <div class="metric-label">Time Period</div>
        <div class="metric-value">12 mo</div>
        <div class="metric-sub">Clinical norm for cardiovascular trials</div>
    </div>
    <div class="metric-card red">
        <div class="metric-label">Baseline Risk Score</div>
        <div class="metric-value">100</div>
        <div class="metric-sub">Assigned to non-smoker group</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── PAPER ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <span class="section-title">Research Paper</span>
    <div class="section-header-line"></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="paper-card">

<div class="paper-section-title">Abstract</div>
<div class="paper-body">
<p>In this study, a conceptual simulation is created to observe the impact of curcumin infused NRT on CAD. Unfortunately, NRT is not entirely safe as the patient is still consuming nicotine in small doses throughout treatment. These small doses can still cause atherosclerosis, which is one of the leading causes of CAD. The simulation tracks 4 groups of people on a risk index: regular smokers, non-smokers, smoker on curcumin infused NRT, and a smoker on regular NRT. The results of this paper found that curcumin infused NRT can cause a slight difference in CAD risk. However, this cannot be established clearly as this is a conceptual simulation.</p>
</div>

<div class="paper-section-title">Introduction</div>
<div class="paper-body">
<p>Smoking is one of the leading causes of Cardiovascular Disease (CVD). Approximately one in every four cases are caused by smoking¹. All Cigarettes and e-cigarettes contain a chemical compound called Nicotine, which is highly addictive. Nicotine has several effects on the cardiovascular system and contributes to the development of CVD.</p>
<p>Nicotine causes hypertension (increased blood pressure), thrombosis, inflammation, insulin resistance, and dyslipidemia, which all promote atherosclerosis².</p>
<p>Atherosclerosis is the buildup of fats, cholesterol, and other substances on artery walls known as plaque. This plaque causes arteries to narrow and block blood flow leading to Coronary Artery Disease (CAD), the most common type of CVD³.</p>
<p>Once nicotine is consumed, it enters the blood stream and enters the brain. The nicotine causes the brain to release dopamine, which causes a nicotine buzz or Euphoria. This process is instantaneous as soon as someone consumes it through tobacco. Over time, the brain begins to crave the dopamine released through nicotine consumption, causing several to become addicted⁴. According to the National Institute on Drug Abuse⁵ (NIDA), almost 62 million people disclosed they used nicotine or tobacco products in the past thirty days in 2021, demonstrating its addictive nature.</p>
<p>In recent times, scientists have developed treatments that help others stop consuming nicotine. NRT (Nicotine Replacement Therapy) involves using nicotine patches or gum which will help patients eliminate their cravings for nicotine. Patients who recently quit smoking– or consuming nicotine– are given nicotine patches or gum that contain small doses of nicotine. Over time doses are strategically lowered, helping patients quit nicotine. However, this method is not cardiovascularly risk free. As mentioned above, these patches and gum contain nicotine, which still harms the cardiovascular system⁶. Given the cardiovascular risks of NRT, this raises a question as to how NRT can be modified to eliminate these risks.</p>
<p>It is hypothesized that if Curcumin is paired with NRT, CAD risks can be reduced because Curcumin will stop atherosclerosis from occurring. Curcumin is found in turmeric and contains anti-atherosclerosis properties. A study states that Curcumin is transdermal (it can be injected into skin and absorbed into the bloodstream), which means it is compatible to use with NRT⁷. The aim is to significantly reduce CVD, particularly CAD, risk while ensuring that patients get rid of nicotine addiction.</p>
</div>

<div class="paper-section-title">Materials and Methods</div>
<div class="paper-body">
<p>To simulate Curcumin infused NRT, a graph was constructed. The graph tracks a regular smoker for ten years, non-smoker, smoker for the past ten years on NRT, and a smoker for the past 10 years on Curcumin infused NRT. These groups are tracked over a 12 month period. These groups were chosen to be graphed to effectively compare and contrast Curcumin infused NRT over a 12 month period with regular NRT. Control groups like non-smokers and regular smokers were chosen to illustrate the profound impact smoking has on CVD risk. A period of 12 months was chosen as it is a clinical norm when conducting cardiovascular tests. The period was also most logical to highlight a clear difference between curcumin infused NRT and regular NRT. The values used to simulate these variables over the 12 month period was a risk index or risk score, not clinical percentage values.</p>
<p>This graph was made with an online software called google sheets.</p>
<p>A baseline risk score of 100 was assigned to the non-smoker. This remained constant all season because the non-smoker is not consuming any nicotine, thus keeping their risk score stagnant. A study shows that a smoker that has been smoking for a decade has a CVD risk of 15-20% higher than the baseline⁸. Given this, all smokers– no matter the treatment- were given a baseline risk score of 120. A regular smoker's risk score was incremented by 2 each month as they are continuously smoking, thus increasing their risk. Even though this will surpass the 15-20% increase cited above, this is a modeling choice to clearly illustrate the difference. NRT generally lasts 8-12 weeks, so for the smokers taking NRT, the score increases by 1.5 the first month, 0.75 the second month, and 0.25 the third month. These values are chosen because the smokers on NRT therapy are still consuming nicotine, thus increasing their CVD risk over time. The amount of CVD risk added is being gradually decreased each month as the nicotine consumption of the smoker is being gradually decreased each month. This only happens for the first three months as they are only consuming nicotine for 3 months, given that NRT lasts for 3 months. For curcumin infused NRT treatment, the risk score does not decrease or increase for the first three months, representing the hypothesized effect of curcumin. After the treatment for both smokers, their risk score decreases by 1 each month as cessation reduces CVD risk⁹.</p>
<p>To generate the graph, linear functions were used. Specifically, for the non-smoker, the equation was b(x)=100 as the risk remained constant throughout the simulation, where b(x) is the risk percentage. The smokers equation was g(x)=120+2x where 120 represents the starting risk and 2 represents the risk added per month, x, and g(x) is the risk score. For the smoker on regular NRT, the risk score f(x) is:</p>
<p>
120 + 1.5 × x &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for 0 &lt; x ≤ 1 month<br>
120 + 1.5 + 0.75 × (x − 1) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for 1 &lt; x ≤ 2 months<br>
120 + 1.5 + 0.75 + 0.25 × (x − 2) &nbsp;&nbsp;&nbsp;&nbsp; for 2 &lt; x ≤ 3 months<br>
122.5 − 1 × (x − 3) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for 3 &lt; x ≤ 12 months
</p>
<p>The smoker with Curcumin infused NRT, the risk score r(x) is:</p>
<p>
120 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for 0 &lt; x ≤ 3 months<br>
120 − 1 × (x − 3) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for 3 &lt; x ≤ 12 months
</p>
<p>A linear model for the graph was chosen given its simplicity. Linear models are effective at graphing trends over a certain period of time, which was the purpose of this graph.</p>
</div>

<div class="paper-section-title">Results</div>
<div class="paper-body">
<p>The results of this experiment were found in simulating four groups of people over a 12 month period: regular smoker for ten years, non-smoker, smoker for the past ten years on NRT, and a smoker for the past 10 years on Curcumin infused NRT. The data was recorded into a table and visualized into a graph.</p>
<p>In table and figure 1, the non-smoker had a constant risk score of 100 throughout the course of the simulation. To the contrast, the smoker of 10 years was constantly increasing in its risk score shown through the graph and– as shown in the table–had a risk score of 144 at month 12, which is 24 more than the score at month 0. In other words, the risk score for the smoker without any treatment was increasing by 2 every month. As shown by table 1, the smoker on regular NRT had a change of -7.5 in CVD risk while the smoker on curcumin infused NRT had a change of -9 in risk score. By the end of the simulation, the difference of risk score between these two groups was 1.5 as the smoker with regular NRT had 1.5 points more.</p>
<p>As shown in table one, the smoker on regular NRT increased by 0.75 in risk score for the first three months and then decreased by 1 every month after. However, the smoker on curcumin infused NRT did not increase in risk score at all from start to finish. Rather, the smoker on curcumin infused NRT was decreasing by 1 in risk score every month for the entirety of the simulation.</p>
</div>

<div class="paper-section-title">Discussion</div>
<div class="paper-body">
<p>It was hypothesized that curcumin infused NRT will reduce all the risks of CAD by preventing atherosclerosis from occurring. The data of the simulation illustrated that the curcumin infused NRT allowed for CAD risk to stay stagnant and slowly decrease after the three month period. With regular NRT, there was a slight increase in CAD risk and slow decrease after the three month period. Smokers without treatment increased throughout the simulation and non-smokers stayed stagnant at their baseline risk.</p>
<p>The results of the simulation occurred because Curcumin contains anti-atherosclerosis properties. Moreover, it is found to have anti-inflammatory effects. It stops plaque from building up on the artery walls, thus, eliminating atherosclerosis from occurring and stopping CAD¹⁰. These findings align with previous studies as nano-curcumin lowered Malondialdehyde, Nitric oxide, C-reactive protein levels in smokers¹¹. All of these substances are biomarkers for high oxidative stress and oxidative stress leads to atherosclerosis. This suggests that with NRT, curcumin can eliminate CAD risk from smoking while NRT reduces nicotine cravings.</p>
<p>However, this study was conducted using mathematical equations and the simulation was not based on any clinical studies or evidence. This study is a conceptual simulation that uses risk scores that are assumed. To investigate this further, humans can be tested using curcumin infused NRT, allowing for an accurate depiction of the treatment. Moreover, this graph does not aim to map precise values. In fact, this is one limitation of the model as it does not account for individual variation. To elaborate, many factors cause CVD risk to fluctuate. For instance, things like diet, age, ethnicity, and physical activity can all affect CVD risk. A person who has a diet high in saturated fats, trans fat, and cholesterol, has little to no physical activity, is older, and is American Indian or African American, has a higher chance of developing CVD¹². This graph being a linear model cannot account for these factors and is not completely accurate.</p>
</div>

<div class="paper-section-title">References</div>
<ol class="ref-list">
    <li>Health effects of cigarettes: cardiovascular disease. Smoking and Tobacco Use. 2024, <a href="https://www.cdc.gov/tobacco/about/cigarettes-and-cardiovascular-disease.html" target="_blank">https://www.cdc.gov/tobacco/about/cigarettes-and-cardiovascular-disease.html</a>.</li>
    <li>J. Lee, J. P. Cooke. The role of nicotine in the pathogenesis of atherosclerosis. <em>Atherosclerosis.</em> Vol. 215, pg. 281–283, 2011, <a href="https://doi.org/10.1016/j.atherosclerosis.2011.01.003" target="_blank">https://doi.org/10.1016/j.atherosclerosis.2011.01.003</a>.</li>
    <li>Arteriosclerosis / atherosclerosis - symptoms and causes. Mayo Clinic. <a href="https://www.mayoclinic.org/diseases-conditions/arteriosclerosis-atherosclerosis/symptoms-causes/syc-20350569" target="_blank">https://www.mayoclinic.org/diseases-conditions/arteriosclerosis-atherosclerosis/symptoms-causes/syc-20350569</a>.</li>
    <li>Heart disease facts. Heart Disease. 2024, <a href="https://www.cdc.gov/heart-disease/data-research/facts-stats/index.html" target="_blank">https://www.cdc.gov/heart-disease/data-research/facts-stats/index.html</a>.</li>
    <li>Nicotine: it's why smoking is so addictive. Health and Social Services. <a href="https://www.hss.gov.nt.ca/en/services/health-effects-tobacco/nicotine-it%E2%80%99s-why-smoking-so-addictive" target="_blank">https://www.hss.gov.nt.ca/en/services/health-effects-tobacco/nicotine-it%E2%80%99s-why-smoking-so-addictive</a>.</li>
    <li>Nicotine replacement therapy (NRT). Cleveland Clinic. 2025, <a href="https://my.clevelandclinic.org/health/treatments/nicotine-replacement-therapy-nrt" target="_blank">https://my.clevelandclinic.org/health/treatments/nicotine-replacement-therapy-nrt</a>.</li>
    <li>O. Pelikh, S. R. Pinnapireddy, C. M. Keck. Dermal penetration analysis of curcumin in an ex vivo porcine ear model using epifluorescence microscopy and digital image processing. <em>Skin Pharmacology and Physiology.</em> Vol. 34, pg. 281–299, 2021, <a href="https://doi.org/10.1159/000514498" target="_blank">https://doi.org/10.1159/000514498</a>.</li>
    <li>Curcumin as a natural remedy for atherosclerosis: a pharmacological review. National Library of Medicine. 2021, <a href="https://pubmed.ncbi.nlm.nih.gov/34279384/" target="_blank">https://pubmed.ncbi.nlm.nih.gov/34279384/</a>.</li>
    <li>K. A. Gallagher et al. Current status and principles for the treatment and prevention of diabetic foot ulcers in the cardiovascular patient population: a scientific statement from the American Heart Association. <em>Circulation.</em> Vol. 149, 2024, <a href="https://doi.org/10.1161/cir.0000000000001192" target="_blank">https://doi.org/10.1161/cir.0000000000001192</a>.</li>
    <li>Smoking cessation and benefits to cardiovascular health: a review of literature. National Library of Medicine. 2023, <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10082935/" target="_blank">https://pmc.ncbi.nlm.nih.gov/articles/PMC10082935/</a>.</li>
    <li>P. Mamsharifi et al. Nano-curcumin effects on nicotine dependence, depression, anxiety and metabolic parameters in smokers: a randomized double-blind clinical study. <em>Heliyon.</em> Vol. 9, 2023, <a href="https://doi.org/10.1016/j.heliyon.2023.e21249" target="_blank">https://doi.org/10.1016/j.heliyon.2023.e21249</a>.</li>
    <li>Heart disease risk factors. Heart Disease. 2024, <a href="https://www.cdc.gov/heart-disease/risk-factors/index.html" target="_blank">https://www.cdc.gov/heart-disease/risk-factors/index.html</a>.</li>
</ol>

</div>
""", unsafe_allow_html=True)

# ─── SIMULATION ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <span class="section-title">Monte Carlo Simulation</span>
    <div class="section-header-line"></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sim-card">
<div class="sim-title">CAD Risk Index — Stochastic Simulation</div>
<div class="sim-desc">
    Each group is simulated 100,000 times per month with Gaussian noise (σ = 0.5) 
    applied to the deterministic risk increments. Average risk scores are plotted below.
</div>
""", unsafe_allow_html=True)

# ── EXACT ORIGINAL SIMULATION CODE — UNCHANGED ──────────────────────────────────

n = 200        
months = 13    

g = 0.5

def simulate_non_smoker():
    return [100 for _ in range(months)]


def simulate_smoker():
    person = [120]
    for m in range(1, months):
        change = 2 + random.gauss(0, g)
        person.append(person[-1] + change)
    return person


def simulate_nrt():
    person = [120]
    for m in range(1, months):
        if m == 1:
            change = 1.5 + random.gauss(0, g)
        elif m == 2:
            change = 0.75 + random.gauss(0, g)
        elif m == 3:
            change = 0.25 + random.gauss(0, g)
        else:
            change = -1 + random.gauss(0, g)
        person.append(person[-1] + change)
    return person


def simulate_curcumin():
    person = [120]
    for m in range(1, months):
        if m <= 3:
            change = 0 + random.gauss(0, g)
        else:
            change = -1 + random.gauss(0, g)
        person.append(person[-1] + change)
    return person


def run_many_last(sim_func, runs):
    all_runs = []
    last_num = []
    for _ in range(runs):
        all_runs.append(sim_func())
        last_num.append(all_runs[-1][-1])
        
    st.write(sum(last_num) / len(last_num))
        
    return all_runs


run_many_last(simulate_curcumin, 100000)
run_many_last(simulate_nrt, 100000)
run_many_last(simulate_smoker, 100000)
run_many_last(simulate_non_smoker, 100000)

st.write("\n\n\n")


def run_many_1(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[1])
    
    return sum(nums) / len(nums)


def run_many_2(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[2])
    
    return sum(nums) / len(nums)


def run_many_3(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[3])
    
    return sum(nums) / len(nums)


def run_many_4(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[4])
    
    return sum(nums) / len(nums)


def run_many_5(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[5])
    
    return sum(nums) / len(nums)


def run_many_6(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[6])
    
    return sum(nums) / len(nums)


def run_many_7(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[7])
    
    return sum(nums) / len(nums)


def run_many_8(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[8])
    
    return sum(nums) / len(nums)


def run_many_9(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[9])
    
    return sum(nums) / len(nums)


def run_many_10(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[10])
    
    return sum(nums) / len(nums)


def run_many_11(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[11])
    
    return sum(nums) / len(nums)


def run_many_12(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[12])
    
    return sum(nums) / len(nums)


def run_many_13(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[13])
    
    return sum(nums) / len(nums)


run_many_1(simulate_curcumin, 100000)


avg_list_curcumin = [
    run_many_1(simulate_curcumin, 100000),
    run_many_2(simulate_curcumin, 100000),
    run_many_3(simulate_curcumin, 100000),
    run_many_4(simulate_curcumin, 100000),
    run_many_5(simulate_curcumin, 100000),
    run_many_6(simulate_curcumin, 100000),
    run_many_7(simulate_curcumin, 100000),
    run_many_8(simulate_curcumin, 100000),
    run_many_9(simulate_curcumin, 100000),
    run_many_10(simulate_curcumin, 100000),
    run_many_11(simulate_curcumin, 100000),
    run_many_12(simulate_curcumin, 100000),
]

avg_list_smoker = [
    run_many_1(simulate_smoker, 100000),
    run_many_2(simulate_smoker, 100000),
    run_many_3(simulate_smoker, 100000),
    run_many_4(simulate_smoker, 100000),
    run_many_5(simulate_smoker, 100000),
    run_many_6(simulate_smoker, 100000),
    run_many_7(simulate_smoker, 100000),
    run_many_8(simulate_smoker, 100000),
    run_many_9(simulate_smoker, 100000),
    run_many_10(simulate_smoker, 100000),
    run_many_11(simulate_smoker, 100000),
    run_many_12(simulate_smoker, 100000),
]

avg_list_non_smoker = [
    run_many_1(simulate_non_smoker, 100000),
    run_many_2(simulate_non_smoker, 100000),
    run_many_3(simulate_non_smoker, 100000),
    run_many_4(simulate_non_smoker, 100000),
    run_many_5(simulate_non_smoker, 100000),
    run_many_6(simulate_non_smoker, 100000),
    run_many_7(simulate_non_smoker, 100000),
    run_many_8(simulate_non_smoker, 100000),
    run_many_9(simulate_non_smoker, 100000),
    run_many_10(simulate_non_smoker, 100000),
    run_many_11(simulate_non_smoker, 100000),
    run_many_12(simulate_non_smoker, 100000),
]

avg_list_nrt = [
    run_many_1(simulate_nrt, 100000),
    run_many_2(simulate_nrt, 100000),
    run_many_3(simulate_nrt, 100000),
    run_many_4(simulate_nrt, 100000),
    run_many_5(simulate_nrt, 100000),
    run_many_6(simulate_nrt, 100000),
    run_many_7(simulate_nrt, 100000),
    run_many_8(simulate_nrt, 100000),
    run_many_9(simulate_nrt, 100000),
    run_many_10(simulate_nrt, 100000),
    run_many_11(simulate_nrt, 100000),
    run_many_12(simulate_nrt, 100000),
]

df1 = pd.DataFrame(avg_list_curcumin, columns=["Simulating with Curcumin Treatment "])
df1.index = range(1, len(df1) + 1)

df2 = pd.DataFrame(avg_list_non_smoker, columns=["Simulating with Non-Smoker "])
df2.index = range(1, len(df2) + 1)

df3 = pd.DataFrame(avg_list_smoker, columns=["Simulating with Smoker "])
df3.index = range(1, len(df3) + 1)

df4 = pd.DataFrame(avg_list_nrt, columns=["Simulating with NRT "])
df4.index = range(1, len(df4) + 1)

# ── DATA TABLES ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <span class="section-title">Table 1 — Average Risk Scores by Month</span>
    <div class="section-header-line"></div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.dataframe(df1, use_container_width=True)
    st.dataframe(df3, use_container_width=True)
with col2:
    st.dataframe(df2, use_container_width=True)
    st.dataframe(df4, use_container_width=True)

# ── FIGURE 1 — CHART ────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
    <span class="section-title">Figure 1 — Simulation Comparison</span>
    <div class="section-header-line"></div>
</div>
""", unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(df1.index, df1["Simulating with Curcumin Treatment "],
        label="Curcumin NRT", marker='o', color='#2DD4BF', linewidth=2, markersize=5)
ax.plot(df2.index, df2["Simulating with Non-Smoker "],
        label="Non-Smoker", marker='s', color='#99F6E4', linewidth=2, markersize=5, linestyle='--')
ax.plot(df3.index, df3["Simulating with Smoker "],
        label="Smoker (no treatment)", marker='^', color='#E53E3E', linewidth=2, markersize=5)
ax.plot(df4.index, df4["Simulating with NRT "],
        label="Standard NRT", marker='D', color='#F6AD55', linewidth=2, markersize=5)

ax.set_title("CAD Risk Index Over 12 Months — Monte Carlo Average (n=100,000)", pad=14, fontsize=12)
ax.set_xlabel("Month", fontsize=10)
ax.set_ylabel("Average Risk Score", fontsize=10)
ax.legend(fontsize=9, loc='upper left')
ax.grid(True, linestyle='--', alpha=0.4)
ax.set_xticks(range(1, 13))
plt.tight_layout()

st.pyplot(fig)
plt.close()

st.markdown("</div>", unsafe_allow_html=True)  # close sim-card

st.markdown("""
<div class="caution">
    <strong>⚠ Educational use only.</strong> This is a conceptual simulation based on assumed risk scores 
    and mathematical modeling. It is not grounded in clinical trial data and should not be interpreted 
    as medical evidence or advice.
</div>
""", unsafe_allow_html=True)
