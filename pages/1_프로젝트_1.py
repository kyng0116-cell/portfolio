import streamlit as st


import base64

def img_to_html(img_path, width=40):
    with open(img_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return f'<img src="data:image/png;base64,{data}" width="{width}" height="{width}"/>'
    
st.set_page_config(page_title="다이소 뷰티 전략 분석", page_icon="🟥", layout="wide")

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
    if st.button("🟥  다이소 뷰티 전략 분석", use_container_width=True, key="sb_p1"):
        st.switch_page("pages/1_프로젝트_1.py")
    if st.button("🟩  스타벅스 마케팅 분석", use_container_width=True, key="sb_p2"):
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
.page-header p  { margin: 0; color: rgba(255,255,255,0.7); font-size: 0.9rem; }
.section-box {
    background: #fff; border-radius: 1rem; padding: 1.8rem;
    box-shadow: 0 2px 16px rgba(0,0,0,0.07); margin-bottom: 1.2rem;
    color: #1a1a2e;
}
.section-box p { color: #1a1a2e; word-break: keep-all; overflow-wrap: break-word; }
.section-box h4 { color: #1a1a2e; }
.section-box h3 { margin-top: 0; color: #1a1a2e; border-left: 4px solid #533483; padding-left: 0.75rem; }
</style>
""", unsafe_allow_html=True)

logo_html = img_to_html("assets/daiso.png", width=60)

st.markdown(f"""
<div class="page-header">
    <div style="display:flex; align-items:center; gap:1rem;">
        {logo_html}
        <div>
            <h1>초저가를 넘어 초신뢰로</h1>
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
    with open("assets/다이소.pdf", "rb") as f:
        st.download_button(
            label="📎 발표자료 다운로드",
            data=f,
            file_name="다이소.pdf",
            mime="application/pdf"
        )
    st.markdown("""<div class="section-box"><h3>분석 배경 및 목적</h3><br/><p><strong>거시적 경제 위기:</strong> 2026년 한국 경제성장률이 $1.9%$로 전망되며, 구조적 저성장인 'L자형 침체'가 고착화되는 국면입니다. 
                이에 따라 소비자들이 필수재 외의 지출을 줄이는 상황입니다.<br/><br/>
                <strong>다이소 뷰티의 역설적 성장:</strong> 불황 속에서도 다이소 뷰티 카테고리는 144% 성장하며 
                전체 매출의 약 10%(4,000억 원 규모)를 차지하는 핵심 동력으로 부상했습니다.<br/><br/>
                <strong>신뢰 자산의 위기:</strong> '스텐 세정제 납 검출' 사건과 C-커머스(알리, 테무)의 
                유해 물질 이슈가 맞물리며 '초저가 제품은 위험하다'는 부정적 프레임이 형성되었습니다.<br/><br/>
                <strong>전략적 목적:</strong> 단순 가성비를 넘어 '데이터 기반의 품질 안전'과 
                '고객 맞춤형 효율화'를 통해 2026년의 구조적 위기를 돌파하고 초격차 성장을 달성하는 것입니다.</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="section-box"><h3>분석 과정</h3><p>
                <h4>1. 데이터 수집 및 샘플링</h4><br/>
                <strong>데이터 규모:</strong> 약 30만 건의 리뷰 데이터를 확보하여 분석의 기초로 삼았습니다.<br/>
                <strong>층화 샘플링:</strong> 데이터의 질과 대표성을 위해 5단계 샘플링을 수행했습니다.
                 중복 및 저품질 리뷰를 제거하고, 카테고리별 최소 할당량(대분류 600건 등)을 설정하여 
                다양성을 확보했습니다.
                <strong>감성 비율 보정:</strong> 문제점 발굴을 위해 긍정 리뷰가 압도적인 자연 데이터의 편향을 
                제거하고, 부정 30%, 중립 30%, 긍정 40%로 비율을 인위적으로 조정했습니다.<br/><br/>
                <h4>2. 데이터 전처리 및 라벨링</h4><br/>
                <strong>AI & Human 루프:</strong> GPT-4o-mini로 대량 라벨링을 수행한 뒤, 
                신뢰도가 낮은 데이터는 GPT-4o가 재판정하게 했습니다. 
                최종적으로 1,000건은 사람이 직접 검수하여 '골든셋'을 구축했습니다.
                <strong>DB 구조 혁신:</strong> 기존 'Wide Table'의 중복 문제를 해결하기 위해 
                상품 정보를 Core(기본), Stats(통계), Specs(속성)로 3단 정규화하여 
                데이터 무결성을 높였습니다.<br/><br/>
                <h4>3.분석 모델링</h4><br/>
                <strong>모델 선정:</strong> 실시간 대용량 처리가 필요한 유통 환경의 특성을 고려하여, 
                무거운 트랜스포머 모델 대신 시계열적 흐름과 감성 분류에 효율적인 RNN/LSTM을 채택했습니다.<br/>
                <strong>통계적 검증:</strong> 1,000건의 무작위 검증을 통해 95% 신뢰수준에서 
                데이터 정합성을 입증했습니다.</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="section-box"><h3>주요 인사이트</h3><br/>
                <p><h4>1. 9.2%의 법칙과 스킨케어</h4><br>
                 출시 6개월 후에도 살아남은 '연착륙 제품'이 매출의 상당 부분을 차지하며, 
                이들의 83.3%가 스킨케어 제품이라는 점에 주목해야 합니다.<br/><br/>
                <h4>2. 초신뢰 시스템의 필요성</h4><br/>
                 성분 분석형 소비자를 위해 OCR 기술을 도입하여 상세페이지 이미지의 전성분을 텍스트화하고 
                유해 성분을 자동 차단하는 시스템이 브랜드 신뢰 회복의 핵심입니다.<br/><br/>
                <h4>3. 상권 이원화(Hub & Spoke)</h4><br/> 
                GIS 데이터를 활용해 외국인 관광객이 몰리는 상위 5% 매장을 'Hub'로 지정하고, 
                스킨케어 재고 심도를 일반 매장 대비 대폭 강화하는 물류 최적화가 필요합니다.</p></div>""", unsafe_allow_html=True)

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
    with st.expander("대시보드", expanded=True):
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
