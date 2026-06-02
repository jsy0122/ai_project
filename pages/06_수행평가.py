import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------
# 페이지 설정
# ---------------------
st.set_page_config(
    page_title="🐶 인천 반려동물 관광지",
    page_icon="🐾",
    layout="wide"
)

# ---------------------
# 데이터 불러오기
# ---------------------
@st.cache_data
def load_data():
    return pd.read_csv(
        "인천광역시_반려동물_관광지.csv",
        encoding="cp949"
    )

df = load_data()

# ---------------------
# 제목
# ---------------------
st.title("🐶 인천 반려동물 동반 관광지")

st.markdown(
"""
반려동물과 함께 방문할 수 있는
인천 관광지를 검색해보자!
"""
)

# ---------------------
# KPI
# ---------------------
c1, c2, c3 = st.columns(3)

c1.metric(
    "전체 관광지",
    len(df)
)

c2.metric(
    "지역 수",
    df["지역"].nunique()
)

c3.metric(
    "관광지 유형",
    df["소구분"].nunique()
)

st.divider()

# ---------------------
# 검색
# ---------------------
search = st.text_input(
    "🔍 관광지 검색"
)

region = st.selectbox(
    "지역 선택",
    ["전체"] +
    sorted(df["지역"].unique())
)

category = st.selectbox(
    "관광지 유형",
    ["전체"] +
    sorted(df["소구분"].unique())
)

space = st.selectbox(
    "실내/실외",
    ["전체"] +
    sorted(
        df["반려동물 동행시 이용 가능 공간(실내_실외)"]
        .dropna()
        .unique()
    )
)

filtered = df.copy()

if search:
    filtered = filtered[
        filtered["상호"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

if region != "전체":
    filtered = filtered[
        filtered["지역"] == region
    ]

if category != "전체":
    filtered = filtered[
        filtered["소구분"] == category
    ]

if space != "전체":
    filtered = filtered[
        filtered[
            "반려동물 동행시 이용 가능 공간(실내_실외)"
        ] == space
    ]

# ---------------------
# 결과
# ---------------------
st.subheader(
    f"검색 결과 : {len(filtered)}개"
)

st.dataframe(
    filtered[
        [
            "지역",
            "소구분",
            "상호",
            "주소"
        ]
    ],
    use_container_width=True
)

# ---------------------
# 지역별 그래프
# ---------------------
st.subheader("📊 지역별 관광지 수")

region_count = (
    filtered["지역"]
    .value_counts()
    .reset_index()
)

region_count.columns = [
    "지역",
    "개수"
]

fig = px.bar(
    region_count,
    x="지역",
    y="개수",
    text="개수"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------
# 유형별 그래프
# ---------------------
st.subheader("📈 관광지 유형 분포")

type_count = (
    filtered["소구분"]
    .value_counts()
    .reset_index()
)

type_count.columns = [
    "유형",
    "개수"
]

fig2 = px.pie(
    type_count,
    names="유형",
    values="개수"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ---------------------
# 관광지 상세 정보
# ---------------------
st.subheader("📍 관광지 상세정보")

place = st.selectbox(
    "관광지 선택",
    filtered["상호"]
)

selected = filtered[
    filtered["상호"] == place
].iloc[0]

st.markdown(
f"""
### 🐾 {selected['상호']}

**📍 주소**
- {selected['주소']}

**🏷️ 유형**
- {selected['소구분']}

**🏠 이용 가능 공간**
- {selected['반려동물 동행시 이용 가능 공간(실내_실외)']}

**🐶 입장 제한**
- {selected['입장 가능 반려동물 제한사항']}

**🕒 이용시간**
- {selected['이용시간']}

**💰 이용료**
- {selected['이용료']}

**🚗 주차**
- {selected['주차']}

**📝 특이사항**
- {selected['기타 특이사항']}
"""
)
