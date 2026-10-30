UbukunguLens
Rwanda's Financial Inclusion & Usage Explorer
NISR Big Data Hackathon 2026
Track 2: Financial Inclusion & Poverty Reduction
Development Team
•	Fidele Nsengiyaremye — University of Kigali
•	Aime Dominique UWASE — University of Kigali
Project Type: Interactive Data Analytics and Visualization Platform

1. Project Overview
UbukunguLens is an interactive data analytics and visualization platform developed for the NISR Big Data Hackathon 2026. It is designed to make Rwanda's financial inclusion statistics more accessible, understandable, and useful.
The platform transforms selected published statistical indicators into interactive visual insights, allowing users to explore financial inclusion, formal financial services, mobile money usage, banking access, and gender differences in transactional account uptake.
Through interactive dashboards, indicator comparisons, and an illustrative planning calculator, UbukunguLens aims to support public understanding, research, and evidence-informed discussions about financial inclusion and poverty reduction in Rwanda.
2. Problem Statement
Financial inclusion is an important component of economic participation and socioeconomic development. However, statistical reports and datasets can be difficult for the public, students, researchers, and decision-makers to explore and interpret efficiently.
Understanding the level of financial inclusion, comparing access to different financial services, and identifying areas requiring further investigation are important steps towards addressing financial inclusion challenges.
UbukunguLens addresses this challenge by providing an accessible, interactive platform for exploring selected official statistics and presenting them through meaningful visualizations.


3. Project Objectives
The project aims to:
•	Improve accessibility and understanding of published financial inclusion statistics.
•	Present important indicators through interactive dashboards and visualizations.
•	Enable users to explore and compare selected financial inclusion indicators.
•	Highlight descriptive differences in transactional account uptake between women and men.
•	Provide an illustrative tool for exploring hypothetical financial inclusion targets.
•	Promote transparency through official data references, methodology, and limitations.
•	Encourage further research into financial inclusion barriers and opportunities in Rwanda.
4. System Features and Functionalities
4.1 Executive Overview
The Executive Overview provides a high-level summary of selected national financial inclusion indicators.
It presents:
•	Overall financial inclusion.
•	Formal financial inclusion.
•	Mobile money ownership or usage.
•	Mobile wallets registered in users' own names.
•	Transactional account uptake by gender.
•	National poverty context from EICV7, displayed separately.
The overview helps users understand important indicators and identify areas that may require further investigation.
4.2 Interactive Indicator Explorer
This section allows users to explore published financial inclusion indicators through:
•	Theme-based filtering.
•	Selection of indicators for comparison.
•	Interactive charts and visualizations.
•	Indicator descriptions and population information.
•	Official source references.
•	CSV data export.
Users can interact with the visualizations to examine selected indicators and obtain more information about the statistics presented.

4.3 Gender Gap Analysis
This section presents a descriptive comparison of transactional account uptake between female and male adults.
Group	Transactional account uptake
Female adults	73%
Male adults	82%
Difference	9 percentage points
The comparison highlights a gender-related difference that deserves further investigation.
The current aggregate data does not establish the causes of the observed difference.
4.4 Action Planner
The Action Planner provides an illustrative target-setting calculator for exploring hypothetical financial inclusion scenarios.
Users can enter:
•	A hypothetical population or group size.
•	A baseline uptake percentage.
•	A target uptake percentage.
The system calculates the corresponding baseline number, target number, and numerical difference.
For example, users can explore what moving from 73% to 80% uptake would represent for a hypothetical group of 10,000 people.
The calculator supports scenario exploration and planning discussions. Its results are not predictions, official population estimates, or measurements of actual policy impact.
4.5 Data and Methodology
This section provides information about the statistical sources and methodology used by the platform.
It includes:
•	Official NISR data source references.
•	Indicator descriptions and definitions.
•	Data provenance and methodology.
•	Downloadable indicator data.
It also explains the distinction between published aggregate statistics and individual-level survey microdata.
5. Data Sources
UbukunguLens uses selected published aggregate statistics from official sources of the National Institute of Statistics of Rwanda (NISR).
5.1 FinScope Survey 2024
The FinScope Survey provides information about financial access and usage in Rwanda.
Official references:
•	NISR – FinScope Survey 2024 Publication
•	FinScope 2024 – NISR Microdata Study Catalog
•	FinScope 2024 – Microdata Access Policy
5.2 EICV7 – Integrated Household Living Conditions Survey
EICV7 provides information about household living conditions and poverty in Rwanda.
Official references:
•	NISR – EICV7 Survey and Report
•	EICV7 – NISR Microdata Catalog
The EICV7 national poverty indicator is presented separately as socioeconomic context. It is not linked to FinScope respondents or financial inclusion subgroups.
6. Data Integrity and Methodology
The current version of UbukunguLens uses selected published aggregate statistics from official NISR sources. It does not claim to perform respondent-level microdata analysis.
The indicators are organized in a structured CSV dataset and processed using Python and Pandas. Streamlit provides the interactive interface, while Plotly supports data visualization.
The project follows these data interpretation principles:
•	Published statistics are presented as reported indicators, not as newly calculated microdata estimates.
•	Indicators are interpreted according to their respective definitions and population denominators.
•	Comparisons are descriptive and do not establish causal relationships.
•	Statistics from different surveys are not treated as if they were collected from the same respondents.
•	Hypothetical calculator outputs are distinguished from measured national statistics.
•	Official source references are provided to support verification.

Methodological Limitations
•	The displayed percentages are published aggregate statistics, not newly computed respondent-level estimates.
•	Indicator definitions, reference populations, and denominators may differ.
•	The gender comparison represents a descriptive difference of 9 percentage points; uncertainty intervals are not calculated in this prototype.
•	The EICV7 national poverty rate is separate socioeconomic context, not a FinScope subgroup poverty estimate.
•	The current version does not establish regional, beneficiary-level, or causal relationships unsupported by the published indicators used.
Future development involving individual-level survey microdata would require appropriate data access and documented procedures for survey weights, survey design, variable definitions, missing values, uncertainty estimation, and reproducible analysis.
7. Technology Stack
Technology	Purpose
Python	Main programming language
Streamlit	Interactive web application framework
Pandas	Data processing and organization
Plotly	Interactive charts and data visualization
CSV	Structured indicator data
Git	Source code version control
GitHub	Source code repository and collaboration
8.a) System Architecture
UbukunguLens follows a data-driven application architecture.
           Official NISR Sources
                    |
                    v
           Published Indicators
                    |
                    v
              CSV Dataset
                    |
                    v
           Python Application
                    |
             +------+------+
             |             |
             v             v
           Pandas       Streamlit
             |             |
             v             v
       Data Processing   User Interface
                           |
                           v
                      Plotly Charts
                           |
                           v
                         Users
The CSV dataset provides the published indicators. Pandas handles data processing, Streamlit manages the interactive application interface, and Plotly presents the visualizations.
8.b) Repository Structure
ubukungulens/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── published_indicators.csv
│
├── video/
│   └── demonstration_video.webm
│
└── eligibility_documents/
    ├── Fidele NSENGIYAREMYE/
    └── AIME DOMIQUE UWASE/

File or folder	Description
app.py	Main Streamlit application source code
requirements.txt	Required Python dependencies
README.md	Project documentation
data/	Published indicator dataset used by the application
video/	Application demonstration video, if included in the repository
eligibility_documents/	Student eligibility documents for the two team members
9. Installation and Local Execution
Requirements
•	Python 3.9 or later.
•	pip package manager.
•	A modern web browser.
Step 1: Clone the repository
git clone https://github.com/mediator55/ubukungulens.git
Step 2: Navigate to the project directory
cd ubukungulens
Step 3: Create a virtual environment
python -m venv .venv
Step 4: Activate the virtual environment
Windows:
.venv\Scripts\activate
Linux/macOS:
source .venv/bin/activate
Step 5: Install dependencies
pip install -r requirements.txt
Step 6: Run the application
streamlit run app.py
The application will be accessible locally at:
http://localhost:8501
Open the address in a web browser to interact with UbukunguLens.
10. Deployment and Public Access
UbukunguLens is deployed as a web-based application using Streamlit Community Cloud.
Deployment platform: Streamlit Community Cloud
Live application: https://ubukungulens.streamlit.app/
GitHub repository: https://github.com/mediator55/ubukungulens
The deployed application provides browser-based access to the dashboard without requiring users to install the application locally.
11. Demonstration Video
The demonstration video presents the UbukunguLens application interface, main functionalities, and user interactions.
Watch the UbukunguLens demonstration:
UbukunguLens – Project Demonstration Video
The demonstration is intended to meet the competition's maximum duration requirement of three minutes.
12. Expected Impact
UbukunguLens aims to contribute to a better understanding of financial inclusion in Rwanda by:
•	Making selected official statistics easier to explore.
•	Improving public access to visual representations of financial inclusion indicators.
•	Supporting comparison and interpretation of selected indicators.
•	Highlighting gender-related differences that warrant further investigation.
•	Encouraging research into financial inclusion barriers.
•	Supporting evidence-informed discussions and planning.
The platform is an analytical and educational tool. It does not replace official statistical publications, detailed statistical research, or institutional policy decisions.
13. Reproducibility and Transparency
The repository provides the application source code, dependencies, and indicator dataset required to inspect and run the project.
Users can review the implementation, examine the dataset, install the required packages, and execute the application locally.
Official NISR references are included to support verification and further exploration of the original statistical publications.
14. Originality and AI Assistance Disclosure
UbukunguLens is submitted as the team's project work for the NISR Big Data Hackathon 2026.
AI tools were used as assistants during aspects of project development and documentation. The developers are responsible for reviewing, validating, understanding, and taking responsibility for all submitted code, documentation, data references, and functionality.
External statistical sources and relevant references are acknowledged in this repository.
15. Acknowledgements
The development team acknowledges the National Institute of Statistics of Rwanda (NISR) for publishing the statistical resources that inform this project and for organizing the NISR Big Data Hackathon 2026.


Project: UbukunguLens – Rwanda's Financial Inclusion & Usage Explorer
Competition: NISR Big Data Hackathon 2026
Track: Financial Inclusion & Poverty Reduction
Developed by: Fidele Nsengiyaremye and Aime Dominique UWASE
Institution: University of Kigali
Transforming published statistics into accessible insights for a better understanding of financial inclusion in Rwanda.

