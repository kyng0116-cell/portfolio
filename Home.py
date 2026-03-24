import streamlit as st
import streamlit.components.v1 as components
import base64

def img_to_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

def load_html(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "<p>파일을 불러올 수 없습니다.</p>"

st.set_page_config(page_title="다이소 뷰티 전략 분석", page_icon="🟥", layout="wide", initial_sidebar_state="collapsed")

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
html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }
[data-testid="stAppViewContainer"] { background: #f8f9fa !important; }
[data-testid="stHeader"] { background: #f8f9fa !important; }
.stApp { background: #f8f9fa !important; }
.section-title {
    font-size: 1.4rem; font-weight: 700; color: #1a1a2e;
    margin: 2rem 0 1rem 0; padding-bottom: 0.4rem;
    border-bottom: 2.5px solid #533483; display: inline-block;
}
/* 슬라이드 래퍼 — 반응형 스케일 */
.slide-wrapper {
    width: 100%;
    aspect-ratio: 16 / 9;
    border-radius: 1rem;
    overflow: hidden;
    box-shadow: 0 4px 24px rgba(26,26,46,0.10);
    border: 1px solid #e8e8ee;
    background: #f8f9fa;
}
</style>
""", unsafe_allow_html=True)

# ── 페이지 타이틀 ──────────────────────────────
st.markdown("""
<div style="margin-bottom:1.5rem;">
  <div style="font-size:0.75rem; font-weight:700; color:#e60012; letter-spacing:2px; text-transform:uppercase; margin-bottom:0.4rem;">
    MAIN PROJECT · 2026.02 ~ 03 · 5인 팀
  </div>
  <div style="font-size:2rem; font-weight:900; color:#1a1a2e; line-height:1.3;">
    초저가를 넘어 초신뢰로
  </div>
  <div style="font-size:1rem; color:#777; margin-top:0.3rem;">
    다이소 뷰티 144% 성장 이면의 구조적 결함을 데이터로 해체하다
  </div>
</div>
""", unsafe_allow_html=True)

# ── 슬라이드 1: 문제 정의 ──────────────────────
st.markdown('<div class="section-title">📌 문제 발견</div>', unsafe_allow_html=True)
slide1 = load_html("slides/slide1_problem.html")
components.html(slide1, height=530, scrolling=False)

st.markdown("<div style='margin-top:2rem;'></div>", unsafe_allow_html=True)

# ── 슬라이드 2: 솔루션 ────────────────────────
st.markdown('<div class="section-title">⚙️ 분석 접근법</div>', unsafe_allow_html=True)
slide2 = load_html("slides/slide2_approach.html")
components.html(slide2, height=530, scrolling=False)

st.markdown("<div style='margin-top:2rem;'></div>", unsafe_allow_html=True)

# ── 슬라이드 3: 결과 ──────────────────────────
st.markdown('<div class="section-title">📊 결과 및 인사이트</div>', unsafe_allow_html=True)
slide3 = load_html("slides/slide3_results.html")
components.html(slide3, height=530, scrolling=False)

st.markdown("<div style='margin-top:3rem;'></div>", unsafe_allow_html=True)