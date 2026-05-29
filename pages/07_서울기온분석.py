# app.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np

# -----------------------------------
# 제목
# -----------------------------------
st.title("🌡️ 날짜별 기온 분석")

st.write("월과 일을 선택하면 연도별 최고기온과 최저기온을 확인할 수 있어!")

# -----------------------------------
# 데이터 불러오기
# -----------------------------------
df = pd.read_csv(
    "seoul.csv",
    encoding='cp949'
)

# 컬럼명 변경
df.columns = [
    '날짜',
    '지점',
    '평균기온',
    '최저기온',
    '최고기온'
]

# -----------------------------------
# 날짜 변환
# -----------------------------------
df['날짜'] = pd.to_datetime(
    df['날짜'],
    errors='coerce'
)

df = df.dropna(subset=['날짜'])

# -----------------------------------
# 연/월/일 생성
# -----------------------------------
df['연도'] = df['날짜'].dt.year
df['월'] = df['날짜'].dt.month
df['일'] = df['날짜'].dt.day

# -----------------------------------
# 사용자 선택
# -----------------------------------
month = st.selectbox(
    "📅 월 선택",
    range(1, 13)
)

day = st.selectbox(
    "📌 일 선택",
    range(1, 32)
)

# -----------------------------------
# 미래 연도 선택
# -----------------------------------
future_year = st.number_input(
    "🔮 미래 연도 선택",
    min_value=2026,
    max_value=2100,
    value=2030
)

# -----------------------------------
# 데이터 필터링
# -----------------------------------
filtered = df[
    (df['월'] == month) &
    (df['일'] == day)
]

filtered = filtered.dropna(
    subset=['최고기온', '최저기온']
)

# -----------------------------------
# 그래프 출력
# -----------------------------------
if not filtered.empty:

    # -----------------------------------
    # 예측 모델
    # -----------------------------------
    X = filtered[['연도']]

    # 최고기온 모델
    y_max = filtered['최고기온']
    model_max = LinearRegression()
    model_max.fit(X, y_max)

    # 최저기온 모델
    y_min = filtered['최저기온']
    model_min = LinearRegression()
    model_min.fit(X, y_min)

    # 미래 예측
    future_X = np.array([[future_year]])

    predicted_max = model_max.predict(future_X)[0]
    predicted_min = model_min.predict(future_X)[0]

    # -----------------------------------
    # Plotly 그래프
    # -----------------------------------
    fig = go.Figure()

    # 최고기온
    fig.add_trace(
        go.Scatter(
            x=filtered['연도'],
            y=filtered['최고기온'],
            mode='lines+markers',
            name='최고기온',
            line=dict(color='red', width=3),
            hovertemplate=
            '연도: %{x}<br>최고기온: %{y:.1f}℃<extra></extra>'
        )
    )

    # 최저기온
    fig.add_trace(
        go.Scatter(
            x=filtered['연도'],
            y=filtered['최저기온'],
            mode='lines+markers',
            name='최저기온',
            line=dict(color='blue', width=3),
            hovertemplate=
            '연도: %{x}<br>최저기온: %{y:.1f}℃<extra></extra>'
        )
    )

    # 미래 최고기온 예측
    fig.add_trace(
        go.Scatter(
            x=[future_year],
            y=[predicted_max],
            mode='markers',
            name='예측 최고기온',
            marker=dict(
                color='darkred',
                size=12
            ),
            hovertemplate=
            '예측연도: %{x}<br>예측 최고기온: %{y:.1f}℃<extra></extra>'
        )
    )

    # 미래 최저기온 예측
    fig.add_trace(
        go.Scatter(
            x=[future_year],
            y=[predicted_min],
            mode='markers',
            name='예측 최저기온',
            marker=dict(
                color='darkblue',
                size=12
            ),
            hovertemplate=
            '예측연도: %{x}<br>예측 최저기온: %{y:.1f}℃<extra></extra>'
        )
    )

    # -----------------------------------
    # 그래프 설정
    # -----------------------------------
    fig.update_layout(
        title="날짜별 기온 분석",
        xaxis_title="연도",
        yaxis_title="온도(℃)",
        hovermode='x unified',
        height=600
    )

    # 출력
    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # -----------------------------------
    # 예측 결과 출력
    # -----------------------------------
    st.subheader(f"🔮 {future_year}년 예측 결과")

    st.write(
        f"🔥 예상 최고기온: {predicted_max:.1f}℃"
    )

    st.write(
        f"❄️ 예상 최저기온: {predicted_min:.1f}℃"
    )

else:
    st.warning("해당 날짜 데이터가 없어!")
