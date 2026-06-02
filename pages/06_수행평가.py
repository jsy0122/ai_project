import streamlit as st
import pandas as pd
from pathlib import Path
from urllib.parse import quote

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="🐶 인천 반려동물 관광지",
    page_icon="🐾",
    layout="wide"
)

# -----------------------------
# 데이터 읽기
# -----------------------------
@st.cache_data
def load_data():

    base_dir = Path(__file__).resolve().parent

    csv_file = (
        base_dir /
        "인천광역시_반려동물 동반 관광지 정보 리스트_20260119(1).csv"
    )

    try:
        df = pd.read_csv(
            csv_file,
            encoding="cp949"
        )

    except:
        df = pd.read_csv(
            csv_file,
            encoding="euc-kr"
        )

    return df

# -----------------------------
# 데이터 불러오기
# -----------------------------
try:
    df = load_data()

except Exception as e:

    st.error(
        f"CSV 파일을 찾을 수 없습니다.\n\n{e}"
    )

    st.stop()

# -----------------------------
# 제목
# -----------------------------
st.title("🐶 인천 반려동물 동반 관광지")

st.write(
    "관광지를 선택하면 위치와 정보를 확인할 수 있어!"
)

# -----------------------------
# 통계
# -----------------------------
c1, c2, c3 = st.columns(3)

c1.metric(
    "관광지 수",
    len(df)
)

c2.metric(
    "지역 수",
    df["지역"].nunique()
)

c3.metric(
    "시설 유형",
    df["소구분"].nunique()
)

st.divider()

# -----------------------------
# 시설 선택
# -----------------------------
facility = st.selectbox(
    "🏷️ 이용시설 선택",
    ["전체"] +
    sorted(
        df["소구분"]
        .dropna()
        .unique()
    )
)

filtered = df.copy()

if facility != "전체":

    filtered = filtered[
        filtered["소구분"] == facility
    ]

# -----------------------------
# 관광지 선택
# -----------------------------
place = st.selectbox(
    "📍 관광지 선택",
    sorted(
        filtered["상호"]
        .dropna()
        .unique()
    )
)

selected = filtered[
    filtered["상호"] == place
].iloc[0]

st.divider()

# -----------------------------
# 정보 출력
# -----------------------------
st.subheader(f"🐾 {selected['상호']}")

address = str(selected["주소"])

st.success(f"📍 주소 : {address}")

# -----------------------------
# 지도 링크
# -----------------------------
map_url = (
    "https://www.google.com/maps/search/"
    + quote(address)
)

st.link_button(
    "🗺️ 지도에서 보기",
    map_url
)

# -----------------------------
# 상세 정보
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    st.write("### ⏰ 이용 정보")

    st.write(
        f"이용시간 : {selected.get('이용시간', '-')}"
    )

    st.write(
        f"휴무일 : {selected.get('휴무', '-')}"
    )

    st.write(
        f"이용료 : {selected.get('이용료', '-')}"
    )

with col2:

    st.write("### 🐶 반려동물 정보")

    st.write(
        f"이용 가능 공간 : {selected.get('반려동물 동행시 이용 가능 공간(실내_실외)', '-')}"
    )

    st.write(
        f"입장 제한 : {selected.get('입장 가능 반려동물 제한사항', '-')}"
    )

    st.write(
        f"주차 : {selected.get('주차', '-')}"
    )

# -----------------------------
# 서비스
# -----------------------------
st.write("### 🎁 서비스")

service = selected.get(
    "반려동물용 메뉴 및 서비스 시설 내용",
    "정보 없음"
)

if pd.isna(service):
    service = "정보 없음"

st.write(service)

# -----------------------------
# 특이사항
# -----------------------------
st.write("### 📝 특이사항")

special = selected.get(
    "기타 특이사항",
    "정보 없음"
)

if pd.isna(special):
    special = "정보 없음"

st.write(special)
