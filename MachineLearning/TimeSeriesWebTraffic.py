from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



def test_stationarity(df):
    result = adfuller(df)
    labels = ['ADF Test Statistic','p-value','#Lags Used','Number of Observations Used']
    for value,label in zip(result,labels):
        print(label+' : '+str(value) )
    if result[1] <= 0.05:
        print("P value is less than 0.05 that means we can reject the null hypothesis(Ho). Therefore we can conclude that data has no unit root and is stationary")
    else:
        print("Weak evidence against null hypothesis that means time series has a unit root which indicates that it is non-stationary ")

def make_stationary(df):
    df['WebTrafficShift1'] = df['WebTraffic'] - df['WebTraffic'].shift(1)
    return df.dropna()
    

def fit_model(data):

    # model = ARIMA(endog=data, order=(5,1,0))
    model = sm.tsa.statespace.SARIMAX(data,
                                order=(1, 0, 1),
                                # seasonal_order=(1, 1, 1, 12),
                                trend='c',
                                enforce_stationarity=False,
                                enforce_invertibility=False)
    model = model.fit()

    return model

def predict(data, model):
    predictions = []
    for i in range(30):
        pred = int(model.predict(data.shape[0]+i)[0])
        print(pred)
        predictions.append(pred)

    return np.array(predictions)




if __name__ == '__main__':
    N = int(input())
    data = []
    for i in range(N):
        data.append(int(input()))
    data = np.array(data)

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(data)
    model = fit_model(data)
    predictions = predict(data, model)
    plt.subplot(2, 1, 2)
    plt.plot(predictions)
    plt.show()
    
    
        
