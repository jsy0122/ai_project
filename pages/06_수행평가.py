import streamlit as st
import pandas as pd
import folium

from pathlib import Path
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from streamlit_folium import st_folium

st.set_page_config(
    page_title="🐶 반려동물 관광지",
    page_icon="🐾",
    layout="wide"
)

# -------------------
# 데이터 읽기
# -------------------
@st.cache_data
def load_data():

    BASE_DIR = Path(__file__).resolve().parent

    csv_path = (
        BASE_DIR /
        "인천광역시_반려동물 동반 관광지 정보 리스트_20260119(1).csv"
    )

    try:
        return pd.read_csv(
            csv_path,
            encoding="cp949"
        )
    except:
        return pd.read_csv(
            csv_path,
            encoding="euc-kr"
        )

df = load_data()

# -------------------
# 제목
# -------------------
st.title("🐶 인천 반려동물 동반 관광지")

st.write(
    "이용시설을 선택하면 해당 관광지가 지도에 표시됩니다."
)

# -------------------
# 시설 종류 선택
# -------------------
facility = st.selectbox(
    "🏷️ 이용시설 선택",
    ["전체"] +
    sorted(
        df["소구분"]
        .dropna()
        .unique()
        .tolist()
    )
)

filtered = df.copy()

if facility != "전체":
    filtered = filtered[
        filtered["소구분"] == facility
    ]

# -------------------
# 좌표 변환
# -------------------
@st.cache_data
def get_coordinates(addresses):

    geolocator = Nominatim(
        user_agent="pet_trip"
    )

    geocode = RateLimiter(
        geolocator.geocode,
        min_delay_seconds=1
    )

    coords = []

    for address in addresses:

        try:
            location = geocode(str(address))

            if location:
                coords.append(
                    (
                        location.latitude,
                        location.longitude
                    )
                )
            else:
                coords.append(
                    (None, None)
                )

        except:
            coords.append(
                (None, None)
            )

    return coords

coords = get_coordinates(
    filtered["주소"].tolist()
)

filtered["위도"] = [
    c[0] for c in coords
]

filtered["경도"] = [
    c[1] for c in coords
]

# -------------------
# 지도
# -------------------
m = folium.Map(
    location=[37.4563, 126.7052],
    zoom_start=10
)

for _, row in filtered.iterrows():

    if pd.notna(row["위도"]):

        folium.Marker(
            location=[
                row["위도"],
                row["경도"]
            ],
            popup=f"""
            <b>{row['상호']}</b><br>
            {row['주소']}
            """,
            tooltip=row["상호"]
        ).add_to(m)

st_folium(
    m,
    width=1200,
    height=600
)

# -------------------
# 관광지 선택
# -------------------
st.subheader("📍 관광지 정보")

place = st.selectbox(
    "관광지 선택",
    filtered["상호"]
)

selected = filtered[
    filtered["상호"] == place
].iloc[0]

st.info(
    f"""
📍 주소

{selected['주소']}
"""
)

st.write(
    f"⏰ 이용시간 : {selected['이용시간']}"
)

st.write(
    f"🚗 주차 : {selected['주차']}"
)

st.write(
    f"🐶 제한사항 : {selected['입장 가능 반려동물 제한사항']}"
)
