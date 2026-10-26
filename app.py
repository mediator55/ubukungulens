import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# 1. Page Configuration
st.set_page_config(
    page_title="UbukunguLens | NISR Hackathon 2026",
    page_icon="🇷🇼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Data Sources
FINSCOPE_CATALOG = "https://www.microdata.statistics.gov.rw/index.php/catalog/120/study-description"
FINSCOPE_REPORT = "https://www.statistics.gov.rw/statistical-publications/business-establishment-finance-trade/finscope-survey-2024"
EICV_CATALOG = "https://www.microdata.statistics.gov.rw/index.php/catalog/119"
EICV_REPORT = "https://statistics.gov.rw/data-sources/surveys/EICV/integrated-household-living-conditions-survey-7-eicv-7"

indicators = pd.DataFrame([
    {"Indicator": "Financially included", "Value (%)": 96, "Population / definition": "Adults; formal and/or informal financial products", "Survey": "FinScope 2024", "Theme": "Overall inclusion", "Source": FINSCOPE_REPORT},
    {"Indicator": "Formally financially included", "Value (%)": 92, "Population / definition": "Adults; formal financial products/services", "Survey": "FinScope 2024", "Theme": "Overall inclusion", "Source": FINSCOPE_REPORT},
    {"Indicator": "Own or have used mobile money", "Value (%)": 86, "Population / definition": "Adults who own or have used mobile money", "Survey": "FinScope 2024", "Theme": "Digital finance", "Source": FINSCOPE_REPORT},
    {"Indicator": "Registered mobile wallet in own name", "Value (%)": 77, "Population / definition": "Adults with a registered mobile wallet in their own name", "Survey": "FinScope 2024", "Theme": "Digital finance", "Source": FINSCOPE_REPORT},
    {"Indicator": "Transactional account — women", "Value (%)": 73, "Population / definition": "Female adults; transactional account uptake", "Survey": "FinScope 2024", "Theme": "Gender", "Source": FINSCOPE_REPORT},
    {"Indicator": "Transactional account — men", "Value (%)": 82, "Population / definition": "Male adults; transactional account uptake", "Survey": "FinScope 2024", "Theme": "Gender", "Source": FINSCOPE_REPORT},
    {"Indicator": "Banked", "Value (%)": 22, "Population / definition": "Adults; uptake of banking products", "Survey": "FinScope 2024", "Theme": "Banking", "Source": FINSCOPE_REPORT},
    {"Indicator": "Bank account used monthly", "Value (%)": 55, "Population / definition": "Banked population; monthly account use", "Survey": "FinScope 2024", "Theme": "Banking", "Source": FINSCOPE_REPORT},
])

poverty_rate = 27.4
history_data = pd.DataFrame({"Year": ["2008", "2012", "2016", "2020", "2024"], "Financial Inclusion (%)": [48, 72, 89, 93, 96]})
poverty_history = pd.DataFrame({"Survey": ["EICV 4 (2016/17)", "EICV 5 (2023/24)"], "Poverty Rate (%)": [38.2, 27.4]})

# 3. Premium UI Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: #1e293b; }
.stApp { background-color: #f8fafc; }
.hero { padding: 3rem 2rem; border-radius: 24px; background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #0f766e 100%); color: white; margin-bottom: 2rem; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1); position: relative; overflow: hidden; }
.hero::after { content: ''; position: absolute; top: -50px; right: -50px; width: 200px; height: 200px; background: radial-gradient(circle, rgba(96,165,250,0.4) 0%, rgba(0,0,0,0) 70%); border-radius: 50%; }
.hero h1 { color: white; font-weight: 800; font-size: 3rem; margin: 0; letter-spacing: -0.03em; }
.hero p { color: #93c5fd; font-size: 1.2rem; margin-top: 0.5rem; font-weight: 500; }
.kicker { text-transform: uppercase; letter-spacing: 0.15em; font-size: 0.85rem; font-weight: 800; color: #2dd4bf; }
div[data-testid="stMetricValue"] { color: #0f172a !important; font-weight: 800 !important; font-size: 2.8rem !important; }
div[data-testid="stMetric"] { background-color: #ffffff; padding: 1.5rem !important; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); transition: transform 0.2s ease-in-out; }
div[data-testid="stMetric"]:hover { transform: translateY(-2px); box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); }
.section-card { border: 1px solid #e2e8f0; padding: 1.5rem; border-radius: 16px; height: 100%; background-color: #ffffff; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); }
.section-card h2 { color: #0f172a; }
div[data-testid="stAlert"] { border-radius: 12px; border: none; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
.small-note { font-size: 0.85rem; color: #64748b; margin-top: 10px; }
[data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e2e8f0; }
/* Mobile Responsiveness */
@media (max-width: 768px) { .hero h1 { font-size: 2rem; } }
</style>
""", unsafe_allow_html=True)

# 4. Sidebar
with st.sidebar:
    st.markdown("## 🇷🇼 UbukunguLens")
    st.caption("NISR Big Data Hackathon 2026 · Track 2")
    page = st.radio("Navigation", ["Executive overview", "Explore indicators", "Gender gap lab", "Action planner & Algorithms", "Data & methodology"])
    st.divider()
    st.success("**NST2 & Vision 2050 Aligned**")
    st.caption("Directly supports scaling access to formal financial services and poverty eradication.")
    st.divider()
    st.markdown("[FinScope 2024 source ↗](%s)" % FINSCOPE_REPORT)
    st.markdown("[EICV7 source ↗](%s)" % EICV_REPORT)

# 5. Hero Banner
st.markdown("""
<div class="hero">
  <div class="kicker">Evidence for inclusive growth</div>
  <h1>UbukunguLens</h1>
  <p>Rwanda's Financial Inclusion & Usage Explorer</p>
</div>
""", unsafe_allow_html=True)

st.caption("An independent student prototype using published NISR survey findings. It is not an official NISR product.")

# 6. Page Routing
if page == "Executive overview":
    st.markdown("### The headline")
    st.write("Rwanda reports high overall financial inclusion, but the headline rate alone does not tell the whole story. UbukunguLens helps reviewers inspect different dimensions of access, digital finance and account uptake.")

    a,b,c,d = st.columns(4)
    a.metric("Financially included", "96%", help="FinScope 2024; formal and/or informal financial products.")
    b.metric("Formally included", "92%", help="FinScope 2024; formal financial products/services.")
    c.metric("Own/use mobile money", "86%", help="FinScope 2024; adults who own or have used mobile money.")
    d.metric("Mobile wallet in own name", "77%", help="FinScope 2024; adults with a registered mobile wallet in their own name.")

    st.markdown("---")
    st.error("**The Core Paradox:** While 96% of Rwandan adults are financially included, only **22% are banked**, and there is a **9-point gender gap** in who holds a transactional account. Access is high, but usage depth remains a challenge.")
    st.markdown("---")

    st.markdown("### Progress Over Time")
    col_hist1, col_hist2 = st.columns(2)
    
    with col_hist1:
        fig_history = px.line(history_data, x="Year", y="Financial Inclusion (%)", markers=True, text="Financial Inclusion (%)", title="Financial Inclusion Growth (2008–2024)")
        fig_history.update_traces(textposition="top center", line=dict(color="#0f766e", width=4), marker=dict(size=10))
        fig_history.update_layout(yaxis=dict(range=[0, 105], ticksuffix="%"), xaxis_title="Survey Year", yaxis_title="Adults Included (%)", margin=dict(l=10,r=10,t=40,b=10))
        st.plotly_chart(fig_history, use_container_width=True)
        st.caption("Source: FinScope Rwanda Surveys. Access has grown from 48% to 96%.")

    with col_hist2:
        fig_pov = px.bar(poverty_history, x="Survey", y="Poverty Rate (%)", text="Poverty Rate (%)", color="Survey", color_discrete_sequence=["#94a3b8", "#0f766e"])
        fig_pov.update_traces(texttemplate='%{text}%', textposition='outside')
        fig_pov.update_layout(yaxis=dict(range=[0, 50], ticksuffix="%"), showlegend=False, margin=dict(l=10,r=10,t=40,b=10), title="National Poverty Reduction (EICV)")
        st.plotly_chart(fig_pov, use_container_width=True)
        st.caption("Source: EICV 4 & 5. National poverty rate dropped to 27.4%.")

elif page == "Explore indicators":
    st.markdown("### Indicator explorer")
    st.write("Filter published indicators by theme, compare their values, and inspect definitions before interpreting them.")
    themes = ["All themes"] + sorted(indicators["Theme"].unique().tolist())
    selected_theme = st.selectbox("Theme", themes)
    filtered = indicators if selected_theme == "All themes" else indicators[indicators["Theme"] == selected_theme]
    selected = st.multiselect("Indicators to display", filtered["Indicator"].tolist(), default=filtered["Indicator"].tolist())
    chart_data = filtered[filtered["Indicator"].isin(selected)]
    if not chart_data.empty:
        fig = px.bar(chart_data, x="Value (%)", y="Indicator", orientation="h", text="Value (%)", color="Theme", hover_data=["Population / definition","Survey"])
        fig.update_traces(texttemplate="%{text}%", textposition="outside", cliponaxis=False)
        fig.update_layout(xaxis=dict(range=[0,110], ticksuffix="%"), yaxis_title="", xaxis_title="Published percentage (%)", margin=dict(l=10,r=35,t=15,b=10), legend_title="Theme")
        st.plotly_chart(fig, use_container_width=True)
    st.markdown("#### Indicator definitions")
    st.dataframe(chart_data[["Indicator","Value (%)","Population / definition","Survey","Theme","Source"]], use_container_width=True, hide_index=True, column_config={"Source": st.column_config.LinkColumn("Source", display_text="Open official source")})

elif page == "Gender gap lab":
    st.markdown("### Gender gap lab")
    st.write("Inspect the published difference in transactional account uptake. The values are fixed published aggregates; controls help communicate the difference, not simulate or estimate causes.")
    
    col1, col2 = st.columns(2)
    with col1:
        gender = pd.DataFrame({"Group":["Female adults","Male adults"],"Uptake (%)":[73,82]})
        fig = go.Figure()
        fig.add_trace(go.Bar(x=gender["Group"], y=gender["Uptake (%)"], text=[f"{x}%" for x in gender["Uptake (%)"]], textposition="outside", marker_color=["#0f766e","#173f5f"]))
        fig.update_layout(yaxis=dict(range=[0,100],ticksuffix="%"), yaxis_title="Transactional account uptake (%)", xaxis_title="", showlegend=False, margin=dict(l=15,r=15,t=25,b=15))
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number+delta", value = 82, domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Male Uptake (Target: Female 73%)", 'font': {'size': 18}},
            delta = {'reference': 73, 'increasing': {'color': "green"}},
            gauge = {'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"}, 'bar': {'color': "#1e3a8a"}, 'bgcolor': "white", 'borderwidth': 2, 'bordercolor': "gray",
                     'steps': [{'range': [0, 73], 'color': '#f1f5f9'}, {'range': [73, 82], 'color': '#fca5a5'}],
                     'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 90}}))
        fig_gauge.update_layout(margin=dict(l=20,r=20,t=50,b=20))
        st.plotly_chart(fig_gauge, use_container_width=True)

elif page == "Action planner & Algorithms":
    st.markdown("### Decision Support & Algorithms")
    st.write("To provide real-world value, UbukunguLens includes algorithmic logic to assist financial institutions and policymakers in targeting interventions.")
    
    st.markdown("#### 1. Micro-Savings & Credit Risk Simulator")
    st.caption("This algorithm demonstrates how demographic factors correlate with formal credit uptake. It is a simulated logic model for planning purposes, not a real credit score.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        location = st.selectbox("Location Type", ["Urban", "Rural"])
    with col2:
        gender = st.selectbox("Gender", ["Male", "Female"])
    with col3:
        income = st.slider("Estimated Monthly Income (RWF)", 10000, 500000, 100000, step=10000)
        
    # Algorithmic Logic (Simulated based on known gaps)
    base_score = 50
    if location == "Urban": base_score += 15
    if gender == "Male": base_score += 10
    if income > 200000: base_score += 20
    elif income > 100000: base_score += 10
    
    risk_score = min(max(base_score, 10), 95)
    
    st.markdown("---")
    if risk_score > 70:
        st.success(f"**Credit Readiness Score: {risk_score}/100** - High potential for formal financial products. Recommended: Direct them to bank loan products.")
    elif risk_score > 50:
        st.warning(f"**Credit Readiness Score: {risk_score}/100** - Moderate potential. Recommended: Digital savings groups (SACCOs) or micro-leasing.")
    else:
        st.error(f"**Credit Readiness Score: {risk_score}/100** - Vulnerable. Recommended: Social protection integration (VUP) and financial literacy programs.")

    st.markdown("---")
    st.markdown("#### 2. Policy Intervention Calculator")
    st.write("Calculate the scale required to close the gender gap in transactional accounts.")
    target_pop = st.number_input("Target District Population (Adults)", min_value=1000, max_value=1000000, value=50000, step=1000)
    current_female = round(target_pop * 0.73)
    target_female = round(target_pop * 0.80)
    gap = target_female - current_female
    st.metric("Additional Women Needing Accounts to Reach 80% Target", f"{gap:,}")

elif page == "Data & methodology":
    st.markdown("### Data provenance and limitations")
    st.write("The current prototype prioritizes traceability over unsupported detail. It uses published aggregate indicators and does not claim to have processed individual respondent records.")
    
    st.markdown("#### Method and limitations")
    st.markdown("""
    - **Data Pipeline (Phase 1):** This MVP uses officially published aggregate statistics to establish the national baseline. The dashboard is architected so that Phase 2 will seamlessly integrate the raw NISR Microdata (FinScope 2024 & EICV7) via the same Pandas dataframe structure.
    - **Microdata Access:** The team has registered on the NISR portal. Upon approval of the microdata access request, respondent-level analysis (with proper survey weights) will replace the national aggregates to enable district-level and demographic drill-downs.
    - **FinScope 2024:** The study catalog reports an edited anonymous dataset with 13,994 cases and 2,500 variables.
    - **Gender comparison:** The 9 percentage-point difference is calculated as 82% minus 73%. It is descriptive.
    - **Poverty:** EICV7's 27.4% national poverty rate is shown only as separate national context.
    - **No unsupported breakdowns:** No regional, VUP-beneficiary, formal-credit, or group-level poverty estimates are included without a verified source and matching definitions.
    - **AI assistance:** Disclose the use of AI tools in accordance with the competition's instructions and review every output before submission.
    """)

st.divider()
st.caption("UbukunguLens · NISR Big Data Hackathon 2026 · Track 2")