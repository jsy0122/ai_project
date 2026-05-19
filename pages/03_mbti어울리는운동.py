```python id="mbti_sports_match"
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 운동 추천 🏃",
    page_icon="💪",
    layout="centered"
)

# MBTI별 운동 데이터
mbti_sports = {
    "INTJ": {
        "sport": "🏹 양궁",
        "reason": "집중력 높고 차분하게 목표를 노리는 INTJ랑 완전 잘 어울려!"
    },

    "INTP": {
        "sport": "♟️ 체스 스포츠",
        "reason": "전략 세우고 깊게 생각하는 걸 좋아하는 INTP 스타일 😎"
    },

    "ENTJ": {
        "sport": "🏀 농구",
        "reason": "리더십 강하고 팀을 이끄는 ENTJ의 매력이 잘 드러나는 운동이야!"
    },

    "ENTP": {
        "sport": "🏄 서핑",
        "reason": "새로운 도전과 자유로운 분위기를 좋아하는 ENTP랑 찰떡 🌊"
    },

    "INFJ": {
        "sport": "🧘 요가",
        "reason": "차분하고 마음의 안정 중요하게 생각하는 INFJ에게 추천!"
    },

    "INFP": {
        "sport": "🎨 피겨스케이팅",
        "reason": "감성적이고 표현력이 풍부한 INFP랑 잘 어울려 ⛸️"
    },

    "ENFJ": {
        "sport": "⚽ 축구",
        "reason": "사람들과 함께하는 걸 좋아하고 팀워크 잘하는 ENFJ 느낌!"
    },

    "ENFP": {
        "sport": "💃 댄스 스포츠",
        "reason": "에너지 넘치고 끼 많은 ENFP에게 딱 어울리는 운동 🎶"
    },

    "ISTJ": {
        "sport": "🏃 마라톤",
        "reason": "꾸준하고 성실하게 목표를 향해 가는 ISTJ 스타일!"
    },

    "ISFJ": {
        "sport": "🏸 배드민턴",
        "reason": "부담 없이 사람들과 즐길 수 있어서 ISFJ에게 잘 맞아 😊"
    },

    "ESTJ": {
        "sport": "🥋 태권도",
        "reason": "책임감 있고 규칙적인 ESTJ와 잘 어울리는 운동이야!"
    },

    "ESFJ": {
        "sport": "🏐 배구",
        "reason": "친화력 좋고 팀 분위기 살리는 ESFJ랑 찰떡!"
    },

    "ISTP": {
        "sport": "🚴 자전거",
        "reason": "혼자서 자유롭게 즐길 수 있는 활동을 좋아하는 ISTP 스타일 😎"
    },

    "ISFP": {
        "sport": "🏊 수영",
        "reason": "조용하고 편안한 분위기에서 즐길 수 있어서 잘 어울려 🌊"
    },

    "ESTP": {
        "sport": "🥊 복싱",
        "reason": "에너지 넘치고 스릴 좋아하는 ESTP에게 완전 추천!"
    },

    "ESFP": {
        "sport": "🎾 테니스",
        "reason": "활발하고 밝은 ESFP의 매력을 보여주기 좋은 운동 🎉"
    }
}

# 제목
st.title("✨ MBTI 운동 추천 서비스 💪✨")
st.write("너의 MBTI에 딱 어울리는 운동을 추천해줄게 😆")

# 선택창
selected_mbti = st.selectbox(
    "💡 너의 MBTI를 선택해봐!",
    list(mbti_sports.keys())
)

# 버튼
if st.button("운동 추천 받기 🚀"):

    data = mbti_sports[selected_mbti]

    st.success(f"{selected_mbti} 유형에게 잘 어울리는 운동이야 🌈")

    st.markdown(f"# {data['sport']}")
    st.write(f"💖 추천 이유 : {data['reason']}")

    st.balloons()

# 하단 문구
st.caption("📌 재미로 보는 MBTI 운동 추천이야 😎 가볍게 즐겨줘!")
```
