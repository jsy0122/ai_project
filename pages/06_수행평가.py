import streamlit as st
import pandas as pd

# ---------------------------------
# 페이지 설정
# ---------------------------------
st.set_page_config(
    page_title="🐾 반려동물 관광지 찾기",
    page_icon="🐶",
    layout="wide"
)

st.title("🐾 인천 반려동물 동반 관광지")
st.markdown(
    """
    반려동물과 함께 갈 수 있는 관광지를 찾아보자! 🐶🐱

    ✅ 지역 선택  
    ✅ 시설 선택  
    ✅ 상세 정보 확인
    """
)

# ---------------------------------
# CSV 불러오기
# ---------------------------------
@st.cache_data
def load_data():

    file_name = "인천광역시_반려동물 동반 관광지 정보 리스트_20260119.csv"

    encodings = [
        "cp949",
        "euc-kr",
        "utf-8-sig",
        "utf-8"
    ]

    for enc in encodings:
        try:
            return pd.read_csv(file_name, encoding=enc)
        except:
            pass

    return None

df = load_data()

if df is None:
    st.error("❌ CSV 파일을 읽을 수 없습니다.")
    st.stop()

# ---------------------------------
# 컬럼 자동 찾기
# ---------------------------------

def find_column(keyword_list):
    for col in df.columns:
        for keyword in keyword_list:
            if keyword in col:
                return col
    return None

지역컬럼 = find_column(["지역"])
시설컬럼 = find_column(["관광지명", "업체명", "시설명", "상호명", "명"])
주소컬럼 = find_column(["주소"])
주차컬럼 = find_column(["주차"])
공간컬럼 = find_column(["공간"])

if 지역컬럼 is None or 시설컬럼 is None:
    st.error("❌ 지역 또는 시설 컬럼을 찾을 수 없습니다.")
    st.write(df.columns.tolist())
    st.stop()

# ---------------------------------
# 지역 선택
# ---------------------------------

지역목록 = ["강화군", "중구"]

선택지역 = st.selectbox(
    "🏙️ 지역을 선택해줘!",
    지역목록
)

지역데이터 = df[df[지역컬럼].astype(str).str.contains(선택지역, na=False)]

if len(지역데이터) == 0:
    st.warning("😢 해당 지역 데이터가 없어!")
    st.stop()

# ---------------------------------
# 시설 선택
# ---------------------------------

시설목록 = sorted(
    지역데이터[시설컬럼]
    .astype(str)
    .dropna()
    .unique()
)

선택시설 = st.selectbox(
    "🐶 어떤 시설이 궁금해?",
    시설목록
)

시설정보 = 지역데이터[
    지역데이터[시설컬럼].astype(str) == 선택시설
].iloc[0]

st.divider()

st.subheader(f"📍 {선택시설}")

# ---------------------------------
# 주요 정보
# ---------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    주소 = 시설정보[주소컬럼] if 주소컬럼 else "정보 없음"
    st.metric("📍 위치", str(주소))

with col2:
    주차 = 시설정보[주차컬럼] if 주차컬럼 else "정보 없음"
    st.metric("🚗 주차", str(주차))

with col3:
    공간 = 시설정보[공간컬럼] if 공간컬럼 else "정보 없음"
    st.metric("🏠 실내/실외", str(공간))

# ---------------------------------
# 상세정보
# ---------------------------------

st.divider()
st.subheader("📋 시설 상세정보")

for col in df.columns:

    value = 시설정보[col]

    if pd.notna(value) and str(value).strip() != "":
        st.write(f"**{col}**")
        st.write(str(value))

st.success("🐾 즐거운 반려동물 여행 되세요!")
