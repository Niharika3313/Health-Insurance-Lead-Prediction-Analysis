# Health Insurance Lead Prediction Analysis

## Table of Contents

* [Project Overview](#project-overview)
* [Objectives](#objectives)
* [Tools & Technologies](#tools--technologies)
* [Dataset](#dataset)
* [Executive Summary](#executive-summary)
* [Key Insights](#key-insights)

  * [Lead Conversion](#lead-conversion)
  * [Customer Demographics](#customer-demographics)
  * [Policy Category](#policy-category)
  * [Regional Analysis](#regional-analysis)
  * [Premium Analysis](#premium-analysis)
* [Predictive Modeling](#predictive-modeling)
* [Business Recommendations](#business-recommendations)
* [Limitations](#limitations)
* [Conclusion](#conclusion)

---

## Project Background

This portfolio project analyzes a health insurance lead dataset containing **50,882 customer records** to understand the factors that influence whether a customer purchases a health insurance policy.

The objective was to identify demographic, behavioral, and policy-related patterns that affect lead conversion and provide actionable business recommendations. The project demonstrates the complete data analysis workflow—from data cleaning and exploratory analysis to interactive dashboards and a basic machine learning model for predictive analysis.

## Objectives

* Clean and prepare the dataset for analysis.
* Explore customer demographics and policy-related information.
* Identify factors influencing lead conversion.
* Create meaningful visualizations and dashboards.
* Generate business recommendations based on the findings.
* Explore whether a machine learning model can predict customer conversion.

---

## Tools & Technologies

* **SQL** – Data exploration and business queries
* **Python** – Data cleaning, EDA, visualization, and modeling
* **Power BI** – Interactive dashboard development
* **Excel** – Initial data inspection

**Python Libraries**

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## Dataset

* **Records:** 50,882
* **Features:** 14
* **Target Variable:** Response (Interested / Not Interested)

The dataset contains customer demographic information, policy details, premium information, and previous insurance history.

---

# Executive Summary

The analysis shows an overall conversion rate of **24%**, indicating that approximately one out of every four leads purchases a policy.

Some of the key findings include:

* Customers aged **36–45** have the highest conversion rate.
* **Recommended Policy Category** is the strongest factor associated with conversion.
* Premium amount alone does not significantly influence customer decisions.
* Conversion rates vary noticeably across different cities and regions.
* Accommodation type has only a small impact on customer conversion.

These findings can help businesses improve lead targeting and marketing strategies.

---

# Key Insights

## Lead Conversion

* Total Customers: **50,882**
* Interested Customers: **12,209 (24%)**
* Not Interested: **38,673 (76%)**

The business opportunity lies in improving conversion by focusing marketing efforts on customers with a higher likelihood of purchasing.

---

## Customer Demographics

Analysis shows that conversion does not increase steadily with age.

Instead, customers between **36 and 45 years** have the highest conversion rate, while the **18–25** age group has the lowest.

---

## Policy Category

The recommended policy category has the strongest relationship with customer conversion.

This suggests that recommending the right policy is likely more important than focusing only on demographic characteristics.

---

## Regional Analysis

Customer response varies across cities.

Some cities consistently perform better than others, indicating that regional marketing strategies could improve campaign effectiveness.

---

## Premium Analysis

Customers who converted and those who did not received similar premium recommendations.

This suggests that premium amount alone is not the primary reason customers decide to purchase a policy.

---

# Predictive Modeling

As an additional learning exercise, I built a **Random Forest Classifier** to predict customer conversion.

Since my primary focus is Data Analytics rather than Machine Learning, I used an AI coding assistant to help implement the machine learning code while ensuring I understood the workflow, evaluation metrics, and interpretation of the results.

The model achieved a **ROC-AUC score of approximately 0.62**, showing moderate predictive capability.

Feature importance analysis identified **Recommended Policy Category** as the strongest predictor of customer conversion.

---

# Business Recommendations

Based on the analysis, the following recommendations were identified:

* Improve policy recommendations based on customer profiles.
* Focus marketing efforts on the 26–45 age group.
* Analyze successful cities and replicate their strategies in lower-performing regions.
* Develop more personalized customer targeting instead of relying on demographic variables alone.
* Explore additional feature engineering and techniques to improve predictive model performance.

---

# Conclusion

This project demonstrates an end-to-end data analytics workflow involving data cleaning, exploratory data analysis, SQL querying, dashboard creation, business insight generation, and introductory predictive modeling.

The focus of the project is not only to build visualizations but also to translate data into practical business recommendations that can support decision-making.
tive_modeling.ipynb).
