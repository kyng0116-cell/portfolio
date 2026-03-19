import streamlit as st

import base64

def img_to_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

st.set_page_config(page_title="포트폴리오", page_icon="💼", layout="wide")

with st.sidebar:
    st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    }
    [data-testid="stSidebar"] * { color: white !important; }
    [data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.15); }
    [data-testid="stSidebar"] .stButton button {
        background: transparent;
        border: 1px solid rgba(255,255,255,0.2);
        color: white !important;
        text-align: left;
        border-radius: 0.5rem;
    }
    [data-testid="stSidebar"] .stButton button:hover {
        background: rgba(233,69,96,0.25);
        border-color: #e94560;
    }
    [data-testid="stSidebarNav"] { display: none; }

    </style>
    """, unsafe_allow_html=True)
    st.markdown("## 💼 포트폴리오")
    st.caption("김재경 · Data Analyst")
    st.divider()
    if st.button("🏠  홈",         use_container_width=True, key="sb_home"):
        st.switch_page("Home.py")
    if st.button("🟩  스타벅스 마케팅 분석", use_container_width=True, key="sb_p1"):
        st.switch_page("pages/1_프로젝트_1.py")
    if st.button("🟥  다이소 뷰티 전략 분석", use_container_width=True, key="sb_p2"):
        st.switch_page("pages/2_프로젝트_2.py")
    st.divider()


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }
.profile-card {
    display: flex; align-items: flex-start; gap: 2.5rem;
    padding: 2.5rem;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%);
    border-radius: 1.2rem; color: white; margin-bottom: 2rem;
    box-shadow: 0 8px 32px rgba(0,0,0,0.18);
}
.profile-img-placeholder {
    width: 120px; height: 120px; border-radius: 50%;
    background: #e94560; display: flex; align-items: center;
    justify-content: center; font-size: 3rem; flex-shrink: 0;
    border: 3px solid rgba(255,255,255,0.2);
}
.profile-info h1 { font-size: 1.9rem; font-weight: 700; margin: 0 0 0.3rem 0; }
.profile-cols { display: flex; gap: 3rem; margin-top: 0.5rem; }
.profile-col h4 { font-size: 0.78rem; text-transform: uppercase; letter-spacing: 1px; opacity: 0.6; margin: 0 0 0.4rem 0; }
.profile-col p  { font-size: 0.88rem; margin: 0.15rem 0; opacity: 0.9; }
.section-title {
    font-size: 1.2rem; font-weight: 700; color: #1a1a2e;
    margin: 1.8rem 0 1rem 0; padding-bottom: 0.4rem;
    border-bottom: 2.5px solid #e94560; display: inline-block;
}
.skill-card {
    background: #fff; border-radius: 0.8rem; padding: 0.9rem 1.1rem;
    margin-bottom: 0.6rem; box-shadow: 0 2px 10px rgba(0,0,0,0.06);
    display: flex; align-items: center; gap: 0.9rem;
}
.skill-icon { font-size: 1.4rem; width: 1.8rem; text-align: center; }
.skill-name { font-weight: 600; font-size: 0.88rem; color: #1a1a2e; min-width: 85px; }
.skill-bar-wrap { flex: 1; background: #f0f0f5; border-radius: 99px; height: 7px; overflow: hidden; }
.skill-bar { height: 100%; border-radius: 99px; background: linear-gradient(90deg, #e94560, #0f3460); }
.skill-pct { font-size: 0.8rem; color: #999; min-width: 30px; text-align: right; }
</style>
""", unsafe_allow_html=True)

import base64

def img_to_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

cert1_b64 = img_to_base64("images/사조사 자격증_1.png")  # 👉 나중에 파일명 변경
cert2_b64 = img_to_base64("images/직상 자격증_1.png")  # 👉 나중에 파일명 변경
cert3_b64 = img_to_base64("images/청상 자격증.jpeg")  # 👉 나중에 파일명 변경

st.markdown(f"""
<div class="profile-card">
    <img src="https://ca.slack-edge.com/T088AB0N865-U09EHSCUNSF-3bef5911dc38-512"
         style="width:120px; height:120px; border-radius:50%; object-fit:cover; border:3px solid rgba(255,255,255,0.2); flex-shrink:0;">
    <div class="profile-info">
        <h1>김재경</h1>
        <p style="opacity:0.85; font-size:0.92rem; margin: 0.4rem 0 0.8rem 0;">
            숫자 뒤에 숨은 이유를 찾습니다.<br><br>
            심리학을 전공하며 쌓은 사회통계 기반 위에서, z-score·상관분석·ANOVA 등 다양한 통계 기법을 비즈니스 문제에 적용합니다. 그중에서도 클러스터링으로 패턴을 발견하고, 인과추론(PSM, IPTW, OW)으로 '왜'를 증명해 실행 가능한 의사결정을 이끌어냅니다.
        </p>
        <div class="profile-cols">
            <div class="profile-col">
                <h4>연락처</h4>
                <p>📧 kyng0116@gmail.com</p>
                <p>📱 010-5021-9745</p>
                <p>🔗 <a href="https://github.com/kyng0116-cell" target="_blank" style="color:white;">GitHub</a></p>
                <p>🔗 <a href="https://www.linkedin.com/in/재경-김-6061463b7/" target="_blank" style="color:white;">LinkedIn</a></p>
            </div>
            <div class="profile-col">
                <h4>학력</h4>
                <p>🎓 단국대학교 | 심리학 학사 (2015.03 ~ 2020.02)</p>
            </div>
            <div class="profile-col">
                <h4>자격증</h4>
                <details style="margin-bottom:0.3rem;">
                    <summary style="cursor:pointer; list-style:none;">📜 사회조사분석사 2급<span style="font-size:0.75rem; opacity:0.5;">&nbsp;&nbsp; ▶ 클릭</span></summary>
                    <img src="data:image/png;base64,{cert1_b64}" style="width:400px; margin-top:0.5rem; border-radius:0.5rem;">
                </details>
                <details style="margin-bottom:0.3rem;">
                    <summary style="cursor:pointer; list-style:none;">📜 직업상담사 2급<span style="font-size:0.75rem; opacity:0.5;">&nbsp;&nbsp; ▶ 클릭</span></summary>
                    <img src="data:image/png;base64,{cert2_b64}" style="width:400px; margin-top:0.5rem; border-radius:0.5rem;">
                </details>
                <details style="margin-bottom:0.3rem;">
                    <summary style="cursor:pointer; list-style:none;">📜 청소년상담사 3급<span style="font-size:0.75rem; opacity:0.5;">&nbsp;&nbsp; ▶ 클릭</span></summary>
                    <img src="data:image/png;base64,{cert3_b64}" style="width:400px; margin-top:0.5rem; border-radius:0.5rem;">
                </details>
            </div>
            <div class="profile-col">
                <h4>경력</h4>
                <details style="margin-bottom:0.3rem;">
                    <summary style="cursor:pointer; list-style:none;">🏢 테슬라 | 인턴 (2024.02 ~ 2024.05)<span style="font-size:0.75rem; opacity:0.5;">&nbsp;&nbsp; ▶ 클릭</span></summary>
                    <div style="margin-top:0.5rem; font-size:0.85rem; opacity:0.85; line-height:1.7;">
                        <p>• 전기차 보조금 지원 신청</p>
                        <p>• 누락 서류 파악 및 담당자에게 서류 정보 전달</p>
                        <p>• 지자체 별 관련 공고문 정리</p>
                    </div>
                </details>
                <details style="margin-bottom:0.3rem;">
                    <summary style="cursor:pointer; list-style:none;">🏢 스파르타 내일배움캠프 데이터분석가 과정 | 학생 (2025.10 ~ 2026.3)<span style="font-size:0.75rem; opacity:0.5;">&nbsp;&nbsp; ▶ 클릭</span></summary>
                    <div style="margin-top:0.5rem; font-size:0.85rem; opacity:0.85; line-height:1.7;">
                        <p>• SQL, 파이썬, 데이터 분석 관련 하드스킬 학습</p>
                        <p>• 프로젝트 진행</p>
                        <p>• 데이터리터러시 능력, 사회통계역량 강화</p>
                    </div>
                </details>
                <details style="margin-bottom:0.3rem;">
                    <summary style="cursor:pointer; list-style:none;">🏢 그리트라운지 | 팀장 (2024.05 ~ 2025.04)<span style="font-size:0.75rem; opacity:0.5;">&nbsp;&nbsp; ▶ 클릭</span></summary>
                    <div style="margin-top:0.5rem; font-size:0.85rem; opacity:0.85; line-height:1.7;">
                        <p>• 테슬라 전기차 보조금 업무 인수인계 후 팀장으로 업무 확장</p>
                        <p>• 전기차 보조금 지원신청</p>
                        <p>• 이메일 제목에서 예약번호 추출 자동화</p>
                        <p>• 신청 누락 방지 시스템 설계</p>
                        <p>• 지자체 별 특이사항 혹은 고객 특이사항(영주권자, 재외동포, 타국 영주권 소지자)등 정리 후 공유</p>
                        <p>• 지자체 별 공고문 정리</p>
                    </div>
                </details>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">🛠 Skills</div>', unsafe_allow_html=True)

import base64

def img_to_html(img_path, width=40):
    with open(img_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return f'<img src="data:image/png;base64,{data}" width="{width}" height="{width}"/>'


tools = [
    (img_to_html("assets/tableau.png"), "Tableau", 85),
    ('<img src="https://cdn.simpleicons.org/mysql" width="40" height="40" alt="MySQL"/>', "MySQL", 75),
    ('<img src="https://cdn.simpleicons.org/jupyter" width="40" height="40" alt="Jupyter"/>', "Jupyter Notebook", 85),
]
languages = [
    ('<img src="https://cdn.simpleicons.org/python" width="40" height="40" alt="Python"/>', "Python", 90),
    (img_to_html("assets/SQL.png"), "SQL", 85),
]
libraries = [
    ('<img src="https://cdn.simpleicons.org/pandas" width="40" height="40" alt="Pandas"/>', "Pandas", 90),
    (img_to_html("assets/matplotlib.png"), "Matplotlib", 80),
    (img_to_html("assets/seaborn.png"), "Seaborn", 78),
    ('<img src="https://cdn.simpleicons.org/scikitlearn" width="40" height="40" alt="Scikit-learn"/>', "Scikit-learn", 70),
    ("🗺", "Folium", 75),
    (img_to_html("assets/scipy.png"), "Scipy", 80),
]

def render_skills(items):
    for icon, name, pct in items:
        st.markdown(f"""
        <div class="skill-card">
            <div class="skill-icon">{icon}</div>
            <div class="skill-name">{name}</div>
            <div class="skill-bar-wrap"><div class="skill-bar" style="width:{pct}%"></div></div>
            <div class="skill-pct">{pct}%</div>
        </div>
        """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**🔧 Tools**")
    render_skills(tools)
with col2:
    st.markdown("**💻 Languages**")
    render_skills(languages)
with col3:
    st.markdown("**📦 Libraries**")
    render_skills(libraries)
