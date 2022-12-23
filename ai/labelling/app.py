import streamlit as st
from PIL import Image
import os
import numpy as np
import random
import time
import shutil
import math

data_path = '../crawl_data/data'
newdata_path = '../crawl_data/new_data'
output_path = '../crawl_data/labels.txt'

def randomindex(l):
    return time.time_ns()%l

list_paths = os.listdir(data_path)

def on_change():
    value = st.session_state.my_radio

    if value != -1:
        list_paths = os.listdir(data_path)

        if img_path in list_paths:
            shutil.move(old_path, os.path.join(newdata_path, img_path))
            with open(output_path, 'a') as f:
                f.write(img_path + ' ' + str(value) + '\n')

        else:
            st.text('Ảnh đã được gán nhãn')


if len(list_paths) == 0:
    st.text('Hết ảnh')

else:
    st.session_state.my_radio = -1
    idx = randomindex(len(list_paths))
    img_path = list_paths[idx]
    
    old_path = os.path.join(data_path, img_path)
    img = Image.open(old_path)

    st.text(img_path)
    st.image(img)
    score = st.radio('Mức độ tắc nghẽn (1 là thoáng nhất, 5 là tắc nhất, 9999 là ảnh ko hợp lệ)',
                     (-1, 1, 2, 3, 4, 5, 9999),
                     index=0,
                     horizontal=True,
                     on_change=on_change,
                     key='my_radio')