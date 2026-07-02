# Premier League Analytics Pipeline

A robust, automated data pipeline designed to extract, transform, and analyze Premier League football data. This project leverages Python, pandas, and GitHub Actions to automate data processing workflows.

## 🚀 Project Overview
This pipeline performs daily automated data collection from the Football-Data API. It processes raw data into cleaned, analytical-ready formats, enabling data-driven insights into league standings and team performance.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Data Manipulation:** pandas
- **Automation:** GitHub Actions
- **API:** [Football-Data.org](https://www.football-data.org/)
- **Infrastructure:** GitHub CLI

## ⚙️ How it Works
1. **Extraction:** Fetches raw standings data daily.
2. **Transformation:** Cleans data and calculates key performance indicators (KPIs).
3. **Orchestration:** GitHub Actions triggers the process automatically every day at 08:00 AM UTC.



## 📋 Getting Started
To run this project locally:

1. Clone the repository: `git clone https://github.com/freddantes/premier-league-analytics.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set your API_KEY in a `.env` file.
4. Run the pipeline: `python -m src.main`

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!