#!/usr/bin/env python
# coding: utf-8

# ## 1. packages & libraries

# In[1]:

from scipy.io import loadmat
from scipy.signal import cwt, ricker
import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler
from concurrent.futures import ThreadPoolExecutor
from math import ceil
import gc


# ## 2. path setting

# In[2]:

eeg_folder_path = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/EEG'
sub_id_path = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/sub_id2.csv'



# ## 3. load EEG data from '.mat' + Wavelet trans
# ## + Zero Padding + MinMaxScaler

# In[ ]:


from sklearn.preprocessing import MinMaxScaler

def load_and_scale_eeg_data(eeg_folder_path, sub_id_path, batch_size=6):
    # Load sub_id
    sub_id_df = pd.read_csv(sub_id_path)
    sub_id_list = sub_id_df['sub_id'].apply(lambda x: f"{x:03d}").tolist()

    max_length = 0
    eeg_data = []
    for sub_id in sub_id_list:
        mat_file_path = os.path.join(eeg_folder_path, f"{sub_id}.mat")
        if os.path.exists(mat_file_path):
            mat = loadmat(mat_file_path)
        else:
            print(f"Error: File not found for sub_id {sub_id}")
            continue

        for segment in ['Segment_3', 'Segment_6', 'Segment_9', 'Segment_12', 'Segment_15', 'Segment_18']:
            eeg_segment = mat[segment]
            max_length = max(max_length, eeg_segment.shape[1])  # update max_length
            eeg_data.append(eeg_segment)

        print(f"Processed data for sub_id {sub_id}")

    # Zero padding
    for i in range(len(eeg_data)):
        if eeg_data[i].shape[1] < max_length:
            zero_pad = np.zeros((eeg_data[i].shape[0], max_length - eeg_data[i].shape[1]))
            eeg_data[i] = np.hstack((eeg_data[i], zero_pad))

    # Convert list of arrays into 3D array
    eeg_data = np.stack(eeg_data)

    # Min-Max Scaling
    scaler = MinMaxScaler()
    eeg_data = eeg_data.reshape(-1, eeg_data.shape[-1])  # collapse the first two dimensions
    eeg_data = scaler.fit_transform(eeg_data)  # scale the data
    eeg_data = eeg_data.reshape(-1, max_length, 10)  # reshape back into original shape

    # Split the data into batches
    num_batches = eeg_data.shape[0] // batch_size
    eeg_data = eeg_data[:num_batches*batch_size]  # ignore last few samples if not enough for a batch
    eeg_data = eeg_data.reshape(num_batches, batch_size, max_length, 10)

    return eeg_data

eeg_data = load_and_scale_eeg_data(eeg_folder_path, sub_id_path, batch_size=6)
eeg_data = eeg_data.astype(np.float32)  # change the data type to float32

