import streamlit as st
import pandas as pd
import os
from matplotlib import pyplot as plt
import seaborn as sns
#import japanize_matplotlib
import numpy as np

st.header("ワイブルプロットによる故障の解析")

st.subheader("故障のデータ")
st.write("Time: 評価時間")
st.write("Failure: 故障の有無(0: 故障していない　1: 故障発生)")

df = pd.read_csv("./data/Weibull_plot/Weibull_Failure_Data.csv")
st.write(df)

fig, ax = plt.subplots()
#sns.histplot(df["Time"], kde=False, ax=ax)
sns.histplot(df[df["Failure"]==1]["Time"], kde=False, ax=ax, color="#DD8452", edgecolor="none", alpha=0.5, label="1")
sns.histplot(df[df["Failure"]==0]["Time"], kde=False, ax=ax, color="#4C72B0", edgecolor="none", alpha=0.5, label="0")

plt.xlim(0, 2500)  # x軸の範囲を0から3000に設定
ax.set_title("データの分布")
plt.legend()

st.pyplot(fig)



st.subheader("解析結果")

failure_data = df[df['Failure'] == 1]['Time'].sort_values().values
num_failures = len(failure_data)
rank = np.arange(1, num_failures + 1)
failure_probability = (rank - 0.3) / (num_failures + 0.4)

fig, ax = plt.subplots()
ax.plot(failure_data, failure_probability, marker="o", linestyle="-", color="orange")
ax.set_xlabel("Time")
ax.set_ylabel("累積故障率")
ax.set_title("累積故障率")
ax.grid(True)
st.pyplot(fig)

fig, ax = plt.subplots()
ax.plot(np.log(failure_data), np.log(-np.log(1-failure_probability)), marker="o", linestyle="-", color="blue")
ax.set_xlabel("Log(Time)")
ax.set_ylabel("Log(-Log(1 - 累積故障率)")
ax.set_title("ワイブルプロット")
ax.grid(True)
st.pyplot(fig)

# バスタブカーブの計算

time_intervals = np.linspace(failure_data.min(), failure_data.max(), 10)
failure_rate = []

for i in range(len(time_intervals) - 1):
    interval_start = time_intervals[i]
    interval_end = time_intervals[i + 1]
    failures_in_interval = ((failure_data >= interval_start) & (failure_data < interval_end)).sum()
    interval_length = interval_end - interval_start
    failure_rate.append(failures_in_interval / interval_length if interval_length > 0 else 0)

interval_centers = (time_intervals[:-1] + time_intervals[1:]) / 2

fig, ax = plt.subplots()
ax.plot(interval_centers, failure_rate, marker="o", linestyle="-", color="blue")
ax.set_xlabel("Time")
ax.set_ylabel("故障率")
ax.set_title("バスタブ曲線")
ax.grid(True)
st.pyplot(fig)