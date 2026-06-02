import streamlit as st
import pandas as pd

# -------------------------
# 페이지 설정
# -------------------------
st.set_page_config(
    page_title="🐶 인천 반려동물 관광지",
    page_icon="🐾",
    layout="wide"
)

# -------------------------
# 데이터 불러오기
# -------------------------
@st.cache_data
def load_data():
    try:
        return pd.read_csv(
           인천광역시_반려동물 동반 관광지 정보 리스트_20260119(1).csv,
            encoding="cp949"
        )
    except:
        return pd.read_csv(
            인천광역시_반려동물 동반 관광지 정보 리스트_20260119(1).csv,
            encoding="euc-kr"
        )

df = load_data()

# -------------------------
# 제목
# -------------------------
st.title("🐶 인천 반려동물 동반 관광지")
st.write("반려동물과 함께 방문할 수 있는 관광지를 찾아보자!")

# -------------------------
# 통계
# -------------------------
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("관광지 수", len(df))

with c2:
    st.metric("지역 수", df["지역"].nunique())

with c3:
    st.metric("관광지 유형", df["소구분"].nunique())

st.divider()

# -------------------------
# 지역 선택
# -------------------------
region = st.selectbox(
    "🏙️ 지역 선택",
    ["전체"] + sorted(df["지역"].dropna().unique())
)

filtered = df.copy()

if region != "전체":
    filtered = filtered[
        filtered["지역"] == region
    ]

# -------------------------
# 유형 선택
# -------------------------
category = st.selectbox(
    "🏷️ 관광지 유형",
    ["전체"] + sorted(filtered["소구분"].dropna().unique())
)

if category != "전체":
    filtered = filtered[
        filtered["소구분"] == category
    ]

# -------------------------
# 시설 선택
# -------------------------
place = st.selectbox(
    "📍 관광지 선택",
    sorted(filtered["상호"].dropna().unique())
)

selected = filtered[
    filtered["상호"] == place
].iloc[0]

st.divider()

# -------------------------
# 상세 정보
# -------------------------
st.subheader(f"🐾 {selected['상호']}")

st.info(
    f"📍 위치\n\n{selected['주소']}"
)

col1, col2 = st.columns(2)

with col1:

    st.write("### ⏰ 이용 정보")

    st.write(
        f"**이용시간** : {selected.get('이용시간', '-')}"
    )

    st.write(
        f"**휴무일** : {selected.get('휴무', '-')}"
    )

    st.write(
        f"**이용료** : {selected.get('이용료', '-')}"
    )

with col2:

    st.write("### 🐶 반려동물 정보")

    st.write(
        f"**이용 가능 공간** : {selected.get('반려동물 동행시 이용 가능 공간(실내_실외)', '-')}"
    )

    st.write(
        f"**입장 제한사항** : {selected.get('입장 가능 반려동물 제한사항', '-')}"
    )

    st.write(
        f"**주차 여부** : {selected.get('주차', '-')}"
    )

# -------------------------
# 서비스 정보
# -------------------------
st.write("### 🎁 반려동물 서비스")

service = selected.get(
    "반려동물용 메뉴 및 서비스 시설 내용",
    "-"
)

if pd.isna(service):
    service = "제공 정보 없음"

st.write(service)

# -------------------------
# 특이사항
# -------------------------
st.write("### 📝 특이사항")

special = selected.get(
    "기타 특이사항",
    "-"
)

if pd.isna(special):
    special = "등록된 정보 없음"

st.write(special)

# -------------------------
# 주소 복사
# -------------------------
st.code(
    selected["주소"],
    language=None
)
