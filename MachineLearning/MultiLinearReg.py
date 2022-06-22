# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd


def read_input():
    
    train_info = input().split()
    num_features = train_info[0]
    num_rows = train_info[1]
    
    df_train = []
    # print(train_info)

    for i in range(int(num_rows)):
        row = {}
        data_line = input().split()

        for j in range(int(num_features)+1):
            row[j] = data_line[j]
        df_train.append(row)
        
    df_train = pd.DataFrame.from_dict(df_train)
    X_train = df_train.drop(columns=[int(num_features)])
    y_train = df_train[[int(num_features)]]
    
    df_test = []
    test_info = input().split()
    num_samples = test_info[0]

    for i in range(int(num_samples)):
        row = {}
        data_line = input().split()

        for j in range(int(num_features)):
            row[j] = data_line[j]
        df_test.append(row)
    X_test = pd.DataFrame.from_dict(df_test)
    return X_train, y_train, X_test

def fit_model(X_train, y_train):
        
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return model
    

if __name__ == "__main__":
    
    X_train, y_train, X_test = read_input()
    model = fit_model(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    for pred in y_pred:
        print(pred[0])
    # print(y_pred)
