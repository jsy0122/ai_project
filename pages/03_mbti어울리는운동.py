```python id="mbti_sports_double"
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 운동 추천 💪",
    page_icon="🏃",
    layout="centered"
)

# MBTI 운동 데이터
mbti_sports = {

    "INTJ": [
        {
            "sport": "🏹 양궁",
            "reason": "집중력 높고 차분하게 목표를 노리는 모습이 INTJ랑 완전 닮았어!"
        },
        {
            "sport": "♟️ 체스",
            "reason": "전략적으로 생각하고 계획 세우는 걸 좋아하는 INTJ 스타일 😎"
        }
    ],

    "INTP": [
        {
            "sport": "🚴 자전거",
            "reason": "혼자 자유롭게 즐길 수 있어서 INTP랑 잘 어울려!"
        },
        {
            "sport": "🧗 클라이밍",
            "reason": "문제 해결하듯 코스를 공략하는 재미가 INTP 취향이야 🧠"
        }
    ],

    "ENTJ": [
        {
            "sport": "🏀 농구",
            "reason": "리더십 강하고 팀을 이끄는 ENTJ의 매력이 잘 드러나는 운동!"
        },
        {
            "sport": "🥋 태권도",
            "reason": "목표를 향해 꾸준히 성장하는 ENTJ 스타일과 찰떡 💥"
        }
    ],

    "ENTP": [
        {
            "sport": "🏄 서핑",
            "reason": "새로운 도전과 자유로운 분위기를 좋아하는 ENTP 느낌 🌊"
        },
        {
            "sport": "🎾 테니스",
            "reason": "순발력과 재치 있는 플레이가 ENTP랑 잘 맞아 😆"
        }
    ],

    "INFJ": [
        {
            "sport": "🧘 요가",
            "reason": "차분하고 마음의 안정 중요하게 생각하는 INFJ에게 추천!"
        },
        {
            "sport": "🏊 수영",
            "reason": "조용한 분위기 속에서 혼자 집중할 수 있어서 잘 어울려 🌿"
        }
    ],

    "INFP": [
        {
            "sport": "⛸️ 피겨스케이팅",
            "reason": "감성적이고 표현력 풍부한 INFP와 잘 어울리는 운동!"
        },
        {
            "sport": "💃 댄스",
            "reason": "자신만의 감정을 자유롭게 표현할 수 있어서 딱이야 🎶"
        }
    ],

    "ENFJ": [
        {
            "sport": "⚽ 축구",
            "reason": "팀워크를 중요하게 생각하는 ENFJ와 완전 잘 맞아!"
        },
        {
            "sport": "🏐 배구",
            "reason": "사람들과 함께 호흡 맞추는 걸 좋아하는 성격이 닮았어 😊"
        }
    ],

    "ENFP": [
        {
            "sport": "💃 댄스 스포츠",
            "reason": "에너지 넘치고 분위기 메이커인 ENFP 느낌 그 자체 🎉"
        },
        {
            "sport": "🏄 스케이트보드",
            "reason": "자유롭고 개성 넘치는 스타일이 ENFP랑 찰떡!"
        }
    ],

    "ISTJ": [
        {
            "sport": "🏃 마라톤",
            "reason": "꾸준함과 성실함이 중요한 운동이라 ISTJ랑 잘 맞아!"
        },
        {
            "sport": "🏸 배드민턴",
            "reason": "규칙적으로 연습하며 실력 늘리는 재미가 있어 😎"
        }
    ],

    "ISFJ": [
        {
            "sport": "🏸 배드민턴",
            "reason": "부담 없이 친구들과 즐기기 좋아서 ISFJ에게 추천!"
        },
        {
            "sport": "🚶 걷기 운동",
            "reason": "편안하고 안정적인 활동을 좋아하는 ISFJ 스타일 🌼"
        }
    ],

    "ESTJ": [
        {
            "sport": "🥋 태권도",
            "reason": "규칙과 목표가 뚜렷한 운동이라 ESTJ와 잘 어울려!"
        },
        {
            "sport": "🏋️ 헬스",
            "reason": "계획 세우고 꾸준히 성장하는 모습이 ESTJ 느낌 💪"
        }
    ],

    "ESFJ": [
        {
            "sport": "🏐 배구",
            "reason": "친화력 좋고 팀 분위기를 살리는 ESFJ와 찰떡!"
        },
        {
            "sport": "🕺 줌바댄스",
            "reason": "사람들과 신나게 어울리는 걸 좋아하는 성격과 잘 맞아 🎵"
        }
    ],

    "ISTP": [
        {
            "sport": "🚴 자전거",
            "reason": "혼자 자유롭게 즐길 수 있어서 ISTP 스타일 😎"
        },
        {
            "sport": "🥊 복싱",
            "reason": "순간 판단력과 집중력이 필요한 운동이라 잘 어울려!"
        }
    ],

    "ISFP": [
        {
            "sport": "🏊 수영",
            "reason": "조용하고 편안한 분위기 속에서 즐길 수 있어 🌊"
        },
        {
            "sport": "🧘 필라테스",
            "reason": "감성적이고 섬세한 ISFP에게 잘 맞는 운동이야 ✨"
        }
    ],

    "ESTP": [
        {
            "sport": "🥊 복싱",
            "reason": "에너지 넘치고 스릴을 좋아하는 ESTP 스타일 💥"
        },
        {
            "sport": "🏂 스노보드",
            "reason": "도전적이고 활동적인 성격과 완전 잘 어울려 ❄️"
        }
    ],

    "ESFP": [
        {
            "sport": "🎾 테니스",
            "reason": "밝고 활발한 ESFP의 매력을 보여주기 좋은 운동!"
        },
        {
            "sport": "💃 댄스",
            "reason": "끼 많고 에너지 넘치는 성격과 찰떡 🎉"
        }
    ]
}

# 제목
st.title("✨ MBTI 운동 추천 서비스 💪✨")
st.write("너의 MBTI에 어울리는 운동 2개를 추천해줄게 😆")

# MBTI 선택
selected_mbti = st.selectbox(
    "💡 MBTI를 골라봐!",
    list(mbti_sports.keys())
)

# 버튼
if st.button("운동 추천 받기 🚀"):

    st.success(f"{selected_mbti} 유형에게 잘 어울리는 운동이야 🌈")

    sports = mbti_sports[selected_mbti]

    for idx, item in enumerate(sports, start=1):
        st.markdown(f"## {idx}. {item['sport']}")
        st.write(f"💖 추천 이유 : {item['reason']}")
        st.divider()

    st.balloons()

# 하단 문구
st.caption("📌 재미로 보는 MBTI 운동 추천이야 😎 가볍게 즐겨줘!")
```
