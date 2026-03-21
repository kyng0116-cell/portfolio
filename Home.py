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

st.set_page_config(page_title="포트폴리오", page_icon="💼", layout="wide", initial_sidebar_state="collapsed")

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
        border-color: #533483;
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
html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; letter-spacing: 1px; }
* { word-break: keep-all !important; overflow-wrap: break-word !important; }
strong { font-size: 1.25rem !important; }
.profile-card {
    display: flex; align-items: flex-start; gap: 2.5rem;
    padding: 2.5rem;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%);
    border-radius: 1.2rem; color: white; margin-bottom: 2rem;
    box-shadow: 0 8px 32px rgba(0,0,0,0.18);
    height: auto; min-height: fit-content;
}
.profile-info { flex: 1; width: 100%; min-width: 0; }
.profile-info h1 { font-size: 1.9rem; font-weight: 700; margin: 0 0 0.3rem 0; color: white; }
.profile-cols { display: flex; gap: 1rem; margin-top: 0.5rem; flex-wrap: wrap; width: 100%; }
.profile-col { min-width: 160px; flex: 1; background: rgba(255,255,255,0.08); border-radius: 0.8rem; padding: 0.8rem 1rem; }
.profile-col h4 { font-size: 1.375rem; text-transform: uppercase; letter-spacing: 1px; color: rgba(255,255,255,0.6); margin: 0 0 0.4rem 0; }
.profile-col p  { font-size: 1.125rem; margin: 0.15rem 0; color: rgba(255,255,255,0.9); }
.section-title {
    font-size: 1.5rem; font-weight: 700; color: #1a1a2e;
    margin: 1.8rem 0 1rem 0; padding-bottom: 0.4rem;
    border-bottom: 2.5px solid #533483; display: inline-block;
}
.skill-card {
    background: #ffffff !important; border-radius: 0.8rem; padding: 0.9rem 1.1rem;
    margin-bottom: 0.6rem; box-shadow: 0 2px 10px rgba(0,0,0,0.06);
    display: flex; align-items: center; gap: 0.9rem;
}
.skill-icon { font-size: 1.4rem; width: 1.8rem; text-align: center; }
.skill-name { font-weight: 600; font-size: 1.125rem; color: #1a1a2e !important; min-width: 120px; white-space: nowrap; }
.skill-pct { font-size: 0.94rem; color: #999 !important; min-width: 30px; text-align: right; }
[data-testid="stAppViewContainer"] { background: #f8f9fa !important; }
</style>
""", unsafe_allow_html=True)

cert1_b64 = img_to_base64("images/사조사 자격증_1.png")
cert2_b64 = img_to_base64("images/직상 자격증_1.png")
cert3_b64 = img_to_base64("images/청상 자격증.jpeg")
cert4_b64 = img_to_base64("images/최우수상.png")

st.markdown(f"""
<div class="profile-card">
    <img src="https://ca.slack-edge.com/T088AB0N865-U09EHSCUNSF-3bef5911dc38-512"
         style="width:120px; height:120px; border-radius:50%; object-fit:cover; border:3px solid rgba(255,255,255,0.2); flex-shrink:0;">
    <div class="profile-info">
        <h1>김재경</h1>
        <p style="color:rgba(255,255,255,0.85); font-size:1.125rem; margin: 0.4rem 0 0.8rem 0; line-height:2;">
            <strong>● 통계 분석 역량:</strong> 데이터 이면의 숨겨진 맥락을 읽고, 인과추론, 회귀분석 등 다양한 통계기법을 활용할 수 있습니다.<br/>
            <strong>● End-to-End 역량:</strong> 데이터 수집부터 EDA, ML 모델링, 시각화에 이르는 전체 데이터 라이프사이클을 주도적으로 수행합니다.<br/>
            <strong>● 데이터 기반 문제 해결:</strong> 퍼널(Funnel) 분석 및 잔존율(Retention) 분석 등의 방법론을 활용해 지표를 진단하고 비즈니스 문제를 해결합니다.<br/>
            <strong>● 새로운 가치 창출:</strong> 비즈니스 성장은 물론, 고객의 일상에 실질적인 도움이 되는 새로운 가치를 끊임없이 탐구하고 발견하겠습니다.
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
                <p>🎓 단국대학교 | 심리학 학사 <br/> (2015.03 ~ 2020.02)</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">📋 자격증 & 수상이력 & 경력</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div style="background:rgba(255,255,255,0.05); border-radius:1rem; padding:1.2rem; border:1px solid rgba(255,255,255,0.1);">
        <h4 style="color:#533483; font-size:1.375rem; text-transform:uppercase; letter-spacing:1px; margin:0 0 0.8rem 0;">자격증</h4>
        <details style="margin-bottom:0.3rem;">
            <summary style="cursor:pointer; list-style:none; font-size:1.125rem; color:#1a1a2e; word-break:keep-all; overflow-wrap:break-word;">📜 사회조사분석사 2급<span style="font-size:0.94rem; color:#999; margin-left:0.8rem;">▶ 펼쳐보기</span></summary>
            <img src="data:image/png;base64,{cert1_b64}" style="width:100%; margin-top:0.5rem; border-radius:0.5rem;">
        </details>
        <details style="margin-bottom:0.3rem;">
            <summary style="cursor:pointer; list-style:none; font-size:1.125rem; color:#1a1a2e; word-break:keep-all; overflow-wrap:break-word;">📜 직업상담사 2급<span style="font-size:0.94rem; color:#999; margin-left:0.8rem;">▶ 펼쳐보기</span></summary>
            <img src="data:image/png;base64,{cert2_b64}" style="width:100%; margin-top:0.5rem; border-radius:0.5rem;">
        </details>
        <details style="margin-bottom:0.3rem;">
            <summary style="cursor:pointer; list-style:none; font-size:1.125rem; color:#1a1a2e; word-break:keep-all; overflow-wrap:break-word;">📜 청소년상담사 3급<span style="font-size:0.94rem; color:#999; margin-left:0.8rem;">▶ 펼쳐보기</span></summary>
            <img src="data:image/png;base64,{cert3_b64}" style="width:100%; margin-top:0.5rem; border-radius:0.5rem;">
        </details>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background:rgba(255,255,255,0.05); border-radius:1rem; padding:1.2rem; border:1px solid rgba(255,255,255,0.1);">
        <h4 style="color:#533483; font-size:1.25rem; text-transform:uppercase; letter-spacing:1px; margin:0 0 0.8rem 0;">수상이력</h4>
        <details style="margin-bottom:0.3rem;">
            <summary style="cursor:pointer; list-style:none; font-size:1.125rem; color:#1a1a2e; word-break:keep-all; overflow-wrap:break-word;">🏆 스파르타 최종 프로젝트 최우수상 (2026.03)<span style="font-size:0.94rem; color:#999; margin-left:0.8rem;">▶ 펼쳐보기</span></summary>
            <img src="data:image/png;base64,{cert4_b64}" style="width:100%; margin-top:0.5rem; border-radius:0.5rem;">
        </details>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background:rgba(255,255,255,0.05); border-radius:1rem; padding:1.2rem; border:1px solid rgba(255,255,255,0.1);">
        <h4 style="color:#533483; font-size:1.375rem; text-transform:uppercase; letter-spacing:1px; margin:0 0 0.8rem 0;">경력</h4>
        <details style="margin-bottom:0.3rem;">
            <summary style="cursor:pointer; list-style:none; font-size:1.125rem; color:#1a1a2e; word-break:keep-all; overflow-wrap:break-word;">🏢 테슬라 | 인턴 (2024.02 ~ 2024.05)<span style="font-size:0.94rem; color:#999; margin-left:0.8rem;">▶ 펼쳐보기</span></summary>
            <div style="margin-top:0.5rem; font-size:1.125rem; color:#444; line-height:1.7; word-break:keep-all;">
                <p>• 전기차 보조금 지원 신청</p>
                <p>• 누락 서류 파악 및 담당자에게 서류 정보 전달</p>
                <p>• 지자체 별 관련 공고문 정리</p>
            </div>
        </details>
        <details style="margin-bottom:0.3rem;">
            <summary style="cursor:pointer; list-style:none; font-size:1.125rem; color:#1a1a2e; word-break:keep-all; overflow-wrap:break-word;">🏢 스파르타 내일배움캠프 데이터분석가 과정 | 학생 (2025.10 ~ 2026.3)<span style="font-size:0.94rem; color:#999; margin-left:0.8rem;">▶ 펼쳐보기</span></summary>
            <div style="margin-top:0.5rem; font-size:1.125rem; color:#444; line-height:1.7; word-break:keep-all;">
                <p>• SQL, 파이썬, 데이터 분석 관련 하드스킬 학습</p>
                <p>• 프로젝트 진행</p>
                <p>• 데이터리터러시 능력, 사회통계역량 강화</p>
            </div>
        </details>
        <details style="margin-bottom:0.3rem;">
            <summary style="cursor:pointer; list-style:none; font-size:1.125rem; color:#1a1a2e; word-break:keep-all; overflow-wrap:break-word;">🏢 그리트라운지 | 팀장 (2024.05 ~ 2025.04)<span style="font-size:0.94rem; color:#999; margin-left:0.8rem;">▶ 펼쳐보기</span></summary>
            <div style="margin-top:0.5rem; font-size:1.125rem; color:#444; line-height:1.7; word-break:keep-all;">
                <p>• 테슬라 전기차 보조금 업무 인수인계 후 팀장으로 업무 확장</p>
                <p>• 전기차 보조금 지원신청</p>
                <p>• 이메일 제목에서 예약번호 추출 자동화</p>
                <p>• 신청 누락 방지 시스템 설계</p>
                <p>• 지자체 별 특이사항 혹은 고객 특이사항(영주권자, 재외동포, 타국 영주권 소지자)등 정리 후 공유</p>
                <p>• 지자체 별 공고문 정리</p>
            </div>
        </details>
        <details style="margin-bottom:0.3rem;">
            <summary style="cursor:pointer; list-style:none; font-size:1.125rem; color:#1a1a2e; word-break:keep-all; overflow-wrap:break-word;">🏢 위덕대학교 LINC3.0사업단 | 계약직 (2023.08 ~ 2023.10)<span style="font-size:0.94rem; color:#999; margin-left:0.8rem;">▶ 펼쳐보기</span></summary>
            <div style="margin-top:0.5rem; font-size:1.125rem; color:#444; line-height:1.7; word-break:keep-all;">
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

daiso_logo = img_to_html("assets/daiso.png", width=40)
starbucks_logo = img_to_html("assets/starbucks.png", width=40)

with col1:
    st.markdown(f"""
    <div style="background:#fff; border-radius:1rem; padding:1.5rem; box-shadow:0 2px 16px rgba(0,0,0,0.07); border-top: 4px solid #e60012; min-height:320px;">
        <div style="display:flex; align-items:center; gap:0.7rem; margin-bottom:0.8rem;">
            {daiso_logo}
            <strong style="font-size:1.375rem; color:#1a1a2e;">초저가를 넘어 초신뢰로</strong>
            <p style="margin-left:auto; margin-bottom:0;">🏆최우수상</p>
        </div>
        <p style="font-size:1.125rem; color:#444; margin-bottom:1rem;">다이소 뷰티 30만 건 리뷰 분석을 통한 2026년 성장 전략 도출</p>
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap; margin-bottom:1rem;">
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.94rem; color:#555;">RNN/LSTM</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.94rem; color:#555;">인과추론(PSM·IPTW·OW)</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.94rem; color:#555;">층화 샘플링</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.94rem; color:#555;">OCR</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.94rem; color:#555;">GIS 분석</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.94rem; color:#555;">DB 정규화</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.94rem; color:#555;">Tableau</span>
        </div>
        <div style="display:flex; gap:1.5rem; margin-bottom:1rem;">
            <div style="text-align:center;">
                <div style="font-size:1.3rem; font-weight:700; color:#e60012;">30만건</div>
                <div style="font-size:0.94rem; color:#888;">리뷰 데이터</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.3rem; font-weight:700; color:#e60012;">83.3%</div>
                <div style="font-size:0.94rem; color:#888;">연착륙 제품 중 스킨케어</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.3rem; font-weight:700; color:#e60012;">144%</div>
                <div style="font-size:0.94rem; color:#888;">뷰티 카테고리 성장률</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🟥 프로젝트 보기", use_container_width=True, key="proj1_btn"):
        st.switch_page("pages/1_프로젝트_1.py")

with col2:
    st.markdown(f"""
    <div style="background:#fff; border-radius:1rem; padding:1.5rem; box-shadow:0 2px 16px rgba(0,0,0,0.07); border-top: 4px solid #00704a; min-height:320px;">
        <div style="display:flex; align-items:center; gap:0.7rem; margin-bottom:0.8rem;">
            {starbucks_logo}
            <strong style="font-size:1.375rem; color:#1a1a2e;">Starbucks Next Level</strong>
        </div>
        <p style="font-size:1.125rem; color:#444; margin-bottom:1rem;">행동경제학 기반 프로모션 채널 효과 분석 및 고객 세그먼트 전략 수립</p>
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap; margin-bottom:1rem;">
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.94rem; color:#555;">K-means</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.94rem; color:#555;">엘보우 방법</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.94rem; color:#555;">Kruskal-Wallis</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.94rem; color:#555;">카이제곱 검정</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.94rem; color:#555;">행동경제학</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.2rem 0.7rem; font-size:0.94rem; color:#555;">Tableau</span>
        </div>
        <div style="display:flex; gap:1.5rem; margin-bottom:1rem;">
            <div style="text-align:center;">
                <div style="font-size:1.3rem; font-weight:700; color:#00704a;">43.97%p</div>
                <div style="font-size:0.94rem; color:#888;">SNS 채널 효과</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.3rem; font-weight:700; color:#00704a;">4개</div>
                <div style="font-size:0.94rem; color:#888;">고객 세그먼트</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.3rem; font-weight:700; color:#00704a;">3가지</div>
                <div style="font-size:0.94rem; color:#888;">행동경제학 인사이트</div>
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
    ('<img src="https://cdn.simpleicons.org/dbeaver" width="40" height="40" alt="DBeaver"/>', "DBeaver", 85),
('<img src="https://cdn.simpleicons.org/vscode" width="40" height="40" alt="VSCode"/>', "VS Code", 85)
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
            <div style="margin-left:auto; font-size:1.1rem; color:#e94560; letter-spacing:2px; text-align:right; display:flex; align-items:center; gap:0.3rem;">
                <span style="font-size:0.94rem; color:#999;">숙련도</span>
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
