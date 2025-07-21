import matplotlib.pyplot as plt
import base64
from io import BytesIO

def plot_predictions(df, future_dates, predictions):
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Value'], label='Historical')
    plt.plot(future_dates, predictions, label='Prediction', linestyle='--')
    plt.legend()
    plt.title('Historical and Predicted Values')
    plt.xlabel('Date')
    plt.ylabel('Value')
    
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return img_base64