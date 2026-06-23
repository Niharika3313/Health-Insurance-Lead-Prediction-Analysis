import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

# Ensure the visualizations directory exists
os.makedirs('visualizations', exist_ok=True)

# Set the visualization style
sns.set_style('whitegrid')

print("Loading data...")
try:
    # Load the raw dataset
    df = pd.read_excel('data/raw/Health Insurance Lead Prediction.xlsx', sheet_name='Sheet1')
    print("Data loaded successfully.")
except Exception as e:
    print(f"Error loading data: {e}")
    print("Please make sure 'data/raw/Health Insurance Lead Prediction.xlsx' exists.")
    exit()

# Clean data (mirroring the notebook steps)
if 'Response' in df.columns:
    df = df.dropna(subset=['Response'])
    df = df[df['Response'].isin([0, 1])]

# ---------------------------------------------------------
# 1. Lead Conversion Rate
# ---------------------------------------------------------
print("Generating Lead Conversion Rate plot...")
plt.figure(figsize=(6, 4))
ax = sns.countplot(x='Response', hue='Response', data=df, palette='viridis', legend=False)
plt.title('Distribution of Lead Conversion (Response)')
plt.xlabel('Response (0 = No, 1 = Yes)')
plt.ylabel('Count')
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom')
plt.tight_layout()
plt.savefig('visualizations/lead_conversion_rate.png', dpi=300)
plt.close()

# ---------------------------------------------------------
# 2. Conversion by Accommodation Type
# ---------------------------------------------------------
print("Generating Conversion by Accommodation plot...")
plt.figure(figsize=(8, 5))
sns.countplot(x='Accomodation_Type', hue='Response', data=df, palette='Set2')
plt.title('Lead Conversion by Accommodation Type')
plt.xlabel('Accommodation Type')
plt.ylabel('Count')
plt.legend(title='Response')
plt.tight_layout()
plt.savefig('visualizations/conversion_by_accommodation.png', dpi=300)
plt.close()

# ---------------------------------------------------------
# 3. Age Distribution of Leads vs Non-Leads
# ---------------------------------------------------------
print("Generating Age Distribution plot...")
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Upper_Age', hue='Response', bins=30, kde=True, palette='coolwarm')
plt.title('Age Distribution by Lead Conversion')
plt.xlabel('Upper Age')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('visualizations/age_distribution.png', dpi=300)
plt.close()

# ---------------------------------------------------------
# 4. Premium vs Conversion
# ---------------------------------------------------------
print("Generating Premium vs Conversion plot...")
plt.figure(figsize=(10, 6))
sns.boxplot(x='Response', y='Reco_Policy_Premium', hue='Response', data=df, palette='pastel', legend=False)
plt.title('Recommended Policy Premium vs. Lead Conversion')
plt.xlabel('Response')
plt.ylabel('Recommended Premium')
plt.tight_layout()
plt.savefig('visualizations/premium_vs_conversion.png', dpi=300)
plt.close()

# ---------------------------------------------------------
# 5. Conversion by Profile (Insurance Type / Spouse)
# ---------------------------------------------------------
if 'Reco_Insurance_Type' in df.columns and 'Is_Spouse' in df.columns:
    print("Generating Conversion by Profile plot...")
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    sns.countplot(x='Reco_Insurance_Type', hue='Response', data=df, palette='Set1')
    plt.title('Conversion by Insurance Type')
    
    plt.subplot(1, 2, 2)
    sns.countplot(x='Is_Spouse', hue='Response', data=df, palette='Set1')
    plt.title('Conversion by Spouse Status')
    
    plt.tight_layout()
    plt.savefig('visualizations/conversion_by_profile.png', dpi=300)
    plt.close()

# ---------------------------------------------------------
# 6. Regional Performance (Top Cities)
# ---------------------------------------------------------
if 'City_Code' in df.columns:
    print("Generating Top Cities Performance plot...")
    # Get top 10 cities by volume
    top_cities = df['City_Code'].value_counts().head(10).index
    city_df = df[df['City_Code'].isin(top_cities)]
    
    # Calculate conversion rate per city
    city_conversion = city_df.groupby('City_Code')['Response'].mean().sort_values(ascending=False).reset_index()
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='City_Code', y='Response', hue='City_Code', data=city_conversion, palette='mako', legend=False)
    plt.title('Lead Conversion Rate by Top Cities')
    plt.xlabel('City Code')
    plt.ylabel('Conversion Rate')
    plt.axhline(y=df['Response'].mean(), color='r', linestyle='--', label='Overall Avg')
    plt.legend()
    plt.tight_layout()
    plt.savefig('visualizations/top_cities.png', dpi=300)
    plt.close()

# ---------------------------------------------------------
# 7. Correlation Heatmap
# ---------------------------------------------------------
print("Generating Correlation Heatmap...")
# Select only numeric columns for correlation
numeric_df = df.select_dtypes(include=[np.number])
plt.figure(figsize=(12, 8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Feature Correlation Heatmap')
plt.tight_layout()
plt.savefig('visualizations/correlation_heatmap.png', dpi=300)
plt.close()

# ---------------------------------------------------------
# 8. Policy Category Performance
# ---------------------------------------------------------
if 'Reco_Policy_Cat' in df.columns:
    print("Generating Policy Category Performance plot...")
    plt.figure(figsize=(12, 6))
    cat_conversion = df.groupby('Reco_Policy_Cat')['Response'].mean().reset_index()
    sns.barplot(x='Reco_Policy_Cat', y='Response', hue='Reco_Policy_Cat', data=cat_conversion, palette='rocket', legend=False)
    plt.title('Lead Conversion Rate by Policy Category')
    plt.xlabel('Policy Category')
    plt.ylabel('Conversion Rate')
    plt.axhline(y=df['Response'].mean(), color='b', linestyle='--', label='Overall Avg')
    plt.legend()
    plt.tight_layout()
    plt.savefig('visualizations/policy_category_performance.png', dpi=300)
    plt.close()

# ---------------------------------------------------------
# Predictive Modeling Visualizations (Confusion Matrix & Feature Importance)
# ---------------------------------------------------------
print("Running a quick model to generate ML visualizations...")
# Quick preprocessing
df_ml = df.copy()
if 'ID' in df_ml.columns: df_ml = df_ml.drop('ID', axis=1)
if 'Id' in df_ml.columns: df_ml = df_ml.drop('Id', axis=1)

categorical_cols = df_ml.select_dtypes(include=['object']).columns
le = LabelEncoder()
for col in categorical_cols:
    df_ml[col] = df_ml[col].astype(str)
    df_ml[col] = le.fit_transform(df_ml[col])

# Fill any remaining NaNs to prevent model errors
df_ml = df_ml.fillna(0)

X = df_ml.drop('Response', axis=1)
y = df_ml['Response']

if len(X) > 0 and len(y) > 0:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    rf_model = RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42, class_weight='balanced')
    rf_model.fit(X_train, y_train)
    y_pred = rf_model.predict(X_test)
    
    # ---------------------------------------------------------
    # 9. Confusion Matrix
    # ---------------------------------------------------------
    print("Generating Confusion Matrix plot...")
    plt.figure(figsize=(6, 5))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.tight_layout()
    plt.savefig('visualizations/confusion_matrix.png', dpi=300)
    plt.close()
    
    # ---------------------------------------------------------
    # 10. Feature Importance
    # ---------------------------------------------------------
    print("Generating Feature Importance plot...")
    importances = rf_model.feature_importances_
    feature_importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': importances})
    feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
    
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Importance', y='Feature', hue='Feature', data=feature_importance_df.head(15), palette='viridis', legend=False)
    plt.title('Top 15 Most Important Features for Lead Prediction')
    plt.xlabel('Relative Importance')
    plt.ylabel('Feature')
    plt.tight_layout()
    plt.savefig('visualizations/feature_importance.png', dpi=300)
    plt.close()

print("All visualizations generated successfully in the 'visualizations/' directory.")
