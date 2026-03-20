import streamlit as st

import base64
def img_to_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()
    
def img_to_html(img_path, width=40):
    with open(img_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return f'<img src="data:image/png;base64,{data}" width="{width}" height="{width}"/>'
    
st.set_page_config(page_title="스타벅스 마케팅 분석", page_icon="🟩", layout="wide", initial_sidebar_state="collapsed")

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
        border-color: #533483;
    }
    [data-testid="stSidebarNav"] { display: none; }
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
.page-header { background: linear-gradient(135deg, #1a1a2e, #0f3460); color: white; padding: 1.8rem 2rem; border-radius: 1rem; margin-bottom: 1.5rem; }
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

logo_html = img_to_html("assets/starbucks.png", width=60)

st.markdown(f"""
<div class="page-header">
    <div style="display:flex; align-items:center; gap:1rem;">
        {logo_html}
        <div>
            <h1>Starbucks Next Level</h1>
            <p>행동경제학 X 마케팅을 통한 기획 분석</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

tab = st.radio(
    label="섹션 선택",
    options=["💡 인사이트", "📋 대시보드 설명"],
    index=0, horizontal=True, label_visibility="collapsed"
)

st.markdown("""<div class="section-box">
<h3>프로젝트 개요</h3>
<div style="display:flex; gap:2rem; align-items:flex-start;">
    <div style="flex:1; border-right:1px solid #f0f0f5; padding-right:1.5rem;">
        <p style="margin:0.3rem 0; font-size:1.125rem;"><strong>기간</strong>&nbsp;&nbsp; 2026.01.08 ~ 2026.01.21</p>
        <p style="margin:0.3rem 0; font-size:1.125rem;"><strong>인원</strong>&nbsp;&nbsp; 5인팀</p>
        <p style="margin:0.3rem 0; font-size:1.125rem;"><strong>역할</strong>&nbsp;&nbsp; 데이터 전처리, 채널 별 효과크기 산출, 대시보드 제작</p>
        <p style="margin:0.3rem 0; font-size:1.125rem;"><strong>언어</strong>&nbsp;&nbsp; SQL, Python</p>
        <p style="margin:0.3rem 0; font-size:1.125rem;"><strong>시각화</strong>&nbsp;&nbsp; Tableau</p>
        <br/>
        <p style="font-size:1.25rem; color:#533483; font-weight:600; margin-bottom:0.4rem;">분석 기법</p>
        <div style="display:flex; flex-wrap:wrap; gap:0.4rem;">
            <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.94rem; color:#555;">K-means</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.94rem; color:#555;">엘보우 방법</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.94rem; color:#555;">Kruskal-Wallis</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.94rem; color:#555;">카이제곱 검정</span>
            <span style="background:#f0f0f5; border-radius:99px; padding:0.15rem 0.6rem; font-size:0.94rem; color:#555;">행동경제학</span>
        </div>
    </div>
    <div style="flex:1.5;">
        <p style="font-size:1.125rem; color:#555; line-height:1.8; margin-bottom:1rem;">
        스타벅스 프로모션 데이터 분석을 통해 채널별 순수 효과를 정량화하고, 고객 세그먼트 기반 맞춤형 마케팅 전략 기준을 도출했습니다.
        </p>
        <p style="font-size:1.25rem; font-weight:600; color:#533483; margin-bottom:0.5rem;">핵심 성과</p>
        <p style="font-size:1.125rem; color:#444; line-height:2;">
        📡 SNS 43.97%p · Mobile 19.41%p · Web 7.16%p 채널 효과 정량화<br/>
        👥 K-means 기반 고객 4개 세그먼트 분류<br/>
        🧠 행동경제학 3가지 인사이트 도출<br/>
        📊 Tableau 동적 필터링 대시보드 구현
        </p>
    </div>
</div>
</div>""", unsafe_allow_html=True)

if tab == "💡 인사이트":
    with open("assets/스타벅스.pdf", "rb") as f:
        st.download_button(
            label="📎 발표자료 다운로드",
            data=f,
            file_name="스타벅스.pdf",
            mime="application/pdf"
        )
    with st.expander("대시보드", expanded=True):
        st.markdown("""
        <div style="overflow: hidden; width: 2200px; height: 1300px;">
            <div style="
                transform-origin: top left;
                transform: scale(1);
                width: 2200px;
                height: 1300px;
            ">
                <iframe src="https://public.tableau.com/views/starbucks_17734801363140/sheet1?:embed=y&:showVizHome=no&:toolbar=yes"
                    width="2200"
                    height="1300"
                    frameborder="0">
                </iframe>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("""<div class="section-box"><h3>분석 배경 및 목적</h3><br/>
                <p><strong>해결하려는 문제:</strong> 결과 중심적 분석에서 프로세스 중심의 행동 전환 분석으로의 전환.<br/>
                단편적인 인구통계 정보만으로는 프로모션 효율의 변동 원인을 객관적으로 설명하기 어렵습니다. 
                이는 비효율적인 자원 배분과 무분별한 메시지 발송으로 인한 고객 피로도를 가중시키는 원인이 됩니다. 
                이를 해결하기 위해 "누가 구매했는가"를 넘어 "어떤 트리거가 행동 전환을 유발했는가"에 
                초점을 맞춘 분석을 수행하고자 합니다.<br/><br/>
                <strong>분석 목적:</strong> 고객 행동 여정 기반의 프로모션 효율 최적화 및 설계 표준 수립.<br/>
                고객의 '수신-확인-참여 완료'에 이르는 행동 여정을 추적하여 구매 전환에 기여하는 핵심 변수를 
                발굴하고자 합니다. 특히 행동경제학 관점에서 혜택의 크기와 참여 난이도, 접점 채널이 전환율에 
                미치는 영향을 분석함으로써, 객관적이고 데이터에 기반한 프로모션 설계 기준을 도출하는 데 
                중점을 두었습니다.</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="section-box"><h3>분석 과정</h3><p><br/>
                <h4>1. 데이터 통합 및 최적화</h4><br/> 
                고객의 행동 여정을 입체적으로 파악하기 위해 프로모션·행동 로그·데모그래픽 데이터를 연동한 
                통합 데이터 마트를 설계했습니다. 세그먼트 분석 데이터셋과 시각화 전용 데이터셋을 
                분리 구조화함으로써, 데이터 처리 속도와 분석의 정확도를 동시에 확보했습니다.<br/><br/>
                <h4>2. 데이터 전처리 및 피처 엔지니어링</h4><br/>
                <strong>비정형 데이터 구조화:</strong> 딕셔너리 형태로 적재된 결제 내역 및 평점 데이터를 관계형 구조로 
                파싱하여 분석 가능한 수치형 변수로 변환했습니다.<br/>
                <strong>분석 변수 통제:</strong> 모든 실험군에 공통 적용된 '이메일' 채널은 
                채널별 순수 기여도 산출 시 변별력이 낮다고 판단하여 분석 범위에서 제외했습니다.<br/>
                <strong>목적별 데이터 정제 이원화:</strong><br/>
                &nbsp;&nbsp;- 군집 분석용: 결측치를 최소화(1.01% 제거)하여 데이터 완전성을 유지했습니다.<br/>
                &nbsp;&nbsp;- 통계 해석용: 엄격한 정제 기준(결측치 6.46% 제거)을 적용하여 노이즈를 차단했습니다.<br/>
                <strong>성과 지표 재정의:</strong> 시간 흐름에 따른 '수신 → 확인 → 완료'의 유효 경로가 성립된 
                케이스만을 진성 전환으로 판정하는 파생 변수를 생성했습니다.<br/><br/>
                <h4>3. 다각적 행동 분석</h4><br/>
                <strong>행동 기반 고객 세분화:</strong> 고객의 반응 패턴(수신-확인-완료)을 K-means 알고리즘으로 
                학습시켜 4개의 전략적 세그먼트를 도출했습니다.<br/>
                <strong>프로모션 속성 통제 분석:</strong> 프로모션 구성 요소를 상수로 두고 채널 변수만을 독립적으로 
                분석하여 카이제곱 검정으로 채널 선정의 중요성을 확인했습니다.<br/>
                <strong>통계적 유의성 확보:</strong> 모든 분석 결과는 통계 검증을 거쳐 객관적인 
                의사결정 근거로서의 신뢰성을 확보했습니다.</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="section-box"><h3>주요 인사이트</h3><p>
                <h4>1. 핵심 고객의 소비 지형: '생활권 중심'의 중장년층 행동 패턴</h4><br/>
                <strong>분석 결과:</strong> 50·60대가 전체 프로모션 참여의 핵심 고객층을 이루며, 
                40대가 그 뒤를 잇는 안정적인 지지층으로 확인되었습니다. 이들은 거주지나 일상 동선 내의 
                '생활권 중심 매장'에서 혜택을 소비하려는 뚜렷한 행동 패턴을 보였습니다.<br/>
                <strong>원인 해석:</strong> 중장년층에게는 파격적인 오퍼보다, 익숙한 생활 반경 내에서 마찰 없이 
                즉각적으로 접근할 수 있는 '편의성과 접근성(Convenience & Accessibility)'이 가장 
                강력한 전환 트리거로 작용합니다.<br/><br/>
                <h4>2. 리워드 설계의 핵심: 고액 혜택보다 '낮은 실질 지불액'과 '즉시 체감'</h4><br/>
                <strong>분석 결과:</strong> 고액 혜택 프로모션보다 조건이 단순하고 즉시 체감할 수 있는 할인 구조에서 
                완료율이 더 높게 관측되었습니다. 고객이 혜택을 받기 위해 결제해야 하는 '실질 지불 금액'이 낮을 때 
                반응률이 극대화되었습니다.<br/>
                <strong>원인 해석:</strong> 고객은 혜택의 기쁨보다 지출에 더 민감한 '손실 회피(Loss Aversion)' 
                경향을 가지므로, 초기 결제 부담을 낮추는 것이 전환 유도에 훨씬 효과적입니다.<br/><br/>
                <h4>3. 채널 영향력: 사회적 증거와 가용성 휴리스틱을 통한 전환율 극대화</h4><br/>
                <strong>분석 결과:</strong> SNS 채널이 Web 채널 대비 약 43.97%p 높은 전환율을 기록했습니다. 
                (SNS 43.97%p > Mobile 19.41%p > Web 7.16%p)<br/>
                <strong>원인 해석:</strong> SNS는 타인의 긍정적 반응이 실시간으로 노출되는 '사회적 증거(Social Proof)'를 
                형성하고, 지속적인 노출로 '가용성 휴리스틱(Availability Heuristic)'을 자극하여 
                신속한 의사결정을 유도합니다.<br/><br/>
                <h4>4. 다중 채널 시너지: 반복 노출을 통한 전환 성과 극대화</h4><br/>
                <strong>분석 결과:</strong> 여러 접점(Multi-channel)에 중복 노출된 고객일수록 최종 구매 완료로 
                이어지는 전환 성과가 유의미하게 증가했습니다.<br/>
                <strong>원인 해석:</strong> 반복적인 메시지 전달은 '단순 노출 효과(Mere-exposure Effect)'를 발생시켜 
                신뢰감을 형성하고 심리적 장벽을 낮추어 최종 행동 전환을 가속화합니다.</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="section-box"><h3>최적화 전략</h3><p>
                <h4>1. 하이퍼 로컬(Hyper-local) 기반 타겟팅 전략</h4><br/>
                <strong>핵심 타겟:</strong> 참여율과 안정성이 검증된 40·50·60대 중장년층에 화력을 집중합니다.<br/>
                <strong>지역 밀착형 운영:</strong> 고객의 거주지 및 일상 동선 내에 위치한 '생활권 중심 매장'을 
                핵심 거점으로 설정합니다.<br/>
                <strong>기대 효과:</strong> 이동에 따른 물리적·인지적 마찰을 제거하여 핵심 고객층의 참여를 
                즉각적으로 이끌어냅니다.<br/><br/>
                <h4>2. 실질 지불 부담 최소화 방식의 리워드 설계</h4><br/>
                <strong>리워드 구조 최적화:</strong> 고객이 실제로 지불해야 하는 '실질 지불 금액'을 낮추는 것에 
                집중합니다.<br/>
                <strong>심리적 진입 장벽 완화:</strong> 참여 조건이 낮은 단순 할인 구조를 우선적으로 편성합니다.<br/>
                <strong>기대 효과:</strong> '손실 회피' 심리를 제어하여 지출에 대한 거부감을 줄이고 완료율을 
                극대화합니다.<br/><br/>
                <h4>3. SNS 중심의 다중 채널 믹스(Multi-channel Mix) 운영</h4><br/>
                <strong>SNS 채널 리딩:</strong> 전환율 기여도가 압도적인(43.97%p) SNS를 메인 접점으로 활용합니다.<br/>
                <strong>다중 노출 시너지 창출:</strong> SNS, Mobile, Web 등 여러 접점에 메시지를 중복 노출시키는 
                리마인드 루프를 구축합니다.<br/>
                <strong>기대 효과:</strong> '단순 노출 효과'와 '사회적 증거'를 결합하여 고객의 심리적 장벽을 
                단계적으로 낮추고 최종 행동 전환을 가속화합니다.</p></div>""", unsafe_allow_html=True)

elif tab == "📋 대시보드 설명":
    st.markdown(f'''
                <h4 style="margin-bottom:0; font-size:1.375rem;">첫 번째 대시보드</h4>
                <img src="data:image/png;base64,{img_to_base64("assets/스타벅스_대시보드1.png")}" style="width:100%; max-width:1200px;">''', unsafe_allow_html=True)
    st.divider()
    st.markdown(f'''
                <h4 style="margin-bottom:0; font-size:1.375rem;">두 번째 대시보드</h4>
                <img src="data:image/png;base64,{img_to_base64("assets/스타벅스_대시보드2.png")}" style="width:100%; max-width:1200px;">''', unsafe_allow_html=True)

st.divider()
if st.button("🏠 홈으로", key="home_btn"):
    st.switch_page("Home.py")
