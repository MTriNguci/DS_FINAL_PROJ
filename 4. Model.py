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

from scipy.stats import pointbiserialr

def correlation_ratio(df, dummies, target):
    """Truyền vào cộ categoreis và hệ đo lường, trả về các giá trị danh sách hệ số tương quan"""
    correlations = {}
    p_values = {}
    for dummy in dummies.columns:
        corr, pval = pointbiserialr(df[target], dummies[dummy])
        correlations[dummy] = corr
        p_values[dummy] = pval

    # Kiểm định ý nghĩa thống kê
    significant_dummies = [dummy for dummy in dummies.columns if p_values[dummy] < 0.05]

    # Lựa chọn các dummy quan trọng
    important_dummies = sorted([(dummy, correlations[dummy]) for dummy in significant_dummies], key=lambda x: abs(x[1]), reverse=True)

    # Lấy ra các dummy có tương quan > 0.25 và chỉ lấy tối đa 10 biến
    important_dummies = [dummy for dummy, corr in important_dummies if abs(corr) > 0.25][:10]
    print(important_dummies)
    return important_dummies


def one_hot(df, col, target):
    df = df.copy()
    dummies = pd.get_dummies(df[col], prefix=col)
    if len(dummies.columns) > 10:
        top_cols = correlation_ratio(df, dummies, target)
        dummies = dummies[top_cols]
    df = pd.concat([df, dummies], axis=1)
    df = df.drop(col, axis=1)
    return df

# Columns to encode
cols = ['Make', 'Body color', 'Interior color', 'Interior material', 'Body', 'Doors', 'Fuel', 'Transmission', 'Drive type', 'Emission class', 'Condition']
for col in cols:
    df = one_hot(df, col, 'Price(EUR)')

# One-hot encoding for multi-selection column
def one_hot_multi(df, col, target):
    df = df.copy()
    dummies = df[col].str.get_dummies(sep='; ')
    # If column has more than 10 values then only take the values with the highest correlation
    if len(dummies.columns) > 10:
        top_cols = correlation_ratio(df, dummies, target)
        dummies = dummies[top_cols]
    df = pd.concat([df, dummies], axis=1)
    df = df.drop(col, axis=1)
    return df

df = one_hot_multi(df, 'Tags', 'Price(EUR)')

# Convert 'First registration' to the number of years until now
df['First registration'] = df['First registration'].str[-4:].astype(int)
df['First registration'] = 2023 - df['First registration']

# Split data into training and test sets
X = df.drop('Price(EUR)', axis=1)
y = df['Price(EUR)']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Random Forest model
model = RandomForestRegressor(n_estimators=200, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predict car prices on the test set
predictions = model.predict(X_test)

# Calculate Mean Absolute Error
mae = mean_absolute_error(y_test, predictions)

print(f"Mean Absolute Error: {mae}")
                              