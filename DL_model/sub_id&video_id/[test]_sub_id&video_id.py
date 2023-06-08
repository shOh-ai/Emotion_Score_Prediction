#!/usr/bin/env python
# coding: utf-8

# # 1. subjects ID Embedding 

# In[ ]:


# 데이터 불러오기

import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/sub_id3_test.csv')


# In[ ]:


# 사람_ID를 범주형 변수로 변환

label_encoder = LabelEncoder()
df['ID_encoded'] = label_encoder.fit_transform(df['sub_id'])


# In[ ]:


# embedding layer 생성

import tensorflow as tf
from tensorflow.keras.layers import Embedding
print(tf.__version__)

n_unique_ids = df['ID_encoded'].nunique()
embedding_dim = min(n_unique_ids // 2, 50)  # 임베딩 차원 설정. 보통은 고유 ID의 수의 절반 혹은 50을 선택

embedding_layer = Embedding(input_dim=n_unique_ids, 
                            output_dim=embedding_dim, 
                            input_length=1, 
                            name='ID_embedding')


# In[ ]:


# 임베딩 레이어를 통과하여 벡터 생성 후, Flatten 적용

from tensorflow.keras.layers import Flatten

# 데이터를 모델에 넣을 수 있는 형태로 변환
input_data = df['ID_encoded'].values.reshape(-1, 1)

# 임베딩 레이어를 통과
embedded_data = embedding_layer(input_data)


# In[ ]:


print(embedded_data.shape)
print(embedded_data.dtype)


# # 2. video_type_OneHotEncoding

# In[ ]:


# 데이터 불러오기
import pandas as pd

df = pd.read_csv('/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/video_id_test.csv')


# In[ ]:


# OneHotEncoding
from sklearn.preprocessing import OneHotEncoder

# Initialize OneHotEncoder
one_hot_encoder = OneHotEncoder(sparse_output=False)

# Perform one-hot encoding
one_hot_encoded = one_hot_encoder.fit_transform(df['video_id'].values.reshape(-1, 1))

# Convert the result back to a dataframe
df_encoded = pd.DataFrame(one_hot_encoded, columns=one_hot_encoder.categories_[0])


# In[ ]:


print(df_encoded.shape)


# In[ ]:


# Convert df_encoded to a suitable input for Keras
video_id_input = df_encoded.values

