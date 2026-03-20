import streamlit as st


import base64
def img_to_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def img_to_html(img_path, width=40):
    with open(img_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return f'<img src="data:image/png;base64,{data}" width="{width}" height="{width}"/>'
    
st.set_page_config(page_title="다이소 뷰티 전략 분석", page_icon="🟥", layout="wide")

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
            <p>가격이 아닌 ‘품질 신뢰’를 만들 때 초저가가 초격차로 전환됩니다.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
tab = st.radio(
    label="섹션 선택",
    options=["💡 인사이트", "📋 대시보드 설명"],
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
    st.markdown("""<div class="section-box"><h3>분석 배경 및 목적</h3><br/><p>
                <strong>거시적 위기와 다이소의 역설:</strong> 2026년 L자형 저성장(1.9%) 국면에서 
                소비자는 필수재 위주로 지갑을 닫았으나, 다이소 뷰티는 144% 급성장하며 매출 4천억 원 규모의 
                핵심 동력이 되었습니다. 이는 실패 비용을 최소화하려는 MZ세대의 '리트머스 소비'와, 
                이에 동조한 4050 액티브 시니어(+139%)의 유입이 만든 결과입니다.<br/><br/>
                <strong>신뢰성 위협:</strong> 성급한 외형 성장의 이면에는 '납 검출' 등 품질 이슈와 
                C-커머스의 공세가 맞물려 '저가 제품은 위험하다'는 브랜드 신뢰 위기가 존재했습니다. 
                특히 다이소 뷰티 소비자의 23%가 '성분 분석형'인 상황에서, 100% 사입 구조를 가진 다이소에게 
                이는 단 한 번의 사고로 전체 성장이 멈출 수 있는 구조적 결함이었습니다.<br/><br/>
                <strong>분석의 지향점:</strong> 단순 가성비를 넘어, 데이터 기반의 품질 안전 시스템과 
                외국인 관광객 트래픽을 고려한 상권별 재고 최적화를 통해 '초신뢰(Hyper-Trust)' 브랜드 이미지를 
                구축하고 경쟁사가 복제할 수 없는 초격차 전략을 수립하는 데 목적을 두었습니다.</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="section-box"><h3>분석 과정</h3><p>
                <h4>1. 데이터 엔지니어링 및 무결성 확보(Data Integrity & Grit)</h4><br/> 
                <strong>이미지 제약 극복을 위한 3-Source OCR 구축:</strong> 상세페이지가 통이미지로 제공되어 
                성분 분석이 불가능한 한계를 돌파하기 위해, Clova OCR과 EasyOCR을 교차 적용하는 파이프라인을 
                구축했습니다. 300개 이상의 패턴 교정과 INCI 표준 변환을 거쳐 이미지 속 전성분을 
                정형 텍스트로 온전히 추출했습니다.<br/>
                <strong>900여 건의 상품 전수 매칭을 통한 분석 기반 마련:<strong> 다이소 내부 데이터와 
                식약처 DB의 기능성 인증 제품 간의 정합성을 높이기 위해 900여 제품을 수기 검수했습니다. 성분 데이터에 
                식약처·EU 기준 알레르기 유발 물질 정보를 결합하여 안전성 리스크가 있는 제품군을 선별해냈으며, 
                이러한 데이터 고도화 작업을 통해 '초저가' 제품에 대한 '초신뢰' 분석이 가능한 
                고품질 통합셋을 완성했습니다.</br>
                <strong>3단 정규화 DB 설계:</strong> 중복이 많은 기존 Wide Table을 Core(기본),
                 Stats(판매 통계), Specs(성분·기능성)로 3단 분리 설계하여 30만 건 이상의 대용량 데이터 
                처리 효율과 참조 무결성을 극대화했습니다.</br></br>
                <h4>2. 고도화된 분석 방법론 적용 (Advanced Methodology)</h4></br>
                <strong>생존 분석(Survival Analysis) 기반 연착륙 제품 식별:</strong> 시장에서 장기 생존하는 
                제품을 정의하기 위해 DTW(동적 시간 왜곡)로 시계열 판매 패턴을 군집화하고, Kaplan-Meier 및 
                Cox PH 생존 분석 모델을 적용하여 핵심 매출을 견인하는 16.7%의 연착륙 제품군을 
                통계적으로 도출했습니다.</br>
                <strong>인과추론(Causal Inference) 기반의 성분별 매출 기여도 정밀 분석:</strong> 기능성 
                성분이 실질적인 매출 성장 동인인지 검증하기 위해 PSM(성향점수매칭), IPTW(역확률 가중치), 
                OW(중첩 가중치) 등의 방법론을 적용했습니다. 카테고리 선호도나 브랜드 파워 같은 
                주요 교란 변수(Confounder)의 간섭을 통계적으로 제어함으로써, 성분의 안전성과 기능성이 
                매출에 미치는 인과적 순수 효과(Net Effect)를정밀하게 산출했습니다.</br>
                <strong>하이브리드 감성 라벨링:</strong> GPT-4o-mini의 대량 처리 속도와 
                인간의 직관(Human-in-the-loop)을 결합해 30만 건의 리뷰를 1차 라벨링하고, 수동 구축한 골든셋으로 
                교차 검증하여 95% 이상의 신뢰도를 확보했습니다.</br><br/>
                <h4>3. 모델 및 알고리즘 최적화 (Model Optimization)</h4><br/>
                <strong>실시간성 중심의 RNN/LSTM 채택:</strong> 유통 현장의 빠른 의사결정과 하드웨어 제약을 
                고려하여, 무거운 트랜스포머 대신 시계열 감성 흐름 파악에 가볍고 최적화된 RNN/LSTM 모델을 
                설계했습니다.<br/>
                <strong>GIS 기반 상권 수요 밀도(Hub Score) 산출:</strong> 최적의 물류 배분을 위해 상권별 
                단기 체류 외국인 수, 유동 인구, 경쟁사 위치 지표를 표준화(z-score) 합산하는 수요 밀도 점수 
                알고리즘을 자체 설계하여 물류 효율화의 통계적 근거를 마련했습니다.</p></div>""", unsafe_allow_html=True)
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
    st.markdown("""<div class="section-box"><h3>최적화 전략</h3><p>내용을 입력하세요.</p></div>""", unsafe_allow_html=True)

elif tab == "📋 대시보드 설명":
    st.markdown(f'''
                <h4 style="margin-bottom:0;">표지</h4>
                <img src="data:image/png;base64,{img_to_base64("assets/다이소_표지.png")}" style="width:100%; max-width:1200px;">''', unsafe_allow_html=True)
    st.divider()
    st.markdown(f'''
                <h4 style="margin-bottom:0;">첫 번째 대시보드 </h4>
                <img src="data:image/png;base64,{img_to_base64("assets/다이소_대시보드1.png")}" style="width:100%; max-width:1200px;">''', unsafe_allow_html=True)
    st.divider()
    st.markdown(f'''
                <h4 style="margin-bottom:0;">두 번째 대시보드 </h4>
                <img src="data:image/png;base64,{img_to_base64("assets/다이소_대시보드2.png")}" style="width:100%; max-width:1200px;">''', unsafe_allow_html=True)
    st.divider()
    st.markdown(f'''
                <h4 style="margin-bottom:0;">세 번째 대시보드 </h4>
                <img src="data:image/png;base64,{img_to_base64("assets/다이소_대시보드3.png")}" style="width:100%; max-width:1200px;">''', unsafe_allow_html=True)
    st.divider()
    st.markdown(f'''
                <h4 style="margin-bottom:0;">네 번째 대시보드 </h4>
                <img src="data:image/png;base64,{img_to_base64("assets/다이소_대시보드4.png")}" style="width:100%; max-width:1200px;">''', unsafe_allow_html=True)
    st.divider()
   

        

st.divider()
if st.button("🏠 홈으로", key="home_btn"):
    st.switch_page("Home.py")
