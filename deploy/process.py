import joblib
import pandas as pd


#Đọc model đã train
model = joblib.load('model.pkl')
def handle_input(data):
    #tạo dataframe từ dữ liệu người dùng nhập vào
    df = pd.DataFrame(data, index=[0])
    print(df.columns)
    
    numeric = ['Seats', 'Power(kW)', 'CO2 emissions(g/km)', 'Mileage(km)', 'Consumption(l/100km or kWh/100km)', 'Engine capacity(ccm)', 'Previous owners']
    for col in numeric:
        df[col] = pd.to_numeric(df[col])

    #Gọi model để dự đoán
    y_pred = model.predict(df)
    return round(y_pred[0], 3)
    



