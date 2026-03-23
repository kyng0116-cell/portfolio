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

# ── 사이드바 ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <style>
    section[data-testid="stSidebar"] > div:first-child {
        background: linear-gradient(160deg, #2b1a4a 0%, #3d2563 100%) !important;
    }
    section[data-testid="stSidebar"] { background: #2b1a4a !important; }
    section[data-testid="stSidebar"] * { color: #e8dcff !important; }
    section[data-testid="stSidebar"] hr { border-color: rgba(200,180,255,0.2) !important; }
    section[data-testid="stSidebar"] .stButton > button {
        background: transparent !important;
        border: 1px solid rgba(200,180,255,0.25) !important;
        color: #e8dcff !important;
        text-align: left !important;
        border-radius: 0.5rem !important;
        transition: all 0.2s;
    }
    section[data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(200,180,255,0.12) !important;
        border-color: #b39ddb !important;
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

# ── 전체 CSS ─────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif;
    letter-spacing: 0.5px;
}
* { word-break: keep-all !important; overflow-wrap: break-word !important; }
strong { font-size: 1.25rem !important; }

/* ── 전체 배경: 진짜 크림 ── */
[data-testid="stAppViewContainer"] > .main {
    background-color: #faf6ef !important;
}
[data-testid="stAppViewContainer"] { background-color: #faf6ef !important; }
[data-testid="stHeader"] { background-color: #faf6ef !important; }
.stApp { background-color: #faf6ef !important; }

/* ── 프로필 카드: 선명한 라일락 ── */
.profile-card {
    display: flex; align-items: flex-start; gap: 2.5rem;
    padding: 2.5rem;
    background: linear-gradient(135deg, #b39ddb 0%, #9b7ec8 50%, #a084c8 100%);
    border-radius: 1.4rem; color: #1a1a2e; margin-bottom: 2rem;
    box-shadow: 0 8px 32px rgba(83,52,131,0.20); border: none;
    height: auto; min-height: fit-content;
}
.profile-info { flex: 1; width: 100%; min-width: 0; }
.profile-info h1 {
    font-size: 1.9rem; font-weight: 700; margin: 0 0 0.3rem 0;
    color: #fff; text-shadow: 0 1px 4px rgba(0,0,0,0.12);
}
.profile-desc {
    color: #f0eaff; font-size: 1.05rem; margin: 0.4rem 0 0.8rem 0; line-height: 2;
}
.profile-desc strong { color: #fff !important; font-weight: 700; }

.profile-cols { display: flex; gap: 1rem; margin-top: 0.5rem; flex-wrap: wrap; width: 100%; }
.profile-col {
    min-width: 160px; flex: 1;
    background: rgba(255,255,255,0.22); backdrop-filter: blur(8px);
    border-radius: 0.8rem; padding: 0.8rem 1rem;
    border: 1px solid rgba(255,255,255,0.3);
}
.profile-col h4 {
    font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1.5px;
    color: rgba(255,255,255,0.7); margin: 0 0 0.5rem 0; font-weight: 600;
}
.profile-col p { font-size: 0.95rem; margin: 0.2rem 0; color: #fff; }
.profile-col a { color: #fff !important; font-weight: 600; text-decoration: underline; text-underline-offset: 2px; }

/* ── 섹션 타이틀 ── */
.section-title {
    font-size: 1.35rem; font-weight: 700; color: #2b1a4a;
    margin: 2rem 0 1rem 0; padding-bottom: 0.4rem;
    border-bottom: 2.5px solid #7c5cbf; display: inline-block; letter-spacing: 0.5px;
}

/* ── 카드 공통 ── */
.card-box {
    background: #fff !important; border-radius: 1rem; padding: 1.4rem;
    border: 1px solid #e8e0f5; box-shadow: 0 2px 12px rgba(83,52,131,0.07);
}

/* ── 스킬 카드 ── */
.skill-card {
    background: #fff !important; border-radius: 0.75rem; padding: 0.85rem 1.1rem;
    margin-bottom: 0.55rem; box-shadow: 0 1px 6px rgba(83,52,131,0.08);
    border: 1px solid #ede5ff; display: flex; align-items: center; gap: 0.9rem;
}
.skill-icon { font-size: 1.4rem; width: 1.8rem; text-align: center; }
.skill-name { font-weight: 600; font-size: 1rem; color: #1a1a2e !important; min-width: 120px; white-space: nowrap; }

/* ── 배지 태그 ── */
.badge-purple {
    background: #ede5ff; border-radius: 99px; padding: 0.2rem 0.75rem;
    font-size: 0.88rem; color: #533483; font-weight: 500;
}
.badge-green {
    background: #e6f4ee; border-radius: 99px; padding: 0.2rem 0.75rem;
    font-size: 0.88rem; color: #00704a; font-weight: 500;
}
.hint { font-size: 0.88rem; color: #b39ddb; margin-left: 0.8rem; }
summary { outline: none; }
details summary::-webkit-details-marker { display: none; }

/* ── 프로젝트 카드 ── */
.proj-card {
    background: #fff; border-radius: 1rem; padding: 1.5rem;
    box-shadow: 0 2px 16px rgba(83,52,131,0.08);
    border: 1px solid #e8e0f5; min-height: 320px;
}
</style>
""", unsafe_allow_html=True)

# ── 이미지 로드 ──────────────────────────────────────────────
cert1_b64 = img_to_base64("images/사조사 자격증_1.png")
cert2_b64 = img_to_base64("images/직상 자격증_1.png")
cert3_b64 = img_to_base64("images/청상 자격증.jpeg")
cert4_b64 = img_to_base64("images/최우수상.png")

# ── 프로필 카드 ──────────────────────────────────────────────
st.markdown(f"""
<div class="profile-card">
    <img src="https://ca.slack-edge.com/T088AB0N865-U09EHSCUNSF-3bef5911dc38-512"
         style="width:120px; height:120px; border-radius:50%; object-fit:cover;
                border:3px solid rgba(255,255,255,0.5); flex-shrink:0;
                box-shadow:0 4px 18px rgba(0,0,0,0.18);">
    <div class="profile-info">
        <h1>김재경</h1>
        <p class="profile-desc">
            <strong>● 통계 분석 역량:</strong> 데이터 이면의 숨겨진 맥락을 읽고, 인과추론, 회귀분석 등 다양한 통계기법을 활용할 수 있습니다.<br/>
            <strong>● End-to-End 역량:</strong> 데이터 수집부터 EDA, ML 모델링, 시각화에 이르는 전체 데이터 라이프사이클을 주도적으로 수행합니다.<br/>
            <strong>● 데이터 기반 문제 해결:</strong> 퍼널(Funnel) 분석 및 잔존율(Retention) 분석 등의 방법론을 활용해 지표를 진단하고 비즈니스 문제를 해결합니다.<br/>
            <strong>● 새로운 가치 창출:</strong> 비즈니스 성장은 물론, 고객의 일상에 실질적인 도움이 되는 새로운 가치를 끊임없이 탐구하고 발견하겠습니다.<br/>
            <strong>● 직관적인 데이터 시각화:</strong> 태블로(Tableau)를 활용해 복잡한 데이터를 직관적인 대시보드로 구현하고, 이해관계자의 빠르고 정확한 데이터 기반 의사결정을 지원합니다.
        </p>
        <div class="profile-cols">
            <div class="profile-col">
                <h4>연락처</h4>
                <p>📧 kyng0116@gmail.com</p>
                <p>📱 010-5021-9745</p>
                <p>🔗 <a href="https://github.com/kyng0116-cell" target="_blank">GitHub</a></p>
                <p>🔗 <a href="https://www.linkedin.com/in/재경-김-6061463b7/" target="_blank">LinkedIn</a></p>
            </div>
            <div class="profile-col">
                <h4>학력</h4>
                <p>🎓 단국대학교 | 심리학 학사<br/>(2015.03 ~ 2020.02)</p>
            </div>
            <div class="profile-col">
                <h4>수상이력</h4>
                <details style="margin-bottom:0.3rem;">
                    <summary style="cursor:pointer; list-style:none; font-size:0.92rem; color:#fff;">
                        🏆 스파르타 최종 프로젝트 최우수상 (2026.03)
                        <span class="hint"><br/>▶ 펼쳐보기</span>
                    </summary>
                    <img src="data:image/png;base64,{cert4_b64}" style="width:400px; margin-top:0.5rem; border-radius:0.5rem;">
                </details>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── 자격증 & 경력 ─────────────────────────────────────────────
st.markdown('<div class="section-title">📋 자격증 & 경력</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="card-box">
        <h4 style="color:#533483; font-size:1rem; text-transform:uppercase; letter-spacing:1.5px; margin:0 0 0.9rem 0; font-weight:700;">자격증</h4>
        <details style="margin-bottom:0.5rem;">
            <summary style="cursor:pointer; list-style:none; font-size:1rem; color:#2b1a4a; font-weight:500;">
                📜 사회조사분석사 2급<span class="hint">▶ 펼쳐보기</span>
            </summary>
            <img src="data:image/png;base64,{cert1_b64}" style="width:100%; margin-top:0.5rem; border-radius:0.5rem;">
        </details>
        <details style="margin-bottom:0.5rem;">
            <summary style="cursor:pointer; list-style:none; font-size:1rem; color:#2b1a4a; font-weight:500;">
                📜 직업상담사 2급<span class="hint">▶ 펼쳐보기</span>
            </summary>
            <img src="data:image/png;base64,{cert2_b64}" style="width:100%; margin-top:0.5rem; border-radius:0.5rem;">
        </details>
        <details style="margin-bottom:0.5rem;">
            <summary style="cursor:pointer; list-style:none; font-size:1rem; color:#2b1a4a; font-weight:500;">
                📜 청소년상담사 3급<span class="hint">▶ 펼쳐보기</span>
            </summary>
            <img src="data:image/png;base64,{cert3_b64}" style="width:100%; margin-top:0.5rem; border-radius:0.5rem;">
        </details>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card-box">
        <h4 style="color:#533483; font-size:1rem; text-transform:uppercase; letter-spacing:1.5px; margin:0 0 0.9rem 0; font-weight:700;">경력</h4>
        <details style="margin-bottom:0.5rem;">
            <summary style="cursor:pointer; list-style:none; font-size:1rem; color:#2b1a4a; font-weight:500;">
                🏢 스파르타 내일배움캠프 데이터분석가 과정 | 학생 (2025.10 ~ 2026.3)<span class="hint">▶ 펼쳐보기</span>
            </summary>
            <div style="margin-top:0.6rem; font-size:0.95rem; color:#444; line-height:1.8; padding-left:1rem;">
                <p>• <span style="color:#533483; font-weight:600;">데이터 시각화 및 대시보드 구축:</span> Tableau를 활용한 비즈니스 지표 시각화 및 Streamlit 기반의 인터랙티브 데이터 분석 포트폴리오 웹사이트 기획<br/>
                • <span style="color:#533483; font-weight:600;">실무 밀착형 프로젝트 주도:</span> 유통/뷰티 도메인(다이소 등)을 포함하여 비즈니스 문제 정의부터 결론 도출까지 총 4개의 데이터 분석 프로젝트 완수<br/>
                • <span style="color:#533483; font-weight:600;">고급 분석 방법론 적용:</span> 인과추론, 통계적 가설 검정, 데이터 리터러시 역량을 바탕으로 단순 집계를 넘어선 논리적 비즈니스 인사이트 도출 훈련</p>
            </div>
        </details>
        <details style="margin-bottom:0.5rem;">
            <summary style="cursor:pointer; list-style:none; font-size:1rem; color:#2b1a4a; font-weight:500;">
                🏢 그리트라운지 | 팀장 (2024.05 ~ 2025.04)<span class="hint">▶ 펼쳐보기</span>
            </summary>
            <div style="margin-top:0.6rem; font-size:0.95rem; color:#444; line-height:1.8; padding-left:1rem;">
                <p>• <span style="color:#533483; font-weight:600;">업무 프로세스 자동화 및 효율성 증대:</span> Google Apps Script(GAS)를 활용해 이메일 제목 내 회원/예약 번호를 일괄 추출하는 자동화 스크립트를 직접 개발하여 업무 소요 시간 대폭 단축<br/>
                • <span style="color:#533483; font-weight:600;">데이터 트래킹 시스템 기획 및 운영:</span> 수천 건의 전기차 보조금 신청건에 대한 누락 방지 트래킹 시스템을 설계하여 신청 성공률 및 운영 안정성 극대화<br/>
                • <span style="color:#533483; font-weight:600;">비정형 데이터의 정형화 및 지식 자산화:</span> 전국 지자체별 복잡한 공고문과 특이 고객의 케이스 데이터를 규격화하고 가이드라인으로 배포하여 팀원들의 업무 혼선 방지<br/>
                • <span style="color:#533483; font-weight:600;">팀 리딩 및 인수인계 총괄:</span> 테슬라 전기차 보조금 실무 전반을 성공적으로 이관받고, 팀장으로서 프로젝트 진행 상황 데이터화 및 리포팅 수행</p>
            </div>
        </details>
        <details style="margin-bottom:0.5rem;">
            <summary style="cursor:pointer; list-style:none; font-size:1rem; color:#2b1a4a; font-weight:500;">
                🏢 테슬라 | 인턴 (2024.02 ~ 2024.05)<span class="hint">▶ 펼쳐보기</span>
            </summary>
            <div style="margin-top:0.6rem; font-size:0.95rem; color:#444; line-height:1.8; padding-left:1rem;">
                <p>• <span style="color:#533483; font-weight:600;">대용량 고객 데이터 검증:</span> 전국 단위 보조금 지원 신청 서류 데이터를 수집하고, 필수 정보 누락 및 오류를 교차 검증하여 데이터 정합성 확보<br/>
                • <span style="color:#533483; font-weight:600;">정책 데이터 모니터링 및 요약:</span> 수시로 변동되는 지자체별 보조금 관련 공고문을 신속하게 파악하고, 핵심 조건 데이터를 정리하여 유관 부서에 적시 공유<br/>
                • <span style="color:#533483; font-weight:600;">고객 커뮤니케이션 지원:</span> 서류 보완이 필요한 고객 데이터를 추출하고, 명확한 안내를 통해 신속한 보조금 접수 완료 지원</p>
            </div>
        </details>
        <details style="margin-bottom:0.5rem;">
            <summary style="cursor:pointer; list-style:none; font-size:1rem; color:#2b1a4a; font-weight:500;">
                🏢 위덕대학교 LINC3.0사업단 | 계약직 (2023.08 ~ 2023.10)<span class="hint">▶ 펼쳐보기</span>
            </summary>
            <div style="margin-top:0.6rem; font-size:0.95rem; color:#444; line-height:1.8; padding-left:1rem;">
                <p>• <span style="color:#533483; font-weight:600;">사업단 핵심 지표(KPI) 데이터 관리:</span> 산학협력 사업의 주요 성과 데이터를 정기적으로 수집 및 가공하여, 대내외 홍보용 성과 뉴스레터 기획 및 발행 주도<br/>
                • <span style="color:#533483; font-weight:600;">프로그램 참여 데이터베이스 운영:</span> 기업 애로기술 과제 신청서 및 학생 현장실습 매칭 데이터를 체계적으로 분류 및 엑셀화하여 행정 처리 속도 개선<br/>
                • <span style="color:#533483; font-weight:600;">이해관계자 요구사항 조율:</span> 학교, 학생, 참여 기업 간의 다양한 요구사항 및 진행 현황을 트래킹하여 원활한 산학협력 프로세스 지원</p>
            </div>
        </details>
    </div>
    """, unsafe_allow_html=True)

# ── 프로젝트 ──────────────────────────────────────────────────
st.markdown('<div class="section-title">📁 Projects</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

daiso_logo = img_to_html("assets/daiso.png", width=40)
starbucks_logo = img_to_html("assets/starbucks.png", width=40)

with col1:
    st.markdown(f"""
    <div class="proj-card" style="border-top: 4px solid #e60012;">
        <div style="display:flex; align-items:center; gap:0.7rem; margin-bottom:0.8rem;">
            {daiso_logo}
            <strong style="font-size:1.15rem; color:#1a1a2e;">초저가를 넘어 초신뢰로</strong>
            <span style="margin-left:auto; font-size:0.9rem; color:#e60012; font-weight:600;">🏆 최우수상</span>
        </div>
        <p style="font-size:0.95rem; color:#555; margin-bottom:1rem; line-height:1.6;">다이소 뷰티 30만 건 리뷰 분석을 통한 2026년 성장 전략 도출</p>
        <div style="display:flex; gap:0.4rem; flex-wrap:wrap; margin-bottom:1.2rem;">
            <span class="badge-purple">RNN/LSTM</span>
            <span class="badge-purple">인과추론(PSM·IPTW·OW)</span>
            <span class="badge-purple">층화 샘플링</span>
            <span class="badge-purple">OCR</span>
            <span class="badge-purple">GIS 분석</span>
            <span class="badge-purple">DB 정규화</span>
            <span class="badge-purple">Tableau</span>
        </div>
        <div style="display:flex; gap:2rem; padding-top:1rem; border-top:1px solid #f0eaff;">
            <div style="text-align:center;">
                <div style="font-size:1.3rem; font-weight:700; color:#e60012;">30만건</div>
                <div style="font-size:0.82rem; color:#999; margin-top:0.2rem;">리뷰 데이터</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.3rem; font-weight:700; color:#e60012;">83.3%</div>
                <div style="font-size:0.82rem; color:#999; margin-top:0.2rem;">연착륙 제품 중 스킨케어</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.3rem; font-weight:700; color:#e60012;">144%</div>
                <div style="font-size:0.82rem; color:#999; margin-top:0.2rem;">뷰티 카테고리 성장률</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🟥 프로젝트 보기", use_container_width=True, key="proj1_btn"):
        st.switch_page("pages/1_프로젝트_1.py")

with col2:
    st.markdown(f"""
    <div class="proj-card" style="border-top: 4px solid #00704a;">
        <div style="display:flex; align-items:center; gap:0.7rem; margin-bottom:0.8rem;">
            {starbucks_logo}
            <strong style="font-size:1.15rem; color:#1a1a2e;">Starbucks Next Level</strong>
        </div>
        <p style="font-size:0.95rem; color:#555; margin-bottom:1rem; line-height:1.6;">행동경제학 기반 프로모션 채널 효과 분석 및 고객 세그먼트 전략 수립</p>
        <div style="display:flex; gap:0.4rem; flex-wrap:wrap; margin-bottom:1.2rem;">
            <span class="badge-green">K-means</span>
            <span class="badge-green">엘보우 방법</span>
            <span class="badge-green">Kruskal-Wallis</span>
            <span class="badge-green">카이제곱 검정</span>
            <span class="badge-green">행동경제학</span>
            <span class="badge-green">Tableau</span>
        </div>
        <div style="display:flex; gap:2rem; padding-top:1rem; border-top:1px solid #e6f4ee;">
            <div style="text-align:center;">
                <div style="font-size:1.3rem; font-weight:700; color:#00704a;">43.97%p</div>
                <div style="font-size:0.82rem; color:#999; margin-top:0.2rem;">SNS 채널 효과</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.3rem; font-weight:700; color:#00704a;">4개</div>
                <div style="font-size:0.82rem; color:#999; margin-top:0.2rem;">고객 세그먼트</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.3rem; font-weight:700; color:#00704a;">3가지</div>
                <div style="font-size:0.82rem; color:#999; margin-top:0.2rem;">행동경제학 인사이트</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🟩 프로젝트 보기", use_container_width=True, key="proj2_btn"):
        st.switch_page("pages/2_프로젝트_2.py")

# ── 스킬 ─────────────────────────────────────────────────────
st.markdown('<div class="section-title">🛠 Skills</div>', unsafe_allow_html=True)

tools = [
    (img_to_html("assets/tableau.png"), "Tableau", 80),
    ('<img src="https://cdn.simpleicons.org/mysql" width="40" height="40" alt="MySQL"/>', "MySQL", 80),
    ('<img src="https://cdn.simpleicons.org/jupyter" width="40" height="40" alt="Jupyter"/>', "Jupyter Notebook", 60),
    ('<img src="https://cdn.simpleicons.org/dbeaver" width="40" height="40" alt="DBeaver"/>', "DBeaver", 80),
    (img_to_html("assets/vscode.png"), "VS Code", 85),
    ('<img src="https://cdn.simpleicons.org/qgis" width="40" height="40" alt="QGIS"/>', "QGIS", 60),
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
            <div style="margin-left:auto; font-size:1.05rem; color:#9b7ec8; letter-spacing:2px;
                        text-align:right; display:flex; align-items:center; gap:0.4rem;">
                <span style="font-size:0.8rem; color:#b39ddb;">숙련도</span>
                {filled}<span style="color:#e8e0f5;">{empty}</span>
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