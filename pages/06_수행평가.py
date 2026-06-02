import streamlit as st
import pandas as pd

# -----------------------------
# 기본 설정
# -----------------------------
st.set_page_config(
    page_title="🐶 인천 반려동물 관광지",
    page_icon="🐾",
    layout="wide"
)

st.title("🐾 인천 반려동물 동반 관광지 찾기")
st.markdown(
    """
    반려동물과 함께 갈 수 있는 관광지를 찾아보자! 🐶🐱

    1️⃣ 지역 선택하기  
    2️⃣ 시설 선택하기  
    3️⃣ 정보 확인하기
    """
)

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(
        "인천광역시_반려동물 동반 관광지 정보 리스트_20260119.csv",
        encoding="utf-8"
    )
    return df

df = load_data()

# -----------------------------
# 컬럼 이름 확인
# -----------------------------
st.sidebar.header("⚙️ 설정")

지역컬럼 = df.columns[0]
시설명컬럼 = df.columns[1]

# -----------------------------
# 지역 선택
# -----------------------------
지역선택 = st.selectbox(
    "🏙️ 지역을 선택해줘!",
    ["강화군", "중구"]
)

지역데이터 = df[df[지역컬럼] == 지역선택]

if len(지역데이터) == 0:
    st.warning("😢 해당 지역 데이터가 없어!")
    st.stop()

# -----------------------------
# 시설 선택
# -----------------------------
시설선택 = st.selectbox(
    "🐾 어떤 시설이 궁금해?",
    sorted(지역데이터[시설명컬럼].astype(str).unique())
)

선택시설 = 지역데이터[
    지역데이터[시설명컬럼] == 시설선택
].iloc[0]

st.divider()

st.subheader(f"📍 {시설선택}")

# -----------------------------
# 주요 정보 출력
# -----------------------------
col1, col2, col3 = st.columns(3)

주소 = ""
주차 = ""
공간 = ""

for col in df.columns:

    if "주소" in col:
        주소 = 선택시설[col]

    if "주차" in col:
        주차 = 선택시설[col]

    if "공간" in col:
        공간 = 선택시설[col]

with col1:
    st.metric("📍 위치", str(주소))

with col2:
    st.metric("🚗 주차", str(주차))

with col3:
    st.metric("🏠 실내/실외", str(공간))

st.divider()

st.subheader("🐶 상세 정보")

for col in df.columns:

    값 = 선택시설[col]

    if pd.notna(값) and str(값).strip() != "":
        st.write(f"**{col}**")
        st.write(str(값))
        st.write("")

st.success("🎉 반려동물과 즐거운 여행 되세요!")
