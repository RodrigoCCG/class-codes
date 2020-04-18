import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


st.title('Aula do dia 16/04')

image = Image.open('peppers.png')

imagem_color_arr = np.array(image)

img_gray = np.mean(imagem_color_arr, axis=2)

st.text(img_gray.shape)

# limiar = st.slider('Limiar?', 0, 255, 25)

# st.text(limiar)

img_gray = np.mean(imagem_color_arr, axis=2)

num_color = st.selectbox("Quantas cores?", \
    (2, 4, 8, 16, 32, 64, 128))

# st.text(num_color)
# img_gray[img_gray != limiar] = 255

interval= round(255/num_color,0)

for i in range(num_color-1):
    img_gray[(img_gray >= (interval*i)) & (img_gray < (interval*(i+1)))] = interval*i

img_gray[(img_gray >= 255-interval)] = 255 

#st.text(np.unique(img_gray))

new_image = Image.fromarray(img_gray)

# plt.axis('off')
# plt.imshow(new_image)
# plt.show()
# st.pyplot()

st.image([new_image.convert("L"), image], caption=['Cinza', 'colorida'], width=480,) 
# st.image(image, caption='Colorida', width=320,)