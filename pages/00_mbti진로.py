import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 진로 추천 🌈",
    page_icon="✨",
    layout="centered"
)

# MBTI별 진로 데이터
mbti_jobs = {
    "INTJ": [
        {
            "job": "데이터 분석가 📊",
            "major": "컴퓨터공학과, 통계학과",
            "personality": "논리적이고 계획 세우는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "연구원 🔬",
            "major": "자연과학계열, 생명과학과",
            "personality": "호기심이 많고 깊게 탐구하는 사람",
            "salary": "평균 연봉 약 4,800만원"
        }
    ],

    "INTP": [
        {
            "job": "프로그래머 💻",
            "major": "소프트웨어학과, 컴퓨터공학과",
            "personality": "창의적이고 문제 해결을 좋아하는 사람",
            "salary": "평균 연봉 약 5,200만원"
        },
        {
            "job": "게임 개발자 🎮",
            "major": "게임공학과, 컴퓨터공학과",
            "personality": "아이디어가 많고 새로운 걸 좋아하는 사람",
            "salary": "평균 연봉 약 4,700만원"
        }
    ],

    "ENTJ": [
        {
            "job": "CEO 🏢",
            "major": "경영학과",
            "personality": "리더십이 강하고 목표지향적인 사람",
            "salary": "평균 연봉 약 7,000만원 이상"
        },
        {
            "job": "마케팅 기획자 📢",
            "major": "광고홍보학과, 경영학과",
            "personality": "도전 정신이 강하고 추진력이 있는 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],

    "ENTP": [
        {
            "job": "창업가 🚀",
            "major": "경영학과",
            "personality": "아이디어가 많고 도전을 즐기는 사람",
            "salary": "평균 연봉 편차 큼"
        },
        {
            "job": "광고 기획자 🎨",
            "major": "광고홍보학과",
            "personality": "창의적이고 말하는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 4,300만원"
        }
    ],

    "INFJ": [
        {
            "job": "상담사 💖",
            "major": "심리학과",
            "personality": "공감 능력이 뛰어나고 따뜻한 사람",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "작가 ✍️",
            "major": "문예창작과",
            "personality": "상상력이 풍부하고 감수성이 깊은 사람",
            "salary": "평균 연봉 약 3,800만원"
        }
    ],

    "INFP": [
        {
            "job": "웹툰 작가 🖌️",
            "major": "만화애니메이션학과",
            "personality": "감성이 풍부하고 창의적인 사람",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "사회복지사 🤝",
            "major": "사회복지학과",
            "personality": "다른 사람을 돕는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 3,500만원"
        }
    ],

    "ENFJ": [
        {
            "job": "교사 🍎",
            "major": "교육학과",
            "personality": "사람들을 이끌고 도와주는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "HR 담당자 👔",
            "major": "경영학과",
            "personality": "소통 능력이 뛰어난 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],

    "ENFP": [
        {
            "job": "유튜버 🎥",
            "major": "미디어커뮤니케이션학과",
            "personality": "에너지가 넘치고 표현력이 좋은 사람",
            "salary": "수익 편차 큼"
        },
        {
            "job": "여행 기획자 ✈️",
            "major": "관광경영학과",
            "personality": "새로운 경험을 좋아하는 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],

    "ISTJ": [
        {
            "job": "공무원 🏛️",
            "major": "행정학과",
            "personality": "책임감이 강하고 꼼꼼한 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "회계사 📚",
            "major": "회계학과",
            "personality": "정확하고 체계적인 사람",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],

    "ISFJ": [
        {
            "job": "간호사 🏥",
            "major": "간호학과",
            "personality": "배려심 많고 성실한 사람",
            "salary": "평균 연봉 약 4,700만원"
        },
        {
            "job": "유치원 교사 🧸",
            "major": "유아교육과",
            "personality": "아이들을 좋아하고 다정한 사람",
            "salary": "평균 연봉 약 3,600만원"
        }
    ],

    "ESTJ": [
        {
            "job": "경찰관 🚔",
            "major": "경찰행정학과",
            "personality": "책임감 있고 리더십이 강한 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "관리자 📋",
            "major": "경영학과",
            "personality": "체계적으로 일하는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 5,500만원"
        }
    ],

    "ESFJ": [
        {
            "job": "승무원 ✈️",
            "major": "항공서비스학과",
            "personality": "친절하고 사교적인 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "호텔리어 🏨",
            "major": "호텔관광학과",
            "personality": "서비스 정신이 뛰어난 사람",
            "salary": "평균 연봉 약 4,200만원"
        }
    ],

    "ISTP": [
        {
            "job": "파일럿 🛫",
            "major": "항공운항학과",
            "personality": "침착하고 집중력이 좋은 사람",
            "salary": "평균 연봉 약 8,000만원"
        },
        {
            "job": "기계 엔지니어 ⚙️",
            "major": "기계공학과",
            "personality": "손으로 만드는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 5,500만원"
        }
    ],

    "ISFP": [
        {
            "job": "디자이너 🎨",
            "major": "시각디자인학과",
            "personality": "감각적이고 예술적인 사람",
            "salary": "평균 연봉 약 4,200만원"
        },
        {
            "job": "플로리스트 🌸",
            "major": "원예학과",
            "personality": "섬세하고 자연을 좋아하는 사람",
            "salary": "평균 연봉 약 3,500만원"
        }
    ],

    "ESTP": [
        {
            "job": "스포츠 선수 ⚽",
            "major": "체육학과",
            "personality": "활동적이고 도전적인 사람",
            "salary": "평균 연봉 편차 큼"
        },
        {
            "job": "영업 전문가 💼",
            "major": "경영학과",
            "personality": "사람 만나는 걸 좋아하는 사람",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],

    "ESFP": [
        {
            "job": "배우 🎭",
            "major": "연극영화과",
            "personality": "끼가 많고 밝은 사람",
            "salary": "평균 연봉 편차 큼"
        },
        {
            "job": "이벤트 플래너 🎉",
            "major": "이벤트학과",
            "personality": "분위기 메이커 역할을 잘하는 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    ]
}

# 제목
st.title("✨ MBTI 진로 추천 서비스 ✨")
st.write("너의 MBTI에 딱 맞는 진로를 추천해줄게 😎")

# 선택창
selected_mbti = st.selectbox(
    "💡 너의 MBTI를 선택해봐!",
    list(mbti_jobs.keys())
)

# 버튼
if st.button("진로 추천 받기 🚀"):

    st.success(f"{selected_mbti} 유형에게 어울리는 진로야! 🌈")

    jobs = mbti_jobs[selected_mbti]

    for idx, job in enumerate(jobs, start=1):
        st.markdown(f"## {idx}. {job['job']}")
        st.write(f"🎓 추천 학과 : {job['major']}")
        st.write(f"🧠 잘 어울리는 성격 : {job['personality']}")
        st.write(f"💰 평균 연봉 : {job['salary']}")
        st.divider()

    st.balloons()

# 하단 문구
st.caption("📌 참고: 연봉은 평균 기준이라 실제와 차이가 있을 수 있어!")
