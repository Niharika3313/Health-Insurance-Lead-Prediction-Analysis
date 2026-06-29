# Health Insurance Lead Prediction Analysis

## Table of Contents

-   [Project Overview](#project-overview)
-   [Executive Summary](#executive-summary)
-   [Key Insights](#key-insights)
    -   [Lead Conversion](#lead-conversion)
    -   [Customer Demographics](#customer-demographics)
    -   [Accommodation & Premium
        Analysis](#accommodation--premium-analysis)
    -   [Customer Profile Segmentation](#customer-profile-segmentation)
    -   [Regional Analysis](#regional-analysis)
    -   [Feature Correlations](#feature-correlations)
    -   [Policy Category Performance](#policy-category-performance)
-   [Predictive Modeling](#predictive-modeling)
    -   [Model Performance](#model-performance)
    -   [Feature Importance](#feature-importance)
-   [Business Recommendations](#business-recommendations)
-   [Limitations](#limitations)
-   [Repository Structure](#repository-structure)

------------------------------------------------------------------------

# Project Overview

This portfolio project analyzes a health insurance lead dataset
containing **50,882 customer records** to identify the demographic,
behavioural, and policy-related factors that influence whether a
customer purchases a health insurance policy.

Using **SQL, Python, and Power BI**, I performed data cleaning,
exploratory data analysis (EDA), statistical analysis, and dashboard
development to uncover meaningful business insights. The objective was
to answer questions such as:

-   Which customers are most likely to purchase a policy?
-   Which policy categories perform best?
-   How do demographic and regional factors influence conversion?
-   What recommendations can improve marketing effectiveness?

### Tools & Technologies

-   **SQL** -- Data exploration and business queries
-   **Python** -- Data cleaning, EDA, visualization, and predictive
    modelling
-   **Power BI** -- Interactive dashboard development
-   **Excel** -- Initial data inspection

**Python Libraries**

-   Pandas
-   NumPy
-   Matplotlib
-   Seaborn
-   Scikit-learn

------------------------------------------------------------------------

# Executive Summary

The analysis of **50,882 customer records** revealed an overall lead
conversion rate of **24%**, with **12,209 interested customers** and
**38,673 non-interested customers**.

Key findings include:

-   Customers aged **36--45** have the highest conversion rate.
-   **Recommended Policy Category** is the strongest predictor of
    customer conversion.
-   Premium amount alone has little influence on customer decisions.
-   Customer response varies across different cities and regions.
-   Accommodation type has only a minimal impact on conversion.

![Lead Conversion Funnel](visualizations/lead_conversion_rate.png)

------------------------------------------------------------------------

# Key Insights

## Lead Conversion

Approximately **1 in every 4 customers** purchased a health insurance
policy.

  Metric                 Value
  ---------------------- ----------------
  Total Records          50,882
  Interested Customers   12,209 (24.0%)
  Not Interested         38,673 (76.0%)

------------------------------------------------------------------------

## Customer Demographics

Customers between **36 and 45 years** recorded the highest conversion
rate, while the **18--25** age group had the lowest.

![Age Distribution](visualizations/age_distribution.png)

------------------------------------------------------------------------

## Accommodation & Premium Analysis

Accommodation type showed very little impact on conversion.

-   Owned: **24.1%**
-   Rented: **23.8%**

Similarly, premium recommendations for interested and non-interested
customers were nearly identical, suggesting that premium amount alone is
not the primary driver of conversion.

![Conversion by
Accommodation](visualizations/conversion_by_accommodation.png)

![Premium Distribution](visualizations/premium_vs_conversion.png)

------------------------------------------------------------------------

## Customer Profile Segmentation

Insurance type and spouse status showed noticeable differences in
customer behaviour, indicating that household profile may influence
purchasing decisions.

![Conversion by Profile](visualizations/conversion_by_profile.png)

------------------------------------------------------------------------

## Regional Analysis

Conversion rates varied across cities. Some cities consistently
outperformed others, suggesting that location-specific marketing
strategies may improve overall conversion.

![Top Cities](visualizations/top_cities.png)

------------------------------------------------------------------------

## Feature Correlations

Correlation analysis showed:

-   Upper_Age and Lower_Age are highly correlated.
-   Premium increases with customer age.
-   Individual features have weak linear relationships with conversion,
    suggesting that customer behaviour is influenced by multiple
    interacting factors.

![Correlation Heatmap](visualizations/correlation_heatmap.png)

------------------------------------------------------------------------

## Policy Category Performance

Recommended Policy Category emerged as one of the strongest business
variables associated with customer conversion.

![Policy Category
Performance](visualizations/policy_category_performance.png)

------------------------------------------------------------------------

# Predictive Modeling

As an additional learning exercise, I built a **Random Forest
Classifier** to explore whether customer conversion could be predicted.

Since my primary focus is **Data Analytics** rather than Machine
Learning, I used an AI coding assistant to help implement parts of the
model while ensuring I understood the preprocessing steps, evaluation
metrics, and interpretation of the results.

## Model Performance

  Metric      Not Interested   Interested
  ----------- ---------------- ------------
  Precision   0.81             0.30
  Recall      0.58             0.56
  F1 Score    0.68             0.39
  ROC-AUC     **0.6222**       

![Confusion Matrix](visualizations/confusion_matrix.png)

## Feature Importance

The Random Forest model identified the following as the strongest
predictors:

1.  Reco_Policy_Cat
2.  Region_Code
3.  Reco_Policy_Premium
4.  City_Code
5.  Upper_Age

![Feature Importance](visualizations/feature_importance.png)

------------------------------------------------------------------------

# Business Recommendations

-   Improve policy recommendations based on customer profiles.
-   Focus marketing campaigns on customer segments with higher
    conversion rates.
-   Study high-performing cities and replicate successful strategies in
    lower-performing regions.
-   Continue exploring interaction features and additional models to
    improve predictive performance.

------------------------------------------------------------------------

# Limitations

-   Missing values were imputed before analysis.
-   The dataset contains class imbalance (76:24).
-   The dataset does not include timestamps, preventing time-series or
    cohort analysis.
-   The machine learning model was created as an exploratory exercise
    rather than a production model.

------------------------------------------------------------------------

# Repository Structure

``` text
├── data/
├── notebooks/
├── sql/
├── dashboard/
├── visualizations/
└── README.md
```

### Project Files

-   **SQL:** Exploratory business queries.
-   **EDA Notebook:** Data cleaning, exploration, and visualizations.
-   **Modeling Notebook:** Random Forest implementation and evaluation.
-   **Power BI Dashboard:** Interactive business dashboard.
