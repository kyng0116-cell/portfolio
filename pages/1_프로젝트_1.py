import streamlit as st


import base64
def img_to_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def img_to_html(img_path, width=40):
    with open(img_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return f'<img src="data:image/png;base64,{data}" width="{width}" height="{width}"/>'
    
st.set_page_config(page_title="다이소 뷰티 전략 분석", page_icon="🟥", layout="wide", initial_sidebar_state="collapsed")

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
html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; letter-spacing: 1px; }
* { word-break: keep-all !important; overflow-wrap: break-word !important; }
strong { font-size: 1.25rem !important; }
.page-header {
    background: linear-gradient(135deg, #0f3460, #533483);
    color: white; padding: 1.8rem 2rem;
    border-radius: 1rem; margin-bottom: 1.5rem;
}
.page-header h1 { margin: 0 0 0.3rem 0; font-size: 1.9rem; }
.page-header p  { margin: 0; color: rgba(255,255,255,0.7); font-size: 1.125rem; }
.section-box { background: #ffffff !important; border-radius: 1rem; padding: 1.8rem; box-shadow: 0 2px 16px rgba(0,0,0,0.07); margin-bottom: 1.2rem; color: #1a1a2e !important; }
.section-box * { color: #1a1a2e !important; }
.section-box p { color: #1a1a2e; font-size: 1.125rem; word-break: keep-all; overflow-wrap: break-word; line-height: 1.8; }
.section-box h3 { margin-top: 0; color: #1a1a2e; font-size: 1.5rem; border-left: 4px solid #533483; padding-left: 0.75rem; }
.section-box h4 { color: #1a1a2e; font-size: 1.375rem; }
.section-box strong { font-size: 1.25rem; }
[data-testid="stAppViewContainer"] { background: #f8f9fa !important; }
</style>
""", unsafe_allow_html=True)

logo_html = img_to_html("assets/daiso.png", width=60)

st.markdown(f"""
<div class="page-header">
    <div style="display:flex; align-items:center; gap:1rem;">
        {logo_html}
        <div>
            <h1>초저가를 넘어 초신뢰로</h1>
            <p>가격이 아닌 '품질 신뢰'를 만들 때 초저가가 초격차로 전환됩니다.</p>
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

st.markdown("""<div class="section-box">
<h3>프로젝트 개요</h3>
<div style="display:flex; gap:2rem; align-items:flex-start;">
    <div style="flex:1; border-right:1px solid #f0f0f5; padding-right:1.5rem;">
        <p style="margin:0.3rem 0; font-size:1.125rem;"><strong>기간</strong>&nbsp;&nbsp; 2026.02.09 ~ 2026.03.11</p>
        <p style="margin:0.3rem 0; font-size:1.125rem;"><strong>인원</strong>&nbsp;&nbsp; 5인</p>
        <p style="margin:0.3rem 0; font-size:1.125rem;"><strong>역할</strong>&nbsp;&nbsp; 데이터 정제, 데이터 전처리, 인과추론, 런칭 시뮬레이션 , 대시보드 제작</p>
        <p style="margin:0.3rem 0; font-size:1.125rem;"><strong>언어</strong>&nbsp;&nbsp; SQL, Python</p>
        <p style="margin:0.3rem 0; font-size:1.125rem;"><strong>시각화</strong>&nbsp;&nbsp; Tableau</p>
        <br/>
        <p style="font-size:1.25rem; color:#533483; font-weight:600; margin-bottom:0.4rem;">분석 기법</p>
        <div style="display:flex; flex-wrap:wrap; gap:0.4rem;">
            <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.94rem; color:#555;">인과추론(PSM·IPTW·OW)</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.94rem; color:#555;">RNN/LSTM</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.94rem; color:#555;">층화 샘플링</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.94rem; color:#555;">OCR</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.94rem; color:#555;">GIS 분석</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.94rem; color:#555;">DB 정규화</span>
        </div>
    </div>
    <div style="flex:1.5;">
        <p style="font-size:1.125rem; color:#555; line-height:1.8; margin-bottom:1rem;">
        저성장 기조 속에서도 144%의 기록적인 성장을 달성한 다이소 뷰티의 핵심 동인을 데이터로 규명하고, 
        '데이터 기반의 초신뢰' 구축을 통해 지속 가능한 성장을 견인할 2026년 통합 성장 전략을 수립했습니다.
        </p>
        <p style="font-size:1.25rem; font-weight:600; color:#533483; margin-bottom:0.5rem;">핵심 성과</p>
        <p style="font-size:1.125rem; color:#444; line-height:2;">
        🔬 900여 제품 수동 검증 및 식약처 인증 상품명 매칭<br/>
        📊 매출 영향 요인 우선순위 규명: 카테고리 &gt; 브랜드<br/>
        💡 기능성의 조절 효과 발견 (단독 효과 없음, 카테고리/브랜드와 결합 시 증폭)<br/>
        🗺 GIS 기반 Hub &amp; Spoke 물류 전략 제안<br/>
        🛒 입점 전략 시뮬레이터 개발
        </p>
    </div>
</div>
</div>""", unsafe_allow_html=True)

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
                <h4>1. 데이터 엔지니어링 및 무결성 확보</h4><br/> 
                <strong>이미지 제약 극복을 위한 3-Source OCR 구축:</strong> 상세페이지가 통이미지로 제공되어 
                성분 분석이 불가능한 한계를 돌파하기 위해, Clova OCR과 EasyOCR을 교차 적용하는 파이프라인을 
                구축했습니다. 300개 이상의 패턴 교정과 INCI 표준 변환을 거쳐 이미지 속 전성분을 
                정형 텍스트로 온전히 추출했습니다.<br/>
                <strong>900여 건의 상품 전수 매칭:</strong> 다이소 내부 데이터와 
                식약처 DB의 기능성 인증 제품 간의 정합성을 높이기 위해 900여 제품을 수기 검수했습니다. 성분 데이터에 
                식약처·EU 기준 알레르기 유발 물질 정보를 결합하여 안전성 리스크가 있는 제품군을 선별해냈습니다.<br/>
                <strong>3단 정규화 DB 설계:</strong> 중복이 많은 기존 Wide Table을 Core(기본),
                 Stats(판매 통계), Specs(성분·기능성)로 3단 분리 설계하여 30만 건 이상의 대용량 데이터 
                처리 효율과 참조 무결성을 극대화했습니다.<br/><br/>
                <h4>2. 고도화된 분석 방법론 적용</h4><br/>
                <strong>생존 분석 기반 연착륙 제품 식별:</strong> DTW(동적 시간 왜곡)로 시계열 판매 패턴을 군집화하고, 
                Kaplan-Meier 및 Cox PH 생존 분석 모델을 적용하여 핵심 매출을 견인하는 16.7%의 연착륙 제품군을 
                통계적으로 도출했습니다.<br/>
                <strong>인과추론 기반의 성분별 매출 기여도 정밀 분석:</strong> PSM(성향점수매칭), IPTW(역확률 가중치), 
                OW(중첩 가중치) 등의 방법론을 적용하여 카테고리 선호도나 브랜드 파워 같은 
                주요 교란 변수의 간섭을 통계적으로 제어했습니다.<br/>
                <strong>하이브리드 감성 라벨링:</strong> GPT-4o-mini의 대량 처리 속도와 
                Human-in-the-loop을 결합해 30만 건의 리뷰를 1차 라벨링하고, 수동 구축한 골든셋으로 
                교차 검증하여 95% 이상의 신뢰도를 확보했습니다.<br/><br/>
                <h4>3. 모델 및 알고리즘 최적화</h4><br/>
                <strong>실시간성 중심의 RNN/LSTM 채택:</strong> 유통 현장의 빠른 의사결정과 하드웨어 제약을 
                고려하여 시계열 감성 흐름 파악에 최적화된 RNN/LSTM 모델을 설계했습니다.<br/>
                <strong>GIS 기반 상권 수요 밀도 산출:</strong> 상권별 단기 체류 외국인 수, 유동 인구, 경쟁사 위치 지표를 
                표준화(z-score) 합산하는 수요 밀도 점수 알고리즘을 자체 설계했습니다.</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="section-box"><h3>주요 인사이트</h3><br/>
                <p><h4>1. 16.7%의 연착륙 법칙과 기초 스킨케어의 저력</h4><br/>
                <strong>데이터의 발견:</strong> 출시 6개월 후에도 살아남은 '연착륙 제품'은 전체의 16.7%에 불과했으나, 
                이 소수 정예 제품들이 뷰티 매출의 약 32.5%(1,300억 원)를 견인하고 있었습니다. 
                이 생존 제품의 83.3%가 스킨케어였으며, 그중 75%가 5,000원짜리 기초 제품이었습니다.<br/>
                <strong>인과적 통찰:</strong> 인과추론(PSM/OW) 결과, '기능성 성분'은 단독으로 매출을 
                일으키기보다 기존의 카테고리 인지도(스킨케어)와 결합할 때 효과가 폭발적으로 증폭되는 
                '조절 변수(Moderator)'로 작용합니다.<br/><br/>
                <h4>2. 관광 상권의 수요 이원화와 K-뷰티 스킨케어의 폭발성</h4><br/>
                <strong>관광객 데이터:</strong> 한국을 방문하는 1위 관광객인 중국인(약 578만 명)의 
                75.8%가 화장품을 구매합니다. 외국인 관광객 1,100만 명 중 42%가 MZ세대이며, 
                이들은 K-뷰티 스킨케어 수요로 직결되고 있습니다.<br/>
                <strong>수요 격차:</strong> GIS 데이터 분석 결과, 외국인이 밀집하는 상위 5% 상권(Hub)에서는 
                특정 품목을 쓸어 담는 '하울(Haul)' 소비 패턴이 극명하게 나타납니다. 
                기능성 더마 코스메틱에 대한 외국인 수요가 폭증하고 있어, 
                '연착륙 스킨케어'의 재고 수요가 일반 상권 대비 압도적으로 높습니다.</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="section-box"><h3>최적화 전략</h3><p>
                <h4>1. Safety: OCR 기반 전성분 필터링 시스템</h4><br/>
                <strong>문제점:</strong> 다이소몰 내 상품 정보가 주로 통이미지 형태로 제공되어 자동 필터링에 한계가 있습니다.<br/>
                <strong>해결 방안:</strong> OCR 파이프라인으로 전성분을 정형 데이터로 추출하고, 식약처·EU 기준 DB와 
                실시간 교차 검증하여 리스크 성분을 자동 스크리닝합니다.<br/>
                <strong>기대 효과:</strong> 소비자 불신 해소 및 시각장애인 정보 접근성 향상을 통한 ESG 경영 실천.<br/><br/>
                <h4>2. Revenue: '연착륙 스킨케어' 집중 및 타겟 마케팅</h4><br/>
                <strong>타겟 집중:</strong> 전체 뷰티 매출의 32.5%를 책임지는 연착륙 제품(16.7%) 중 
                83.3%가 스킨케어임을 확인, 5,000원 기초 제품을 핵심 상품군으로 육성합니다.<br/>
                <strong>협업 제안:</strong> '저자극·수분·데일리' 키워드에 부합하는 '라운드랩 독도 라인'과의 협업 및 
                광복절·독도의 날을 활용한 애국 마케팅으로 C-커머스와 차별화합니다.<br/><br/>
                <h4>3. Efficiency: GIS 기반 Hub & Spoke 이원화 물류</h4><br/>
                <strong>문제점:</strong> 외국인 밀집 상권에서 인기 스킨케어의 조기 품절 현상이 발생하고 있습니다.<br/>
                <strong>해결 방안:</strong> GIS 데이터로 외국인 트래픽 상위 5% 매장을 Hub로 지정하고 
                연착륙 스킨케어 재고 심도를 일반 매장 대비 획기적으로 높입니다.<br/><br/>
                <h4>4. 입점 테스트 시뮬레이션: 머신러닝 기반 매출 예측</h4><br/>
                <strong>문제점:</strong> 100% 사입 구조로 입점 실패 시 브랜드 신뢰도 하락과 재고 부담이 직결됩니다.<br/>
                <strong>해결 방안:</strong> 30만 건의 정제된 리뷰 데이터로 입점 전 단계에서 제품의 연착륙 확률과 
                예상 매출을 정량적으로 시뮬레이션합니다.</p></div>""", unsafe_allow_html=True)

elif tab == "📋 대시보드 설명":
    st.markdown(f'''
                <h4 style="margin-bottom:0; font-size:1.375rem;">표지</h4>
                <img src="data:image/png;base64,{img_to_base64("assets/다이소_표지.png")}" style="width:100%; max-width:1200px;">''', unsafe_allow_html=True)
    st.divider()
    st.markdown(f'''
                <h4 style="margin-bottom:0; font-size:1.375rem;">첫 번째 대시보드</h4>
                <img src="data:image/png;base64,{img_to_base64("assets/다이소_대시보드1.png")}" style="width:100%; max-width:1200px;">''', unsafe_allow_html=True)
    st.divider()
    st.markdown(f'''
                <h4 style="margin-bottom:0; font-size:1.375rem;">두 번째 대시보드</h4>
                <img src="data:image/png;base64,{img_to_base64("assets/다이소_대시보드2.png")}" style="width:100%; max-width:1200px;">''', unsafe_allow_html=True)
    st.divider()
    st.markdown(f'''
                <h4 style="margin-bottom:0; font-size:1.375rem;">세 번째 대시보드</h4>
                <img src="data:image/png;base64,{img_to_base64("assets/다이소_대시보드3.png")}" style="width:100%; max-width:1200px;">''', unsafe_allow_html=True)
    st.divider()
    st.markdown(f'''
                <h4 style="margin-bottom:0; font-size:1.375rem;">네 번째 대시보드</h4>
                <img src="data:image/png;base64,{img_to_base64("assets/다이소_대시보드4.png")}" style="width:100%; max-width:1200px;">''', unsafe_allow_html=True)
    st.divider()

st.divider()
if st.button("🏠 홈으로", key="home_btn"):
    st.switch_page("Home.py")
