import streamlit as st

# 0. 세션 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = 1
if "p1" not in st.session_state:
    st.session_state.p1 = []
if "p2" not in st.session_state:
    st.session_state.p2 = []
if "p3" not in st.session_state:
    st.session_state.p3 = []
if "p4" not in st.session_state:
    st.session_state.p4 = []
if "p5" not in st.session_state:
    st.session_state.p5 = []

# 1. 웹 화면 기본 설정 및 CSS 디자인 입히기
st.set_page_config(page_title="Big5 심리검사", page_icon="📊")

st.markdown("""
<style>
    /* 1. 라디오 버튼 글씨 크기 조절 */
    div[data-testid="stRadio"] > label > div > p {
        font-size: 18px !important;
        font-weight: bold;
    }
    div[data-testid="stRadio"] > div > label > div > div > p {
        font-size: 16px !important;
    }
    
    /* 2. 이전/다음 버튼 예쁘게 디자인 */
    div.stButton > button:first-child, div[data-testid="stFormSubmitButton"] > button {
        background-color: #4F46E5 !important;
        color: white !important;
        font-size: 16px !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        border: none !important;
        width: 100%;
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover, div[data-testid="stFormSubmitButton"] > button:hover {
        background-color: #4338CA !important;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
    }

    /* 3. 결과 화면 카드 디자인 */
    .result-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 8px;
        margin-top: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border-left: 6px solid #4F46E5;
    }
    .result-title {
        font-size: 18px;
        font-weight: bold;
        color: #111827;
        margin-bottom: 8px;
    }
    .result-desc {
        font-size: 14px;
        color: #4B5563;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

st.title("📊 Big5 심리검사 프로그램")
st.write("각 질문을 읽고 자신과 가장 잘 맞는 것을 선택해주세요.")
st.write("---")

# 2. 질문 목록 만들기 (총 45문항)
questions = [
    {"유형": "O", "질문": "1. 새로운 아이디어나 방식을 시도해보는 것을 좋아한다.", "역채점": False},
    {"유형": "O", "질문": "2. 모르는 분야에 대해서도 알아보고 싶어진다.", "역채점": False},
    {"유형": "O", "질문": "3. 낯선 장소에 가면 그곳을 둘러보고 싶어진다.", "역채점": False},
    {"유형": "O", "질문": "4. 현실에 없는 상황을 상상해보는 것을 즐긴다.", "역채점": False},
    {"유형": "O", "질문": "5. 이야기를 들을 때 장면이 머릿속에 잘 그려진다.", "역채점": False},
    {"유형": "O", "질문": "6. 다양한 관점의 이야기를 듣는 것이 흥미롭다.", "역채점": False},
    {"유형": "O", "질문": "7. 미술관, 전시회 등에서 아름다움을 느낀 적이 있다.", "역채점": False},
    {"유형": "O", "질문": "8. 색다른 스타일의 음악이나 예술을 접하는 것을 좋아한다.", "역채점": False},
    {"유형": "O", "질문": "9. 평범한 사물에서도 아름다움을 발견할 때가 있다.", "역채점": False},
    {"유형": "C", "질문": "10. 자기가 맡은 일을 책임감 있게 하는 편이다.", "역채점": False},
    {"유형": "C", "질문": "11. 어떤 일을 포기하지 않고 끈기있게 하는 편이다.", "역채점": False},
    {"유형": "C", "질문": "12. 한번 시작한 일은 끝까지 마무리하는 편이다.", "역채점": False},
    {"유형": "C", "질문": "13. 평소 정리정돈을 잘 하는 편이다.", "역채점": False},
    {"유형": "C", "질문": "14. 평소에 약속 시간을 잘 지키는 편이다.", "역채점": False},
    {"유형": "C", "질문": "15. 규칙이나 원칙을 잘 지키는 편이다.", "역채점": False},
    {"유형": "C", "질문": "16. 일을 처리할 때 미루는 편이다.", "역채점": True},
    {"유형": "C", "질문": "17. 미리 계획을 세우고 그대로 실행하는 편이다.", "역채점": False},
    {"유형": "C", "질문": "18. 하루 일과를 계획적으로 보내는 편이다.", "역채점": False},
    {"유형": "E", "질문": "19. 나는 새로운 친구를 사귀는 것이 두렵지 않다.", "역채점": False},
    {"유형": "E", "질문": "20. 어색한 분위기를 잘 풀어나가는 편이다.", "역채점": False},
    {"유형": "E", "질문": "21. 모임이나 행사에서 먼저 말을 거는 편이다.", "역채점": False},
    {"유형": "E", "질문": "22. 집에 있는 것보다 외부에 있는 것을 선호한다.", "역채점": False},
    {"유형": "E", "질문": "23. 나는 말이 많은 편이다.", "역채점": False},
    {"유형": "E", "질문": "24. 몸을 움직이는 활동을 즐기는 편이다.", "역채점": False},
    {"유형": "E", "질문": "25. 새로운 일을 시작할 때 긍정적인 마음을 가지는 편이다.", "역채점": False},
    {"유형": "E", "질문": "26. 나는 쉽게 기운이 빠지고 좌절하는 편이다.", "역채점": True},
    {"유형": "E", "질문": "27. 평소 기분이 좋은 편이다.", "역채점": False},
    {"유형": "A", "질문": "28. 나는 친구와 의견이 달라도 상대방의 입장을 생각한다.", "역채점": False},
    {"유형": "A", "질문": "29. 다른 사람이 속상해하면 나도 함께 마음이 쓰인다.", "역채점": False},
    {"유형": "A", "질문": "30. 나는 내 생각이 다른 사람의 생각보다 더 중요하다고 여긴다.", "역채점": True},
    {"유형": "A", "질문": "31. 나는 다른 사람이 어려움을 겪고 있으면 도와주려고 한다.", "역채점": False},
    {"유형": "A", "질문": "32. 나는 다른 사람에게 먼저 양보하거나 배려하는 편이다.", "역채점": False},
    {"유형": "A", "질문": "33. 다른 사람의 감정을 상하지 않게 말을 조심하는 편이다.", "역채점": False},
    {"유형": "A", "질문": "34. 나는 다른 사람과 협력하여 일을 하는 것을 좋아한다.", "역채점": False},
    {"유형": "A", "질문": "35. 나는 다른 사람의 부탁을 잘 들어주는 편이다.", "역채점": False},
    {"유형": "A", "질문": "36. 모둠 활동에서 내 역할을 다하려고 노력한다.", "역채점": False},
    {"유형": "N", "질문": "37. 새로운 곳에 갔을 때 불안하다.", "역채점": False},
    {"유형": "N", "질문": "38. 평소 미래 상황에 대한 걱정을 많이 하는 편이다.", "역채점": False},
    {"유형": "N", "질문": "39. 별일 아닌 일에도 마음이 조마조마할 때가 있다.", "역채점": False},
    {"유형": "N", "질문": "40. 스트레스를 잘 받는다.", "역채점": False},
    {"유형": "N", "질문": "41. 시끄러운 곳에서 집중이 안 된다.", "역채점": False},
    {"유형": "N", "질문": "42. 다른 사람의 사소한 말이나 행동에 신경이 쓰인다.", "역채점": False},
    {"유형": "N", "질문": "43. 예상하지 못한 변수가 생기면 당황하는 편이다.", "역채점": False},
    {"유형": "N", "질문": "44. 어떤 일을 확인하고 또 확인하는 편이다.", "역채점": False},
    {"유형": "N", "질문": "45. 기분이 자주 오르락내리락하는 편이다.", "역채점": False}
]

q1 = questions[0:9]
q2 = questions[9:18]
q3 = questions[18:27]
q4 = questions[27:36]
q5 = questions[36:45]

options_text = ["전혀 아니다", "아니다", "보통이다", "그렇다", "매우 그렇다"]

# 3. 페이지별 질문 렌더링
if st.session_state.page == 1:
    with st.form("survey_form_1"):
        user_answers = []
        for q in q1:
            answer = st.radio(str(q["질문"]), options_text, horizontal=True, index=None, key=q["질문"])
            user_answers.append((q, answer))
            st.write("")
        if st.form_submit_button("다음 페이지로 ➡️"):
            st.session_state.p1 = user_answers
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 2:
    with st.form("survey_form_2"):
        user_answers = []
        for q in q2:
            answer = st.radio(str(q["질문"]), options_text, horizontal=True, index=None, key=q["질문"])
            user_answers.append((q, answer))
            st.write("")
        col1, col2 = st.columns(2)
        btn_prev = col1.form_submit_button("⬅️ 이전 페이지")
        btn_next = col2.form_submit_button("다음 페이지로 ➡️")
        if btn_prev:
            st.session_state.page -= 1
            st.rerun()
        if btn_next:
            st.session_state.p2 = user_answers
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 3:
    with st.form("survey_form_3"):
        user_answers = []
        for q in q3:
            answer = st.radio(str(q["질문"]), options_text, horizontal=True, index=None, key=q["질문"])
            user_answers.append((q, answer))
            st.write("")
        col1, col2 = st.columns(2)
        btn_prev = col1.form_submit_button("⬅️ 이전 페이지")
        btn_next = col2.form_submit_button("다음 페이지로 ➡️")
        if btn_prev:
            st.session_state.page -= 1
            st.rerun()
        if btn_next:
            st.session_state.p3 = user_answers
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 4:
    with st.form("survey_form_4"):
        user_answers = []
        for q in q4:
            answer = st.radio(str(q["질문"]), options_text, horizontal=True, index=None, key=q["질문"])
            user_answers.append((q, answer))
            st.write("")
        col1, col2 = st.columns(2)
        btn_prev = col1.form_submit_button("⬅️ 이전 페이지")
        btn_next = col2.form_submit_button("다음 페이지로 ➡️")
        if btn_prev:
            st.session_state.page -= 1
            st.rerun()
        if btn_next:
            st.session_state.p4 = user_answers
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 5:
    with st.form("survey_form_5"):
        user_answers = []
        for q in q5:
            answer = st.radio(str(q["질문"]), options_text, horizontal=True, index=None, key=q["질문"])
            user_answers.append((q, answer))
            st.write("")
        col1, col2 = st.columns(2)
        btn_prev = col1.form_submit_button("⬅️ 이전 페이지")
        btn_next = col2.form_submit_button("결과 보기 🚀")
        if btn_prev:
            st.session_state.page -= 1
            st.rerun()
        if btn_next:
            st.session_state.p5 = user_answers
            st.session_state.page += 1
            st.rerun()

# 4. 결과 보기 화면
elif st.session_state.page == 6:
    all_user_answers = st.session_state.p1 + st.session_state.p2 + st.session_state.p3 + st.session_state.p4 + st.session_state.p5

    # 누락된 답변이 있는지 검사
    is_all_answered = True
    for q, ans in all_user_answers:
        if ans == None:
            is_all_answered = False
            break

    if is_all_answered == False:
        st.error("⚠️ 아직 답변하지 않은 문항이 있습니다. 이전 페이지로 돌아가 확인해주세요!")
        if st.button("⬅️ 이전 페이지로 돌아가기"):
            st.session_state.page -= 1
            st.rerun()
    else:
        scores = {"O": 0, "C": 0, "E": 0, "A": 0, "N": 0}

        for q, ans in all_user_answers:
            if ans == "전혀 아니다": num_ans = 1
            elif ans == "아니다": num_ans = 2
            elif ans == "보통이다": num_ans = 3
            elif ans == "그렇다": num_ans = 4
            elif ans == "매우 그렇다": num_ans = 5

            if q["역채점"] == True:
                final_score = 6 - num_ans
            else:
                final_score = num_ans

            scores[q["유형"]] += final_score

        # 상단 축하 메시지
        st.subheader("🎉 당신의 Big5 검사 결과")
        st.success("검사가 성공적으로 완료되었습니다!")
        st.write("")
        
        # [UI 개선] 점수 요약(Metric) 한 줄에 나란히 배치
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("개방성(O)", f"{scores['O']}점")
        col2.metric("성실성(C)", f"{scores['C']}점")
        col3.metric("외향성(E)", f"{scores['E']}점")
        col4.metric("우호성(A)", f"{scores['A']}점")
        col5.metric("신경성(N)", f"{scores['N']}점")
        st.write("---")

        # [UI 개선] Custom CSS를 활용한 결과 카드와 프로그레스 바 적용
        descriptions = {
            "O": ("개방성", "새로운 경험과 아이디어를 기꺼이 받아들이는 정도입니다. 호기심이 많고 상상력이 풍부하며, 예술적인 아름다움을 잘 느끼는 성향을 나타냅니다."),
            "C": ("성실성", "목표를 향해 꾸준하고 계획적으로 노력하는 정도입니다. 책임감이 강하고 규칙을 잘 지키며, 일을 미루지 않고 끝까지 해내는 성향을 나타냅니다."),
            "E": ("외향성", "외부 세계와 사람들과의 교류를 통해 에너지를 얻는 정도입니다. 사교적이고 활발하며, 매사에 긍정적인 감정을 자주 느끼는 성향을 나타냅니다."),
            "A": ("우호성", "타인과 조화롭게 지내고 타인을 배려하는 정도입니다. 다른 사람의 마음에 깊이 공감하고, 기꺼이 양보하며 협력하는 것을 좋아하는 성향을 나타냅니다."),
            "N": ("신경성", "스트레스나 자극에 얼마나 민감하게 반응하는지를 나타냅니다. 점수가 높을수록 주변 환경 변화에 예민하고 불안이나 걱정을 비교적 쉽게 느낄 수 있습니다.")
        }

        for key in ["O", "C", "E", "A", "N"]:
            # 카드 HTML 출력
            st.markdown(f"""
            <div class="result-card">
                <div class="result-title">🔹 {descriptions[key][0]} ({key}) : {scores[key]} / 45점</div>
                <div class="result-desc">{descriptions[key][1]}</div>
            </div>
            """, unsafe_allow_html=True)
            # 게이지 바 출력 (0.0 ~ 1.0 비율로 계산)
            st.progress(scores[key] / 45.0)
            st.write("")

        st.write("---")
        st.subheader("📊 다섯 가지 성향 비교")
        scores1 = list(scores.items())
        scores1.sort(reverse=True, key=lambda x: x[1])
        st.info(f"**{scores1[0][0]} > {scores1[1][0]} > {scores1[2][0]} > {scores1[3][0]} > {scores1[4][0]}**")
        
        st.write("")
        if st.button("처음부터 다시 검사하기 🔄"):
            st.session_state.page = 1
            st.session_state.p1 = []
            st.session_state.p2 = []
            st.session_state.p3 = []
            st.session_state.p4 = []
            st.session_state.p5 = []
            st.rerun()
