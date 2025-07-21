import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def train_model(df: pd.DataFrame, look_back=30):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df[['Value']])
    
    X, y = [], []
    for i in range(look_back, len(scaled_data)):
        X.append(scaled_data[i-look_back:i, 0])
        y.append(scaled_data[i, 0])
    X, y = np.array(X), np.array(y)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))
    
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)))
    model.add(LSTM(50))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=5, batch_size=16, verbose=0)
    
    return model, scaler

def predict_future(df: pd.DataFrame, model, scaler, look_back=30, n_future=7):
    last_values = scaler.transform(df[['Value']])[-look_back:]
    predictions = []
    future_dates = pd.date_range(df['Date'].iloc[-1] + pd.Timedelta(days=1), periods=n_future)
    current_input = last_values.copy()
    for _ in range(n_future):
        pred = model.predict(current_input.reshape(1, look_back, 1), verbose=0)
        predictions.append(pred[0,0])
        current_input = np.append(current_input[1:], [[pred[0,0]]], axis=0)
    predictions = scaler.inverse_transform(np.array(predictions).reshape(-1, 1)).flatten()
    return future_dates, predictions