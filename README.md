# Health Insurance Lead Prediction Analysis

## Table of Contents

-   [Project Overview](#project-overview)
-   [Dataset](#dataset)
-   [Tools & Technologies](#tools--technologies)
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
-   [Business Recommendations](#business-recommendations)
-   [Limitations](#limitations)
-   [Repository Structure](#repository-structure)

------------------------------------------------------------------------

## Project Overview

This project analyzes a health insurance lead dataset containing
**50,882 customer records** to understand the factors influencing
customer conversion.

The primary objective of this project was to understand why only **24%
of health insurance leads converted into policy purchases** and identify
the demographic, behavioural, geographic, and policy-related factors
associated with customer decisions.

Using **SQL, Python, and Power BI**, I cleaned the data, performed
exploratory data analysis (EDA), created visualizations, and built an
interactive dashboard to uncover actionable business insights.

------------------------------------------------------------------------

## Dataset

-   **Records:** 50,882
-   **Features:** 14
-   **Target Variable:** Response (Interested / Not Interested)

The dataset contains customer demographics, policy information, premium
details, and previous insurance history.

------------------------------------------------------------------------

## Tools & Technologies

  Tool          Purpose
  ------------- -------------------------------------------------
  SQL (MySQL)   Data exploration and business queries
  Python        Data cleaning, EDA, visualization, and modeling
  Excel         Initial data inspection

**Python Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn

------------------------------------------------------------------------

## Executive Summary

Out of **50,882 customer records**, only **24% of leads converted** into
policy purchases.

Key findings include:

-   **Recommended Policy Category** was the strongest predictor of
    customer conversion within this dataset.
-   Customers aged **36--45** recorded the highest conversion rate
    (25.1%).
-   **City C32** achieved the highest conversion rate at **28.7%**.
-   Premium amount alone did not explain conversion differences.

![Lead Conversion Funnel](visualizations/lead_conversion_rate.png)

------------------------------------------------------------------------

## Key Insights

### Lead Conversion

  Metric                 Value
  ---------------------- ----------------
  Total Records          50,882
  Interested Customers   12,209 (24.0%)
  Not Interested         38,673 (76.0%)

------------------------------------------------------------------------

### Customer Demographics

  Age Group   Conversion Rate
  ----------- -----------------
  18--25      22.7%
  26--35      24.6%
  36--45      25.1%
  46+         \~23.8--23.9%

One possible explanation is that customers aged **36--45** are more
likely to have family responsibilities and greater financial stability,
making health insurance a higher priority.

![Age Distribution](visualizations/age_distribution.png)

------------------------------------------------------------------------

### Accommodation & Premium Analysis

I initially expected homeowners to convert at meaningfully higher rates.
The data showed only a small difference:

-   Owned: **24.1%**
-   Rented: **23.8%**

Premium distributions for interested and non-interested customers were
also very similar, suggesting that **policy fit is likely more important
than premium amount alone.**

![Conversion by
Accommodation](visualizations/conversion_by_accommodation.png)

![Premium Distribution](visualizations/premium_vs_conversion.png)

------------------------------------------------------------------------

### Customer Profile Segmentation

Insurance type and spouse status showed noticeable variation in
conversion patterns, suggesting that household profile may influence
purchasing behaviour.

![Conversion by Profile](visualizations/conversion_by_profile.png)

------------------------------------------------------------------------

### Regional Analysis

Cities showed meaningful differences in conversion rates.

-   **C32:** 28.7% (highest)
-   **C1 & C2:** Highest customer volumes with \~24.5% conversion
-   Several cities converted below 20%, indicating opportunities for
    targeted regional strategies.

![Top Cities](visualizations/top_cities.png)

------------------------------------------------------------------------

### Feature Correlations

-   Upper_Age and Lower_Age are highly correlated (0.92).
-   Premium increases with age.
-   No single variable shows a strong linear relationship with
    conversion, suggesting customer behaviour is influenced by multiple
    interacting factors.

![Correlation Heatmap](visualizations/correlation_heatmap.png)

------------------------------------------------------------------------

### Policy Category Performance

Recommended Policy Category (`Reco_Policy_Cat`) displayed the greatest
variation in customer conversion and emerged as the strongest predictor
within this dataset.

![Policy Category
Performance](visualizations/policy_category_performance.png)

------------------------------------------------------------------------

## Predictive Modeling

As an additional learning exercise, I built a **Random Forest
Classifier** to explore whether customer conversion could be predicted.

Since my primary focus is Data Analytics rather than Machine Learning, I
used an AI coding assistant to help implement parts of the Scikit-learn
workflow while ensuring I understood the preprocessing steps, evaluation
metrics, and interpretation of the results.

### Model Performance

  Metric      Not Interested (0)   Interested (1)
  ----------- -------------------- ----------------
  Precision   0.81                 0.30
  Recall      0.58                 0.56
  F1 Score    0.68                 0.39
  ROC-AUC     **0.6222**           ---

The model correctly identified **56%** of interested customers.
Performance was affected by the class imbalance (76% non-converters
vs. 24% converters).

![Confusion Matrix](visualizations/confusion_matrix.png)

### Feature Importance

  Rank   Feature               Importance
  ------ --------------------- ------------
  1      Reco_Policy_Cat       32.4%
  2      Region_Code           13.9%
  3      Reco_Policy_Premium   13.6%
  4      City_Code             8.7%
  5      Upper_Age             7.6%

![Feature Importance](visualizations/feature_importance.png)

------------------------------------------------------------------------

## Business Recommendations

1.  Improve the policy recommendation process to better match customers
    with appropriate products.

2.  Prioritize customers aged **26--45**, as they consistently showed
    stronger conversion rates.

3.  Investigate why **City C32** performs exceptionally well and
    evaluate whether those strategies can be replicated elsewhere.

4.  Focus on improving policy fit rather than relying primarily on
    premium discounts.

------------------------------------------------------------------------

## Limitations

-   Missing values were imputed before analysis.
-   The dataset has a 76:24 class imbalance.
-   Temporal analysis and cohort analysis were not possible because
    timestamps were unavailable.
-   The machine learning model was developed for exploratory analysis
    rather than production deployment.

------------------------------------------------------------------------

## Repository Structure

``` text
├── data/
├── notebooks/
│   ├── 01_data_cleaning_and_eda.ipynb
│   └── 02_predictive_modeling.ipynb
├── sql/
├── dashboard/
├── visualizations/
└── README.md
```
