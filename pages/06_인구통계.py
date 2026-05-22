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
# 한글 폰트 직접 등록
# -----------------------------
font_path = "NanumGothic.ttf"

fontprop = fm.FontProperties(fname=font_path)

plt.rcParams['font.family'] = fontprop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# 데이터 불러오기
# -----------------------------
df = pd.read_csv("population.csv", encoding="euc-kr")

# -----------------------------
# 컬럼 이름 변경
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

# ==================================================
# 1️⃣ 행정구 선택 그래프
# ==================================================

st.subheader("🏙️ 행정구별 연령대 인구 그래프")

district = st.selectbox(
    "행정구를 선택하세요",
    df["행정구역"]
)

selected = df[df["행정구역"] == district]

ages = age_columns
population = selected.iloc[0, 1:]

# 그래프 생성
fig, ax = plt.subplots(figsize=(11, 5))

# 배경색
fig.patch.set_facecolor("#EAF7FF")
ax.set_facecolor("#EAF7FF")

# 꺾은선 그래프
ax.plot(
    ages,
    population,
    marker='o',
    markersize=8,
    linewidth=3,
    color='darkblue'
)

# 제목
ax.set_title(
    "서울시의 인구통계",
    fontsize=20,
    fontweight='bold',
    fontproperties=fontprop
)

# 축 이름
ax.set_xlabel(
    "연령대",
    fontsize=13,
    fontproperties=fontprop
)

ax.set_ylabel(
    "인구수",
    fontsize=13,
    fontproperties=fontprop
)

# x축 한글 적용
ax.set_xticklabels(
    ages,
    fontproperties=fontprop,
    rotation=20
)

# 격자
ax.grid(True, linestyle='--', alpha=0.5)

# 출력
st.pyplot(fig)

# ==================================================
# 2️⃣ 연령대별 인구 많은 행정구
# ==================================================

st.divider()

st.subheader("🔍 연령대별 인구가 가장 많은 행정구")

selected_age = st.selectbox(
    "연령대를 선택하세요",
    age_columns
)

# 가장 많은 지역 찾기
max_idx = df[selected_age].idxmax()

top_district = df.loc[max_idx, "행정구역"]
top_population = df.loc[max_idx, selected_age]

# 결과 출력
st.success(
    f"🎉 {selected_age} 인구가 가장 많은 지역은 "
    f"👉 {top_district} 이고 "
    f"인구수는 {top_population:,}명 입니다!"
)

# ==================================================
# 3️⃣ TOP5 그래프
# ==================================================

top5 = df.sort_values(by=selected_age, ascending=False).head(5)

fig2, ax2 = plt.subplots(figsize=(10, 5))

# 배경색
fig2.patch.set_facecolor("#EAF7FF")
ax2.set_facecolor("#EAF7FF")

# 막대 그래프
ax2.bar(
    top5["행정구역"],
    top5[selected_age],
    color='darkblue'
)

# 제목
ax2.set_title(
    f"{selected_age} 인구 TOP 5 행정구",
    fontsize=18,
    fontweight='bold',
    fontproperties=fontprop
)

# 축 이름
ax2.set_xlabel(
    "행정구역",
    fontproperties=fontprop
)

ax2.set_ylabel(
    "인구수",
    fontproperties=fontprop
)

# x축 한글 적용
ax2.set_xticklabels(
    top5["행정구역"],
    fontproperties=fontprop
)

# 격자
ax2.grid(True, linestyle='--', alpha=0.3)

# 출력
st.pyplot(fig2)
