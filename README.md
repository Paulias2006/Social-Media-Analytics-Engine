# Social Media Analytics Engine

Portfolio project for Python, SQL, sentiment analysis, dashboard reporting, and marketing analytics.

## Client Problem

Brands, creators, and agencies need a fast way to understand social media performance: what content drives engagement, which topics are growing, and whether audience sentiment is positive or negative.

This project builds a complete analytics workflow:

- generate a privacy-safe demo dataset of social media posts;
- calculate sentiment with an explainable lexicon method;
- detect hashtag and platform trends;
- store posts and metrics in SQLite;
- export CSV tables for Excel, Power BI, or SQL;
- generate a client-ready HTML dashboard.

## Files

- `config/settings.json` - project settings, platforms, topics, and dataset size
- `src/run_pipeline.py` - main orchestration script
- `src/data_generation.py` - demo post dataset generator
- `src/sentiment.py` - transparent sentiment scoring
- `src/analytics.py` - KPI and trend calculations
- `src/database.py` - SQLite storage and query helpers
- `src/dashboard.py` - HTML dashboard generator
- `src/csv_utils.py` - CSV export helper
- `sql/social_media_queries.sql` - SQL portfolio queries
- `outputs/` - generated CSV files and dashboard
- `reports/portfolio_case_study.md` - project case study
- `UPWORK_PROJECT_DESCRIPTION.md` - text ready to publish on Upwork

## Run

```bash
python src/run_pipeline.py
```

No external dependency is required. The project intentionally uses only the Python standard library.

## Portfolio Angle

This project demonstrates practical data analytics: data preparation, sentiment scoring, SQL reporting, trend detection, and dashboard delivery.
