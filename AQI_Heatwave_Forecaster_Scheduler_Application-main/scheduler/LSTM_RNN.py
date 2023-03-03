from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

class LSTM_Model:
  data=None
  timestep=None
  LSTM_Neurons=None
  scaler=None
  trained_model=None

  def __init__(self,LSTM_Neurons,timestep) -> None:
     self.LSTM_Neurons=LSTM_Neurons
     self.timestep=timestep
  
  def load_data(self,data,name):
    self.data = data
    if name=='AQI':
        self.data=np.array(self.data['AQI'].tolist())
    else:
        self.data=np.array(self.data['Max Temp (°C)'].tolist())

  def get_scaler(self):
    return self.scaler
    
  #Preprocessing and scaling the data
  def preprocess_data(self):
    self.scaler = MinMaxScaler()
    self.scaler = self.scaler.fit(self.data.reshape(-1, 1))
    scaled_data = self.scaler.transform(self.data.reshape(-1, 1))
    return scaled_data

  def create_data_and_labels(self):
    scaled_data=self.preprocess_data()
    X = []
    y = []
    for i in range(self.timestep, len(self.data)):
        X.append(scaled_data[i-self.timestep:i, 0])
        y.append(scaled_data[i, 0])
    X, y = np.array(X), np.array(y)
    return X,y

  def create_training_and_testing_data(self,X,y):
    # Split the data into training and testing sets
    split_idx = int(0.8 * len(X))
    X_train, X_test = X, X[split_idx:]
    y_train, y_test = y, y[split_idx:]
    return X_train,y_train,X_test,y_test
    
  # Define the LSTM model architecture
  def create_LSTM_Model(self):
    model = Sequential()
    model.add(LSTM(self.LSTM_Neurons, input_shape=(self.timestep, 1),activation="tanh"))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

  def fit_data(self,model,X_train,y_train):
    model.fit(X_train, y_train, epochs=100, batch_size=32,verbose=0)
    return model

  def predict(self,model,X_test,y_test):
    y_pred = model.predict(X_test,verbose=0)
    y_pred = self.scaler.inverse_transform(y_pred)
    y_test = self.scaler.inverse_transform(y_test.reshape(1,-1))
    return y_pred,y_test

  def evaluate_rmse(self,model,y_pred,y_test):
    mse = np.mean((y_pred - y_test)**2)
    print("Mean squared error:", mse)
  
  def get_model(self):
    return self.trained_model

  def forecast_future(self,forecast_horizon):
    last_values = self.data[-self.timestep:]
    input_sequence = self.scaler.transform(last_values.reshape(-1, 1)).reshape(1, self.timestep)
    output=[]
    for i in range(forecast_horizon):
        # Predict the next value based on the previous `timesteps` values
        next_value = self.trained_model.predict(input_sequence,verbose=0)[0, 0]
        
        # Add the predicted value to the input sequence and remove the first value
        input_sequence = np.concatenate([input_sequence[:, 1:], [[next_value]]], axis=1)
        
        # Scale the input sequence for the next prediction
        input_sequence_scaled = self.scaler.inverse_transform(input_sequence.reshape(-1, 1)).reshape(1, self.timestep, 1)
        
        # Print the predicted value
        output.append(next_value)
    return self.scaler.inverse_transform(np.array(output).reshape(-1,1))
    
  def execute(self):
    X,y=self.create_data_and_labels()
    X_train,y_train,X_test,y_test=self.create_training_and_testing_data(X,y)
    # model=self.create_LSTM_Model()
    # fitted_model=self.fit_data(model,X_train,y_train)
    # y_pred,y_test=self.predict(fitted_model,X_test,y_test)
    # self.evaluate_rmse(fitted_model,y_pred,y_test)
    model=self.create_LSTM_Model()
    fitted_model=self.fit_data(model,X,y)
    self.trained_model=fitted_model

