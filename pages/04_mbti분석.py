# app.py

import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# -----------------------------------
# 페이지 설정
# -----------------------------------
st.set_page_config(
    page_title="🌍 MBTI 국가 분석",
    page_icon="🌎",
    layout="wide"
)

# -----------------------------------
# 한국어 국가명 매핑
# -----------------------------------
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
}

# -----------------------------------
# 데이터 불러오기
# -----------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")

    # 한국어 컬럼 추가
    df["Country_KR"] = df["Country"].apply(
        lambda x: country_kr[x] if x in country_kr else x
    )

    return df

df = load_data()

# -----------------------------------
# MBTI 컬럼
# -----------------------------------
mbti_columns = [col for col in df.columns if col not in ["Country", "Country_KR"]]

# -----------------------------------
# 제목
# -----------------------------------
st.title("🌍 국가별 MBTI 분석 대시보드")
st.markdown(
    """
    ### 원하는 기능을 골라서 MBTI 데이터를 탐험해봐! ✨
    """
)

# -----------------------------------
# 탭 생성
# -----------------------------------
tab1, tab2 = st.tabs([
    "📊 국가별 MBTI 비율",
    "🏆 MBTI TOP 10 국가"
])

# =====================================================
# TAB 1
# =====================================================
with tab1:

    st.subheader("🌎 국가 선택 분석")

    # 가나다순 정렬
    countries_kr = sorted(df["Country_KR"].unique())

    selected_country_kr = st.selectbox(
        "국가를 선택해줘!",
        countries_kr
    )

    # 영어 국가명 찾기
    selected_row = df[df["Country_KR"] == selected_country_kr].iloc[0]

    # 데이터 생성
    mbti_df = pd.DataFrame({
        "MBTI": mbti_columns,
        "Ratio": [selected_row[col] for col in mbti_columns]
    })

    mbti_df["Percent"] = mbti_df["Ratio"] * 100

    mbti_df = mbti_df.sort_values(
        by="Percent",
        ascending=False
    ).reset_index(drop=True)

    # ----------------------------
    # 색상
    # ----------------------------
    top_value = mbti_df["Percent"].max()

    top_color = "#F4B400"

    green_scale = px.colors.sequential.Greens

    colors = []

    for value in mbti_df["Percent"]:

        if value == top_value:
            colors.append(top_color)

        else:
            normalized = value / top_value

            idx = int(
                normalized * (len(green_scale) - 1)
            )

            colors.append(green_scale[idx])

    # ----------------------------
    # 그래프
    # ----------------------------
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=mbti_df["MBTI"],
            y=mbti_df["Percent"],
            marker_color=colors,
            text=mbti_df["Percent"].round(1).astype(str) + "%",
            textposition="outside",
            hovertemplate=
            "<b>%{x}</b><br>" +
            "비율: %{y:.2f}%<extra></extra>"
        )
    )

    fig.update_layout(
        title=f"📊 {selected_country_kr} MBTI 비율",
        template="plotly_white",
        height=650,
        xaxis_title="MBTI 유형",
        yaxis_title="비율 (%)",
        font=dict(size=16),
        title_font=dict(size=26)
    )

    st.success(
        f"🏆 {selected_country_kr}에서 가장 높은 MBTI는 "
        f"**{mbti_df.iloc[0]['MBTI']}** 이야!"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================================
# TAB 2
# =====================================================
with tab2:

    st.subheader("🏆 MBTI 유형별 TOP 10 국가")

    selected_mbti = st.selectbox(
        "MBTI를 선택해줘!",
        mbti_columns
    )

    # TOP10 국가
    top10_df = df[["Country_KR", selected_mbti]].copy()

    top10_df["Percent"] = top10_df[selected_mbti] * 100

    top10_df = top10_df.sort_values(
        by="Percent",
        ascending=False
    ).head(10)

    top10_df = top10_df.sort_values(
        by="Percent",
        ascending=True
    )

    # ----------------------------
    # 색상
    # ----------------------------
    top_value = top10_df["Percent"].max()

    top_color = "#F4B400"

    green_scale = px.colors.sequential.Greens

    colors = []

    for value in top10_df["Percent"]:

        if value == top_value:
            colors.append(top_color)

        else:
            normalized = value / top_value

            idx = int(
                normalized * (len(green_scale) - 1)
            )

            colors.append(green_scale[idx])

    # ----------------------------
    # 그래프
    # ----------------------------
    fig2 = go.Figure()

    fig2.add_trace(
        go.Bar(
            x=top10_df["Percent"],
            y=top10_df["Country_KR"],
            orientation="h",
            marker_color=colors,
            text=top10_df["Percent"].round(1).astype(str) + "%",
            textposition="outside",
            hovertemplate=
            "<b>%{y}</b><br>" +
            "비율: %{x:.2f}%<extra></extra>"
        )
    )

    fig2.update_layout(
        title=f"🌟 {selected_mbti} 비율 TOP 10 국가",
        template="plotly_white",
        height=700,
        xaxis_title="비율 (%)",
        yaxis_title="국가",
        font=dict(size=16),
        title_font=dict(size=26)
    )

    st.info(
        f"🔥 {selected_mbti} 비율이 가장 높은 나라는 "
        f"**{top10_df.iloc[-1]['Country_KR']}** 이야!"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # 데이터 보기
    with st.expander("📋 TOP10 데이터 보기"):
        st.dataframe(
            top10_df,
            use_container_width=True
        )
