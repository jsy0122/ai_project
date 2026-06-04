import streamlit as st
import pandas as pd
import random

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="🐾 인천 반려동물 관광 추천",
    page_icon="🐶",
    layout="wide"
)

# -----------------------------
# CSV 읽기 함수
# -----------------------------
@st.cache_data
def load_data():

    encodings = [
        "utf-8",
        "utf-8-sig",
        "cp949",
        "euc-kr"
    ]

    for enc in encodings:
        try:
            df = pd.read_csv("aa.csv", encoding=enc)
            return df
        except:
            pass

    return None

# -----------------------------
# 데이터 불러오기
# -----------------------------
df = load_data()

if df is None:
    st.error("❌ aa.csv 파일을 읽을 수 없어!")
    st.stop()

# -----------------------------
# 제목
# -----------------------------
st.title("🐶 인천 반려동물 관광지 추천기")

st.markdown("""
안녕! 😊

인천에서 반려동물과 함께 갈 만한 관광지를 추천해줄게!

🐾 지역 선택하기  
🎯 관광지 추천받기  
📋 관광지 정보 확인하기  

재미있게 둘러보자! 🚀
""")

st.markdown("---")

# -----------------------------
# 지역 선택
# -----------------------------
regions = sorted(df["지역"].dropna().unique())

selected_region = st.selectbox(
    "🏙️ 어느 지역으로 놀러 갈까?",
    regions
)

# -----------------------------
# 해당 지역 데이터
# -----------------------------
region_df = df[df["지역"] == selected_region]

st.markdown("---")

st.header(f"🌟 {selected_region} 추천 관광지")

# -----------------------------
# 추천 관광지 2개
# -----------------------------
recommend_df = region_df.sample(
    min(2, len(region_df)),
    random_state=random.randint(1, 9999)
)

for i, (_, row) in enumerate(recommend_df.iterrows(), start=1):

    st.subheader(f"🐾 추천 {i}. {row['상호']}")

    st.write(f"📍 주소 : {row['주소']}")

    reasons = []

    if "반려동물용 메뉴 및 서비스 시설" in df.columns:
        if pd.notna(row["반려동물용 메뉴 및 서비스 시설"]):
            reasons.append("🐶 반려동물 편의시설이 준비되어 있어!")

    if "주차" in df.columns:
        if pd.notna(row["주차"]):
            reasons.append("🚗 주차 정보를 제공해서 방문하기 편해!")

    if "이용시간" in df.columns:
        if pd.notna(row["이용시간"]):
            reasons.append("⏰ 운영시간 정보가 잘 정리되어 있어!")

    if not reasons:
        reasons.append("✨ 지역에서 유명한 관광지야!")

    st.success(f"추천 이유 : {random.choice(reasons)}")

    st.markdown("---")

# -----------------------------
# 상세 정보
# -----------------------------
st.header("🔍 관광지 자세히 보기")

place = st.selectbox(
    "궁금한 관광지를 선택해봐!",
    sorted(region_df["상호"].unique())
)

selected = region_df[
    region_df["상호"] == place
].iloc[0]

col1, col2 = st.columns(2)

with col1:

    st.subheader("📋 기본 정보")

    st.write(f"🏷️ 관광지명 : {selected['상호']}")
    st.write(f"📍 주소 : {selected['주소']}")

    if "이용시간" in df.columns:
        if pd.notna(selected["이용시간"]):
            st.write(f"⏰ 이용시간 : {selected['이용시간']}")

    if "이용료" in df.columns:
        if pd.notna(selected["이용료"]):
            st.write(f"💰 이용료 : {selected['이용료']}")

with col2:

    st.subheader("🐶 반려동물 정보")

    if "반려동물용 메뉴 및 서비스 시설" in df.columns:
        if pd.notna(selected["반려동물용 메뉴 및 서비스 시설"]):
            st.write(
                f"🦴 편의시설 : {selected['반려동물용 메뉴 및 서비스 시설']}"
            )

    if "입장 가능 반려동물 제한사항" in df.columns:
        if pd.notna(selected["입장 가능 반려동물 제한사항"]):
            st.write(
                f"⚠️ 제한사항 : {selected['입장 가능 반려동물 제한사항']}"
            )

    if "주차" in df.columns:
        if pd.notna(selected["주차"]):
            st.write(
                f"🚗 주차 : {selected['주차']}"
            )

# -----------------------------
# 추가 정보
# -----------------------------
st.markdown("---")

if "기타 특이사항" in df.columns:
    if pd.notna(selected["기타 특이사항"]):
        st.info(
            f"✨ 특이사항 : {selected['기타 특이사항']}"
        )

# -----------------------------
# 지역 통계
# -----------------------------
st.markdown("---")

st.header("📊 지역 관광지 수")

count_df = (
    df["지역"]
    .value_counts()
    .reset_index()
)

count_df.columns = ["지역", "관광지 수"]

st.dataframe(
    count_df,
    use_container_width=True
)

# -----------------------------
# 마지막 메시지
# -----------------------------
messages = [
    "🐕 반려동물과 즐거운 추억 만들기!",
    "📸 예쁜 사진 많이 찍고 와!",
    "🌳 산책도 하고 힐링도 해보자!",
    "💙 행복한 여행 되길 바랄게!",
    "🐾 오늘도 멍멍이와 좋은 하루!"
]

st.markdown("---")
st.success(random.choice(messages))
