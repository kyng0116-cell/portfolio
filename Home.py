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

st.markdown("""
<p style="font-size:1.25rem; color:#1a1a2e; margin: 0 0 0.8rem 0.2rem; letter-spacing:0.3px; font-weight:700;">
    심리학적 사고로 소비자 행동을 해석하고, 데이터로 비즈니스 문제를 풀어내는 데이터 분석가입니다.
</p>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <style>
    /* 사이드바 — 밝은 흰색 계열, 회색 배경과 통일 */
    section[data-testid="stSidebar"],
    section[data-testid="stSidebar"] > div,
    section[data-testid="stSidebar"] > div > div,
    section[data-testid="stSidebar"] > div > div > div {
        background-color: #ffffff !important;
        background-image: none !important;
    }
    section[data-testid="stSidebar"] * { color: #1a1a2e !important; }
    section[data-testid="stSidebar"] hr { border-color: rgba(26,26,46,0.1) !important; }
    section[data-testid="stSidebar"] .stButton > button {
        background: transparent !important;
        border: 1px solid rgba(26,26,46,0.15) !important;
        color: #1a1a2e !important;
        text-align: left !important;
        border-radius: 0.5rem !important;
        font-size: 0.9rem !important;
        transition: all 0.18s;
    }
    section[data-testid="stSidebar"] .stButton > button:hover {
        background: #f0f0f5 !important;
        border-color: #533483 !important;
    }
    [data-testid="stSidebarNav"] { display: none !important; }
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

/* 배경 — 원본 회색 유지 */
[data-testid="stAppViewContainer"] { background: #f8f9fa !important; }
[data-testid="stHeader"] { background: #f8f9fa !important; }
.stApp { background: #f8f9fa !important; }

/* 프로필 카드 — 흰색 밝은 계열, 회색 배경 위에 자연스럽게 */
.profile-card {
    display: flex; align-items: flex-start; gap: 2.5rem;
    padding: 2.5rem;
    background: #ffffff;
    border-radius: 1.2rem; color: #1a1a2e; margin-bottom: 2rem;
    box-shadow: 0 2px 20px rgba(26,26,46,0.08);
    border: 1px solid #e8e8ee;
    height: auto; min-height: fit-content;
}
.profile-info { flex: 1; width: 100%; min-width: 0; }
.profile-info h1 { font-size: 1.9rem; font-weight: 700; margin: 0 0 0.3rem 0; color: #1a1a2e; }
.profile-cols { display: flex; gap: 1rem; margin-top: 0.5rem; flex-wrap: wrap; width: 100%; }
.profile-col {
    min-width: 160px; flex: 1;
    background: #f8f9fa;
    border-radius: 0.8rem; padding: 0.8rem 1rem;
    border: 1px solid #e8e8ee;
}
.profile-col h4 {
    font-size: 0.72rem; text-transform: uppercase; letter-spacing: 1.5px;
    color: #888; margin: 0 0 0.4rem 0; font-weight: 600;
}
.profile-col p  { font-size: 1rem; margin: 0.18rem 0; color: #1a1a2e; }
.profile-col a  { color: #533483 !important; text-decoration: underline; text-underline-offset: 2px; font-weight: 500; }
.profile-col a:hover { color: #3b2470 !important; }

.section-title {
    font-size: 1.5rem; font-weight: 700; color: #1a1a2e;
    margin: 1.8rem 0 1rem 0; padding-bottom: 0.4rem;
    border-bottom: 2.5px solid #533483; display: inline-block;
}
.skill-card {
    background: #ffffff !important; border-radius: 0.8rem; padding: 0.9rem 1.1rem;
    margin-bottom: 0.6rem; box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    border: 1px solid #e8e8ee;
    display: flex; align-items: center; gap: 0.9rem;
}
.skill-icon { font-size: 1.4rem; width: 1.8rem; text-align: center; }
.skill-name { font-weight: 600; font-size: 1.125rem; color: #1a1a2e !important; min-width: 120px; white-space: nowrap; }
summary { outline: none; }
details summary::-webkit-details-marker { display: none; }
</style>
""", unsafe_allow_html=True)

cert1_b64 = img_to_base64("images/사조사 자격증_1.png")
cert2_b64 = img_to_base64("images/직상 자격증_1.png")
cert3_b64 = img_to_base64("images/청상 자격증.jpeg")
cert4_b64 = img_to_base64("images/최우수상.png")
pdf_b64 = img_to_base64("assets/김재경_포트폴리오.pdf")  # ← 추가


st.markdown(f"""
<div class="profile-card">
    <img src="https://ca.slack-edge.com/T088AB0N865-U09EHSCUNSF-3bef5911dc38-512"
         style="width:120px; height:120px; border-radius:50%; object-fit:cover;
                border:3px solid #e8e8ee; flex-shrink:0;
                box-shadow:0 2px 12px rgba(0,0,0,0.10);">
    <div class="profile-info">
        <h1 style="display:flex; align-items:center; gap:1rem;">
            김재경
            <a href="data:application/pdf;base64,{pdf_b64}"
                download="김재경_포트폴리오.pdf"
                style="font-size:0.82rem; font-weight:600; color:#533483;
                    border:1.5px solid #533483; border-radius:99px;
                    padding:0.25rem 0.8rem; text-decoration:none;
                    white-space:nowrap; letter-spacing:0.3px;">
                📄 포트폴리오 PDF 다운로드
            </a>
        </h1>
        <p style="color:#1a1a2e; font-size:1.05rem; margin: 0.4rem 0 0.8rem 0; line-height:2;">
            <strong>● 통계 분석:</strong> 숫자 뒤에 숨은 맥락을 읽고, 인과추론·회귀분석 등 다양한 통계 기법으로 데이터를 해석합니다.<br/>
            <strong>● End-to-End 분석:</strong> 데이터 수집부터 EDA, ML 모델링, 시각화에 이르는 전체 분석 과정을 빠짐없이 수행합니다.<br/>
            <strong>● 문제 해결:</strong> 퍼널·잔존율 분석 등을 활용해 지표를 진단하고, 비즈니스 문제의 원인을 데이터로 찾아냅니다.<br/>
            <strong>● 가치 창출:</strong> 비즈니스 성장뿐만 아니라 고객 일상에 실질적인 도움이 되는 인사이트를 끊임없이 탐구합니다.<br/>
            <strong>● 데이터 시각화:</strong> Tableau로 복잡한 데이터를 직관적인 대시보드로 구현해 빠른 의사결정을 지원합니다.
        </p>
        <div class="profile-cols">
            <div class="profile-col">
                <h4>연락처</h4>
                <p>📧 kyng0116@gmail.com</p>
                <p>🔗 <a href="https://github.com/kyng0116-cell" target="_blank">GitHub</a></p>
                <p>🔗 <a href="https://www.linkedin.com/in/재경-김-6061463b7/" target="_blank">LinkedIn</a></p>
            </div>
            <div class="profile-col">
                <h4>학력</h4>
                <p>🎓 단국대학교 | 심리학 학사 <br/> (2015.03 ~ 2020.02)</p>
            </div>
            <div class="profile-col">
                <h4>수상이력</h4>
                <details style="margin-bottom:0.3rem;">
                    <summary style="cursor:pointer; list-style:none; font-size:0.92rem; color:#1a1a2e;">
                        🏆 스파르타 최종 프로젝트 최우수상 (2026.03)
                        <span style="font-size:0.88rem; color:#aaa; margin-left:0.5rem;"><br/>▶ 펼쳐보기</span>
                    </summary>
                    <img src="data:image/png;base64,{cert4_b64}" style="width:400px; margin-top:0.5rem; border-radius:0.5rem;">
                </details>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

daiso_logo = img_to_html("assets/daiso.png", width=36)
starbucks_logo = img_to_html("assets/starbucks.png", width=36)
st.markdown('<div class="section-title">Main Project : 다이소 뷰티 전략 분석</div>', unsafe_allow_html=True)

daiso_card_html = f"""
<div class="project-card" style="border-top:5px solid #e60012;">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:15px;">
        {daiso_logo} <strong style="font-size:1.4rem;">초저가를 넘어 '초신뢰' 브랜드로의 전환 전략</strong>
        <span style="margin-left:auto; background:#fff0f0; color:#e60012; padding:4px 12px; border-radius:15px; font-size:0.85rem; font-weight:700;">최우수상 수상</span>
    </div>

    <div style="display:grid; grid-template-columns: 1.2fr 1.8fr; gap:20px;">
        <div style="background:#fff5f5; padding:1.2rem; border-radius:12px;">
            <h4 style="color:#e60012; margin-top:0;">🚩 Problem Definition</h4>
            <ul style="font-size:0.92rem; color:#444; padding-left:20px;">
                <li><b>성장의 역설:</b> 144% 급성장(4천억 매출) 이면의 납 검출 등 품질 이슈 발생</li>
                <li><b>구조적 위협:</b> 100% 사입 구조로 인해 단 한 번의 품질 사고가 브랜드 전체의 생존을 위협</li>
                <li><b>분석 질문:</b> "초저가 이미지를 유지하면서 어떻게 '초신뢰' 브랜드를 구축할 것인가?"</li>
            </ul>
        </div>
        <div style="background:#f9f9f9; padding:1.2rem; border-radius:12px; border:1px solid #eee;">
            <h4 style="color:#1a1a2e; margin-top:0;">🛠 Solution & <span style="color:#533483;">My Contribution</span></h4>
            <div style="font-size:0.9rem; line-height:1.6;">
                <p><span class="contribution-badge">내 기여</span> <b>OCR 파이프라인 구축:</b> Clova/EasyOCR 교차 검증으로 30만 건의 비정형 데이터 정형화</p>
                <p><span class="contribution-badge">내 기여</span> <b>인과추론 분석:</b> PSM·IPTW·OW 기법을 통해 성분-브랜드 간 '상호작용 효과' 규명</p>
                <p><b>GIS 알고리즘:</b> 유동인구·외국인 비중 z-score 표준화 기반 Hub 매장 재고 전략 도출</p>
            </div>
        </div>
    </div>

    <div style="display:grid; grid-template-columns: repeat(3, 1fr); gap:15px; margin-top:20px;">
        <div style="text-align:center; padding:15px; background:#f8f9fa; border-radius:10px;">
            <div style="font-size:1.8rem; font-weight:800; color:#e60012;">32.5%</div>
            <div style="font-size:0.85rem; color:#666;">연착륙 제품 매출 견인율</div>
        </div>
        <div style="text-align:center; padding:15px; background:#f8f9fa; border-radius:10px;">
            <div style="font-size:1.8rem; font-weight:800; color:#533483;">Interaction</div>
            <div style="font-size:0.85rem; color:#666;">기능성 성분 x 브랜드 신뢰 효과</div>
        </div>
        <div style="text-align:center; padding:15px; background:#f8f9fa; border-radius:10px;">
            <div style="font-size:1.8rem; font-weight:800; color:#0056b3;">Hub 전략</div>
            <div style="font-size:0.85rem; color:#666;">상권별 입점 시뮬레이터 개발</div>
        </div>
    </div>
    <div style="margin-top:15px; padding:12px; background:#1a1a2e; color:#e8e8ee; border-radius:8px; font-size:0.95rem;">
        💡 <b>Insight:</b> 분석은 현상 설명이 아닌 의사결정 도구여야 합니다. 성분 단독 효과보다 <b>'카테고리 신뢰'</b>가 결합될 때 구매 전환이 폭발함을 데이터로 증명했습니다.
    </div>
</div>
"""
st.markdown(daiso_card_html, unsafe_allow_html=True)
if st.button("🟥 다이소 프로젝트 상세 분석 보기", use_container_width=True):
    st.switch_page("pages/1_프로젝트_1.py")


# 3. 서브 프로젝트 (스타벅스)
st.markdown('<div class="section-title">Sub Project : Starbucks Next Level</div>', unsafe_allow_html=True)

sbux_card_html = f"""
<div class="project-card" style="border-top:5px solid #00704a;">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:15px;">
        {starbucks_logo} <strong style="font-size:1.4rem;">채널별 전환 트리거 정량화 및 행동경제학적 해석</strong>
    </div>
    
    <div style="display:grid; grid-template-columns: 1fr 1fr; gap:20px;">
        <div style="font-size:0.92rem; line-height:1.7;">
            <p><b>핵심 질문:</b> "어떤 트리거가 고객의 결제 버튼을 누르게 만드는가?"</p>
            <p><span class="contribution-badge">내 기여</span> <b>통계 검증:</b> 카이제곱 검정으로 SNS 채널의 압도적 효율(Web 대비 +43.9%p) 규명</p>
            <p><span class="contribution-badge">내 기여</span> <b>심리 모델링:</b> 손실 회피 및 사회적 증거 이론을 데이터 패턴과 연결해 해석</p>
        </div>
        <div style="background:#f0faf5; padding:1rem; border-radius:10px; font-size:0.9rem;">
            <ul style="margin:0; padding-left:15px;">
                <li><b>SNS 전환율:</b> 43.97%p (Web 7.16%p 대비 압도적 우위)</li>
                <li><b>멀티채널 시너지:</b> 3개 채널 노출 시 완료율 50% (2.4배 상승)</li>
                <li><b>리워드 설계:</b> 고액 할인보다 '낮은 실질 지불액'이 전환에 3배 효과</li>
            </ul>
        </div>
    </div>
</div>
"""
st.markdown(sbux_card_html, unsafe_allow_html=True)
if st.button("🟩 스타벅스 프로젝트 상세 분석 보기", use_container_width=True):
    st.switch_page("pages/2_프로젝트_2.py")

st.markdown('<div class="section-title">🛠 Skills</div>', unsafe_allow_html=True)

tools = [
    (img_to_html("assets/tableau.png"), "Tableau", 80),
    ('<img src="https://cdn.simpleicons.org/mysql" width="40" height="40" alt="MySQL"/>', "MySQL", 80),
    ('<img src="https://cdn.simpleicons.org/jupyter" width="40" height="40" alt="Jupyter"/>', "Jupyter Notebook", 60),
    ('<img src="https://cdn.simpleicons.org/dbeaver" width="40" height="40" alt="DBeaver"/>', "DBeaver", 80),
    (img_to_html("assets/vscode.png"), "VS Code", 85),
    ('<img src="https://cdn.simpleicons.org/qgis" width="40" height="40" alt="QGIS"/>', "QGIS", 60)
]
languages = [
    ('<img src="https://cdn.simpleicons.org/python" width="40" height="40" alt="Python"/>', "Python", 60),
    (img_to_html("assets/SQL.png"), "SQL", 80),
]
libraries = [
    ('<img src="https://cdn.simpleicons.org/pandas" width="40" height="40" alt="Pandas"/>', "Pandas", 80),
    (img_to_html("assets/matplotlib.png"), "Matplotlib", 80),
    (img_to_html("assets/seaborn.png"), "Seaborn", 80),
    ('<img src="https://cdn.simpleicons.org/scikitlearn" width="40" height="40" alt="Scikit-learn"/>', "Scikit-learn", 60),
    ("🗺", "Folium", 60),
    (img_to_html("assets/scipy.png"), "Scipy", 60),
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
            <div style="margin-left:auto; font-size:1.1rem; letter-spacing:2px; text-align:right; display:flex; align-items:center; gap:0.3rem;">
                <span style="font-size:0.88rem; color:#aaa;">숙련도</span>
                <span style="color:#e94560;">{filled}</span><span style="color:#ddd;">{empty}</span>
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


