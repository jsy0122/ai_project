# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# 마이너스 깨짐 방지
# -----------------------------------
plt.rcParams['axes.unicode_minus'] = False

# -----------------------------------
# 제목
# -----------------------------------
st.title("🌡️ Temperature Analysis")

st.write("Select month and day!")

# -----------------------------------
# 데이터 불러오기
# -----------------------------------
df = pd.read_csv(
    "seoul.csv",
    encoding='cp949'
)

# 컬럼명 변경
df.columns = [
    'date',
    'station',
    'avg_temp',
    'min_temp',
    'max_temp'
]

# -----------------------------------
# 날짜 변환
# -----------------------------------
df['date'] = pd.to_datetime(
    df['date'],
    errors='coerce'
)

# 오류 제거
df = df.dropna(subset=['date'])

# -----------------------------------
# 연/월/일 생성
# -----------------------------------
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

# -----------------------------------
# 사용자 선택
# -----------------------------------
month = st.selectbox(
    "Month",
    range(1, 13)
)

day = st.selectbox(
    "Day",
    range(1, 32)
)

# -----------------------------------
# 데이터 필터링
# -----------------------------------
filtered = df[
    (df['month'] == month) &
    (df['day'] == day)
]

# 결측 제거
filtered = filtered.dropna(
    subset=['max_temp', 'min_temp']
)

# -----------------------------------
# 그래프
# -----------------------------------
if not filtered.empty:

    fig, ax = plt.subplots(
        figsize=(14, 6)
    )

    # 최고기온
    ax.plot(
        filtered['year'],
        filtered['max_temp'],
        color='red',
        linewidth=2,
        label='Max Temp'
    )

    # 최저기온
    ax.plot(
        filtered['year'],
        filtered['min_temp'],
        color='blue',
        linewidth=2,
        label='Min Temp'
    )

    # 제목
    ax.set_title(
        f"Temperature Analysis ({month}/{day})",
        fontsize=20
    )

    # 축
    ax.set_xlabel(
        "Year",
        fontsize=14
    )

    ax.set_ylabel(
        "Temperature (°C)",
        fontsize=14
    )

    # 범례
    ax.legend(
        fontsize=12
    )

    # 격자
    ax.grid(
        True,
        linestyle='--',
        alpha=0.5
    )

    # 출력
    st.pyplot(fig)

else:
    st.warning("No data!")
