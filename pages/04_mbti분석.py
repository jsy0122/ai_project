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
