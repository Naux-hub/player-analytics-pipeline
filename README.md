# 🕹️ Player Analytics Pipeline & Dashboard

This project demonstrates a full-scale **ELT (Extract, Load, Transform) pipeline** designed to analyze player monetization and lifecycle behavior. Using a dataset of over 100,000 transactions, the project transforms raw e-commerce data into actionable gaming insights like **ARPPU**, **Player Retention**, and **Geographical Monetization**.

## 🚀 Live Demo
[LINK TO YOUR STREAMLIT CLOUD APP HERE]

## 🛠️ Tech Stack
*   **Python:** Data processing and dashboarding.
*   **dbt (Data Build Tool):** SQL modeling and transformations.
*   **DuckDB:** In-process analytical database.
*   **Streamlit:** Interactive visualization.
*   **Plotly:** Dynamic charting.

## 📊 Key Analytics Features
*   **Monetization Metrics:** Real-time calculation of Gross Revenue and ARPPU (Average Revenue Per Paying User).
*   **Retention Modeling:** Advanced SQL window functions to track "Days to 2nd Purchase" (Re-engagement).
*   **Geographical Analysis:** Identification of high-value player regions for targeted marketing efforts.
*   **Cohort Filtering:** Dynamic time-based filtering to analyze acquisition cycles.

## 🏗️ Pipeline Architecture
1.  **Staging Layer:** Raw CSV data is ingested into DuckDB and cleaned using dbt.
2.  **Marts Layer:** Business logic is applied (e.g., identity resolution across unique IDs) to create fact tables for orders and retention.
3.  **Visualization:** Streamlit connects directly to the DuckDB instance to serve insights to stakeholders.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Naux-hub/player-analytics-pipeline.git](https://github.com/Naux-hub/player-analytics-pipeline.git)
   cd player-analytics-pipeline
