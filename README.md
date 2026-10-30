# UbukunguLens — Competition-ready prototype

**Rwanda's Financial Inclusion & Usage Explorer**  
NISR Big Data Hackathon 2026 · Track 2: Financial Inclusion & Poverty Reduction

## What it does
UbukunguLens presents published aggregate statistics in a clear, interactive dashboard. It includes:
- Executive overview with key published indicators.
- Interactive indicator explorer with theme filtering, definitions, official source links, and CSV export.
- A descriptive gender-gap view.
- An explicitly illustrative target-setting calculator (not a prediction or impact estimate).
- Data provenance, methodology, limitations, and a microdata-analysis roadmap.

## Data integrity
This version uses published aggregate figures from official FinScope 2024 and EICV7 2023/24 sources. It does **not** claim to analyze respondent-level microdata. The EICV7 national poverty rate is displayed separately and is not linked to FinScope respondents or subgroups.

No unsupported regional, VUP-beneficiary, formal-credit, or group-level poverty figures are included.

## Official sources
- [FinScope 2024 study catalog](https://www.microdata.statistics.gov.rw/index.php/catalog/120/study-description)
- [FinScope 2024 NISR publication page](https://www.statistics.gov.rw/statistical-publications/business-establishment-finance-trade/finscope-survey-2024)
- [EICV7 catalog](https://www.microdata.statistics.gov.rw/index.php/catalog/119)
- [EICV7 2023/24 report page](https://statistics.gov.rw/data-sources/surveys/EICV/integrated-household-living-conditions-survey-7-eicv-7)

## Run locally
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Deploy
1. Upload `app.py`, `requirements.txt`, `README.md`, and `data/` to a public GitHub repository.
2. Deploy on [Streamlit Community Cloud](https://share.streamlit.io/) using `app.py` as the entry point.
3. Open the public URL in a private/incognito window and test every page, filter, chart, source link, and CSV download.
4. Record a screen demonstration no longer than 3 minutes.
5. Submit the public GitHub link, live app link, and documentation as required by NISR.


## Method limitations
- The percentages are published aggregates, not newly computed microdata estimates.
- Definitions and denominators differ by indicator.
- The gender gap is a descriptive difference (82% − 73% = 9 percentage points), without uncertainty intervals in this prototype.
- EICV7's national poverty rate is separate context, not a FinScope subgroup estimate.
- A future microdata version should document weights, survey design, missing-value handling, variable definitions, uncertainty, and reproducible analysis.
- Disclose AI assistance according to competition requirements and review all code/content before submission.

## Project status
This is an independent student prototype, not an official NISR product. It is not yet a live deployment until the team deploys and verifies it.
