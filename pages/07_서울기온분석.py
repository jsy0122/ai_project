# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import os

# -----------------------------------
# 한글 안 깨지게 설정 (파일 다운로드 필요 없음)
# -----------------------------------
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# -----------------------------------
# 제목
# -----------------------------------
st.title("🌡️ 날짜별 기온 분석")

st.write("월과 일을 선택하면 연도별 기온 변화를 볼 수 있어!")

# -----------------------------------
# 데이터 불러오기
# -----------------------------------
df = pd.read_csv(
    "seoul.csv",
    encoding='cp949'
)

# 컬럼명 변경
df.columns = [
    '날짜',
    '지점',
    '평균기온',
    '최저기온',
    '최고기온'
]

# -----------------------------------
# 날짜 변환
# -----------------------------------
df['날짜'] = pd.to_datetime(
    df['날짜'],
    errors='coerce'
)

# 오류 제거
df = df.dropna(subset=['날짜'])

# -----------------------------------
# 연/월/일 생성
# -----------------------------------
df['연도'] = df['날짜'].dt.year
df['월'] = df['날짜'].dt.month
df['일'] = df['날짜'].dt.day

# -----------------------------------
# 사용자 선택
# -----------------------------------
month = st.selectbox(
    "📅 월 선택",
    range(1, 13)
)

day = st.selectbox(
    "📌 일 선택",
    range(1, 32)
)

# -----------------------------------
# 데이터 필터링
# -----------------------------------
filtered = df[
    (df['월'] == month) &
    (df['일'] == day)
]

# 결측 제거
filtered = filtered.dropna(
    subset=['최고기온', '최저기온']
)

# -----------------------------------
# 그래프 출력
# -----------------------------------
if not filtered.empty:

    fig, ax = plt.subplots(
        figsize=(14, 6)
    )

    # 최고기온
    ax.plot(
        filtered['연도'],
        filtered['최고기온'],
        color='red',
        linewidth=2,
        label='최고기온'
    )

    # 최저기온
    ax.plot(
        filtered['연도'],
        filtered['최저기온'],
        color='lightblue',
        linewidth=2,
        label='최저기온'
    )

    # 제목
    ax.set_title(
        f"{month}월 {day}일 날짜별 기온 분석",
        fontsize=20
    )

    # 축 이름
    ax.set_xlabel(
        "연도",
        fontsize=14
    )

    ax.set_ylabel(
        "온도(℃)",
        fontsize=14
    )

    # 범례
    ax.legend(fontsize=12)

    # 격자
    ax.grid(
        True,
        linestyle='--',
        alpha=0.5
    )

    # Streamlit 출력
    st.pyplot(fig)

else:
    st.warning("해당 날짜 데이터가 없어!")
