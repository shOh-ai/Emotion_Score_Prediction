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


# ## 2. path setting

# In[2]:


eeg_folder_path = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/EEG'
sub_id_path = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/sub_id2.csv'


# ## 3. load EEG data from '.mat' + Wavelet trans
# ## + Zero Padding + MinMaxScaler

# In[ ]:


def load_eeg_data(eeg_folder_path, sub_id_path):
    # Load sub_id
    sub_id_df = pd.read_csv(sub_id_path)
    sub_id_list = sub_id_df['sub_id'].apply(lambda x: f"{x:03d}").tolist()

    eeg_data = []
    max_length = 0
    for sub_id in sub_id_list:
        mat_file_path = os.path.join(eeg_folder_path, f"{sub_id}.mat")
        if os.path.exists(mat_file_path):
            mat = loadmat(mat_file_path)
        else:
            print(f"Error: File not found for sub_id {sub_id}")
            continue  # skip this iteration if file not found
        
        for segment in ['Segment_3', 'Segment_6', 'Segment_9', 'Segment_12', 'Segment_15', 'Segment_18']:
            eeg_segment = mat[segment]  # get segment data
            for channel_data in eeg_segment:  # iterate over each channel
                widths = np.arange(1, 31)  # range of scales for the wavelet transform
                cwtmatr = cwt(channel_data, ricker, widths)  # compute wavelet transform
                if cwtmatr.shape[1] > max_length:
                    max_length = cwtmatr.shape[1]
                eeg_data.append(cwtmatr)
                
        print(f"Processed data for sub_id {sub_id}")  # Print when data processing for a sub_id is completed
              
    # Zero padding
    for i in range(len(eeg_data)):
        if eeg_data[i].shape[1] < max_length:
            zero_pad = np.zeros((eeg_data[i].shape[0], max_length - eeg_data[i].shape[1]))
            eeg_data[i] = np.hstack((eeg_data[i], zero_pad))

    # Flatten all the data into a single array for scaling
    all_data = np.concatenate(eeg_data, axis=0)
            
    # Min-Max Scaling
    scaler = MinMaxScaler()
    all_data = scaler.fit_transform(all_data)

    # Split the data back into its original form
    eeg_data_scaled = np.split(all_data, len(eeg_data))

    return eeg_data_scaled


# Call the function and check the returned data
eeg_data = load_eeg_data(eeg_folder_path, sub_id_path)
print(f"Total number of data points: {len(eeg_data)}")  # Print the total number of data points
print(f"Shape of the first data point: {eeg_data[0].shape}")  # Print the shape of the first data point

