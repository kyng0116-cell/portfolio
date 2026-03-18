import streamlit as st


import base64

def img_to_html(img_path, width=40):
    with open(img_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return f'<img src="data:image/png;base64,{data}" width="{width}" height="{width}"/>'
    
st.set_page_config(page_title="다이소 뷰티 전략 분석", page_icon="📈", layout="wide")

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
.page-header {
    background: linear-gradient(135deg, #0f3460, #533483);
    color: white; padding: 1.8rem 2rem;
    border-radius: 1rem; margin-bottom: 1.5rem;
}
.page-header h1 { margin: 0 0 0.3rem 0; font-size: 1.7rem; }
.page-header p  { margin: 0; opacity: 0.7; font-size: 0.9rem; }
.section-box {
    background: #fff; border-radius: 1rem; padding: 1.8rem;
    box-shadow: 0 2px 16px rgba(0,0,0,0.07); margin-bottom: 1.2rem;
}
.section-box h3 { margin-top: 0; color: #1a1a2e; border-left: 4px solid #533483; padding-left: 0.75rem; }
</style>
""", unsafe_allow_html=True)

logo_html = img_to_html("assets/daiso.png", width=60)

st.markdown(f"""
<div class="page-header">
    <div style="display:flex; align-items:center; gap:1rem;">
        {logo_html}
        <div>
            <h1>초저가에서 초신뢰로</h1>
            <p>프로젝트 1 한 줄 설명을 입력하세요.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
tab = st.radio(
    label="섹션 선택",
    options=["💡 인사이트", "📋 대시보드 설명", "📊 대시보드"],
    index=0, horizontal=True, label_visibility="collapsed"
)
st.divider()

if tab == "💡 인사이트":
    st.markdown('<div class="section-box"><h3>분석 배경 및 목적</h3><p>어떤 문제를 해결하려 했는지 작성하세요.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-box"><h3>분석 과정</h3><p>데이터 수집 → 전처리 → 분석 → 시각화 순서로 작성하세요.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-box"><h3>주요 인사이트</h3><p>분석을 통해 얻은 핵심 인사이트를 정리하세요.</p></div>', unsafe_allow_html=True)

elif tab == "📋 대시보드 설명":
    st.markdown("#### 첫 번째 대시보드")
    st.image("https://via.placeholder.com/900x500?text=Dashboard+1+Description", use_container_width=True)
    # 👉 실제 사용: st.image("images/proj2_dash1_desc.png", use_container_width=True)
    st.divider()
    st.markdown("#### 두 번째 대시보드")
    st.image("https://via.placeholder.com/900x500?text=Dashboard+2+Description", use_container_width=True)
    # 👉 실제 사용: st.image("images/proj2_dash2_desc.png", use_container_width=True)
    st.divider()
    st.markdown("#### 세 번째 대시보드")
    st.image("https://via.placeholder.com/900x500?text=Dashboard+3+Description", use_container_width=True)
    # 👉 실제 사용: st.image("images/proj2_dash3_desc.png", use_container_width=True)
    st.divider()
    st.markdown("#### 네 번째 대시보드")
    st.image("https://via.placeholder.com/900x500?text=Dashboard+4+Description", use_container_width=True)
    # 👉 실제 사용: st.image("images/proj2_dash4_desc.png", use_container_width=True)

elif tab == "📊 대시보드":
    with st.expander("📌 첫 번째 대시보드", expanded=True):
        st.markdown("""
        <div style="overflow: hidden; width: 1210px; height: 1375px;">
            <div style="
                transform-origin: top left;
                transform: scale(0.55);
                width: 2200px;
                height: 2500px;
            ">
                <iframe src="https://public.tableau.com/views/_17733968701580/sheet0?:embed=y&:showVizHome=no&:toolbar=yes"
                    width="2200"
                    height="2500"
                    frameborder="0">
                </iframe>
            </div>
        </div>
        """, unsafe_allow_html=True)

        

st.divider()
if st.button("🏠 홈으로", key="home_btn"):
    st.switch_page("Home.py")
