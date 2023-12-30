import joblib
import pandas as pd


#Đọc model đã train
model = joblib.load('model.pkl')

def handle_input(data):
    #tạo dataframe từ dữ liệu người dùng nhập vào
    df = pd.DataFrame(data, index=[0])

    #Tạo 4 cột Ferrari, Lamborghini, Rolls-Royce, Others
    df['Ferrari'] = 0
    df['Lamborghini'] = 0
    df['Rolls-Royce'] = 0
    df['Others'] = 0

    # Nếu giá trị cột Make là Ferrari thì gán cột Ferrari = 1, tương tự với các cột còn lại
    make = df['Make'][0]
    if make in ['Ferrari', 'Lamborghini', 'Rolls-Royce', 'Others']:
        df[make] = 1

    df = df.drop(['Make'], axis=1)
    
    numeric = ['Seats', 'Power(kW)', 'CO2 emissions(g/km)', 'Mileage(km)', 'Consumption(l/100km or kWh/100km)', 'Engine capacity(ccm)', 'Previous owners']
    for col in numeric:
        df[col] = pd.to_numeric(df[col])

    #Gọi model để dự đoán
    y_pred = model.predict(df)
    return round(y_pred[0], 3)
    



