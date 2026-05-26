# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# -----------------------------
# 한글 폰트 설정
# -----------------------------
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# 제목
# -----------------------------
st.title("🌡️ 날짜별 기온 분석")

st.write("월과 일을 선택하면 연도별 최고기온과 최저기온을 확인할 수 있어!")

# -----------------------------
# 데이터 불러오기
# -----------------------------
df = pd.read_csv("seoul.csv", encoding='cp949')

# 컬럼 이름 정리
df.columns = ['날짜', '지점', '평균기온', '최저기온', '최고기온']

# 날짜 형식 변환
df['날짜'] = pd.to_datetime(df['날짜'])

# 연/월/일 컬럼 생성
df['연도'] = df['날짜'].dt.year
df['월'] = df['날짜'].dt.month
df['일'] = df['날짜'].dt.day

# -----------------------------
# 사용자 선택
# -----------------------------
month = st.selectbox(
    "📅 월 선택",
    list(range(1, 13))
)

day = st.selectbox(
    "📌 일 선택",
    list(range(1, 32))
)

# -----------------------------
# 데이터 필터링
# -----------------------------
filtered = df[
    (df['월'] == month) &
    (df['일'] == day)
]

# 결측 제거
filtered = filtered.dropna(subset=['최고기온', '최저기온'])

# -----------------------------
# 그래프 출력
# -----------------------------
if len(filtered) > 0:

    fig, ax = plt.subplots(figsize=(12, 6))

    # 최고기온
    ax.plot(
        filtered['연도'],
        filtered['최고기온'],
        color='red',
        label='최고기온',
        linewidth=2
    )

    # 최저기온
    ax.plot(
        filtered['연도'],
        filtered['최저기온'],
        color='lightblue',
        label='최저기온',
        linewidth=2
    )

    # 제목 및 축
    ax.set_title("날짜별 기온분석", fontsize=18)
    ax.set_xlabel("연도", fontsize=13)
    ax.set_ylabel("온도(℃)", fontsize=13)

    # 범례
    ax.legend()

    # 격자
    ax.grid(True, linestyle='--', alpha=0.5)

    # Streamlit 출력
    st.pyplot(fig)

else:
    st.warning("선택한 날짜의 데이터가 없어!")
