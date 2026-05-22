import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="서울시 인구통계",
    layout="centered"
)

st.title("📊 서울시의 인구통계")

# -----------------------------
# 한글 폰트 설정
# -----------------------------
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# 데이터 불러오기
# -----------------------------
df = pd.read_csv("population.csv", encoding="euc-kr")

# -----------------------------
# 컬럼 이름 정리
# -----------------------------
df.columns = [
    "행정구역",
    "0~9세",
    "10~19세",
    "20~29세",
    "30~39세",
    "40~49세",
    "50~59세",
    "60~69세",
    "70~79세",
    "80~89세",
    "90~99세",
    "100세 이상"
]

# -----------------------------
# 숫자형 변환
# -----------------------------
age_columns = df.columns[1:]

for col in age_columns:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", "")
        .astype(int)
    )

# -----------------------------
# 행정구 선택
# -----------------------------
district = st.selectbox(
    "🏙️ 행정구를 선택하세요",
    df["행정구역"]
)

# -----------------------------
# 선택한 데이터 추출
# -----------------------------
selected = df[df["행정구역"] == district]

ages = age_columns
population = selected.iloc[0, 1:]

# -----------------------------
# 그래프 생성
# -----------------------------
fig, ax = plt.subplots(figsize=(10, 5))

# 그래프 바탕색
fig.patch.set_facecolor("#EAF7FF")
ax.set_facecolor("#EAF7FF")

# 꺾은선 그래프
ax.plot(
    ages,
    population,
    marker='o',
    linewidth=3,
    color='darkblue'
)

# 제목
ax.set_title(
    "서울시의 인구통계",
    fontsize=18,
    fontweight='bold'
)

# 축 이름
ax.set_xlabel("연령대", fontsize=12)
ax.set_ylabel("인구수", fontsize=12)

# 눈금 회전
plt.xticks(rotation=20)

# 격자
ax.grid(True, linestyle='--', alpha=0.5)

# Streamlit 출력
st.pyplot(fig)
