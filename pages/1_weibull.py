import streamlit as st
import pandas as pd
import os
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


#st.set_page_config(layout="wide")

st.header("ワイブルプロットによる故障の解析")

st.subheader("故障のデータ")
st.write("Time: 評価時間")
st.write("Failure: 故障の有無(0: 故障していない　1: 故障発生)")

df = pd.read_csv("./data/Weibull_plot/Weibull_Failure_Data.csv")

col1, col2 = st.columns(2)

with col2:
    st.write(df)

with col1:
    fig, ax = plt.subplots()
    #sns.histplot(df["Time"], kde=False, ax=ax)
    sns.histplot(df[df["Failure"]==1]["Time"], kde=False, ax=ax, color="#DD8452", edgecolor="none", alpha=0.5, label="1")
    sns.histplot(df[df["Failure"]==0]["Time"], kde=False, ax=ax, color="#4C72B0", edgecolor="none", alpha=0.5, label="0")
    
    plt.xlim(0, 2500)  # x軸の範囲を0から3000に設定
    ax.set_title("Data Distribution")
    plt.legend()
    
    st.pyplot(fig)


st.subheader("解析結果")

col1, col2 = st.columns(2)

with col1:
    failure_data = df[df['Failure'] == 1]['Time'].sort_values().values
    num_failures = len(failure_data)
    rank = np.arange(1, num_failures + 1)
    failure_probability = (rank - 0.3) / (num_failures + 0.4)
    
    fig, ax = plt.subplots()
    ax.plot(failure_data, failure_probability, marker="o", linestyle="-", color="blue")
    ax.set_xlabel("Time")
    ax.set_ylabel("Cumulative Failure Rate")
    ax.set_title("Cumulative Failure Rate")
    ax.grid(True)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    ax.plot(np.log(failure_data), np.log(-np.log(1-failure_probability)), marker="o", linestyle="-", color="blue")
    ax.set_xlabel("Log(Time)")
    ax.set_ylabel("Log(-Log(1 - Faillure Rate)")
    ax.set_title("Weibull Plot")
    ax.grid(True)
    st.pyplot(fig)

# バスタブカーブの計算

col1, col2 = st.columns(2)

with col1:
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
    ax.set_ylabel("Failure Rate")
    ax.set_title("Bath-Tub Curve")
    ax.grid(True)
    st.pyplot(fig)

with col2:
    st.subheader("")
    st.subheader("平均故障時間: XXX時間")
    st.subheader("XXX時間生存率: XX%")

