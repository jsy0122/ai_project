# app.py

import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="🌍 Countries MBTI Dashboard",
    page_icon="🌎",
    layout="wide"
)

# -----------------------------
# 제목
# -----------------------------
st.title("🌍 국가별 MBTI 비율 분석")
st.markdown(
    """
    나라를 선택하면 각 MBTI 유형의 비율을 인터랙티브한 그래프로 보여줘! ✨
    """
)

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# -----------------------------
# 국가 선택
# -----------------------------
countries = sorted(df["Country"].unique())

selected_country = st.selectbox(
    "🌎 국가를 선택해줘!",
    countries
)

# -----------------------------
# 선택한 국가 데이터
# -----------------------------
country_data = df[df["Country"] == selected_country].iloc[0]

mbti_columns = [col for col in df.columns if col != "Country"]

mbti_df = pd.DataFrame({
    "MBTI": mbti_columns,
    "Ratio": [country_data[col] for col in mbti_columns]
})

# 퍼센트 변환
mbti_df["Percent"] = mbti_df["Ratio"] * 100

# 내림차순 정렬
mbti_df = mbti_df.sort_values(
    by="Percent",
    ascending=False
).reset_index(drop=True)

# -----------------------------
# 색상 설정
# -----------------------------
top_value = mbti_df["Percent"].max()

# 1등 색상 (진한 노란색)
top_color = "#F4B400"

# 초록 그라데이션 생성
green_scale = px.colors.sequential.Greens

colors = []

for value in mbti_df["Percent"]:
    if value == top_value:
        colors.append(top_color)
    else:
        normalized = value / top_value

        # 초록 그라데이션 index 계산
        idx = int(normalized * (len(green_scale) - 1))
        colors.append(green_scale[idx])

# -----------------------------
# 그래프 생성
# -----------------------------
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

# -----------------------------
# 그래프 꾸미기
# -----------------------------
fig.update_layout(
    title=f"📊 {selected_country} MBTI 비율",
    xaxis_title="MBTI 유형",
    yaxis_title="비율 (%)",
    template="plotly_white",
    height=650,
    font=dict(
        size=16
    ),
    title_font=dict(
        size=26
    ),
    hoverlabel=dict(
        font_size=16
    ),
    margin=dict(
        l=30,
        r=30,
        t=80,
        b=30
    )
)

fig.update_traces(
    marker_line_width=1.5,
    marker_line_color="white"
)

# -----------------------------
# 최고 MBTI 표시
# -----------------------------
top_mbti = mbti_df.iloc[0]["MBTI"]
top_percent = mbti_df.iloc[0]["Percent"]

st.success(
    f"🏆 {selected_country}에서 가장 높은 MBTI는 "
    f"**{top_mbti}** ({top_percent:.1f}%) 이야!"
)

# -----------------------------
# 그래프 출력
# -----------------------------
st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# 데이터 테이블
# -----------------------------
with st.expander("📋 데이터 보기"):
    st.dataframe(
        mbti_df,
        use_container_width=True
    )
