import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 동물 추천 🐾",
    page_icon="🦊",
    layout="centered"
)

# MBTI별 동물 데이터
mbti_animals = {
    "INTJ": [
        {
            "animal": "🦉 올빼미",
            "reason": "조용하지만 엄청 똑똑하고 관찰력이 뛰어난 모습이 INTJ랑 닮았어!"
        },
        {
            "animal": "🐺 늑대",
            "reason": "독립적이고 리더십 있는 분위기가 INTJ 느낌이야 😎"
        }
    ],

    "INTP": [
        {
            "animal": "🐱 고양이",
            "reason": "혼자만의 시간을 좋아하고 자유로운 성격이 비슷해!"
        },
        {
            "animal": "🦊 여우",
            "reason": "호기심 많고 영리한 모습이 INTP랑 잘 어울려 🧠"
        }
    ],

    "ENTJ": [
        {
            "animal": "🦁 사자",
            "reason": "카리스마 넘치고 무리를 이끄는 리더 느낌이 딱 ENTJ!"
        },
        {
            "animal": "🦅 독수리",
            "reason": "멀리 보고 목표를 향해 돌진하는 모습이 닮았어 🚀"
        }
    ],

    "ENTP": [
        {
            "animal": "🐬 돌고래",
            "reason": "장난기 많고 똑똑한 성격이 ENTP랑 찰떡!"
        },
        {
            "animal": "🐒 원숭이",
            "reason": "에너지 넘치고 새로운 걸 좋아하는 모습이 비슷해 😆"
        }
    ],

    "INFJ": [
        {
            "animal": "🦌 사슴",
            "reason": "조용하고 따뜻한 분위기가 INFJ 느낌이야 🌿"
        },
        {
            "animal": "🐋 고래",
            "reason": "깊은 감성과 차분함이 INFJ와 닮았어!"
        }
    ],

    "INFP": [
        {
            "animal": "🐰 토끼",
            "reason": "감수성 풍부하고 순수한 이미지가 INFP랑 잘 어울려 🩷"
        },
        {
            "animal": "🦄 유니콘",
            "reason": "상상력 넘치고 특별한 분위기가 딱 INFP 스타일!"
        }
    ],

    "ENFJ": [
        {
            "animal": "🐶 강아지",
            "reason": "사람을 좋아하고 따뜻하게 챙겨주는 모습이 ENFJ 같아 🥰"
        },
        {
            "animal": "🐘 코끼리",
            "reason": "든든하고 믿음직한 리더 느낌이 닮았어!"
        }
    ],

    "ENFP": [
        {
            "animal": "🦜 앵무새",
            "reason": "활발하고 밝은 에너지가 ENFP랑 똑같아 🎉"
        },
        {
            "animal": "🐬 돌고래",
            "reason": "친화력 좋고 장난꾸러기 같은 매력이 비슷해 😆"
        }
    ],

    "ISTJ": [
        {
            "animal": "🐜 개미",
            "reason": "성실하고 책임감 강한 모습이 ISTJ와 닮았어!"
        },
        {
            "animal": "🐴 말",
            "reason": "묵묵하게 자기 할 일을 해내는 느낌이 비슷해 🐎"
        }
    ],

    "ISFJ": [
        {
            "animal": "🐼 판다",
            "reason": "따뜻하고 평화로운 분위기가 ISFJ 느낌이야 🖤🤍"
        },
        {
            "animal": "🐧 펭귄",
            "reason": "가족과 친구를 소중하게 생각하는 모습이 닮았어!"
        }
    ],

    "ESTJ": [
        {
            "animal": "🦅 독수리",
            "reason": "결단력 있고 강한 리더십이 ESTJ 스타일 😎"
        },
        {
            "animal": "🐯 호랑이",
            "reason": "카리스마 넘치고 추진력 강한 모습이 비슷해!"
        }
    ],

    "ESFJ": [
        {
            "animal": "🐶 리트리버",
            "reason": "친절하고 사람들과 잘 어울리는 성격이 ESFJ 같아 🩵"
        },
        {
            "animal": "🦢 백조",
            "reason": "우아하면서도 배려심 있는 모습이 닮았어!"
        }
    ],

    "ISTP": [
        {
            "animal": "🐆 치타",
            "reason": "빠르고 침착하게 움직이는 모습이 ISTP 느낌!"
        },
        {
            "animal": "🦅 매",
            "reason": "집중력 강하고 혼자서도 잘하는 모습이 비슷해 😎"
        }
    ],

    "ISFP": [
        {
            "animal": "🦋 나비",
            "reason": "감성적이고 아름다운 걸 좋아하는 ISFP와 잘 어울려!"
        },
        {
            "animal": "🐨 코알라",
            "reason": "조용하고 편안한 분위기가 닮았어 🌿"
        }
    ],

    "ESTP": [
        {
            "animal": "🐆 표범",
            "reason": "도전적이고 에너지 넘치는 모습이 ESTP 느낌!"
        },
        {
            "animal": "🐬 돌고래",
            "reason": "활발하고 모험을 좋아하는 성격이 비슷해 🌊"
        }
    ],

    "ESFP": [
        {
            "animal": "🦚 공작새",
            "reason": "화려하고 사람들의 관심 받는 걸 좋아하는 모습이 닮았어 ✨"
        },
        {
            "animal": "🐹 햄스터",
            "reason": "귀엽고 통통 튀는 매력이 ESFP랑 잘 어울려 😆"
        }
    ]
}

# 제목
st.title("✨ MBTI 동물 추천 테스트 🐾✨")
st.write("너의 MBTI랑 닮은 귀엽고 멋진 동물을 추천해줄게 😎")

# 선택창
selected_mbti = st.selectbox(
    "💡 MBTI를 골라봐!",
    list(mbti_animals.keys())
)

# 버튼
if st.button("동물 추천 받기 🐾"):

    st.success(f"{selected_mbti} 유형과 닮은 동물이야 🌈")

    animals = mbti_animals[selected_mbti]

    for idx, animal in enumerate(animals, start=1):
        st.markdown(f"## {idx}. {animal['animal']}")
        st.write(f"💖 닮은 이유 : {animal['reason']}")
        st.divider()

    st.balloons()

# 하단 문구
st.caption("📌 재미로 보는 MBTI 동물 매칭이야 😆 너무 진지하게 보진 말기!")
