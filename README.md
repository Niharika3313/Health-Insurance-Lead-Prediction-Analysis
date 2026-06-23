# Health Insurance Lead Prediction Analysis

Table of Contents
- [Project Background](#project-background)
- [Executive Summary](#executive-summary)
- [Insights Deep-Dive](#insights-deep-dive)
    - [Lead Conversion Rate](#lead-conversion-rate)
    - [Demographic Trends](#demographic-trends)
    - [Accommodation & Premium Impact](#accommodation--premium-impact)
- [Predictive Modeling](#predictive-modeling)
    - [Model Performance](#model-performance)
    - [Key Drivers of Conversion](#key-drivers-of-conversion)
- [Recommendations](#recommendations)
- [Assumptions and Caveats](#assumptions-and-caveats)

***

## Project Background

As a data analyst partnering with the marketing and product teams of a major health insurance provider, this project aims to extract actionable insights from customer lead data. The goal is to identify the demographic and behavioral factors that most strongly predict a customer's likelihood to respond positively to a health insurance offer, ultimately optimizing marketing spend and improving conversion rates.

## Executive Summary

Analysis of over 50,000 customer records reveals a baseline conversion rate of approximately 24%. The data indicates that older demographics, particularly those over the age of 50, are significantly more likely to convert into positive leads. Furthermore, customers living in owned accommodations tend to accept policy offers more frequently than those in rented accommodations. To maximize lead generation, the company should target older homeowners while investigating why conversion drops significantly among younger audiences and those with extremely high policy premiums.

## Insights Deep-Dive

### Lead Conversion Rate
The overall lead conversion rate stands at approximately 24%, showing a healthy baseline but leaving significant room for optimization in marketing outreach.

![Lead Conversion Rate](visualizations/lead_conversion_rate.png)

### Demographic Trends
Age is a crucial factor in policy conversion. Our analysis shows a higher density of positive responses as the customer's age increases, peaking around the 50-60 age bracket. Younger demographics show a noticeably lower response rate.

![Age Distribution](visualizations/age_distribution.png)

### Accommodation & Premium Impact
Customers residing in owned accommodations show a slightly higher propensity to purchase health insurance compared to those renting. Additionally, while the recommended policy premium is relatively consistent across responses, there are fewer conversions at the extreme upper boundaries of the premium scale.

![Conversion by Accommodation](visualizations/conversion_by_accommodation.png)
![Premium vs Conversion](visualizations/premium_vs_conversion.png)

## Predictive Modeling

To move beyond descriptive analytics, a Random Forest Classifier was built to predict the likelihood of a customer responding positively to an insurance offer based on their profile. 

### Model Performance
The machine learning model achieved a strong balance between precision and recall, with a high ROC-AUC score indicating excellent discriminatory power between leads and non-leads. The confusion matrix below illustrates the model's accuracy on the unseen test set.

![Confusion Matrix](visualizations/confusion_matrix.png)

### Key Drivers of Conversion
By analyzing the Feature Importance from the Random Forest model, we determined the most critical variables influencing a customer's decision. `Upper_Age`, `City_Code`, and `Reco_Policy_Premium` are the top three drivers of conversion.

![Feature Importance](visualizations/feature_importance.png)

## Recommendations

- **Targeted Marketing Campaigns**: Reallocate marketing budgets to heavily target the 50+ age demographic, as they show the highest natural conversion rate and are the strongest predictor in our machine learning model.
- **Premium Optimization**: Reassess the pricing strategies for policy premiums at the extreme high end, as conversion drops significantly. Offering tiered or customizable plans could capture the segment that currently rejects offers due to high perceived costs.
- **Geographic Focus**: `City_Code` is the second most important feature in predicting a lead. Marketing teams should launch localized campaigns in the top-performing cities and conduct further market research in underperforming regions to understand the disparity.

## Assumptions and Caveats
- **Missing Data Imputation**: Missing values in the `Health Indicator` and `Holding_Policy_Duration` columns were imputed using mode and constant values (treating missing durations as 0). This assumes that a missing duration implies no previous policy.
- **Data Integrity**: An outlier value of `12200.0` was found in the `Response` target variable and was dropped prior to training to ensure a strict binary classification (0 or 1).
