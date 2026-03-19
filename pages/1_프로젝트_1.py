import streamlit as st

import base64

def img_to_html(img_path, width=40):
    with open(img_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return f'<img src="data:image/png;base64,{data}" width="{width}" height="{width}"/>'
    
    
st.set_page_config(page_title="스타벅스 마케팅 분석", page_icon="🟩", layout="wide")

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
html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }.section-box p { word-break: keep-all; }
.page-header {
    background: linear-gradient(135deg, #1a1a2e, #0f3460);
    color: white; padding: 1.8rem 2rem;
    border-radius: 1rem; margin-bottom: 1.5rem;
}
.page-header h1 { margin: 0 0 0.3rem 0; font-size: 1.7rem; }
.page-header p  { margin: 0; opacity: 0.7; font-size: 0.9rem; }
.section-box {
    background: #fff; border-radius: 1rem; padding: 1.8rem;
    box-shadow: 0 2px 16px rgba(0,0,0,0.07); margin-bottom: 1.2rem;
}
.section-box h3 { margin-top: 0; color: #1a1a2e; border-left: 4px solid #e94560; padding-left: 0.75rem; }
</style>
""", unsafe_allow_html=True)

logo_html = img_to_html("assets/starbucks.png", width=60)

st.markdown(f"""
<div class="page-header">
    <div style="display:flex; align-items:center; gap:1rem;">
        {logo_html}
        <div>
            <h1>starbucks next level</h1>
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
    with open("assets/스타벅스.pdf", "rb") as f:
        st.download_button(
            label="📎 발표자료 다운로드",
            data=f,
            file_name="스타벅스.pdf",
            mime="application/pdf"
        )
    st.markdown("""<div class="section-box"><h3>분석 배경 및 목적</h3><p>**해결하려는 문제:** 기존의 인구통계학(Who) 중심의 단순 성과 지표로는 
                "왜 특정 프로모션이 성공 또는 실패했는지"에 대한 근본적인 원인을 파악하고 다음 마케팅 액션에 적용하기 어려웠습니다.<br/><br/>
                **분석 목적**: 고객의 프로모션 수신부터 확인, 완료에 이르는 '행동 여정(Customer Journey)'에 집중하여, 
                어떤 조건(난이도/혜택)과 접점(채널)이 실제 행동 전환을 유발하는지 행동경제학 관점에서 분석하고 객관적인 프로모션 설계 기준을 도출하고자 했습니다.</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="section-box"><h3>분석 과정</h3><p>
                ###1.데이터 수집<br/> 
                프로모션 조건 정보(Portfolio), 고객 행동 로그(Transcript), 고객 인구통계(Profile) 등 
                3가지 핵심 데이터셋을 연동하여 분석용 통합 DB를 구축했습니다.<br/><br/>
                ###2. 전처리<br/> 
                **목적별 이원화 정제:** 고객 행동 패턴을 온전히 보존하기 위한 '군집 분석용(결측치 1.01% 제거)'과 변수 간 비교의 신뢰도를 높이기 위한 '통계 해석용(결측치 6.46% 제거)'으로 데이터를 분리하여 정제 효율을 높였습니다.<br/>
                **전환(Success) 정의:** 단순 구매 발생이 아닌, 시간 순서상 '수신 → 확인 → 완료'의 행동 흐름이 유효하게 성립된 경우만을 진짜 '성과'로 판정하는 파생변수를 생성했습니다.<br/><br/>
                ###3. 분석<br/>
                K-means 군집화: 엘보우 방법(Elbow Method)을 통해 최적 군집 수(K=4)를 결정하고, 행동 지표(조회율, 완료율, 이탈률)를 기준으로 고객을 4개의 세그먼트(충성전환형, 설득가능전환형, 관심관망형, 저반응이탈형)로 세분화했습니다.<br/>
                **통계적 검증:** 비모수 검정(Kruskal-Wallis)을 통해 군집 간 지표 분포 차이의 유의성을 확인하고, 카이제곱 검정으로 프로모션 속성을 통제한 상태에서 채널 자체가 미치는 강력한 영향력을 통계적으로 입증했습니다.<br/><br/></p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="section-box"><h3>주요 인사이트</h3><p>
                ###1. 사회적 증거와 가용성 휴리스틱 (채널의 힘)<br/>
                SNS 채널은 타인의 반응이 노출되고 반복적으로 브랜드가 인지됨으로써 '사회적 증거'를 형성합니다. 이는 인지적 구두쇠 성향을 가진 고객의 탐색 비용을 줄여, Web 채널 대비 약 43.97%p 더 높은 압도적인 반응률을 이끌어냈습니다.<br/><br/>
                ###2. 손실 회피와 실질 지불액 (DISCOUNT의 조건)<br/>
                고객은 절대적인 할인 금액($3 vs $5)의 크기보다, 혜택을 얻기 위해 결제해야 하는 '최소 지불 금액(실질 부담액)'이 낮을 때 손실에 대한 저항감을 덜 느끼고 더 높은 완료율을 보였습니다.<br/><br/>
                ###3. 현재 편향과 즉각적 보상 (BOGO의 유효기간)<br/>
                직관적인 1+1 혜택(BOGO)의 경우, 유효기간이 7일일 때보다 5일로 짧을 때 성과가 약 10%p 더 높게 나타났습니다. 이는 마찰 비용을 낮추고 보상을 미루지 않게 만드는 '현재 편향'을 자극한 결과입니다</p></div>""", unsafe_allow_html=True)

elif tab == "📋 대시보드 설명":
    st.markdown("#### 첫 번째 대시보드")
    st.image("https://via.placeholder.com/900x500?text=Dashboard+1+Description", use_container_width=True)
    # 👉 실제 사용: st.image("images/proj1_dash1_desc.png", use_container_width=True)
    st.divider()
    st.markdown("#### 두 번째 대시보드")
    st.image("https://via.placeholder.com/900x500?text=Dashboard+2+Description", use_container_width=True)
    # 👉 실제 사용: st.image("images/proj1_dash2_desc.png", use_container_width=True)

elif tab == "📊 대시보드":
    with st.expander("대시보드", expanded=True):
        st.markdown("""
        <div style="overflow: hidden; width: 1210px; height: 715px;">
            <div style="
                transform-origin: top left;
                transform: scale(0.55);
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
        
        # 👉 예시:
        # import plotly.express as px, pandas as pd
        # df = pd.read_csv("data/proj1.csv")
        # st.plotly_chart(px.bar(df, x="날짜", y="값"), use_container_width=True)

st.divider()
if st.button("🏠 홈으로", key="home_btn"):
    st.switch_page("Home.py")
