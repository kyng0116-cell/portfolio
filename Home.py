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

[data-testid="stAppViewContainer"] { background: #f8f9fa !important; }
[data-testid="stHeader"] { background: #f8f9fa !important; }
.stApp { background: #f8f9fa !important; }

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
pdf_b64 = img_to_base64("assets/김재경_포트폴리오.pdf")


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

# ─────────────────────────────────────────────
#  다이소 카드 — 풀 버전 (슬라이드 3·4·5 기반)
# ─────────────────────────────────────────────
daiso_card = f"""
<div style="background:#fff; border-radius:1.2rem; padding:2rem 2rem 1.6rem;
            box-shadow:0 2px 18px rgba(0,0,0,0.07); border:1px solid #e8e8ee;
            border-top:4px solid #e60012;">

  <!-- 헤더 -->
  <div style="display:flex; align-items:center; gap:0.8rem; margin-bottom:0.3rem;">
    {daiso_logo}
    <div>
      <div style="font-size:0.72rem; font-weight:700; color:#e60012; letter-spacing:2px; text-transform:uppercase;">MAIN PROJECT · 5인 팀 &nbsp;|&nbsp; 내 역할: 데이터 전처리·인과추론·GIS·런칭 시뮬레이터·대시보드</div>
      <div style="font-size:1.45rem; font-weight:800; color:#1a1a2e; margin-top:0.2rem; line-height:1.3;">
        초저가를 넘어 초신뢰로<br>
        <span style="font-size:1rem; font-weight:500; color:#555;">— 다이소 뷰티 144% 성장 이면의 구조적 결함을 데이터로 해체하다</span>
      </div>
    </div>
    <span style="margin-left:auto; background:#fff8e6; border:1.5px solid #e6a817; border-radius:99px;
                 padding:0.3rem 1rem; font-size:0.85rem; color:#c48a00; font-weight:700;
                 white-space:nowrap; flex-shrink:0;">🏆 최우수상</span>
  </div>
  <p style="font-size:0.85rem; color:#aaa; margin:0 0 1.6rem 2.9rem;">2026.02 ~ 03 &nbsp;·&nbsp; SQL · Python · Tableau · OCR · GIS</p>

  <!-- ── 섹션 1: 문제 정의 ── -->
  <div style="background:#fff5f5; border-radius:0.9rem; padding:1.1rem 1.3rem; margin-bottom:1.1rem; border:1px solid #ffd6d6;">
    <div style="font-size:0.72rem; font-weight:700; color:#e60012; letter-spacing:2px; margin-bottom:0.7rem;">📌 WHY THIS PROBLEM?</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.8rem;">
      <div style="text-align:center; padding:0.8rem 0.5rem; background:#fff; border-radius:0.6rem; border:1px solid #ffd6d6;">
        <div style="font-size:1.7rem; font-weight:800; color:#e60012;">144%</div>
        <div style="font-size:0.78rem; color:#888; margin-top:0.2rem;">다이소 뷰티 성장률</div>
        <div style="font-size:0.75rem; color:#555; margin-top:0.15rem;">저성장(1.9%) 국면 역행</div>
      </div>
      <div style="text-align:center; padding:0.8rem 0.5rem; background:#fff; border-radius:0.6rem; border:1px solid #ffd6d6;">
        <div style="font-size:1.7rem; font-weight:800; color:#e60012;">4,000억</div>
        <div style="font-size:0.78rem; color:#888; margin-top:0.2rem;">다이소 뷰티 연매출</div>
        <div style="font-size:0.75rem; color:#555; margin-top:0.15rem;">L자형 저성장 속 폭발 성장</div>
      </div>
      <div style="text-align:center; padding:0.8rem 0.5rem; background:#fff; border-radius:0.6rem; border:1px solid #ffd6d6;">
        <div style="font-size:1.7rem; font-weight:800; color:#e60012;">23%</div>
        <div style="font-size:0.78rem; color:#888; margin-top:0.2rem;">성분 분석형 소비자</div>
        <div style="font-size:0.75rem; color:#555; margin-top:0.15rem;">납 검출 이슈 + 100% 사입</div>
      </div>
    </div>
    <div style="margin-top:0.9rem; padding:0.75rem 1rem; background:#1a1a2e; border-radius:0.6rem; display:flex; align-items:center; gap:0.6rem;">
      <span style="font-size:1rem;">🔍</span>
      <span style="font-size:0.88rem; color:#f0f0f0;"><span style="color:#ffd966; font-weight:700;">HMW. </span>초저가 이미지를 유지하면서 '초신뢰' 브랜드를 만들 수 있는가?</span>
    </div>
  </div>

  <!-- ── 섹션 2: 솔루션 3단계 ── -->
  <div style="margin-bottom:1.1rem;">
    <div style="font-size:0.72rem; font-weight:700; color:#533483; letter-spacing:2px; margin-bottom:0.7rem;">⚙️ MY APPROACH — 3-STEP PIPELINE</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.8rem;">

      <div style="background:#f8f5ff; border-radius:0.8rem; padding:1rem; border:1px solid #d8caff; position:relative;">
        <span style="position:absolute; top:0.7rem; right:0.7rem; background:#533483; color:#fff;
                     font-size:0.65rem; font-weight:700; padding:0.15rem 0.5rem; border-radius:99px;
                     letter-spacing:1px;">내 기여</span>
        <div style="font-size:0.75rem; font-weight:700; color:#533483; margin-bottom:0.5rem;">STEP 1 · 데이터 무결성</div>
        <div style="font-size:0.83rem; color:#333; line-height:1.75;">
          Clova OCR + EasyOCR<br>
          <b>교차 파이프라인</b> 구축<br>
          300+ 패턴 교정<br>
          900여 제품 수기 검수<br>
          식약처 DB 매칭<br>
          Wide → Core·Stats·Specs<br>
          <b>3단 정규화</b> (30만 건)
        </div>
      </div>

      <div style="background:#f5f9ff; border-radius:0.8rem; padding:1rem; border:1px solid #c4daff; position:relative;">
        <span style="position:absolute; top:0.7rem; right:0.7rem; background:#2563eb; color:#fff;
                     font-size:0.65rem; font-weight:700; padding:0.15rem 0.5rem; border-radius:99px;
                     letter-spacing:1px;">내 기여</span>
        <div style="font-size:0.75rem; font-weight:700; color:#2563eb; margin-bottom:0.5rem;">STEP 2 · 인과추론</div>
        <div style="font-size:0.83rem; color:#333; line-height:1.75;">
          PSM · IPTW · OW<br>
          <b>3가지 방법 교차 검증</b><br>
          브랜드·카테고리·기능성<br>
          혼동 변수 제거<br>
          → 기능성 성분<br>
          <b>단독 효과 없음</b><br>
          조절 변수로만 작동
        </div>
      </div>

      <div style="background:#f0faf5; border-radius:0.8rem; padding:1rem; border:1px solid #b8e8d0; position:relative;">
        <span style="position:absolute; top:0.7rem; right:0.7rem; background:#059669; color:#fff;
                     font-size:0.65rem; font-weight:700; padding:0.15rem 0.5rem; border-radius:99px;
                     letter-spacing:1px;">내 기여</span>
        <div style="font-size:0.75rem; font-weight:700; color:#059669; margin-bottom:0.5rem;">STEP 3 · GIS 수요 알고리즘</div>
        <div style="font-size:0.83rem; color:#333; line-height:1.75;">
          외국인 수·유동인구<br>
          경쟁사 위치 z-score<br>
          <b>표준화 합산 알고리즘</b><br>
          자체 설계<br>
          → Hub & Spoke<br>
          <b>물류 전략</b> 도출
        </div>
      </div>
    </div>
  </div>

  <!-- ── 섹션 3: 수치 결과 ── -->
  <div style="margin-bottom:1.1rem;">
    <div style="font-size:0.72rem; font-weight:700; color:#e6a817; letter-spacing:2px; margin-bottom:0.7rem;">📊 RESULTS — 수치로 증명된 3가지 인사이트</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.8rem;">
      <div style="background:#f8f9fa; border-radius:0.8rem; padding:1rem 0.9rem; text-align:center; border-top:3px solid #e60012;">
        <div style="font-size:1.75rem; font-weight:800; color:#e60012; line-height:1.1;">16.7%</div>
        <div style="font-size:0.78rem; color:#888; margin-top:0.35rem;">연착륙 제품 비율</div>
        <div style="font-size:0.8rem; color:#1a1a2e; font-weight:600; margin-top:0.2rem;">→ 뷰티 매출 32.5% 견인</div>
        <div style="font-size:0.75rem; color:#aaa; margin-top:0.15rem;">≈ 1,300억 원 / KM·Cox PH</div>
      </div>
      <div style="background:#f8f9fa; border-radius:0.8rem; padding:1rem 0.9rem; text-align:center; border-top:3px solid #5b9cf6;">
        <div style="font-size:1.75rem; font-weight:800; color:#5b9cf6; line-height:1.1;">조절 변수</div>
        <div style="font-size:0.78rem; color:#888; margin-top:0.35rem;">기능성 성분의 실제 역할</div>
        <div style="font-size:0.8rem; color:#1a1a2e; font-weight:600; margin-top:0.2rem;">카테고리·브랜드 결합 시 증폭</div>
        <div style="font-size:0.75rem; color:#aaa; margin-top:0.15rem;">PSM/IPTW/OW 교차 확인</div>
      </div>
      <div style="background:#f8f9fa; border-radius:0.8rem; padding:1rem 0.9rem; text-align:center; border-top:3px solid #059669;">
        <div style="font-size:1.75rem; font-weight:800; color:#059669; line-height:1.1;">75.8%</div>
        <div style="font-size:0.78rem; color:#888; margin-top:0.35rem;">중국인 관광객 화장품 구매율</div>
        <div style="font-size:0.8rem; color:#1a1a2e; font-weight:600; margin-top:0.2rem;">Hub 상권 재고 수요 압도적</div>
        <div style="font-size:0.75rem; color:#aaa; margin-top:0.15rem;">외국인 상위 5% 상권 분석</div>
      </div>
    </div>
  </div>

  <!-- ── KEY INSIGHT ── -->
  <div style="background:#1a1a2e; border-radius:0.7rem; padding:0.9rem 1.1rem; margin-bottom:1.2rem;
              display:flex; align-items:flex-start; gap:0.7rem;">
    <span style="font-size:1.1rem; margin-top:0.1rem;">💡</span>
    <div>
      <span style="font-size:0.72rem; font-weight:700; color:#e6a817; letter-spacing:2px;">KEY INSIGHT &nbsp;</span>
      <span style="font-size:0.9rem; color:#e8e8ee;">
        분석은 현상 설명이 아니라 <span style="color:#fff; font-weight:700;">의사결정 도구</span>여야 한다 —
        기능성 성분 단독 효과 없음, <span style="color:#fff; font-weight:700;">카테고리 신뢰</span>와 결합 시 폭발적 증폭.
        입점 전 <span style="color:#ffd966; font-weight:700;">런칭 시뮬레이터</span>로 실증.
      </span>
    </div>
  </div>

  <!-- 태그 -->
  <div style="display:flex; gap:0.4rem; flex-wrap:wrap;">
    <span style="background:#f0f0f5; border-radius:99px; padding:0.25rem 0.8rem; font-size:0.83rem; color:#1a1a2e;">인과추론(PSM·IPTW·OW)</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.25rem 0.8rem; font-size:0.83rem; color:#1a1a2e;">생존분석(KM·Cox PH)</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.25rem 0.8rem; font-size:0.83rem; color:#1a1a2e;">OCR 파이프라인</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.25rem 0.8rem; font-size:0.83rem; color:#1a1a2e;">GIS</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.25rem 0.8rem; font-size:0.83rem; color:#1a1a2e;">RNN/LSTM</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.25rem 0.8rem; font-size:0.83rem; color:#1a1a2e;">Tableau</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.25rem 0.8rem; font-size:0.83rem; color:#1a1a2e;">데이터 정규화</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.25rem 0.8rem; font-size:0.83rem; color:#1a1a2e;">런칭 시뮬레이터</span>
  </div>
</div>
"""

# ─────────────────────────────────────────────
#  스타벅스 카드 — 압축형 (슬라이드 6 기반)
# ─────────────────────────────────────────────
sbux_card = f"""
<div style="background:#fff; border-radius:1.2rem; padding:2rem;
            box-shadow:0 2px 12px rgba(0,0,0,0.06); border:1px solid #e8e8ee;
            border-top:4px solid #00704a;">
  <div style="display:flex; align-items:center; gap:0.8rem; margin-bottom:0.4rem;">
    {starbucks_logo}
    <div>
      <div style="font-size:0.72rem; font-weight:600; color:#00704a; letter-spacing:2px; text-transform:uppercase;">SUB PROJECT · 5인 팀 &nbsp;|&nbsp; 내 역할: 전처리·효과크기 산출·대시보드</div>
      <div style="font-size:1.3rem; font-weight:700; color:#1a1a2e; margin-top:0.1rem;">Starbucks Next Level</div>
      <div style="font-size:0.9rem; color:#555; margin-top:0.2rem;">'누가 구매했는가'가 아닌 '어떤 트리거가 전환을 유발했는가'를 묻다</div>
    </div>
  </div>
  <p style="font-size:0.85rem; color:#aaa; margin:0 0 1.4rem 2.8rem;">2026.01 &nbsp;·&nbsp; SQL · Python · Tableau</p>

  <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.8rem; margin-bottom:1.1rem;">
    <div style="background:#f0faf5; border-left:3px solid #00704a; border-radius:0 0.6rem 0.6rem 0; padding:0.9rem 1rem;">
      <div style="font-size:0.72rem; font-weight:700; color:#00704a; letter-spacing:2px; margin-bottom:0.5rem;">PROBLEM</div>
      <div style="font-size:0.9rem; color:#333; line-height:1.7;">
        채널별 순수 기여도 불명확<br>
        → <span style="color:#1a1a2e; font-weight:600;">비효율적 예산 배분</span> + 고객 피로도
      </div>
    </div>
    <div style="background:#f8f5ff; border-left:3px solid #7c5cbf; border-radius:0 0.6rem 0.6rem 0; padding:0.9rem 1rem;">
      <div style="font-size:0.72rem; font-weight:700; color:#7c5cbf; letter-spacing:2px; margin-bottom:0.5rem;">APPROACH</div>
      <div style="font-size:0.85rem; color:#333; line-height:1.8;">
        ① K-means 4개 세그먼트 분류<br>
        ② 카이제곱 검정 통계 유의성 확보<br>
        ③ 행동경제학 3 프레임 전환 해석
      </div>
    </div>
  </div>

  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.8rem; margin-bottom:1.1rem;">
    <div style="background:#f8f9fa; border-radius:0.8rem; padding:1rem 0.8rem; text-align:center; border-top:2px solid #00704a;">
      <div style="font-size:1.7rem; font-weight:800; color:#00704a; line-height:1;">43.97%p</div>
      <div style="font-size:0.78rem; color:#888; margin-top:0.3rem;">SNS 채널 전환 효과</div>
      <div style="font-size:0.78rem; color:#555; margin-top:0.15rem;">Web 7.16%p 대비 압도적</div>
    </div>
    <div style="background:#f8f9fa; border-radius:0.8rem; padding:1rem 0.8rem; text-align:center; border-top:2px solid #5b9cf6;">
      <div style="font-size:1.7rem; font-weight:800; color:#5b9cf6; line-height:1;">2.4배</div>
      <div style="font-size:0.78rem; color:#888; margin-top:0.3rem;">3채널 중복 노출 효과</div>
      <div style="font-size:0.78rem; color:#555; margin-top:0.15rem;">완료율 50% (단일 20.44%)</div>
    </div>
    <div style="background:#f8f9fa; border-radius:0.8rem; padding:1rem 0.8rem; text-align:center; border-top:2px solid #9b7fe8;">
      <div style="font-size:1.7rem; font-weight:800; color:#9b7fe8; line-height:1;">3배</div>
      <div style="font-size:0.78rem; color:#888; margin-top:0.3rem;">실질 지불액 효과</div>
      <div style="font-size:0.78rem; color:#555; margin-top:0.15rem;">2,000원 vs 7,000원 오퍼</div>
    </div>
  </div>

  <div style="background:#1a1a2e; border-radius:0.7rem; padding:0.9rem 1rem; margin-bottom:1.2rem;
              display:flex; align-items:flex-start; gap:0.7rem;">
    <span style="font-size:1.1rem; margin-top:0.1rem;">💡</span>
    <div>
      <span style="font-size:0.72rem; font-weight:700; color:#e6a817; letter-spacing:2px;">KEY INSIGHT &nbsp;</span>
      <span style="font-size:0.9rem; color:#e8e8ee;">고액 할인보다 실질 지불액 최소화가 전환율 3배 — <span style="color:#fff; font-weight:600;">손실 회피 심리</span> + 사회적 증거 + 단순 노출 효과</span>
    </div>
  </div>

  <div style="display:flex; gap:0.4rem; flex-wrap:wrap;">
    <span style="background:#f0f0f5; border-radius:99px; padding:0.25rem 0.8rem; font-size:0.83rem; color:#1a1a2e;">K-means</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.25rem 0.8rem; font-size:0.83rem; color:#1a1a2e;">카이제곱 검정</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.25rem 0.8rem; font-size:0.83rem; color:#1a1a2e;">Kruskal-Wallis</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.25rem 0.8rem; font-size:0.83rem; color:#1a1a2e;">행동경제학</span>
    <span style="background:#f0f0f5; border-radius:99px; padding:0.25rem 0.8rem; font-size:0.83rem; color:#1a1a2e;">Tableau</span>
  </div>
</div>
"""

st.markdown('<div class="section-title">📁 Projects</div>', unsafe_allow_html=True)

st.markdown(daiso_card, unsafe_allow_html=True)
if st.button("🟥 다이소 뷰티 — 프로젝트 상세 보기", use_container_width=True, key="proj1_btn"):
    st.switch_page("pages/1_프로젝트_1.py")

st.markdown("<div style='margin-top:1.4rem;'></div>", unsafe_allow_html=True)

st.markdown(sbux_card, unsafe_allow_html=True)
if st.button("🟩 스타벅스 — 프로젝트 상세 보기", use_container_width=True, key="proj2_btn"):
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