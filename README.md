🏡 Bangalore Home Price Prediction: End-to-End ML System

This project demonstrates a complete machine learning pipeline: from rigorous statistical data cleaning and model optimization to full-stack MLOps deployment using a Flask REST API and a custom frontend.

🔗 Live Deployment

Your project is live and working here:

🔵 Live App:
https://house-price-prediction-model-x677.onrender.com

🛠️ Technical Stack
Component	Technology	Purpose
Model	Scikit-learn, Lasso Regression	Regularized model for high-dimensional feature selection.
Backend	Flask (API), Gunicorn	RESTful API to serve predictions, running on Render.
Frontend	HTML, CSS, JavaScript	Interactive web application for user input and display.
Data Tools	Pandas, NumPy	Cleaning, feature engineering, and numerical operations.
🔬 Data Engineering & Statistical Rigor

The high R² score is achieved through advanced data preprocessing:

✔️ Statistical Outlier Removal

Implemented location-based Z-score filtering on the derived Price Per SqFt feature, removing ≈ 23% of anomalies and ensuring data integrity.

✔️ Domain Logic Filtering

Applied business rules to clean messy inputs, including:

Converting area ranges (e.g., '1000-1200') to averages

Enforcing logical constraint: bath ≤ bhk + 1

✔️ Dimensionality Reduction

Consolidated 1,304 raw location categories into ≈ 250 features by grouping low-count entries, stabilizing the model for One-Hot Encoding.

🧠 Modeling & Performance

The Lasso Regression model was chosen via GridSearchCV for its ability to perform automatic feature selection on the 250+ location features.

Metric	Score	Insight
Test R² Score	0.845	The model explains 84.5% of the variance in house prices.
Test RMSE	≈ ₹28 Lakhs	The average prediction error on the test set.
