import streamlit as st
import base64

def img_to_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

def img_to_html(img_path, width=40):
    try:
        with open(img_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        return f'<img src="data:image/png;base64,{data}" width="{width}" height="{width}"/>'
    except:
        return ""

st.set_page_config(page_title="포트폴리오", page_icon="💼", layout="wide")

st.markdown("""
<style>
* { word-break: keep-all; overflow-wrap: break-word; }
</style>
""", unsafe_allow_html=True)
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
    if st.button("🏠  홈", use_container_width=True, key="sb_home"):
        st.switch_page("Home.py")
    if st.button("🟥  다이소 뷰티 전략 분석", use_container_width=True, key="sb_p1"):
        st.switch_page("pages/1_프로젝트_1.py")
    if st.button("🟩  스타벅스 마케팅 분석", use_container_width=True, key="sb_p2"):
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
    height: auto; min-height: fit-content;
}
.profile-info h1 { font-size: 1.9rem; font-weight: 700; margin: 0 0 0.3rem 0; color: white; }
.profile-cols { display: flex; gap: 1rem; margin-top: 0.5rem; flex-wrap: wrap; }
.profile-col {
    min-width: 160px; flex: 1;
    background: rgba(255,255,255,0.08);
    border-radius: 0.8rem;
    padding: 0.8rem 1rem;
}
.profile-col h4 { font-size: 0.78rem; text-transform: uppercase; letter-spacing: 1px; color: rgba(255,255,255,0.6); margin: 0 0 0.4rem 0; }
.profile-col p  { font-size: 0.88rem; margin: 0.15rem 0; color: rgba(255,255,255,0.9); }
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

cert1_b64 = img_to_base64("images/사조사 자격증_1.png")
cert2_b64 = img_to_base64("images/직상 자격증_1.png")
cert3_b64 = img_to_base64("images/청상 자격증.jpeg")

# 프로필 카드 - 연락처, 학력만
st.markdown(f"""
<div class="profile-card">
    <img src="https://ca.slack-edge.com/T088AB0N865-U09EHSCUNSF-3bef5911dc38-512"
         style="width:120px; height:120px; border-radius:50%; object-fit:cover; border:3px solid rgba(255,255,255,0.2); flex-shrink:0;">
    <div class="profile-info">
        <h1>김재경</h1>
        <p style="color:rgba(255,255,255,0.85); font-size:0.92rem; margin: 0.4rem 0 0.8rem 0;">
            <strong>데이터 이면의 마음을 읽고, 집요하게 진실을 증명하는 분석가 김재경입니다.</strong><br><br>
            1. 심리학 전공의 통계적 통찰력을 바탕으로, 숫자 속에 숨겨진 고객의 행동 동기와 비즈니스의 인과관계(PSM, OW)를 깊이 있게 파고듭니다.<br>
            2. 900여 건의 제품을 직접 검수하며 알레르기·기능성 DB를 정교하게 연결했던 경험처럼, 작은 데이터 하나에도 진심을 다해 분석의 무결성을 확보합니다.<br>
            3. 30만 건의 목소리에 RNN/LSTM 감성 분석을 더해 시장의 미세한 흐름을 읽고, 고객의 일상에 연착륙할 수 있는 실질적인 전략을 제안합니다.<br>
            4. 이커머스 라이프사이클 전반을 경험하며 퍼널 분석을 통해 서비스의 병목을 진단하고, 데이터 기반의 최적화된 고객 경험을 설계합니다.<br>
            5. 단순히 효율을 높이는 것을 넘어, 데이터로 '초신뢰'의 가치를 증명하며 고객과 비즈니스를 단단하게 연결하는 가교가 되고 싶습니다.
        </p>
        <div class="profile-cols">
            <div class="profile-col">
                <h4>연락처</h4>
                <p style="font-size:0.92rem;">📧 kyng0116@gmail.com</p>
                <p style="font-size:0.92rem;">📱 010-5021-9745</p>
                <p style="font-size:0.92rem;">🔗 <a href="https://github.com/kyng0116-cell" target="_blank" style="color:white;">GitHub</a></p>
                <p style="font-size:0.92rem;">🔗 <a href="https://www.linkedin.com/in/재경-김-6061463b7/" target="_blank" style="color:white;">LinkedIn</a></p>
            </div>
            <div class="profile-col">
                <h4>학력</h4>
                <p style="font-size:0.92rem;">🎓 단국대학교 | 심리학 학사 <br/> (2015.03 ~ 2020.02)</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 자격증 & 경력 섹션
st.markdown('<div class="section-title">📋 자격증 & 경력</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div style="background:rgba(255,255,255,0.05); border-radius:1rem; padding:1.2rem; border:1px solid rgba(255,255,255,0.1);">
        <h4 style="color:#e94560; margin:0 0 0.8rem 0; font-size:0.85rem; text-transform:uppercase; letter-spacing:1px;">자격증</h4>
        <details style="margin-bottom:0.3rem;">
            <summary style="cursor:pointer; list-style:none; font-size:0.92rem; color:#1a1a2e; word-break:keep-all; overflow-wrap:break-word;">📜 사회조사분석사 2급<span style="font-size:0.75rem; color:#999;">&nbsp;&nbsp; ▶ 펼쳐보기</span></summary>
            <img src="data:image/png;base64,{cert1_b64}" style="width:100%; margin-top:0.5rem; border-radius:0.5rem;">
        </details>
        <details style="margin-bottom:0.3rem;">
            <summary style="cursor:pointer; list-style:none; font-size:0.92rem; color:#1a1a2e; word-break:keep-all; overflow-wrap:break-word;">📜 직업상담사 2급<span style="font-size:0.75rem; color:#999;">&nbsp;&nbsp; ▶ 펼쳐보기</span></summary>
            <img src="data:image/png;base64,{cert2_b64}" style="width:100%; margin-top:0.5rem; border-radius:0.5rem;">
        </details>
        <details style="margin-bottom:0.3rem;">
            <summary style="cursor:pointer; list-style:none; font-size:0.92rem; color:#1a1a2e; word-break:keep-all; overflow-wrap:break-word;">📜 청소년상담사 3급<span style="font-size:0.75rem; color:#999;">&nbsp;&nbsp; ▶ 펼쳐보기</span></summary>
            <img src="data:image/png;base64,{cert3_b64}" style="width:100%; margin-top:0.5rem; border-radius:0.5rem;">
        </details>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background:rgba(255,255,255,0.05); border-radius:1rem; padding:1.2rem; border:1px solid rgba(255,255,255,0.1);">
        <h4 style="color:#e94560; margin:0 0 0.8rem 0; font-size:0.85rem; text-transform:uppercase; letter-spacing:1px;">경력</h4>
        <details style="margin-bottom:0.3rem;">
            <summary style="cursor:pointer; list-style:none; font-size:0.92rem; color:#1a1a2e; word-break:keep-all; overflow-wrap:break-word;">🏢 테슬라 | 인턴 (2024.02 ~ 2024.05)<span style="font-size:0.75rem; color:#999;">&nbsp;&nbsp; ▶ 펼쳐보기</span></summary>
            <div style="margin-top:0.5rem; font-size:0.88rem; color:#444; line-height:1.7; word-break:keep-all;">
                <p>• 전기차 보조금 지원 신청</p>
                <p>• 누락 서류 파악 및 담당자에게 서류 정보 전달</p>
                <p>• 지자체 별 관련 공고문 정리</p>
            </div>
        </details>
        <details style="margin-bottom:0.3rem;">
            <summary style="cursor:pointer; list-style:none; font-size:0.92rem; color:#1a1a2e; word-break:keep-all; overflow-wrap:break-word;">🏢 스파르타 내일배움캠프 데이터분석가 과정 | 학생 (2025.10 ~ 2026.3)<span style="font-size:0.75rem; color:#999;">&nbsp;&nbsp; ▶ 펼쳐보기</span></summary>
            <div style="margin-top:0.5rem; font-size:0.88rem; color:#444; line-height:1.7; word-break:keep-all;">
                <p>• SQL, 파이썬, 데이터 분석 관련 하드스킬 학습</p>
                <p>• 프로젝트 진행</p>
                <p>• 데이터리터러시 능력, 사회통계역량 강화</p>
            </div>
        </details>
        <details style="margin-bottom:0.3rem;">
            <summary style="cursor:pointer; list-style:none; font-size:0.92rem; color:#1a1a2e; word-break:keep-all; overflow-wrap:break-word;">🏢 그리트라운지 | 팀장 (2024.05 ~ 2025.04)<span style="font-size:0.75rem; color:#999;">&nbsp;&nbsp; ▶ 펼쳐보기</span></summary>
            <div style="margin-top:0.5rem; font-size:0.88rem; color:#444; line-height:1.7; word-break:keep-all;">
                <p>• 테슬라 전기차 보조금 업무 인수인계 후 팀장으로 업무 확장</p>
                <p>• 전기차 보조금 지원신청</p>
                <p>• 이메일 제목에서 예약번호 추출 자동화</p>
                <p>• 신청 누락 방지 시스템 설계</p>
                <p>• 지자체 별 특이사항 혹은 고객 특이사항(영주권자, 재외동포, 타국 영주권 소지자)등 정리 후 공유</p>
                <p>• 지자체 별 공고문 정리</p>
            </div>
        </details>
        <details style="margin-bottom:0.3rem;">
            <summary style="cursor:pointer; list-style:none; font-size:0.92rem; color:#1a1a2e; word-break:keep-all; overflow-wrap:break-word;">🏢 위덕대학교 LINC3.0사업단 | 계약직 (2023.08 ~ 2023.10)<span style="font-size:0.75rem; color:#999;">&nbsp;&nbsp; ▶ 펼쳐보기</span></summary>
            <div style="margin-top:0.5rem; font-size:0.88rem; color:#444; line-height:1.7; word-break:keep-all;">
                <p>• 산학협력 사업 행정 지원 전반 관리</p>
                <p>• 기업 애로기술 과제 신청서 검토 및 진행 상황 관리</p>
                <p>• 학생 현장실습 신청 및 배치 관리</p>
                <p>• 사업단 성과 데이터 수집 및 뉴스레터 발행 관리</p>
            </div>
        </details>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">📁 Projects</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background:#fff; border-radius:1rem; padding:1.5rem; box-shadow:0 2px 16px rgba(0,0,0,0.07); border-top: 4px solid #e60012; min-height:320px;">
        <div style="display:flex; align-items:center; gap:0.7rem; margin-bottom:0.8rem;">
            <span style="font-size:1.5rem;">🟥</span>
            <strong style="font-size:1.1rem; color:#1a1a2e;">초저가를 넘어 초신뢰로</strong>
        </div>
        <p style="font-size:0.88rem; color:#444; margin-bottom:1rem;">다이소 뷰티 30만 건 리뷰 분석을 통한 2026년 성장 전략 도출</p>
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap; margin-bottom:1rem;">
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.78rem; color:#555;">RNN/LSTM</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.78rem; color:#555;">인과추론(PSM·IPTW·OW)</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.78rem; color:#555;">층화 샘플링</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.78rem; color:#555;">OCR</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.78rem; color:#555;">GIS 분석</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.78rem; color:#555;">DB 정규화</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.78rem; color:#555;">Tableau</span>
        </div>
        <div style="display:flex; gap:1.5rem; margin-bottom:1rem;">
            <div style="text-align:center;">
                <div style="font-size:1.3rem; font-weight:700; color:#e60012;">30만건</div>
                <div style="font-size:0.75rem; color:#888;">리뷰 데이터</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.3rem; font-weight:700; color:#e60012;">83.3%</div>
                <div style="font-size:0.75rem; color:#888;">연착륙 제품 중 스킨케어</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.3rem; font-weight:700; color:#e60012;">144%</div>
                <div style="font-size:0.75rem; color:#888;">뷰티 카테고리 성장률</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🟥 프로젝트 보기", use_container_width=True, key="proj1_btn"):
        st.switch_page("pages/1_프로젝트_1.py")

with col2:
    st.markdown("""
    <div style="background:#fff; border-radius:1rem; padding:1.5rem; box-shadow:0 2px 16px rgba(0,0,0,0.07); border-top: 4px solid #00704a; min-height:320px;">
        <div style="display:flex; align-items:center; gap:0.7rem; margin-bottom:0.8rem;">
            <span style="font-size:1.5rem;">🟩</span>
            <strong style="font-size:1.1rem; color:#1a1a2e;">starbucks next level</strong>
        </div>
        <p style="font-size:0.88rem; color:#444; margin-bottom:1rem;">행동경제학 기반 프로모션 채널 효과 분석 및 고객 세그먼트 전략 수립</p>
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap; margin-bottom:1rem;">
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.78rem; color:#555;">K-means</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.78rem; color:#555;">엘보우 방법</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.78rem; color:#555;">Kruskal-Wallis</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.78rem; color:#555;">카이제곱 검정</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.78rem; color:#555;">행동경제학</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.78rem; color:#555;">Tableau</span>
        </div><br/>
        <div style="display:flex; gap:1.5rem; margin-bottom:1rem;">
            <div style="text-align:center;">
                <div style="font-size:1.3rem; font-weight:700; color:#00704a;">43.97%p</div>
                <div style="font-size:0.75rem; color:#888;">SNS 채널 효과</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.3rem; font-weight:700; color:#00704a;">4개</div>
                <div style="font-size:0.75rem; color:#888;">고객 세그먼트</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.3rem; font-weight:700; color:#00704a;">3가지</div>
                <div style="font-size:0.75rem; color:#888;">행동경제학 인사이트</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🟩 프로젝트 보기", use_container_width=True, key="proj2_btn"):
        st.switch_page("pages/2_프로젝트_2.py")


st.markdown('<div class="section-title">🛠 Skills</div>', unsafe_allow_html=True)

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
        stars = round(pct / 20)
        filled = "★" * stars
        empty = "☆" * (5 - stars)
        st.markdown(f"""
        <div class="skill-card">
            <div class="skill-icon">{icon}</div>
            <div class="skill-name">{name}</div>
            <div style="margin-left:auto; font-size:1.1rem; color:#e94560; letter-spacing:2px; text-align:right;">
                <span style="font-size:0.75rem; color:#999; margin-right:0.4rem;">숙련도</span>
                {filled}<span style="color:#ddd;">{empty}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**💻 Languages**")
    render_skills(languages)
with col2:
    st.markdown("**🔧 Tools**")
    render_skills(tools)
with col3:
    st.markdown("**📦 Libraries**")
    render_skills(libraries)
