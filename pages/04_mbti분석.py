# app.py

import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# ------------------------------------------------
# 페이지 설정
# ------------------------------------------------
st.set_page_config(
    page_title="🌍 MBTI 국가 분석",
    page_icon="🌎",
    layout="wide"
)

# ------------------------------------------------
# MBTI 한글 번역
# ------------------------------------------------
mbti_kr = {
    "INTJ": "전략가 INTJ",
    "INTP": "논리술사 INTP",
    "ENTJ": "통솔자 ENTJ",
    "ENTP": "변론가 ENTP",
    "INFJ": "옹호자 INFJ",
    "INFP": "중재자 INFP",
    "ENFJ": "선도자 ENFJ",
    "ENFP": "활동가 ENFP",
    "ISTJ": "현실주의자 ISTJ",
    "ISFJ": "수호자 ISFJ",
    "ESTJ": "경영자 ESTJ",
    "ESFJ": "집정관 ESFJ",
    "ISTP": "장인 ISTP",
    "ISFP": "모험가 ISFP",
    "ESTP": "사업가 ESTP",
    "ESFP": "연예인 ESFP"
}

# ------------------------------------------------
# 국가 한글 번역
# ------------------------------------------------
country_kr = {
    "South Korea": "대한민국",
    "Japan": "일본",
    "China": "중국",
    "United States": "미국",
    "Canada": "캐나다",
    "France": "프랑스",
    "Germany": "독일",
    "Italy": "이탈리아",
    "Spain": "스페인",
    "Brazil": "브라질",
    "India": "인도",
    "Australia": "호주",
    "Russia": "러시아",
    "United Kingdom": "영국",
    "Mexico": "멕시코",
    "Portugal": "포르투갈",
    "Chile": "칠레",
    "Cuba": "쿠바",
    "Iceland": "아이슬란드",
    "Nigeria": "나이지리아",
    "Ghana": "가나",
    "Rwanda": "르완다",
    "Nicaragua": "니카라과",
    "Maldives": "몰디브"
}

# ------------------------------------------------
# 데이터 로드
# ------------------------------------------------
@st.cache_data
def load_data():

    df = pd.read_csv("countriesMBTI_16types.csv")

    # 국가 한글화
    df["Country_KR"] = df["Country"].apply(
        lambda x: country_kr[x] if x in country_kr else x
    )

    return df


df = load_data()

# ------------------------------------------------
# MBTI 컬럼
# ------------------------------------------------
mbti_columns = [
    col for col in df.columns
    if col not in ["Country", "Country_KR"]
]

# ------------------------------------------------
# 제목
# ------------------------------------------------
st.title("🌍 세계 국가 MBTI 분석")
st.markdown(
    """
    ### 국가별 MBTI 비율과 유형별 TOP 국가를 확인해봐! ✨
    """
)

# ------------------------------------------------
# 탭 생성
# ------------------------------------------------
tab1, tab2 = st.tabs([
    "📊 국가별 MBTI 분석",
    "🏆 MBTI TOP 10 국가"
])

# ==========================================================
# TAB 1
# ==========================================================
with tab1:

    st.subheader("🌎 국가별 MBTI 비율")

    # 가나다순 정렬
    countries_kr = sorted(df["Country_KR"].unique())

    selected_country = st.selectbox(
        "국가를 선택해줘!",
        countries_kr
    )

    # 선택 국가
    selected_row = df[
        df["Country_KR"] == selected_country
    ].iloc[0]

    # 데이터 생성
    mbti_df = pd.DataFrame({
        "MBTI": mbti_columns,
        "비율": [
            selected_row[col] * 100
            for col in mbti_columns
        ]
    })

    # 한글 MBTI 추가
    mbti_df["MBTI_KR"] = mbti_df["MBTI"].map(mbti_kr)

    # 정렬
    mbti_df = mbti_df.sort_values(
        by="비율",
        ascending=False
    ).reset_index(drop=True)

    # ------------------------------------------------
    # 색상 설정
    # ------------------------------------------------
    top_value = mbti_df["비율"].max()

    top_color = "#F4B400"

    green_scale = px.colors.sequential.Greens

    colors = []

    for value in mbti_df["비율"]:

        if value == top_value:
            colors.append(top_color)

        else:
            normalized = value / top_value

            idx = int(
                normalized * (len(green_scale) - 1)
            )

            colors.append(green_scale[idx])

    # ------------------------------------------------
    # 그래프
    # ------------------------------------------------
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=mbti_df["MBTI_KR"],
            y=mbti_df["비율"],
            marker_color=colors,
            text=mbti_df["비율"].round(1).astype(str) + "%",
            textposition="outside",
            hovertemplate=
            "<b>%{x}</b><br>" +
            "비율: %{y:.2f}%<extra></extra>"
        )
    )

    fig.update_layout(
        title=f"📊 {selected_country} MBTI 비율",
        template="plotly_white",
        height=700,
        xaxis_title="MBTI 유형",
        yaxis_title="비율 (%)",
        font=dict(size=15),
        title_font=dict(size=28)
    )

    # 최고 MBTI
    top_mbti = mbti_df.iloc[0]["MBTI_KR"]
    top_percent = mbti_df.iloc[0]["비율"]

    st.success(
        f"🏆 {selected_country}에서 가장 많은 MBTI는 "
        f"**{top_mbti}** ({top_percent:.1f}%) 이야!"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================================
# TAB 2
# ==========================================================
with tab2:

    st.subheader("🏆 MBTI 유형별 TOP 10 국가")

    # 한글 선택용 리스트
    mbti_options = [
        mbti_kr[m] for m in mbti_columns
    ]

    selected_mbti_kr = st.selectbox(
        "MBTI를 선택해줘!",
        mbti_options
    )

    # 영어 MBTI 찾기
    reverse_mbti = {
        v: k for k, v in mbti_kr.items()
    }

    selected_mbti = reverse_mbti[selected_mbti_kr]

    # TOP10 데이터
    top10_df = df[[
        "Country_KR",
        selected_mbti
    ]].copy()

    top10_df["비율"] = top10_df[selected_mbti] * 100

    top10_df = top10_df.sort_values(
        by="비율",
        ascending=False
    ).head(10)

    # ------------------------------------------------
    # 색상
    # ------------------------------------------------
    top_value = top10_df["비율"].max()

    top_color = "#F4B400"

    green_scale = px.colors.sequential.Greens

    colors = []

    for value in top10_df["비율"]:

        if value == top_value:
            colors.append(top_color)

        else:
            normalized = value / top_value

            idx = int(
                normalized * (len(green_scale) - 1)
            )

            colors.append(green_scale[idx])

    # ------------------------------------------------
    # 세로 그래프
    # ------------------------------------------------
    fig2 = go.Figure()

    fig2.add_trace(
        go.Bar(
            x=top10_df["Country_KR"],
            y=top10_df["비율"],
            marker_color=colors,
            text=top10_df["비율"].round(1).astype(str) + "%",
            textposition="outside",
            hovertemplate=
            "<b>%{x}</b><br>" +
            "비율: %{y:.2f}%<extra></extra>"
        )
    )

    fig2.update_layout(
        title=f"🌟 {selected_mbti_kr} 비율 TOP 10 국가",
        template="plotly_white",
        height=700,
        xaxis_title="국가",
        yaxis_title="비율 (%)",
        font=dict(size=15),
        title_font=dict(size=28)
    )

    # 1위 국가
    best_country = top10_df.iloc[0]["Country_KR"]
    best_percent = top10_df.iloc[0]["비율"]

    st.info(
        f"🔥 {selected_mbti_kr} 비율이 가장 높은 나라는 "
        f"**{best_country}** ({best_percent:.1f}%) 이야!"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # 데이터 테이블
    with st.expander("📋 TOP10 데이터 보기"):
        st.dataframe(
            top10_df[["Country_KR", "비율"]],
            use_container_width=True
        )
        # ------------------------------------------------
# 국가 영어 -> 한국어 전체 번역 추가
# ------------------------------------------------
country_kr = {

    "Afghanistan": "아프가니스탄",
    "Albania": "알바니아",
    "Algeria": "알제리",
    "Andorra": "안도라",
    "Angola": "앙골라",
    "Argentina": "아르헨티나",
    "Armenia": "아르메니아",
    "Australia": "호주",
    "Austria": "오스트리아",
    "Azerbaijan": "아제르바이잔",

    "Bahamas": "바하마",
    "Bahrain": "바레인",
    "Bangladesh": "방글라데시",
    "Belarus": "벨라루스",
    "Belgium": "벨기에",
    "Belize": "벨리즈",
    "Benin": "베냉",
    "Bhutan": "부탄",
    "Bolivia": "볼리비아",
    "Bosnia and Herzegovina": "보스니아 헤르체고비나",
    "Botswana": "보츠와나",
    "Brazil": "브라질",
    "Brunei": "브루나이",
    "Bulgaria": "불가리아",
    "Burkina Faso": "부르키나파소",
    "Burundi": "부룬디",

    "Cambodia": "캄보디아",
    "Cameroon": "카메룬",
    "Canada": "캐나다",
    "Chile": "칠레",
    "China": "중국",
    "Colombia": "콜롬비아",
    "Costa Rica": "코스타리카",
    "Croatia": "크로아티아",
    "Cuba": "쿠바",
    "Cyprus": "키프로스",
    "Czech Republic": "체코",

    "Denmark": "덴마크",
    "Dominican Republic": "도미니카 공화국",

    "Ecuador": "에콰도르",
    "Egypt": "이집트",
    "El Salvador": "엘살바도르",
    "Estonia": "에스토니아",
    "Ethiopia": "에티오피아",

    "Faroe Islands": "페로제도",
    "Finland": "핀란드",
    "France": "프랑스",

    "Georgia": "조지아",
    "Germany": "독일",
    "Ghana": "가나",
    "Greece": "그리스",
    "Greenland": "그린란드",
    "Guatemala": "과테말라",

    "Haiti": "아이티",
    "Honduras": "온두라스",
    "Hungary": "헝가리",

    "Iceland": "아이슬란드",
    "India": "인도",
    "Indonesia": "인도네시아",
    "Iran": "이란",
    "Iraq": "이라크",
    "Ireland": "아일랜드",
    "Israel": "이스라엘",
    "Italy": "이탈리아",

    "Jamaica": "자메이카",
    "Japan": "일본",
    "Jordan": "요르단",

    "Kazakhstan": "카자흐스탄",
    "Kenya": "케냐",
    "Kuwait": "쿠웨이트",
    "Kyrgyzstan": "키르기스스탄",

    "Laos": "라오스",
    "Latvia": "라트비아",
    "Lebanon": "레바논",
    "Libya": "리비아",
    "Lithuania": "리투아니아",
    "Luxembourg": "룩셈부르크",

    "Madagascar": "마다가스카르",
    "Malaysia": "말레이시아",
    "Maldives": "몰디브",
    "Mali": "말리",
    "Mexico": "멕시코",
    "Mongolia": "몽골",
    "Morocco": "모로코",
    "Myanmar": "미얀마",

    "Nepal": "네팔",
    "Netherlands": "네덜란드",
    "New Zealand": "뉴질랜드",
    "Nicaragua": "니카라과",
    "Nigeria": "나이지리아",
    "North Korea": "북한",
    "Norway": "노르웨이",

    "Pakistan": "파키스탄",
    "Panama": "파나마",
    "Paraguay": "파라과이",
    "Peru": "페루",
    "Philippines": "필리핀",
    "Poland": "폴란드",
    "Portugal": "포르투갈",

    "Qatar": "카타르",

    "Romania": "루마니아",
    "Russia": "러시아",
    "Rwanda": "르완다",

    "Saudi Arabia": "사우디아라비아",
    "Senegal": "세네갈",
    "Serbia": "세르비아",
    "Singapore": "싱가포르",
    "Slovakia": "슬로바키아",
    "Slovenia": "슬로베니아",
    "Somalia": "소말리아",
    "South Africa": "남아프리카공화국",
    "South Korea": "대한민국",
    "Spain": "스페인",
    "Sri Lanka": "스리랑카",
    "Sudan": "수단",
    "Sweden": "스웨덴",
    "Switzerland": "스위스",
    "Syria": "시리아",

    "Taiwan": "대만",
    "Tajikistan": "타지키스탄",
    "Thailand": "태국",
    "Tunisia": "튀니지",
    "Turkey": "튀르키예",

    "Ukraine": "우크라이나",
    "United Arab Emirates": "아랍에미리트",
    "United Kingdom": "영국",
    "United States": "미국",
    "Uruguay": "우루과이",
    "Uzbekistan": "우즈베키스탄",

    "Venezuela": "베네수엘라",
    "Vietnam": "베트남",

    "Yemen": "예멘",

    "Zambia": "잠비아",
    "Zimbabwe": "짐바브웨"
}
