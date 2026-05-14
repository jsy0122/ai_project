import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 책 & 영화 추천 🎬📚",
    page_icon="✨",
    layout="centered"
)

# 데이터
mbti_contents = {
    "INTJ": {
        "book": {
            "title": "사피엔스 📘",
            "reason": "깊게 생각하고 분석하는 INTJ에게 딱 어울리는 책이야!",
            "story": "인류의 역사와 문명의 발전 과정을 흥미롭게 설명하는 책이야.",
            "creator": "저자: 유발 하라리 ✍️ / 출판사: 김영사"
        },
        "movie": {
            "title": "인터스텔라 🚀",
            "reason": "우주, 과학, 철학을 좋아하는 INTJ 취향 저격 영화!",
            "story": "인류를 구하기 위해 우주로 떠나는 탐험 이야기야.",
            "creator": "감독: 크리스토퍼 놀란 🎬 / 제작사: 워너 브라더스"
        }
    },

    "INTP": {
        "book": {
            "title": "코스모스 🌌",
            "reason": "호기심 많고 탐구심 강한 INTP에게 추천!",
            "story": "우주와 과학의 신비를 쉽게 설명하는 과학 명작이야.",
            "creator": "저자: 칼 세이건 ✍️ / 출판사: 사이언스북스"
        },
        "movie": {
            "title": "매트릭스 💻",
            "reason": "철학적이고 상상력 넘치는 세계관이 INTP랑 잘 맞아!",
            "story": "가상 세계 속 진실을 깨닫게 되는 이야기야.",
            "creator": "감독: 워쇼스키 자매 🎬 / 제작사: 워너 브라더스"
        }
    },

    "ENTJ": {
        "book": {
            "title": "린 스타트업 🚀",
            "reason": "도전 정신 강한 ENTJ에게 완전 추천!",
            "story": "성공적인 창업과 비즈니스 전략을 알려주는 책이야.",
            "creator": "저자: 에릭 리스 ✍️ / 출판사: 인사이트"
        },
        "movie": {
            "title": "아이언맨 🤖",
            "reason": "카리스마 넘치는 리더형 ENTJ 스타일!",
            "story": "천재 사업가가 히어로가 되는 이야기야.",
            "creator": "감독: 존 파브로 🎬 / 제작사: 마블 스튜디오"
        }
    },

    "ENTP": {
        "book": {
            "title": "데미안 🌟",
            "reason": "새로운 생각과 자유를 좋아하는 ENTP에게 추천!",
            "story": "자아를 찾아가는 한 소년의 성장 이야기야.",
            "creator": "저자: 헤르만 헤세 ✍️ / 출판사: 민음사"
        },
        "movie": {
            "title": "인셉션 🌀",
            "reason": "상상력 넘치고 반전 좋아하는 ENTP 취향!",
            "story": "꿈속에 들어가 생각을 조작하는 이야기야.",
            "creator": "감독: 크리스토퍼 놀란 🎬 / 제작사: 워너 브라더스"
        }
    },

    "INFJ": {
        "book": {
            "title": "어린 왕자 👑",
            "reason": "감수성 풍부한 INFJ에게 잘 어울려!",
            "story": "순수함과 인간관계를 따뜻하게 그린 이야기야.",
            "creator": "저자: 생텍쥐페리 ✍️ / 출판사: 열린책들"
        },
        "movie": {
            "title": "코코 🎸",
            "reason": "감동적이고 따뜻한 이야기라 INFJ가 좋아할 확률 높아!",
            "story": "음악을 사랑하는 소년의 모험 이야기야.",
            "creator": "감독: 리 언크리치 🎬 / 제작사: 픽사"
        }
    },

    "INFP": {
        "book": {
            "title": "모모 ⏰",
            "reason": "상상력과 감성이 풍부한 INFP에게 추천!",
            "story": "시간의 소중함을 알려주는 판타지 이야기야.",
            "creator": "저자: 미하엘 엔데 ✍️ / 출판사: 비룡소"
        },
        "movie": {
            "title": "센과 치히로의 행방불명 🐉",
            "reason": "감성적이고 환상적인 분위기가 INFP 취향이야!",
            "story": "신비한 세계에 들어간 소녀의 성장 이야기야.",
            "creator": "감독: 미야자키 하야오 🎬 / 제작사: 스튜디오 지브리"
        }
    },

    "ENFP": {
        "book": {
            "title": "미움받을 용기 🔥",
            "reason": "자유롭고 열정적인 ENFP에게 힘이 되는 책!",
            "story": "행복하게 사는 법과 인간관계를 이야기해.",
            "creator": "저자: 기시미 이치로 ✍️ / 출판사: 인플루엔셜"
        },
        "movie": {
            "title": "라라랜드 🎹",
            "reason": "꿈과 열정을 사랑하는 ENFP에게 추천!",
            "story": "꿈을 향해 달려가는 두 사람의 이야기야.",
            "creator": "감독: 데이미언 셔젤 🎬 / 제작사: 라이언스게이트"
        }
    },

    "ISTJ": {
        "book": {
            "title": "죽은 시인의 사회 🍎",
            "reason": "책임감 강한 ISTJ에게 새로운 시각을 줄 수 있어!",
            "story": "학생들이 꿈과 자유를 찾아가는 이야기야.",
            "creator": "저자: N.H.클라인바움 ✍️ / 출판사: 서교출판사"
        },
        "movie": {
            "title": "포레스트 검프 🏃",
            "reason": "성실함과 꾸준함의 가치가 잘 드러나는 영화야.",
            "story": "한 남자의 인생 여정을 그린 감동 영화야.",
            "creator": "감독: 로버트 저메키스 🎬 / 제작사: 파라마운트"
        }
    },

    "ISFJ": {
        "book": {
            "title": "나미야 잡화점의 기적 📮",
            "reason": "따뜻하고 배려심 많은 ISFJ에게 추천!",
            "story": "편지를 통해 사람들의 고민을 해결하는 이야기야.",
            "creator": "저자: 히가시노 게이고 ✍️ / 출판사: 현대문학"
        },
        "movie": {
            "title": "업 🎈",
            "reason": "따뜻한 감동을 좋아하는 ISFJ 취향!",
            "story": "할아버지와 소년의 특별한 모험 이야기야.",
            "creator": "감독: 피트 닥터 🎬 / 제작사: 픽사"
        }
    },

    "ESTP": {
        "book": {
            "title": "해리포터 ⚡",
            "reason": "모험과 액션을 좋아하는 ESTP에게 딱!",
            "story": "마법학교에서 벌어지는 판타지 모험 이야기야.",
            "creator": "저자: J.K. 롤링 ✍️ / 출판사: 문학수첩"
        },
        "movie": {
            "title": "분노의 질주 🚗",
            "reason": "스릴 넘치는 액션 좋아하면 무조건 추천!",
            "story": "레이싱과 팀워크를 중심으로 한 액션 영화야.",
            "creator": "감독: 저스틴 린 🎬 / 제작사: 유니버설 픽처스"
        }
    },

    "ESFP": {
        "book": {
            "title": "아몬드 🌰",
            "reason": "감정 표현에 관심 많은 ESFP에게 추천!",
            "story": "감정을 잘 느끼지 못하는 소년의 성장 이야기야.",
            "creator": "저자: 손원평 ✍️ / 출판사: 창비"
        },
        "movie": {
            "title": "겨울왕국 ❄️",
            "reason": "신나고 감동적인 분위기를 좋아하는 ESFP 취향!",
            "story": "자매의 사랑과 모험을 담은 이야기야.",
            "creator": "감독: 크리스 벅 🎬 / 제작사: 디즈니"
        }
    }
}

# 부족한 MBTI 자동 추가
all_mbti = [
    "INTJ","INTP","ENTJ","ENTP",
    "INFJ","INFP","ENFJ","ENFP",
    "ISTJ","ISFJ","ESTJ","ESFJ",
    "ISTP","ISFP","ESTP","ESFP"
]

for mbti in all_mbti:
    if mbti not in mbti_contents:
        mbti_contents[mbti] = {
            "book": {
                "title": "어린 왕자 📘",
                "reason": "다양한 성격 유형에게 사랑받는 명작이야!",
                "story": "순수함과 인간관계를 다룬 감동 이야기야.",
                "creator": "저자: 생텍쥐페리 ✍️ / 출판사: 열린책들"
            },
            "movie": {
                "title": "인터스텔라 🚀",
                "reason": "몰입감 넘치고 생각할 거리가 많은 영화야!",
                "story": "우주 탐사를 통해 인류를 구하려는 이야기야.",
                "creator": "감독: 크리스토퍼 놀란 🎬 / 제작사: 워너 브라더스"
            }
        }

# 제목
st.title("✨ MBTI 책 & 영화 추천 서비스 ✨")
st.write("너의 MBTI에 어울리는 책이랑 영화를 추천해줄게 😆📚🎬")

# 선택
selected_mbti = st.selectbox(
    "💡 MBTI를 선택해봐!",
    all_mbti
)

# 버튼
if st.button("추천 받기 🚀"):

    data = mbti_contents[selected_mbti]

    st.success(f"{selected_mbti} 유형을 위한 추천이야 🌈")

    # 책 추천
    st.markdown("## 📚 추천 책")
    st.markdown(f"### {data['book']['title']}")
    st.write(f"💖 추천 이유 : {data['book']['reason']}")
    st.write(f"📖 줄거리 : {data['book']['story']}")
    st.write(f"🏢 제작 정보 : {data['book']['creator']}")

    st.divider()

    # 영화 추천
    st.markdown("## 🎬 추천 영화")
    st.markdown(f"### {data['movie']['title']}")
    st.write(f"💖 추천 이유 : {data['movie']['reason']}")
    st.write(f"🎞️ 줄거리 : {data['movie']['story']}")
    st.write(f"🏢 제작 정보 : {data['movie']['creator']}")

    st.balloons()

# 하단
st.caption("📌 재미로 보는 추천이니까 가볍게 즐겨줘 😎")
