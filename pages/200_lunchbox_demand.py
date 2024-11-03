import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

st.header("(作成中)お弁当の需要予測")
st.write("https://signate.jp/competitions/24")

train_df = pd.read_csv("./data/lunchbox_demand/train.csv")
train_df["datetime"] = pd.to_datetime(train_df["datetime"])

st.write(train_df)

fig, ax = plt.subplots()
ax.plot(train_df["datetime"], train_df["y"])
plt.gcf().autofmt_xdate()
plt.title("y")
plt.ylabel("y")
st.pyplot(fig)

##########################################3

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# データの作成
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 列を2つ作成
col1, col2, col3 = st.columns(3)

# 1つ目のグラフを表示
with col1:
    fig, ax = plt.subplots()
    ax.plot(x, y1, label="sin(x)")
    ax.set_title("Sine Wave")
    st.pyplot(fig)

# 2つ目のグラフを表示
with col2:
    fig, ax = plt.subplots()
    ax.plot(x, y2, label="cos(x)", color="orange")
    ax.set_title("Cosine Wave")
    st.pyplot(fig)

with col3:
    st.write(train_df)
