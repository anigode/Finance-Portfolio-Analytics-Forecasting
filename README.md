# Finance-Portfolio-Analytics-Forecasting
This project focuses on analyzing long-term financial market data to evaluate portfolio performance and compare statistical and machine learning-based forecasting models. The analysis combines historical price data, return calculations, and predictive modeling to assess risk, return, and forecast accuracy. Interactive Power BI dashboards are used to communicate insights to business and investment stakeholders.

# Table of Contents
- Business Problem
- Objective
- Introduction
- Installation
- Usage
- Data
- Analysis
- Evaluation
- Libraries

# Business Problem
Investment managers and analysts need to understand historical portfolio behavior while evaluating different forecasting approaches to support data-driven investment decisions.
- Key challenges include:
  - Measuring portfolio growth and volatility over time
  - Comparing traditional time-series models with machine learning models
  - Evaluating forecast accuracy and directional performance
  - Communicating results clearly to non-technical stakeholders

# Objective
- Analyze historical portfolio returns and portfolio value trends
- Forecast future returns using ARIMA and Random Forest models
- Compare models using RMSE, MAE, MAPE, and directional accuracy
- Build Power BI dashboards to visualize portfolio performance and model comparison

# Introduction
The goal of this project is to combine financial analytics, forecasting, and business intelligence into a single end-to-end workflow. Historical market data is processed to compute daily returns and portfolio value, followed by statistical and machine learning forecasting. The final output is an interactive Power BI dashboard that enables stakeholders to explore portfolio performance, risk metrics, and model effectiveness.

# Installation
- Clone the repository
- Install the required libraries
- Ensure Python 3.8 or above is installed
- Open the Jupyter notebooks to reproduce data processing and modeling steps

# Usage
- Place the processed market data files in the data/processed directory
- Run the notebook Ingest_merge.ipynb to prepare portfolio metrics
- Execute forecasting scripts to generate ARIMA and ML predictions
- Load the exported CSV files into Power BI to explore interactive dashboards

# Data
The project uses historical market and portfolio data with the following features:

- Date
- Daily Return
- Actual Return
- Portfolio Value
- ARIMA Forecast Return
- ML (Random Forest) Forecast Return

Key preprocessing steps include:
- Handling missing values
- Return calculation and normalization
- Time-series alignment for model comparison

# Analysis
- The analysis focuses on:
- Portfolio growth and drawdown analysis
- Daily return distribution and volatility assessment
- ARIMA vs ML forecast comparison
- Directional accuracy and error metric evaluation

# Evaluation
- Model performance is evaluated using:
- RMSE, MAE, and MAPE
- Directional accuracy for ARIMA and Random Forest
- Visual comparison of actual vs predicted returns
  
# Libraries
- pandas
- numpy
- scikit-learn
- statsmodels
- matplotlib
- seaborn
- joblib
- Power BI (for visualization)
