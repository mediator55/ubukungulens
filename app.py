import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Page Configuration
st.set_page_config(
    page_title="UbukunguLens | Rwanda Financial Inclusion",
    page_icon="🇷🇼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Data Sources & Definitions
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
poverty_rate = 27.4  # EICV7 2023/24 national poverty rate

# 3. Enhanced UI Styling (Kigali Tech Theme)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

/* Global Font & Background */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: #1e293b;
}
.stApp {
    background-color: #f8fafc;
}

/* The Hero Banner */
.hero {
    padding: 3rem 2rem; 
    border-radius: 24px; 
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #0f766e 100%); 
    color: white; 
    margin-bottom: 2rem;
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    position: relative;
    overflow: hidden;
}
/* Add a subtle glowing orb to the hero */
.hero::after {
    content: '';
    position: absolute;
    top: -50px;
    right: -50px;
    width: 200px;
    height: 200px;
    background: radial-gradient(circle, rgba(96,165,250,0.4) 0%, rgba(0,0,0,0) 70%);
    border-radius: 50%;
}
.hero h1 {
    color: white; 
    font-weight: 800;
    font-size: 3rem; 
    margin: 0;
    letter-spacing: -0.03em;
}
.hero p {
    color: #93c5fd; 
    font-size: 1.2rem;
    margin-top: 0.5rem;
    font-weight: 500;
}
.kicker {
    text-transform: uppercase; 
    letter-spacing: 0.15em; 
    font-size: 0.85rem; 
    font-weight: 800; 
    color: #2dd4bf;
}

/* Make Metrics Pop */
div[data-testid="stMetricValue"] {
    color: #0f172a !important;
    font-weight: 800 !important;
    font-size: 2.8rem !important;
}
div[data-testid="stMetric"] {
    background-color: #ffffff;
    padding: 1.5rem !important;
    border-radius: 16px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    transition: transform 0.2s ease-in-out;
}
div[data-testid="stMetric"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

/* Clean up the Section Cards */
.section-card {
    border: 1px solid #e2e8f0; 
    padding: 1.5rem; 
    border-radius: 16px; 
    height: 100%;
    background-color: #ffffff;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
}
.section-card h2 {
    color: #0f172a;
}

/* Better Alerts */
div[data-testid="stAlert"] {
    border-radius: 12px;
    border: none;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
.small-note { font-size: 0.85rem; color: #64748b; margin-top: 10px; }

/* Style the Sidebar */
[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #e2e8f0;
}
</style>
""", unsafe_allow_html=True)
# 4. Sidebar Navigation
with st.sidebar:
    st.markdown("## 🇷🇼 UbukunguLens")
    st.caption("NISR Big Data Hackathon 2026 · Track 2")
    page = st.radio("Explore", ["Executive overview", "Explore indicators", "Gender gap lab", "Action planner", "Data & methodology"])
    st.divider()
    st.markdown("**Data integrity**")
    st.caption("Published aggregate statistics only. No invented regional, VUP, credit, or subgroup poverty estimates.")
    st.markdown("[FinScope 2024 source ↗](%s)" % FINSCOPE_REPORT)
    st.markdown("[EICV7 source ↗](%s)" % EICV_REPORT)

# 5. Global Hero Banner
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
    st.write("Rwanda reports high overall financial inclusion, but the headline rate alone does not tell the whole story. UbukunguLens helps reviewers inspect different dimensions of access, digital finance and account uptake—and keeps the poverty indicator separate where the surveys do not support a direct linkage.")

    a,b,c,d = st.columns(4)
    a.metric("Financially included", "96%", help="FinScope 2024; formal and/or informal financial products.")
    b.metric("Formally included", "92%", help="FinScope 2024; formal financial products/services.")
    c.metric("Own/use mobile money", "86%", help="FinScope 2024; adults who own or have used mobile money.")
    d.metric("Mobile wallet in own name", "77%", help="FinScope 2024; adults with a registered mobile wallet in their own name.")

    st.markdown("---")
    st.error("**The Core Paradox:** While 96% of Rwandan adults are financially included, only **22% are banked**, and there is a **9-point gender gap** in who holds a transactional account. Access is high, but usage depth remains a challenge.")
    st.markdown("---")

    st.markdown("### A closer look at access")
    left,right = st.columns([1.15,1])
    with left:
        g = pd.DataFrame({"Group":["Women","Men"],"Transactional account uptake (%)":[73,82]})
        fig = px.bar(g, x="Group", y="Transactional account uptake (%)", text="Transactional account uptake (%)",
                     range_y=[0,100], color="Group", color_discrete_sequence=["#0f766e","#173f5f"])
        fig.update_traces(texttemplate="%{text}%", textposition="outside", cliponaxis=False)
        fig.update_layout(showlegend=False, margin=dict(l=10,r=10,t=15,b=10), yaxis_ticksuffix="%", yaxis_title="Adults (%)", xaxis_title="")
        st.plotly_chart(fig, use_container_width=True)
        st.caption("FinScope 2024 reports 73% for female adults and 82% for male adults on transactional account uptake.")
    with right:
        gap = 82-73
        st.markdown(f"""
        <div class="section-card">
          <div class="kicker" style="color:#087e8b">Signal to investigate</div>
          <h2 style="font-size:2.5rem;margin:.2rem 0;color:#12233f">{gap} percentage points</h2>
          <p><b>Transactional account uptake gap</b> between male and female adults in the published FinScope 2024 figures.</p>
          <p class="small-note">This is a descriptive difference, not evidence of why the gap exists. The app does not infer causes or individual outcomes.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("")
        st.metric("National poverty rate", f"{poverty_rate}%", help="EICV7 2023/24 national estimate. Separate survey; not linked to the FinScope groups shown.")
        st.caption("Poverty context is deliberately separate because the available published aggregates do not establish a person-level relationship between poverty and financial-service use.")

    st.markdown("### What a decision-maker can take away")
    st.markdown("""
    - **Measure more than access:** overall inclusion, formal inclusion, digital finance and account use are different indicators.
    - **Investigate the gender gap:** the published transactional-account figures show a 9-point difference worth further analysis.
    - **Avoid unsupported conclusions:** these aggregate statistics do not identify causes, district-level patterns, VUP effects, or poverty outcomes by financial-service group.
    - **Next analytical step:** request authorized FinScope microdata and, where permitted, link analysis to suitable welfare data using a defensible methodology.
    """)
    st.info("Interpretation guardrail: the percentages shown have different definitions and sometimes different denominators. They are not a single funnel and should not be added together.")

elif page == "Explore indicators":
    st.markdown("### Indicator explorer")
    st.write("Filter published indicators by theme, compare their values, and inspect definitions before interpreting them.")
    themes = ["All themes"] + sorted(indicators["Theme"].unique().tolist())
    selected_theme = st.selectbox("Theme", themes)
    filtered = indicators if selected_theme == "All themes" else indicators[indicators["Theme"] == selected_theme]
    selected = st.multiselect("Indicators to display", filtered["Indicator"].tolist(), default=filtered["Indicator"].tolist())
    chart_data = filtered[filtered["Indicator"].isin(selected)]
    if not chart_data.empty:
        fig = px.bar(chart_data, x="Value (%)", y="Indicator", orientation="h", text="Value (%)",
                     color="Theme", hover_data=["Population / definition","Survey"])
        fig.update_traces(texttemplate="%{text}%", textposition="outside", cliponaxis=False)
        fig.update_layout(xaxis=dict(range=[0,110], ticksuffix="%"), yaxis_title="", xaxis_title="Published percentage (%)",
                          margin=dict(l=10,r=35,t=15,b=10), legend_title="Theme")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Choose at least one indicator.")
    st.markdown("#### Indicator definitions")
    st.dataframe(chart_data[["Indicator","Value (%)","Population / definition","Survey","Theme","Source"]], use_container_width=True, hide_index=True,
                 column_config={"Source": st.column_config.LinkColumn("Source", display_text="Open official source")})
    st.download_button("Download selected indicators (CSV)", data=chart_data.to_csv(index=False).encode("utf-8"),
                       file_name="ubukungulens_selected_indicators.csv", mime="text/csv")

elif page == "Gender gap lab":
    st.markdown("### Gender gap lab")
    st.write("Inspect the published difference in transactional account uptake. The values are fixed published aggregates; controls help communicate the difference, not simulate or estimate causes.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        gender = pd.DataFrame({"Group":["Female adults","Male adults"],"Uptake (%)":[73,82]})
        fig = go.Figure()
        fig.add_trace(go.Bar(x=gender["Group"], y=gender["Uptake (%)"], text=[f"{x}%" for x in gender["Uptake (%)"]],
                             textposition="outside", marker_color=["#0f766e","#173f5f"]))
        fig.update_layout(yaxis=dict(range=[0,100],ticksuffix="%"), yaxis_title="Transactional account uptake (%)",
                          xaxis_title="", showlegend=False, margin=dict(l=15,r=15,t=25,b=15))
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = 82,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Male Uptake (Target: Female 73%)", 'font': {'size': 18}},
            delta = {'reference': 73, 'increasing': {'color': "green"}},
            gauge = {
                'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "#1e3a8a"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 73], 'color': '#f1f5f9'},
                    {'range': [73, 82], 'color': '#fca5a5'}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        ))
        fig_gauge.update_layout(margin=dict(l=20,r=20,t=50,b=20))
        st.plotly_chart(fig_gauge, use_container_width=True)

    gap = 82 - 73
    x,y,z = st.columns(3)
    x.metric("Female adults", "73%")
    y.metric("Male adults", "82%")
    z.metric("Difference", f"{gap} pp")

    st.markdown("#### Questions for a future microdata analysis")
    st.markdown("""
    1. Does the gap persist after accounting for age, education, employment, household characteristics and location?
    2. Are account ownership and actual usage different, and how are those outcomes defined in the questionnaire?
    3. What uncertainty estimates and survey weights are required for valid subgroup comparisons?
    4. Which barriers are directly measured in the survey, rather than assumed?
    """)
    st.warning("The current published aggregate figures cannot answer these questions. Do not present them as findings until the authorized microdata analysis is completed.")

elif page == "Action planner":
    st.markdown("### Action planner: turn evidence into a testable question")
    st.write("This is a transparent planning aid—not a forecast, causal model, or claim about how many people a policy will reach.")
    st.markdown("#### Illustrative target-setting calculator")
    st.caption("The baseline and target below are user-entered planning assumptions applied to a hypothetical group size. They are not official population counts or predictions.")
    col1,col2,col3 = st.columns(3)
    with col1:
        group_size = st.number_input("Hypothetical group size", min_value=100, max_value=10000000, value=10000, step=100)
    with col2:
        baseline = st.slider("Baseline uptake (%)", min_value=0, max_value=100, value=73)
    with col3:
        target = st.slider("Illustrative target uptake (%)", min_value=0, max_value=100, value=80)
    baseline_count = round(group_size * baseline / 100)
    target_count = round(group_size * target / 100)
    delta = target_count - baseline_count
    q1,q2,q3 = st.columns(3)
    q1.metric("At baseline", f"{baseline_count:,}", help="Arithmetic illustration only.")
    q2.metric("At target", f"{target_count:,}", help="Arithmetic illustration only.")
    q3.metric("Difference", f"{delta:+,}", help="Not an estimate of policy impact.")
    st.info("Use this calculator to frame a measurable goal. A real impact estimate would require a defined intervention, eligible population, baseline data, a comparison strategy, and uncertainty analysis.")
    st.markdown("#### Suggested evidence-to-action cycle")
    st.markdown("""
    **1. Diagnose:** identify the service and group of interest using valid survey definitions.  
    **2. Understand barriers:** use questionnaire variables or additional research; do not infer causes from a gap alone.  
    **3. Design a pilot:** specify the target group, service, timeline and measurable outcome.  
    **4. Evaluate:** compare baseline and follow-up outcomes with an appropriate evaluation design.  
    **5. Report responsibly:** publish methods, limitations and uncertainty alongside results.
    """)

elif page == "Data & methodology":
    st.markdown("### Data provenance and limitations")
    st.write("The current prototype prioritizes traceability over unsupported detail. It uses published aggregate indicators and does not claim to have processed individual respondent records.")
    st.markdown("#### Official sources")
    st.markdown(f"- [FinScope 2024 study catalog]({FINSCOPE_CATALOG})")
    st.markdown(f"- [FinScope 2024 NISR publication page]({FINSCOPE_REPORT})")
    st.markdown(f"- [EICV7 catalog]({EICV_CATALOG})")
    st.markdown(f"- [EICV7 2023/24 report page]({EICV_REPORT})")
    st.markdown("#### Data table")
    st.dataframe(indicators, use_container_width=True, hide_index=True,
                 column_config={"Source": st.column_config.LinkColumn("Official source", display_text="Open source")})
    st.download_button("Download all published indicators (CSV)", data=indicators.to_csv(index=False).encode("utf-8"),
                       file_name="ubukungulens_published_indicators.csv", mime="text/csv")
    st.markdown("#### Method and limitations")
    st.markdown("""
    - **Data type:** manually transcribed published aggregate statistics, not microdata.
    - **FinScope 2024:** the study catalog reports an edited anonymous dataset with 13,994 cases and 2,500 variables; the published survey description also reports a sample of approximately 14,000 households. These counts describe different catalog/reporting details and should not be treated as identical units without checking the source documentation.
    - **Gender comparison:** the 9 percentage-point difference is calculated as 82% minus 73%. It is descriptive and has no uncertainty interval in this prototype.
    - **Poverty:** EICV7's 27.4% national poverty rate is shown only as separate national context. It is not a poverty rate for FinScope respondents or any subgroup in this dashboard.
    - **No unsupported breakdowns:** no regional, VUP-beneficiary, formal-credit, or group-level poverty estimates are included without a verified source and matching definitions.
    - **Next step:** if microdata access is granted, document variable selection, weights, missing data, complex survey design, uncertainty, and reproducible processing before making subgroup claims.
    - **AI assistance:** disclose the use of AI tools in accordance with the competition's instructions and review every output before submission.
    """)
    st.markdown("#### Reproducibility")
    st.code("python -m venv .venv\n# Windows: .venv\\Scripts\\activate\npip install -r requirements.txt\nstreamlit run app.py", language="bash")

st.divider()
st.caption("UbukunguLens · NISR Big Data Hackathon 2026 · Track 2: Financial Inclusion & Poverty Reduction")
st.caption("Independent student prototype. Statistics are attributed to official sources. This is not an official NISR application and should not be used as a substitute for the source reports.")