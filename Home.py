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

st.markdown('<div class="section-title">📁 Projects</div>', unsafe_allow_html=True)

st.markdown(daiso_card, unsafe_allow_html=True)
if st.button("🟥 프로젝트 상세 보기", use_container_width=True, key="proj1_btn"):
    st.switch_page("pages/1_프로젝트_1.py")

st.markdown("<div style='margin-top:1rem;'></div>", unsafe_allow_html=True)

st.markdown(sbux_card, unsafe_allow_html=True)
if st.button("🟩 프로젝트 상세 보기", use_container_width=True, key="proj2_btn"):
    st.switch_page("pages/2_프로젝트_2.py")

daiso_logo = img_to_html("assets/daiso.png", width=40)
starbucks_logo = img_to_html("assets/starbucks.png", width=40)

daiso_card = f"""
<div style="background:#fff; border-radius:1rem; padding:1.5rem;max-width:860px;
            box-shadow:0 2px 12px rgba(0,0,0,0.06); border:1px solid #e8e8ee;
            border-top:4px solid #e60012;">
  <div style="display:flex; align-items:center; gap:0.7rem; margin-bottom:0.4rem;">
    {daiso_logo}
    <strong style="font-size:1.1rem; color:#1a1a2e;">초저가를 넘어 초신뢰로</strong>
    <span style="margin-left:auto; font-size:0.82rem; color:#e60012; font-weight:600;">🏆 최우수상</span>
  </div>
  <p style="font-size:0.88rem; color:#888; margin:0 0 1rem 0;">2026.02 ~ 03 &nbsp;|&nbsp; 5인 &nbsp;|&nbsp; SQL · Python · Tableau</p>
  <div style="background:#fff5f5; border-left:3px solid #e60012; border-radius:0 0.5rem 0.5rem 0; padding:0.6rem 0.9rem; margin-bottom:0.8rem;">
    <div style="font-size:0.72rem; font-weight:700; color:#e60012; letter-spacing:1px; margin-bottom:0.2rem;">PROBLEM</div>
    <div style="font-size:0.92rem; color:#1a1a2e; line-height:1.6;">
      144% 급성장 이면의 <b>납 검출 이슈 + 100% 사입 구조</b> → 단 1건의 사고로 전체 성장이 멈출 수 있는 구조적 결함
    </div>
  </div>
  <div style="background:#f8f5ff; border-left:3px solid #533483; border-radius:0 0.5rem 0.5rem 0; padding:0.6rem 0.9rem; margin-bottom:0.8rem;">
    <div style="font-size:0.72rem; font-weight:700; color:#533483; letter-spacing:1px; margin-bottom:0.3rem;">APPROACH</div>
    <div style="font-size:0.88rem; color:#1a1a2e; line-height:1.8;">
      ① OCR 파이프라인으로 900여 제품 전성분 정형화<br>
      ② PSM·IPTW·OW 인과추론으로 매출 동인 우선순위 확정<br>
      ③ GIS 수요 밀도 점수 설계 → Hub 매장 재고 전략 도출
    </div>
  </div>
  <div style="display:flex; gap:0.8rem; margin-bottom:0.8rem; padding-top:0.8rem; border-top:1px solid #f0f0f5;">
    <div style="flex:1; text-align:center; background:#f8f9fa; border-radius:0.6rem; padding:0.6rem 0.3rem;">
      <div style="font-size:1.3rem; font-weight:700; color:#e60012;">16.7%</div>
      <div style="font-size:0.75rem; color:#888; margin-top:0.1rem;">연착륙 제품 비율</div>
      <div style="font-size:0.75rem; color:#555;">→ 매출 32.5% 견인</div>
    </div>
    <div style="flex:1; text-align:center; background:#f8f9fa; border-radius:0.6rem; padding:0.6rem 0.3rem;">
      <div style="font-size:1.3rem; font-weight:700; color:#e60012;">83.3%</div>
      <div style="font-size:0.75rem; color:#888; margin-top:0.1rem;">연착륙 중 스킨케어</div>
      <div style="font-size:0.75rem; color:#555;">→ 5,000원 기초 제품</div>
    </div>
    <div style="flex:1; text-align:center; background:#f8f9fa; border-radius:0.6rem; padding:0.6rem 0.3rem;">
      <div style="font-size:1.3rem; font-weight:700; color:#e60012;">30만건</div>
      <div style="font-size:0.75rem; color:#888; margin-top:0.1rem;">리뷰 데이터 정제</div>
      <div style="font-size:0.75rem; color:#555;">→ 입점 시뮬레이터</div>
    </div>
  </div>
  <div style="background:#1a1a2e; border-radius:0.5rem; padding:0.6rem 0.9rem; margin-bottom:0.8rem;">
    <span style="font-size:0.72rem; font-weight:700; color:#e60012; letter-spacing:1px;">KEY INSIGHT &nbsp;</span>
    <span style="font-size:0.85rem; color:#e8e8ee;">기능성 성분은 단독 효과 없음 — 카테고리 신뢰와 결합 시 증폭되는 조절 변수</span>
  </div>
  <div style="display:flex; gap:0.35rem; flex-wrap:wrap;">
    <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.82rem; color:#1a1a2e;">인과추론(PSM·IPTW·OW)</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.82rem; color:#1a1a2e;">생존분석</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.82rem; color:#1a1a2e;">OCR</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.82rem; color:#1a1a2e;">GIS</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.82rem; color:#1a1a2e;">RNN/LSTM</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.82rem; color:#1a1a2e;">Tableau</span>
  </div>
</div>
"""

sbux_card = f"""
<div style="background:#fff; border-radius:1rem; padding:1.5rem;
            box-shadow:0 2px 12px rgba(0,0,0,0.06); border:1px solid #e8e8ee;
            border-top:4px solid #00704a;">
  <div style="display:flex; align-items:center; gap:0.7rem; margin-bottom:0.4rem;">
    {starbucks_logo}
    <strong style="font-size:1.1rem; color:#1a1a2e;">Starbucks Next Level</strong>
  </div>
  <p style="font-size:0.88rem; color:#888; margin:0 0 1rem 0;">2026.01 &nbsp;|&nbsp; 5인 &nbsp;|&nbsp; SQL · Python · Tableau</p>
  <div style="background:#f0faf5; border-left:3px solid #00704a; border-radius:0 0.5rem 0.5rem 0; padding:0.6rem 0.9rem; margin-bottom:0.8rem;">
    <div style="font-size:0.72rem; font-weight:700; color:#00704a; letter-spacing:1px; margin-bottom:0.2rem;">PROBLEM</div>
    <div style="font-size:0.92rem; color:#1a1a2e; line-height:1.6;">
      채널별 순수 기여도 불명확 → <b>비효율적 예산 배분</b>과 무분별한 메시지 발송으로 인한 고객 피로도 가중
    </div>
  </div>
  <div style="background:#f8f5ff; border-left:3px solid #533483; border-radius:0 0.5rem 0.5rem 0; padding:0.6rem 0.9rem; margin-bottom:0.8rem;">
    <div style="font-size:0.72rem; font-weight:700; color:#533483; letter-spacing:1px; margin-bottom:0.3rem;">APPROACH</div>
    <div style="font-size:0.88rem; color:#1a1a2e; line-height:1.8;">
      ① K-means로 고객 반응 패턴 4개 세그먼트 분류<br>
      ② 카이제곱 검정으로 채널 독립 효과 통계 검증<br>
      ③ 행동경제학 3가지 프레임으로 전환 트리거 분석
    </div>
  </div>
  <div style="display:flex; gap:0.8rem; margin-bottom:0.8rem; padding-top:0.8rem; border-top:1px solid #f0f0f5;">
    <div style="flex:1; text-align:center; background:#f8f9fa; border-radius:0.6rem; padding:0.6rem 0.3rem;">
      <div style="font-size:1.3rem; font-weight:700; color:#00704a;">43.97%p</div>
      <div style="font-size:0.75rem; color:#888; margin-top:0.1rem;">SNS 채널 효과</div>
      <div style="font-size:0.75rem; color:#555;">Web 대비 압도적</div>
    </div>
    <div style="flex:1; text-align:center; background:#f8f9fa; border-radius:0.6rem; padding:0.6rem 0.3rem;">
      <div style="font-size:1.3rem; font-weight:700; color:#00704a;">2.4배</div>
      <div style="font-size:0.75rem; color:#888; margin-top:0.1rem;">3채널 중복 효과</div>
      <div style="font-size:0.75rem; color:#555;">완료율 50% 달성</div>
    </div>
    <div style="flex:1; text-align:center; background:#f8f9fa; border-radius:0.6rem; padding:0.6rem 0.3rem;">
      <div style="font-size:1.3rem; font-weight:700; color:#00704a;">4개</div>
      <div style="font-size:0.75rem; color:#888; margin-top:0.1rem;">고객 세그먼트</div>
      <div style="font-size:0.75rem; color:#555;">행동 기반 분류</div>
    </div>
  </div>
  <div style="background:#1a1a2e; border-radius:0.5rem; padding:0.6rem 0.9rem; margin-bottom:0.8rem;">
    <span style="font-size:0.72rem; font-weight:700; color:#00704a; letter-spacing:1px;">KEY INSIGHT &nbsp;</span>
    <span style="font-size:0.85rem; color:#e8e8ee;">고액 할인보다 실질 지불액 최소화가 전환율 3배 — 손실 회피 심리 작동</span>
  </div>
  <div style="display:flex; gap:0.35rem; flex-wrap:wrap;">
    <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.82rem; color:#1a1a2e;">K-means</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.82rem; color:#1a1a2e;">카이제곱 검정</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.82rem; color:#1a1a2e;">Kruskal-Wallis</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.82rem; color:#1a1a2e;">행동경제학</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.82rem; color:#1a1a2e;">Tableau</span>
  </div>
</div>
"""

with col1:
    st.markdown(daiso_card, unsafe_allow_html=True)
    if st.button("🟥 프로젝트 상세 보기", use_container_width=True, key="proj1_btn"):
        st.switch_page("pages/1_프로젝트_1.py")

with col2:
    st.markdown(sbux_card, unsafe_allow_html=True)
    if st.button("🟩 프로젝트 상세 보기", use_container_width=True, key="proj2_btn"):
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


