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
