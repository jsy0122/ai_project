import streamlit as st
import pandas as pd
import random

# ------------------------
# 페이지 설정
# ------------------------
st.set_page_config(
    page_title="🐶 인천 반려동물 관광 추천",
    page_icon="🐾",
    layout="wide"
)

# ------------------------
# 데이터 불러오기
# ------------------------
df = pd.read_csv("aa.csv")

# ------------------------
# 제목
# ------------------------
st.title("🐾 인천 반려동물 관광 추천기")

st.markdown("""
안녕! 😊

어느 지역으로 놀러 갈지 고민 중이라면
내가 반려동물과 함께 가기 좋은 관광지를 추천해줄게!

🐶 반려동물 동반 가능  
📍 지역별 관광지 추천  
✨ 추천 이유까지 설명
""")

# ------------------------
# 지역 선택
# ------------------------
regions = sorted(df["지역"].dropna().unique())

selected_region = st.selectbox(
    "🏙️ 가고 싶은 지역을 선택해봐!",
    regions
)

# ------------------------
# 지역 데이터
# ------------------------
region_df = df[df["지역"] == selected_region]

st.markdown("---")

st.header(f"🎯 {selected_region} 추천 관광지")

# 관광지 2개 추천
recommend_df = region_df.sample(
    min(2, len(region_df)),
    random_state=random.randint(1, 10000)
)

for idx, (_, row) in enumerate(recommend_df.iterrows(), start=1):

    st.subheader(f"🌟 추천 {idx}. {row['상호']}")

    st.write(f"📍 주소 : {row['주소']}")

    # 추천 이유 생성
    reason = []

    if pd.notna(row.get("반려동물용 메뉴 및 서비스 시설")):
        reason.append("반려동물 편의시설이 준비되어 있어!")

    if pd.notna(row.get("주차")):
        reason.append("주차 정보를 제공해서 방문하기 편해!")

    if pd.notna(row.get("이용시간")):
        reason.append("운영시간 정보가 잘 정리되어 있어!")

    if len(reason) == 0:
        reason.append("지역에서 인기가 많은 관광지야!")

    st.success(
        f"💡 추천 이유 : {reason[0]}"
    )

    st.markdown("---")

# ------------------------
# 상세 관광지 보기
# ------------------------
st.header("🔍 관광지 자세히 보기")

place = st.selectbox(
    "궁금한 관광지를 선택해봐!",
    region_df["상호"].sort_values().unique()
)

selected = region_df[
    region_df["상호"] == place
].iloc[0]

col1, col2 = st.columns(2)

with col1:

    st.subheader("📋 기본 정보")

    st.write(f"🏷️ 관광지 : {selected['상호']}")
    st.write(f"📍 주소 : {selected['주소']}")

    if pd.notna(selected.get("이용시간")):
        st.write(f"⏰ 이용시간 : {selected['이용시간']}")

    if pd.notna(selected.get("이용료")):
        st.write(f"💰 이용료 : {selected['이용료']}")

with col2:

    st.subheader("🐶 반려동물 정보")

    if pd.notna(selected.get("반려동물용 메뉴 및 서비스 시설")):
        st.write(
            f"🦴 편의시설 : {selected['반려동물용 메뉴 및 서비스 시설']}"
        )

    if pd.notna(selected.get("입장 가능 반려동물 제한사항")):
        st.write(
            f"⚠️ 제한사항 : {selected['입장 가능 반려동물 제한사항']}"
        )

    if pd.notna(selected.get("주차")):
        st.write(
            f"🚗 주차 : {selected['주차']}"
        )

st.markdown("---")

# ------------------------
# 한줄 추천
# ------------------------
messages = [
    "🐕 반려동물과 함께 특별한 추억을 만들어봐!",
    "📸 예쁜 사진도 꼭 남겨보자!",
    "🌳 산책하기 좋은 곳을 골라봤어!",
    "💙 즐거운 여행 되길 바랄게!",
    "🐾 오늘도 멍멍이와 행복한 하루!"
]

st.info(random.choice(messages))
