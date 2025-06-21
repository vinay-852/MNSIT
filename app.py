from torchvision.datasets import MNIST
from torchvision import transforms
import streamlit as st

st.title("MNIST Dataset Viewer")

data = MNIST(".", train=True, download=True)

st.write("Write the digit you want to generate:")
number = st.number_input("Enter a number (0-9):", min_value=0, max_value=9, value=0)

def get_images(digit):
    images = []
    count = 0
    for i in data:
        if i[1] == digit:
            images.append(i[0])
            count += 1
            if count == 5:
                break
    return images

st.write(f"Images of number {number}:")
images = get_images(number)
for i, img in enumerate(images):
    st.image(img, caption=f"Image {i+1}", use_column_width=True)
