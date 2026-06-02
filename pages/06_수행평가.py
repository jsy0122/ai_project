import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

st.set_page_config(
    page_title="🐶 인천 반려동물 동반 관광지",
    page_icon="🐾",
    layout="wide"
)

st.title("🐶 인천 반려동물 동반 관광지 지도")
st.markdown("반려동물과 함께 갈 수 있는 인천 관광지를 찾아보자!")

uploaded_file = st.file_uploader(
    "CSV 파일 업로드",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file, encoding="cp949")
    except:
        df = pd.read_csv(uploaded_file, encoding="euc-kr")

    st.success(f"총 {len(df)}개의 관광지 데이터 로드 완료!")

    # 컬럼명 확인
    st.subheader("📋 데이터 미리보기")
    st.dataframe(df.head())

    region_col = df.columns[0]
    type_col = df.columns[1]
    name_col = df.columns[2]
    address_col = df.columns[3]

    col1, col2 = st.columns(2)

    with col1:
        selected_region = st.selectbox(
            "지역 선택",
            ["전체"] + sorted(df[region_col].dropna().unique().tolist())
        )

    with col2:
        selected_type = st.selectbox(
            "관광지 유형",
            ["전체"] + sorted(df[type_col].dropna().unique().tolist())
        )

    filtered = df.copy()

    if selected_region != "전체":
        filtered = filtered[
            filtered[region_col] == selected_region
        ]

    if selected_type != "전체":
        filtered = filtered[
            filtered[type_col] == selected_type
        ]

    st.write(f"검색 결과: {len(filtered)}개")

    geolocator = Nominatim(user_agent="pet_trip")
    geocode = RateLimiter(
        geolocator.geocode,
        min_delay_seconds=1
    )

    m = folium.Map(
        location=[37.4563, 126.7052],
        zoom_start=10
    )

    progress = st.progress(0)

    for idx, row in filtered.iterrows():

        try:
            location = geocode(str(row[address_col]))

            if location:

                popup_text = f"""
                <b>{row[name_col]}</b><br>
                유형 : {row[type_col]}<br>
                주소 : {row[address_col]}
                """

                folium.Marker(
                    [location.latitude, location.longitude],
                    popup=folium.Popup(
                        popup_text,
                        max_width=300
                    ),
                    tooltip=row[name_col]
                ).add_to(m)

        except:
            pass

        progress.progress(
            min(
                (idx + 1) / len(filtered),
                1.0
            )
        )

    st.subheader("🗺️ 관광지 지도")

    st_folium(
        m,
        width=1200,
        height=700
    )

    st.subheader("📍 관광지 목록")

    place = st.selectbox(
        "관광지 선택",
        filtered[name_col].tolist()
    )

    selected = filtered[
        filtered[name_col] == place
    ].iloc[0]

    st.markdown(f"## 🐾 {selected[name_col]}")

    for col in filtered.columns:
        value = selected[col]
        st.write(f"**{col}** : {value}")

else:
    st.info("CSV 파일을 업로드해주세요.")
