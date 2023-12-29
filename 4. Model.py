import pandas as pd
import numpy as np
from scipy.stats import pointbiserialr
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load data
data = pd.read_csv('data\cleaned_data_edited.csv')
df = data.copy()
del df['CARNAME'], df['Model']

# Convert 'First registration' to the number of years until now
df['First registration'] = df['First registration'].str[-4:].astype(int)
df['First registration'] = 2023 - df['First registration']

def correlation_ratio(df, dummies, target):
    correlations = {dummy: pointbiserialr(df[target], dummies[dummy]) for dummy in dummies.columns}
    sorted_correlations = sorted([(dummy, corr) for dummy, (corr, pval) in correlations.items() if pval < 0.05], key=lambda x: abs(x[1]), reverse=True)
    print(sorted_correlations)
    return sorted_correlations

def one_hot(df, col, target, multi=False):
    dummies = df[col].str.get_dummies(sep='; ') if multi else pd.get_dummies(df[col], prefix=col)
    if len(dummies.columns) > 10:
        top_cols = [dummy for dummy, corr in correlation_ratio(df, dummies, target) if abs(corr) > 0.25][:10]
        dummies = dummies[top_cols]
    return pd.concat([df, dummies], axis=1).drop(col, axis=1)

cols = ['Make', 'Body color', 'Interior color', 'Interior material', 'Body', 'Doors', 'Fuel', 'Transmission', 'Drive type', 'Emission class', 'Condition']
for col in cols:
    df = one_hot(df, col, 'Price(EUR)')

df = one_hot(df, 'Tags', 'Price(EUR)', multi=True)

# Split data into training and test sets
X = df.drop('Price(EUR)', axis=1)
y = df['Price(EUR)']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Random Forest model
n = 850
model = RandomForestRegressor(n_estimators=n, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predict car prices on the test set
predictions = model.predict(X_test)

# Calculate Mean Absolute Error
mae = mean_absolute_error(y_test, predictions)

print(f"n_estimators: {n}")
print(f"Mean Absolute Error: {mae}")
                              