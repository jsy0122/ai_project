# app.py
import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="서울 인기 관광지 TOP 10 🌏",
    page_icon="📍",
    layout="wide"
)

st.title("🌏 외국인들이 좋아하는 서울 관광지 TOP 10")
st.markdown("폴리움(Folium) 지도로 서울의 인기 관광지를 한눈에 확인해봐! ✨")

# 관광지 데이터
places = [
    {
        "name": "경복궁 🏯",
        "lat": 37.579617,
        "lon": 126.977041,
        "desc": "조선 시대의 대표 궁궐"
    },
    {
        "name": "명동 😄",
        "lat": 37.563757,
        "lon": 126.982893,
        "desc": "쇼핑과 길거리 음식의 천국"
    },
    {
        "name": "N서울타워 🌃",
        "lat": 37.551169,
        "lon": 126.988227,
        "desc": "서울 야경 명소"
    },
    {
        "name": "북촌한옥마을 🏡",
        "lat": 37.582604,
        "lon": 126.983998,
        "desc": "전통 한옥 감성 가득"
    },
    {
        "name": "홍대 🎵",
        "lat": 37.556350,
        "lon": 126.922672,
        "desc": "젊음과 예술의 거리"
    },
    {
        "name": "인사동 🎨",
        "lat": 37.574018,
        "lon": 126.984949,
        "desc": "전통 문화와 기념품 거리"
    },
    {
        "name": "롯데월드 🎢",
        "lat": 37.511115,
        "lon": 127.098167,
        "desc": "세계적인 실내 테마파크"
    },
    {
        "name": "동대문디자인플라자(DDP) ✨",
        "lat": 37.566526,
        "lon": 127.009223,
        "desc": "미래적인 건축 디자인 명소"
    },
    {
        "name": "한강공원 🚴",
        "lat": 37.520694,
        "lon": 126.939894,
        "desc": "서울 시민들의 힐링 장소"
    },
    {
        "name": "코엑스 별마당도서관 📚",
        "lat": 37.512504,
        "lon": 127.058868,
        "desc": "SNS 인기 포토존"
    }
]

# 서울 중심 좌표
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11,
    tiles="OpenStreetMap"
)

# 마커 추가
for place in places:
    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=f"""
        <h4>{place['name']}</h4>
        <p>{place['desc']}</p>
        """,
        tooltip=place["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# 지도 출력
st_folium(m, width=1200, height=700)

# 관광지 리스트
st.subheader("📌 관광지 리스트")

for idx, place in enumerate(places, start=1):
    st.markdown(f"""
    ### {idx}. {place['name']}
    - ✨ 설명: {place['desc']}
    """)

st.success("서울 여행 준비 완료 😎✈️")
