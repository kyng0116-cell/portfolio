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
        background-color: #ffffff !important; background-image: none !important;
    }
    section[data-testid="stSidebar"] * { color: #1a1a2e !important; }
    section[data-testid="stSidebar"] hr { border-color: rgba(26,26,46,0.1) !important; }
    section[data-testid="stSidebar"] .stButton > button {
        background: transparent !important;
        border: 1px solid rgba(26,26,46,0.15) !important;
        color: #1a1a2e !important; text-align: left !important;
        border-radius: 0.5rem !important; font-size: 0.9rem !important;
    }
    section[data-testid="stSidebar"] .stButton > button:hover {
        background: #f0f0f5 !important; border-color: #533483 !important;
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

# ── 전역 스타일 (FA CDN 포함) ───────────────────────
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"/>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;600;700&display=swap" rel="stylesheet"/>
<style>
html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; letter-spacing: 1px; }
* { word-break: keep-all !important; overflow-wrap: break-word !important; }
strong { font-size: 1.25rem !important; }
[data-testid="stAppViewContainer"] { background: #f8f9fa !important; }
[data-testid="stHeader"] { background: #f8f9fa !important; }
.stApp { background: #f8f9fa !important; }

.profile-card {
    display: flex; align-items: flex-start; gap: 2.5rem; padding: 2.5rem;
    background: #ffffff; border-radius: 1.2rem; color: #1a1a2e; margin-bottom: 2rem;
    box-shadow: 0 2px 20px rgba(26,26,46,0.08); border: 1px solid #e8e8ee;
}
.profile-info { flex: 1; width: 100%; min-width: 0; }
.profile-info h1 { font-size: 1.9rem; font-weight: 700; margin: 0 0 0.3rem 0; color: #1a1a2e; }
.profile-cols { display: flex; gap: 1rem; margin-top: 0.5rem; flex-wrap: wrap; width: 100%; }
.profile-col { min-width: 160px; flex: 1; background: #f8f9fa; border-radius: 0.8rem; padding: 0.8rem 1rem; border: 1px solid #e8e8ee; }
.profile-col h4 { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 1.5px; color: #888; margin: 0 0 0.4rem 0; font-weight: 600; }
.profile-col p { font-size: 1rem; margin: 0.18rem 0; color: #1a1a2e; }
.profile-col a { color: #533483 !important; text-decoration: underline; text-underline-offset: 2px; font-weight: 500; }
.section-title {
    font-size: 1.5rem; font-weight: 700; color: #1a1a2e;
    margin: 1.8rem 0 1rem 0; padding-bottom: 0.4rem;
    border-bottom: 2.5px solid #533483; display: inline-block;
}
.skill-card {
    background: #ffffff !important; border-radius: 0.8rem; padding: 0.9rem 1.1rem;
    margin-bottom: 0.6rem; box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    border: 1px solid #e8e8ee; display: flex; align-items: center; gap: 0.9rem;
}
.skill-icon { font-size: 1.4rem; width: 1.8rem; text-align: center; }
.skill-name { font-weight: 600; font-size: 1.125rem; color: #1a1a2e !important; min-width: 120px; white-space: nowrap; }
summary { outline: none; }
details summary::-webkit-details-marker { display: none; }
</style>
""", unsafe_allow_html=True)

cert4_b64 = img_to_base64("images/최우수상.png")
pdf_b64   = img_to_base64("assets/김재경_포트폴리오.pdf")

# ── 프로필 ───────────────────────────────────────────
st.markdown(f"""
<div class="profile-card">
    <img src="https://ca.slack-edge.com/T088AB0N865-U09EHSCUNSF-3bef5911dc38-512"
         style="width:120px; height:120px; border-radius:50%; object-fit:cover;
                border:3px solid #e8e8ee; flex-shrink:0; box-shadow:0 2px 12px rgba(0,0,0,0.10);">
    <div class="profile-info">
        <h1 style="display:flex; align-items:center; gap:1rem;">
            김재경
            <a href="data:application/pdf;base64,{pdf_b64}" download="김재경_포트폴리오.pdf"
               style="font-size:0.82rem; font-weight:600; color:#533483; border:1.5px solid #533483;
                      border-radius:99px; padding:0.25rem 0.8rem; text-decoration:none; white-space:nowrap;">
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
                <p>🎓 단국대학교 | 심리학 학사 (2015.03 ~ 2020.02)</p>
            </div>
            <div class="profile-col">
                <h4>수상이력</h4>
                <details>
                    <summary style="cursor:pointer; list-style:none; font-size:0.92rem; color:#1a1a2e;">
                        🏆 스파르타 최종 프로젝트 최우수상 (2026.03)
                        <span style="font-size:0.88rem; color:#aaa;"><br/>▶ 펼쳐보기</span>
                    </summary>
                    <img src="data:image/png;base64,{cert4_b64}" style="width:400px; margin-top:0.5rem; border-radius:0.5rem;">
                </details>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

daiso_logo     = img_to_html("assets/daiso.png", width=28)
starbucks_logo = img_to_html("assets/starbucks.png", width=28)

# ════════════════════════════════════════
#  PROJECTS
# ════════════════════════════════════════
st.markdown('<div class="section-title">📁 Projects</div>', unsafe_allow_html=True)

# ── 다이소 헤더 ──────────────────────────────────
st.markdown(f"""
<div style="display:flex; align-items:center; gap:0.6rem; margin:0.4rem 0 0.6rem 0;">
    {daiso_logo}
    <div style="flex:1;">
        <div style="font-size:0.65rem; font-weight:700; color:#e60012; letter-spacing:2px; text-transform:uppercase;">
            MAIN PROJECT · 2026.02 ~ 03 · 5인 팀
        </div>
        <div style="font-size:1.1rem; font-weight:800; color:#1a1a2e; line-height:1.3;">초저가를 넘어 초신뢰로</div>
        <div style="font-size:0.82rem; color:#777;">144% 성장 이면의 구조적 결함을 데이터로 해체하다</div>
    </div>
    <span style="background:#fff8e6; border:1.5px solid #e6a817; border-radius:99px;
                 padding:0.2rem 0.75rem; font-size:0.75rem; color:#c48a00; font-weight:700; white-space:nowrap;">
        🏆 최우수상
    </span>
</div>
""", unsafe_allow_html=True)

# ── 슬라이드 1: 문제 발견 ────────────────────────
st.markdown("""
<div style="background:#fff; border-radius:0.9rem; border:1px solid #e8e8ee;
            box-shadow:0 2px 10px rgba(26,26,46,0.05); margin-bottom:0.6rem; overflow:hidden;">
  <div style="padding:0.75rem 1.2rem 0.5rem; border-bottom:1px solid #f0f0f5;">
    <div style="font-size:0.65rem; font-weight:700; color:#e60012; letter-spacing:2px; text-transform:uppercase; margin-bottom:0.15rem;">📌 문제 발견</div>
    <div style="font-size:1rem; font-weight:800; color:#1a1a2e;">144% 성장 이면의 신뢰 위기</div>
  </div>
  <div style="padding:0.85rem 1.2rem 1rem;">

    <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.55rem; margin-bottom:0.7rem;">

      <div style="background:#fafafa; border-radius:0.55rem; padding:0.65rem 0.85rem;
                  border:1px solid #eeeeee; border-left:3px solid #533483;">
        <div style="font-size:0.78rem; font-weight:700; color:#1a1a2e; margin-bottom:0.2rem;">
          📈 폭발적 성장 vs 시장 침체
        </div>
        <div style="font-size:0.75rem; color:#555; line-height:1.6;">
          시장 평균 1.9% 저성장 속 다이소 뷰티 <b>144% 급성장</b> · 매출 4,000억 돌파
        </div>
      </div>

      <div style="background:#fafafa; border-radius:0.55rem; padding:0.65rem 0.85rem;
                  border:1px solid #eeeeee; border-left:3px solid #e60012;">
        <div style="font-size:0.78rem; font-weight:700; color:#e60012; margin-bottom:0.2rem;">
          ⚠️ 신뢰 위기 발생
        </div>
        <div style="font-size:0.75rem; color:#555; line-height:1.6;">
          납 검출 이슈 + C커머스 저가 공세 — 소비자 <b>23%</b>가 성분 분석형으로 전환
        </div>
      </div>

      <div style="background:#fafafa; border-radius:0.55rem; padding:0.65rem 0.85rem;
                  border:1px solid #eeeeee; border-left:3px solid #e6a817;">
        <div style="font-size:0.78rem; font-weight:700; color:#1a1a2e; margin-bottom:0.2rem;">
          🏗️ 100% 사입 구조의 취약점
        </div>
        <div style="font-size:0.75rem; color:#555; line-height:1.6;">
          단 1건의 사고만으로 전체 성장이 멈출 수 있는 <b>구조적 리스크</b>
        </div>
      </div>

      <div style="background:#fafafa; border-radius:0.55rem; padding:0.65rem 0.85rem;
                  border:1px solid #eeeeee; border-left:3px solid #2563eb;">
        <div style="font-size:0.78rem; font-weight:700; color:#1a1a2e; margin-bottom:0.2rem;">
          🏪 현장 운영 불균형
        </div>
        <div style="font-size:0.75rem; color:#555; line-height:1.6;">
          Hub 매장 인기 제품 조기 품절 반복 — <b>기회비용</b> 지속 발생
        </div>
      </div>

    </div>

    <div style="background:#1a1a2e; border-radius:0.55rem; padding:0.6rem 0.9rem;
                display:flex; align-items:center; gap:0.5rem;">
      <span style="font-size:0.85rem;">🔍</span>
      <span style="font-size:0.8rem; color:#e8e8ee;">
        <span style="color:#ffd966; font-weight:700;">HMW. </span>
        초저가 이미지를 유지하면서 '초신뢰' 브랜드를 만들 수 있는가?
      </span>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)

# ── 슬라이드 2: 분석 접근법 ─────────────────────
st.markdown("""
<div style="background:#fff; border-radius:0.9rem; border:1px solid #e8e8ee;
            box-shadow:0 2px 10px rgba(26,26,46,0.05); margin-bottom:0.6rem; overflow:hidden;">
  <div style="padding:0.75rem 1.2rem 0.5rem; border-bottom:1px solid #f0f0f5;">
    <div style="font-size:0.65rem; font-weight:700; color:#533483; letter-spacing:2px; text-transform:uppercase; margin-bottom:0.15rem;">⚙️ 분석 접근법</div>
    <div style="font-size:1rem; font-weight:800; color:#1a1a2e;">3단계 데이터 파이프라인</div>
  </div>
  <div style="padding:0.85rem 1.2rem 1rem;">

    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.55rem; margin-bottom:0.7rem;">

      <div style="background:#f0faf8; border-radius:0.55rem; padding:0.75rem 0.85rem; border:1px solid #d4f1ec;">
        <div style="font-size:0.65rem; font-weight:700; color:#0d9488; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:0.4rem;">
          STEP 1 · 데이터 무결성
          <span style="background:#0d9488; color:#fff; border-radius:99px; padding:0.08rem 0.45rem; font-size:0.6rem; margin-left:0.2rem;">내 기여</span>
        </div>
        <div style="font-size:0.77rem; color:#444; line-height:1.7;">
          Clova OCR + EasyOCR <b>교차 파이프라인</b><br/>
          300+ 패턴 교정 · 900여 제품 수기 검수<br/>
          식약처 DB 매칭 · 30만 건 <b>3단 정규화</b>
        </div>
      </div>

      <div style="background:#f7f4ff; border-radius:0.55rem; padding:0.75rem 0.85rem; border:1px solid #e0d4f7;">
        <div style="font-size:0.65rem; font-weight:700; color:#533483; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:0.4rem;">
          STEP 2 · 인과추론
          <span style="background:#533483; color:#fff; border-radius:99px; padding:0.08rem 0.45rem; font-size:0.6rem; margin-left:0.2rem;">내 기여</span>
        </div>
        <div style="font-size:0.77rem; color:#444; line-height:1.7;">
          <b>PSM · IPTW · OW</b> 3종 교차 검증<br/>
          브랜드·카테고리·기능성 혼동 변수 제거<br/>
          기능성 성분 <b>단독 효과 없음</b> 확정
        </div>
      </div>

      <div style="background:#f0f5ff; border-radius:0.55rem; padding:0.75rem 0.85rem; border:1px solid #d4e4fc;">
        <div style="font-size:0.65rem; font-weight:700; color:#2563eb; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:0.4rem;">
          STEP 3 · GIS 알고리즘
          <span style="background:#2563eb; color:#fff; border-radius:99px; padding:0.08rem 0.45rem; font-size:0.6rem; margin-left:0.2rem;">내 기여</span>
        </div>
        <div style="font-size:0.77rem; color:#444; line-height:1.7;">
          외국인 수·유동인구·경쟁사<br/>
          <b>z-score 합산 알고리즘</b> 자체 설계<br/>
          Hub & Spoke 물류 + <b>런칭 시뮬레이터</b>
        </div>
      </div>

    </div>

    <div style="background:#1a1a2e; border-radius:0.55rem; padding:0.6rem 0.9rem;
                display:flex; align-items:center; gap:0.5rem;">
      <span style="font-size:0.85rem;">💡</span>
      <span style="font-size:0.8rem; color:#e8e8ee;">
        단순 회귀 대신 <span style="color:#e6a817; font-weight:700;">인과추론</span>을 적용 —
        가격·성분·리뷰 공산성 변수를 분리해 진짜 매출 동인만 규명
      </span>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)

# ── 슬라이드 3: 결과 ────────────────────────────
st.markdown("""
<div style="background:#fff; border-radius:0.9rem; border:1px solid #e8e8ee;
            box-shadow:0 2px 10px rgba(26,26,46,0.05); margin-bottom:0.6rem; overflow:hidden;">
  <div style="padding:0.75rem 1.2rem 0.5rem; border-bottom:1px solid #f0f0f5;">
    <div style="font-size:0.65rem; font-weight:700; color:#059669; letter-spacing:2px; text-transform:uppercase; margin-bottom:0.15rem;">📊 결과 및 인사이트</div>
    <div style="font-size:1rem; font-weight:800; color:#1a1a2e;">수치로 증명된 3가지 발견</div>
  </div>
  <div style="padding:0.85rem 1.2rem 1rem;">

    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.55rem; margin-bottom:0.7rem;">

      <div style="background:#fafafa; border-radius:0.55rem; padding:0.8rem 0.6rem;
                  text-align:center; border:1px solid #eee; border-top:3px solid #059669;">
        <div style="font-size:1.7rem; font-weight:800; color:#059669; line-height:1.1;">16.7%</div>
        <div style="font-size:0.72rem; color:#888; margin-top:0.2rem;">연착륙 제품 비율</div>
        <div style="font-size:0.75rem; color:#333; font-weight:600; margin-top:0.15rem;">뷰티 매출 32.5% 견인 (≈1,300억)</div>
        <div style="font-size:0.68rem; color:#aaa; margin-top:0.1rem;">생존분석 KM·Cox PH 검증</div>
      </div>

      <div style="background:#fafafa; border-radius:0.55rem; padding:0.8rem 0.6rem;
                  text-align:center; border:1px solid #eee; border-top:3px solid #533483;">
        <div style="font-size:1.1rem; font-weight:800; color:#533483; line-height:1.3; padding-top:0.3rem;">PSM·IPTW·OW</div>
        <div style="font-size:0.72rem; color:#888; margin-top:0.2rem;">인과추론 3종 교차 검증</div>
        <div style="font-size:0.75rem; color:#333; font-weight:600; margin-top:0.15rem;">기능성 성분 = 조절 변수 확정</div>
        <div style="font-size:0.68rem; color:#aaa; margin-top:0.1rem;">카테고리·브랜드 결합 시 효과 증폭</div>
      </div>

      <div style="background:#fafafa; border-radius:0.55rem; padding:0.8rem 0.6rem;
                  text-align:center; border:1px solid #eee; border-top:3px solid #2563eb;">
        <div style="font-size:1.7rem; font-weight:800; color:#2563eb; line-height:1.1;">75.8%</div>
        <div style="font-size:0.72rem; color:#888; margin-top:0.2rem;">중국인 관광객 화장품 구매율</div>
        <div style="font-size:0.75rem; color:#333; font-weight:600; margin-top:0.15rem;">Hub 상권 재고 수요 압도적</div>
        <div style="font-size:0.68rem; color:#aaa; margin-top:0.1rem;">외국인 상위 5% 상권 GIS 분석</div>
      </div>

    </div>

    <div style="background:#1a1a2e; border-radius:0.55rem; padding:0.6rem 0.9rem;
                display:flex; align-items:center; gap:0.5rem; margin-bottom:0.7rem;">
      <span style="font-size:0.85rem;">💡</span>
      <span style="font-size:0.8rem; color:#e8e8ee;">
        <span style="color:#ffd966; font-weight:700;">Key Insight. </span>
        분석은 현상 설명이 아닌 의사결정 도구 — 기능성 성분은
        <span style="color:#fff; font-weight:600;">카테고리 신뢰</span>와 결합 시 효과 폭발적 증폭
      </span>
    </div>

    <div style="display:flex; gap:0.35rem; flex-wrap:wrap;">
      <span style="background:#f0f0f5; border-radius:99px; padding:0.18rem 0.65rem; font-size:0.75rem; color:#555;">인과추론(PSM·IPTW·OW)</span>
      <span style="background:#f0f0f5; border-radius:99px; padding:0.18rem 0.65rem; font-size:0.75rem; color:#555;">생존분석(KM·Cox PH)</span>
      <span style="background:#f0f0f5; border-radius:99px; padding:0.18rem 0.65rem; font-size:0.75rem; color:#555;">OCR 파이프라인</span>
      <span style="background:#f0f0f5; border-radius:99px; padding:0.18rem 0.65rem; font-size:0.75rem; color:#555;">GIS</span>
      <span style="background:#f0f0f5; border-radius:99px; padding:0.18rem 0.65rem; font-size:0.75rem; color:#555;">RNN/LSTM</span>
      <span style="background:#f0f0f5; border-radius:99px; padding:0.18rem 0.65rem; font-size:0.75rem; color:#555;">Tableau</span>
      <span style="background:#f0f0f5; border-radius:99px; padding:0.18rem 0.65rem; font-size:0.75rem; color:#555;">런칭 시뮬레이터</span>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)

if st.button("🟥 다이소 뷰티 — 프로젝트 상세 보기", use_container_width=True, key="proj1_btn"):
    st.switch_page("pages/1_프로젝트_1.py")

st.markdown("<div style='margin-top:1.8rem;'></div>", unsafe_allow_html=True)

# ── 스타벅스 헤더 ────────────────────────────────
st.markdown(f"""
<div style="display:flex; align-items:center; gap:0.6rem; margin:0.4rem 0 0.6rem 0;">
    {starbucks_logo}
    <div>
        <div style="font-size:0.65rem; font-weight:700; color:#00704a; letter-spacing:2px; text-transform:uppercase;">
            SUB PROJECT · 2026.01 · 5인 팀
        </div>
        <div style="font-size:1.1rem; font-weight:800; color:#1a1a2e; line-height:1.3;">Starbucks Next Level</div>
        <div style="font-size:0.82rem; color:#777;">'누가 구매했는가'가 아닌 '어떤 트리거가 전환을 유발했는가'를 묻다</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── 슬라이드 4: 스타벅스 ─────────────────────────
st.markdown("""
<div style="background:#fff; border-radius:0.9rem; border:1px solid #e8e8ee;
            box-shadow:0 2px 10px rgba(26,26,46,0.05); margin-bottom:0.6rem; overflow:hidden;">
  <div style="padding:0.75rem 1.2rem 0.5rem; border-bottom:1px solid #f0f0f5;">
    <div style="font-size:0.65rem; font-weight:700; color:#00704a; letter-spacing:2px; text-transform:uppercase; margin-bottom:0.15rem;">📊 채널 전환 효과 분석</div>
    <div style="font-size:1rem; font-weight:800; color:#1a1a2e;">행동경제학으로 43.97%p 채널 격차를 설명하다</div>
  </div>
  <div style="padding:0.85rem 1.2rem 1rem;">

    <div style="background:#fafafa; border-left:3px solid #00704a; border-radius:0 0.5rem 0.5rem 0;
                padding:0.6rem 0.85rem; margin-bottom:0.7rem; font-size:0.78rem; color:#444; line-height:1.7;">
      <b style="color:#1a1a2e;">Problem.</b>&nbsp; 채널별 순수 기여도 불명확 → 비효율적 예산 배분 + 고객 피로도 가중<br/>
      <b style="color:#1a1a2e;">Approach.</b>&nbsp; K-means 4개 세그먼트 · 카이제곱 검정 통계 유의성 · 행동경제학 3 프레임 해석
    </div>

    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.55rem; margin-bottom:0.7rem;">

      <div style="background:#fafafa; border-radius:0.55rem; padding:0.8rem 0.6rem;
                  text-align:center; border:1px solid #eee; border-top:3px solid #00704a;">
        <div style="font-size:1.7rem; font-weight:800; color:#00704a; line-height:1.1;">43.97%p</div>
        <div style="font-size:0.72rem; color:#888; margin-top:0.2rem;">SNS 채널 전환 효과</div>
        <div style="font-size:0.75rem; color:#333; font-weight:600; margin-top:0.15rem;">Web 7.16%p 대비 압도적</div>
      </div>

      <div style="background:#fafafa; border-radius:0.55rem; padding:0.8rem 0.6rem;
                  text-align:center; border:1px solid #eee; border-top:3px solid #2563eb;">
        <div style="font-size:1.7rem; font-weight:800; color:#2563eb; line-height:1.1;">2.4배</div>
        <div style="font-size:0.72rem; color:#888; margin-top:0.2rem;">3채널 중복 노출 효과</div>
        <div style="font-size:0.75rem; color:#333; font-weight:600; margin-top:0.15rem;">완료율 50% (단일 20.44%)</div>
      </div>

      <div style="background:#fafafa; border-radius:0.55rem; padding:0.8rem 0.6rem;
                  text-align:center; border:1px solid #eee; border-top:3px solid #7c5cbf;">
        <div style="font-size:1.7rem; font-weight:800; color:#7c5cbf; line-height:1.1;">3배</div>
        <div style="font-size:0.72rem; color:#888; margin-top:0.2rem;">실질 지불액 효과</div>
        <div style="font-size:0.75rem; color:#333; font-weight:600; margin-top:0.15rem;">2,000원 vs 7,000원 오퍼</div>
      </div>

    </div>

    <div style="background:#1a1a2e; border-radius:0.55rem; padding:0.6rem 0.9rem;
                display:flex; align-items:center; gap:0.5rem; margin-bottom:0.7rem;">
      <span style="font-size:0.85rem;">💡</span>
      <span style="font-size:0.8rem; color:#e8e8ee;">
        <span style="color:#ffd966; font-weight:700;">Key Insight. </span>
        고액 할인보다 실질 지불액 최소화가 전환율 3배 —
        <span style="color:#fff; font-weight:600;">손실 회피</span> · 사회적 증거 · 단순 노출 효과
      </span>
    </div>

    <div style="display:flex; gap:0.35rem; flex-wrap:wrap;">
      <span style="background:#f0f0f5; border-radius:99px; padding:0.18rem 0.65rem; font-size:0.75rem; color:#555;">K-means</span>
      <span style="background:#f0f0f5; border-radius:99px; padding:0.18rem 0.65rem; font-size:0.75rem; color:#555;">카이제곱 검정</span>
      <span style="background:#f0f0f5; border-radius:99px; padding:0.18rem 0.65rem; font-size:0.75rem; color:#555;">Kruskal-Wallis</span>
      <span style="background:#f0f0f5; border-radius:99px; padding:0.18rem 0.65rem; font-size:0.75rem; color:#555;">행동경제학</span>
      <span style="background:#f0f0f5; border-radius:99px; padding:0.18rem 0.65rem; font-size:0.75rem; color:#555;">Tableau</span>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)

if st.button("🟩 스타벅스 — 프로젝트 상세 보기", use_container_width=True, key="proj2_btn"):
    st.switch_page("pages/2_프로젝트_2.py")

# ════════════════════════════════════════
#  SKILLS
# ════════════════════════════════════════
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
        empty  = "☆" * (5 - stars)
        st.markdown(f"""
        <div class="skill-card">
            <div class="skill-icon">{icon}</div>
            <div class="skill-name">{name}</div>
            <div style="margin-left:auto; display:flex; align-items:center; gap:0.3rem;">
                <span style="font-size:0.88rem; color:#aaa;">숙련도</span>
                <span style="font-size:1.1rem; letter-spacing:2px; color:#e94560;">{filled}</span>
                <span style="font-size:1.1rem; letter-spacing:2px; color:#ddd;">{empty}</span>
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
