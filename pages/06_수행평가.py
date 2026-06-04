import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="🐶 인천 반려동물 관광지도",
    page_icon="🐾",
    layout="wide"
)

st.title("🐶 인천 반려동물 관광지도")
st.markdown(
    """
    반려동물과 함께 갈 수 있는 인천 관광지를 찾아보자! 🐾

    📍 지도에서 위치 확인  
    🐕 관광지 상세 정보 확인  
    🚗 주차 여부 확인
    """
)

# -----------------------------
# 데이터 불러오기
# -----------------------------
df = pd.read_csv("aa.csv")

# -----------------------------
# 지역별 색상
# -----------------------------
colors = {
    "중구": "red",
    "강화군": "blue",
    "남동구": "green",
    "연수구": "purple",
    "옹진군": "orange",
    "서구": "darkred",
    "계양구": "cadetblue",
    "부평구": "darkgreen",
    "미추홀구": "pink"
}

# -----------------------------
# 좌표 확인
# -----------------------------
lat_col = None
lon_col = None

for col in df.columns:
    if "위도" in col:
        lat_col = col
    if "경도" in col:
        lon_col = col

# -----------------------------
# 지도 생성
# -----------------------------
st.subheader("🗺️ 관광지 지도")

m = folium.Map(
    location=[37.5, 126.6],
    zoom_start=10
)

if lat_col and lon_col:

    for _, row in df.iterrows():

        region = row["지역"]

        color = colors.get(region, "gray")

        popup_text = f"""
        <b>{row['상호']}</b><br>
        📍 {row['주소']}
        """

        folium.Marker(
            [row[lat_col], row[lon_col]],
            popup=popup_text,
            icon=folium.Icon(color=color)
        ).add_to(m)

    st_folium(
        m,
        width=1200,
        height=600
    )

else:
    st.warning(
        "⚠️ 현재 CSV에 위도/경도 정보가 없어 지도를 표시할 수 없어.\n\n"
        "위도와 경도 컬럼을 추가하면 지도에 마커가 표시돼!"
    )

# -----------------------------
# 관광지 선택
# -----------------------------
st.subheader("🔎 관광지 정보 보기")

place = st.selectbox(
    "가고 싶은 관광지를 선택해봐! 😊",
    df["상호"].sort_values().unique()
)

selected = df[df["상호"] == place].iloc[0]

col1, col2 = st.columns(2)

with col1:

    st.markdown("### 🐾 기본 정보")

    st.write("📌 관광지 :", selected["상호"])
    st.write("🏙️ 지역 :", selected["지역"])
    st.write("📍 주소 :", selected["주소"])

    if "이용시간" in df.columns:
        st.write("⏰ 이용시간 :", selected["이용시간"])

    if "이용료" in df.columns:
        st.write("💰 이용료 :", selected["이용료"])

with col2:

    st.markdown("### 🐶 반려동물 정보")

    if "반려동물용 메뉴 및 서비스 시설" in df.columns:
        st.write(
            "🦴 편의시설 :",
            selected["반려동물용 메뉴 및 서비스 시설"]
        )

    if "반려동물용 메뉴 및 서비스 시설 내용" in df.columns:
        st.write(
            "🐕 시설 설명 :",
            selected["반려동물용 메뉴 및 서비스 시설 내용"]
        )

    if "입장 가능 반려동물 제한사항" in df.columns:
        st.write(
            "⚠️ 제한사항 :",
            selected["입장 가능 반려동물 제한사항"]
        )

st.markdown("---")

st.markdown("### 🚗 방문 정보")

if "주차" in df.columns:
    st.info(f"주차 정보 : {selected['주차']}")

if "휴무" in df.columns:
    st.info(f"휴무일 : {selected['휴무']}")

if "기타 특이사항" in df.columns:
    st.success(f"✨ 특이사항 : {selected['기타 특이사항']}")

# -----------------------------
# 같은 지역 관광지 추천
# -----------------------------
st.markdown("### 🎯 비슷한 관광지 추천")

same_region = df[df["지역"] == selected["지역"]]

recommend = (
    same_region["상호"]
    .drop_duplicates()
    .head(5)
)

for item in recommend:
    if item != place:
        st.write(f"🐾 {item}")

st.markdown("---")

st.caption(
    "💙 반려동물과 함께 즐거운 여행 되길 바라! 🐶🐾"
)
