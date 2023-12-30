import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeRegressor
from scipy.stats import pointbiserialr
import numpy as np

# Đọc dữ liệu từ file CSV
df = pd.read_csv('data/cleaned_data_edited.csv')

# Chia dữ liệu thành features (X) và target (y)
X = df.drop('Price(EUR)', axis=1)
y = df['Price(EUR)']

# Định nghĩa các bước preprocessing như một transformer tùy chỉnh
class Preprocessor(BaseEstimator, TransformerMixin):
    def fit(self, X, y):
        self.y = y
        return self

    def transform(self, X, y=None):
        # Xóa các cột 'CARNAME' và 'Model'
        X = X.drop(['CARNAME', 'Model'], axis=1)

        # Chuyển đổi 'First registration' thành số năm từ năm đăng ký đến nay
        X['First registration'] = X['First registration'].str[-4:].astype(int)
        X['First registration'] = 2023 - X['First registration']

        # One-hot encoding cho các cột phân loại
        cols = ['Make', 'Body color', 'Interior color', 'Interior material', 'Body', 'Doors', 'Fuel', 'Transmission', 'Drive type', 'Emission class', 'Condition', 'Tags']
        for col in cols:
            X = self.one_hot(X, col, multi=(col=='Tags'))

        return X

    def correlation_ratio(self, df, dummies):
        # Khởi tạo một từ điển trống để lưu các giá trị tương quan
        correlations = {}

        # Duyệt qua từng cột trong DataFrame 'dummies'
        for dummy in dummies.columns:
            # Tính toán hệ số tương quan và p-value
            print(dummy)
            print(dummies[dummy].shape)
            print(self.y.shape)
            corr, pval = pointbiserialr(dummies[dummy], self.y)

            # Lưu hệ số tương quan và p-value vào từ điển
            correlations[dummy] = (corr, pval)

        # Khởi tạo một danh sách trống để lưu các giá trị tương quan đã được sắp xếp
        sorted_correlations = []

        # Duyệt qua từng phần tử trong từ điển 'correlations'
        for dummy, (corr, pval) in correlations.items():
            # Kiểm tra nếu p-value nhỏ hơn 0.05
            if pval < 0.05:
                # Thêm giá trị tương quan vào danh sách 'sorted_correlations'
                sorted_correlations.append((dummy, corr))

        # Sắp xếp danh sách 'sorted_correlations' theo thứ tự giảm dần của giá trị tuyệt đối hệ số tương quan
        sorted_correlations.sort(key=lambda x: abs(x[1]), reverse=True)

        # Trả về kết quả
        return sorted_correlations


    def one_hot(self, df, col, multi=False):
        dummies = df[col].str.get_dummies(sep='; ') if multi else pd.get_dummies(df[col], prefix=col)
        if len(dummies.columns) > 10:
            top_cols = [dummy for dummy, corr in self.correlation_ratio(df, dummies) if abs(corr) > 0.25][:10]
            dummies = dummies[top_cols]
        return pd.concat([df, dummies], axis=1).drop(col, axis=1)


# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Bước 1: Preprocessing
preprocessor = Preprocessor()

# Bước 2: Model
model = DecisionTreeRegressor()

# Xây dựng pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('model', model)])



# Huấn luyện pipeline với dữ liệu huấn luyện
pipeline.fit(X_train, y_train)

# Đánh giá hiệu suất của pipeline trên tập kiểm tra
score = pipeline.score(X_test, y_test)

print(f"Score on test set: {score}")

# Sử dụng cross validation
scores = cross_val_score(pipeline, X, y, cv=5)

# In ra điểm số cho mỗi fold
for i, score in enumerate(scores, start=1):
    print(f"Score for fold {i}: {score}")
