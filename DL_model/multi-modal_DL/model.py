#!/usr/bin/env python
# coding: utf-8

# # Multi-modal layer & prediction layer

# ### 여러 부분 수정 필요

# In[2]:


# Concatenate (feature fusion)

combined_features = np.concatenate([feature1, feature2, feature3, feature4], axis=1)  # or axis=-1 depending on your feature shape


# In[ ]:


# Concatenate (feature fusion)

combined_features = np.concatenate([feature1, feature2, feature3, feature4], axis=1)  # or axis=-1 depending on your feature shape

# 1D-CNN layer

import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv1D, MaxPooling1D, Flatten, Dense
from sklearn.model_selection import train_test_split

# CSV 파일에서 정답 라벨 데이터를 불러오기

file_path = "/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/train_label_softmax.csv"
label_data = pd.read_csv(file_path)

label_data = label_data.iloc[1:235, :] # Select the required rows (from 2nd row to 235th row)
labels = label_data.values  # numpy array로 변환

# 가정: 'combined_features'는 이미 4가지 모델로부터 추출된 특징을 결합한 배열이다.
# combined_features = ...

# train_X mapping to train_y
X_train = combined_features
y_train = labels

n_time_steps = X_train.shape[1] # 수정 필요
n_channels = X_train.shape[2] # 수정 필요

# 1D-CNN 모델 구축
input_layer = Input(shape=(n_time_steps, n_channels)) # 수정 필요
x = Conv1D(16, 3, activation='relu', padding='same')(input_layer)
x = MaxPooling1D(2, padding='same')(x)
x = Conv1D(8, 3, activation='relu', padding='same')(x)
x = MaxPooling1D(2, padding='same')(x)
x = Flatten()(x)

# 6가지 감정 점수를 예측
output_layer = Dense(6, activation='softmax')(x)  

model = Model(inputs=input_layer, outputs=output_layer)


# In[ ]:


# 모델 성능 측정 지표(metric)
from tensorflow.keras.callbacks import Callback
from sklearn.metrics import mean_squared_error
import numpy as np

class RMSECallback(Callback):
    def __init__(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def on_epoch_end(self, epoch, logs=None):
        predictions = self.model.predict(self.X_train)
        rmse_per_instance = np.sqrt(mean_squared_error(self.y_train, predictions, multioutput='raw_values'))
        total_rmse = np.sqrt(np.mean(np.square(rmse_per_instance)))
        print(f'Epoch {epoch+1}: Total RMSE = {total_rmse}')


# In[ ]:


# 모델 컴파일
model.compile(optimizer='adam', loss='categorical_crossentropy')

# RMSE 콜백 정의
rmse_callback = RMSECallback(X_train, y_train)

# 모델 학습
model.fit(X_train, y_train, epochs=10, batch_size=16, shuffle=True, verbose=2, callbacks=[rmse_callback])

