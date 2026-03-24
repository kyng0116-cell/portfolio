import streamlit as st

# ── 페이지 설정 ──────────────────────────────────────────────
st.set_page_config(
    page_title="김재경 · 데이터 분석가 포트폴리오",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── 전역 CSS ─────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=Space+Mono:wght@400;700&family=Bebas+Neue&display=swap');

/* ── 기본 리셋 ── */
:root {
    --bg:       #0a0a0f;
    --bg2:      #111118;
    --bg3:      #1a1a24;
    --accent:   #e63946;
    --accent2:  #ff6b6b;
    --gold:     #f4a261;
    --text:     #e8e8f0;
    --text2:    #9999b0;
    --border:   rgba(255,255,255,0.08);
    --card:     rgba(255,255,255,0.04);
}

html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Noto Sans KR', sans-serif !important;
}

[data-testid="stSidebar"] {
    background: var(--bg2) !important;
    border-right: 1px solid var(--border) !important;
}

[data-testid="stSidebar"] * { color: var(--text) !important; }

/* 사이드바 라디오 버튼 스타일 */
[data-testid="stSidebar"] .stRadio label {
    font-size: 0.9rem !important;
    padding: 6px 0 !important;
    cursor: pointer !important;
    transition: color 0.2s !important;
}
[data-testid="stSidebar"] .stRadio label:hover { color: var(--accent) !important; }

/* 구분선 */
hr { border-color: var(--border) !important; margin: 2rem 0 !important; }

/* 메트릭 카드 숨기기 */
[data-testid="stMetricValue"] { color: var(--accent) !important; font-family: 'Space Mono', monospace !important; }
[data-testid="stMetricLabel"] { color: var(--text2) !important; font-size: 0.8rem !important; }

/* 버튼 */
.stButton > button {
    background: transparent !important;
    border: 1px solid var(--accent) !important;
    color: var(--accent) !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.1em !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    background: var(--accent) !important;
    color: #fff !important;
}

/* 공통 카드 */
.card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.5rem 1.8rem;
    margin-bottom: 1rem;
    transition: border-color 0.2s;
}
.card:hover { border-color: rgba(230,57,70,0.4); }

/* 태그 */
.tag {
    display: inline-block;
    background: rgba(230,57,70,0.15);
    border: 1px solid rgba(230,57,70,0.4);
    color: var(--accent2);
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    padding: 3px 10px;
    border-radius: 20px;
    margin: 3px 2px;
}
.tag-neutral {
    background: rgba(255,255,255,0.06);
    border-color: rgba(255,255,255,0.15);
    color: var(--text2);
}

/* 스탯 박스 */
.stat-box {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent);
    border-radius: 8px;
    padding: 1rem 1.2rem;
    text-align: center;
}
.stat-num {
    font-family: 'Space Mono', monospace;
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--accent);
    line-height: 1.1;
}
.stat-label {
    font-size: 0.75rem;
    color: var(--text2);
    margin-top: 4px;
    line-height: 1.4;
}

/* 섹션 헤더 */
.sec-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    color: var(--accent);
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}
.sec-title {
    font-size: 1.6rem;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 0.3rem;
    line-height: 1.3;
}

/* 배지 */
.badge-mine {
    background: rgba(230,57,70,0.2);
    border: 1px solid var(--accent);
    color: var(--accent2);
    font-size: 0.65rem;
    padding: 1px 7px;
    border-radius: 4px;
    font-family: 'Space Mono', monospace;
    margin-left: 8px;
    vertical-align: middle;
}
.badge-award {
    background: rgba(244,162,97,0.2);
    border: 1px solid var(--gold);
    color: var(--gold);
    font-size: 0.72rem;
    padding: 3px 10px;
    border-radius: 4px;
    font-family: 'Space Mono', monospace;
}

/* 스텝 박스 */
.step-box {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 0.8rem;
    position: relative;
}
.step-num {
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem;
    color: var(--accent);
    letter-spacing: 0.15em;
    margin-bottom: 0.4rem;
}
.step-title {
    font-weight: 700;
    font-size: 0.95rem;
    margin-bottom: 0.4rem;
}
.step-body {
    font-size: 0.85rem;
    color: var(--text2);
    line-height: 1.7;
}

/* 인사이트 박스 */
.insight-box {
    background: linear-gradient(135deg, rgba(230,57,70,0.08), rgba(230,57,70,0.02));
    border: 1px solid rgba(230,57,70,0.25);
    border-radius: 10px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 0.8rem;
}
.insight-num {
    font-family: 'Space Mono', monospace;
    font-size: 2rem;
    color: rgba(230,57,70,0.3);
    font-weight: 700;
    line-height: 1;
    margin-bottom: 0.3rem;
}
.insight-title {
    font-weight: 700;
    font-size: 0.95rem;
    color: var(--text);
    margin-bottom: 0.4rem;
}
.insight-body {
    font-size: 0.83rem;
    color: var(--text2);
    line-height: 1.7;
}

/* 스킬 바 */
.skill-row {
    display: flex;
    align-items: center;
    margin-bottom: 0.6rem;
    gap: 0.8rem;
}
.skill-name {
    font-family: 'Space Mono', monospace;
    font-size: 0.78rem;
    color: var(--text2);
    min-width: 90px;
}
.skill-bar-bg {
    flex: 1;
    height: 5px;
    background: rgba(255,255,255,0.08);
    border-radius: 3px;
    overflow: hidden;
}
.skill-bar-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--accent), var(--accent2));
    border-radius: 3px;
}

/* 타임라인 */
.timeline-item {
    border-left: 2px solid var(--border);
    padding-left: 1.2rem;
    margin-bottom: 1.5rem;
    position: relative;
}
.timeline-item::before {
    content: '';
    position: absolute;
    left: -5px;
    top: 6px;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--accent);
}
.timeline-period {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    color: var(--accent);
    margin-bottom: 0.3rem;
}
.timeline-role {
    font-weight: 700;
    font-size: 0.95rem;
    margin-bottom: 0.2rem;
}
.timeline-org {
    font-size: 0.82rem;
    color: var(--text2);
    margin-bottom: 0.5rem;
}
.timeline-body {
    font-size: 0.83rem;
    color: var(--text2);
    line-height: 1.7;
}

/* 헤더 큰 타이틀 */
.hero-eyebrow {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.25em;
    color: var(--accent);
    text-transform: uppercase;
    margin-bottom: 0.6rem;
}
.hero-title {
    font-size: clamp(2rem, 4vw, 3.2rem);
    font-weight: 900;
    line-height: 1.15;
    margin-bottom: 0.8rem;
    color: var(--text);
}
.hero-title span { color: var(--accent); }
.hero-sub {
    font-size: 1rem;
    color: var(--text2);
    line-height: 1.8;
    max-width: 560px;
}

/* progress 색상 오버라이드 */
.stProgress > div > div > div > div {
    background: var(--accent) !important;
}

/* 숨길 요소 */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"] { display: none !important; }

/* expander */
details { border: 1px solid var(--border) !important; border-radius: 8px !important; background: var(--card) !important; }
summary { color: var(--text) !important; padding: 0.6rem 0 !important; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# SIDEBAR NAV
# ══════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 1rem 0 0.5rem;'>
        <div style='font-family:"Space Mono",monospace; font-size:0.65rem;
                    letter-spacing:0.2em; color:var(--accent); margin-bottom:6px;'>PORTFOLIO</div>
        <div style='font-size:1.3rem; font-weight:900; color:var(--text);'>김재경</div>
        <div style='font-size:0.78rem; color:var(--text2); margin-top:4px;'>데이터 분석가</div>
    </div>
    <hr style='margin: 1rem 0;'>
    """, unsafe_allow_html=True)

    page = st.radio(
        "",
        ["🏠  홈", "👤  About Me", "🔴  다이소 뷰티 (메인)", "☕  Starbucks (서브)", "🛠  스킬셋", "📬  Contact"],
        label_visibility="collapsed"
    )

    st.markdown("""
    <hr>
    <div style='font-size:0.75rem; color:var(--text2); line-height:1.9; padding-bottom: 1rem;'>
        <div>✉ kyng0116@gmail.com</div>
        <div>📱 010-5021-9745</div>
        <a href='https://github.com/kyng0116-cell' target='_blank'
           style='color:var(--accent2); text-decoration:none;'>
            🔗 github.com/kyng0116-cell
        </a>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# PAGE: 홈
# ══════════════════════════════════════════════════════════════
if "홈" in page:
    # ── Hero ──
    st.markdown("""
    <div style='padding: 3rem 0 2rem;'>
        <div class='hero-eyebrow'>DATA ANALYST · PORTFOLIO 2026</div>
        <div class='hero-title'>
            심리학적 사고로<br>
            소비자를 읽고,<br>
            <span>데이터로 전략을 만듭니다.</span>
        </div>
        <div class='hero-sub'>
            인과추론 · SQL · Python · Tableau<br>
            단국대 심리학 → 데이터 분석가로의 전환,<br>
            "왜"를 증명하는 분석을 합니다.
        </div>
        <div style='margin-top:1.2rem;'>
            <span class='badge-award'>🏆 스파르타 최종 프로젝트 최우수상 2026.03</span>
        </div>
    </div>
    <hr>
    """, unsafe_allow_html=True)

    # ── 핵심 수치 요약 ──
    st.markdown("<div class='sec-label'>KEY NUMBERS</div>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-num'>4</div>
            <div class='stat-label'>완수한<br>데이터 분석 프로젝트</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-num'>30만</div>
            <div class='stat-label'>건 처리한<br>뷰티 리뷰 데이터</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-num'>900+</div>
            <div class='stat-label'>수기 검수한<br>상품 수 (식약처 매칭)</div>
        </div>""", unsafe_allow_html=True)
    with c4:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-num'>3종</div>
            <div class='stat-label'>인과추론 기법<br>PSM · IPTW · OW</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── 메인 프로젝트 피처드 카드 ──
    st.markdown("<div class='sec-label'>FEATURED PROJECT</div>", unsafe_allow_html=True)
    st.markdown("""
    <div style='
        background: linear-gradient(135deg, rgba(230,57,70,0.12) 0%, rgba(26,26,36,0.8) 60%);
        border: 1px solid rgba(230,57,70,0.35);
        border-radius: 16px;
        padding: 2rem 2.2rem;
        margin-bottom: 1.5rem;
        position: relative;
        overflow: hidden;
    '>
        <div style='
            position:absolute; top:-20px; right:-10px;
            font-family:"Space Mono",monospace;
            font-size:7rem; font-weight:900;
            color:rgba(230,57,70,0.06);
            line-height:1; pointer-events:none;
        '>01</div>

        <div style='display:flex; align-items:flex-start; gap:1rem; flex-wrap:wrap;'>
            <div style='flex:1; min-width:240px;'>
                <div style='font-family:"Space Mono",monospace; font-size:0.65rem;
                            letter-spacing:0.2em; color:var(--accent); margin-bottom:0.5rem;'>
                    MAIN PROJECT · 2026.02 – 03 · 5인 팀
                </div>
                <div style='font-size:1.45rem; font-weight:900; color:var(--text);
                            line-height:1.2; margin-bottom:0.8rem;'>
                    초저가를 넘어 초신뢰로<br>
                    <span style='color:var(--accent);'>다이소 뷰티 전략 분석</span>
                </div>
                <div style='font-size:0.88rem; color:var(--text2); line-height:1.8;
                            max-width:480px; margin-bottom:1rem;'>
                    저성장 기조에서 144% 성장한 다이소 뷰티의 핵심 동인을
                    인과추론(PSM·IPTW·OW)으로 규명하고,
                    OCR 파이프라인 · GIS 수요 분석 · ML 시뮬레이터로
                    실행 가능한 2026년 통합 성장 전략을 수립했습니다.
                </div>
                <div>
                    <span class='tag'>인과추론</span>
                    <span class='tag'>OCR 파이프라인</span>
                    <span class='tag'>GIS 분석</span>
                    <span class='tag'>생존 분석</span>
                    <span class='tag'>RNN/LSTM</span>
                    <span class='tag'>Tableau</span>
                </div>
            </div>

            <div style='display:flex; flex-direction:column; gap:0.6rem; min-width:180px;'>
                <div style='background:rgba(255,255,255,0.04); border:1px solid var(--border);
                            border-left:3px solid var(--accent); border-radius:8px; padding:0.8rem 1rem;'>
                    <div style='font-family:"Space Mono",monospace; font-size:1.4rem;
                                font-weight:700; color:var(--accent);'>16.7%</div>
                    <div style='font-size:0.72rem; color:var(--text2); margin-top:3px;'>연착륙 제품 비율<br>→ 매출 32.5% 견인</div>
                </div>
                <div style='background:rgba(255,255,255,0.04); border:1px solid var(--border);
                            border-left:3px solid var(--gold); border-radius:8px; padding:0.8rem 1rem;'>
                    <div style='font-family:"Space Mono",monospace; font-size:1.4rem;
                                font-weight:700; color:var(--gold);'>144%</div>
                    <div style='font-size:0.72rem; color:var(--text2); margin-top:3px;'>저성장 속 다이소<br>뷰티 성장률</div>
                </div>
                <div style='background:rgba(255,255,255,0.04); border:1px solid var(--border);
                            border-left:3px solid #a8dadc; border-radius:8px; padding:0.8rem 1rem;'>
                    <div style='font-family:"Space Mono",monospace; font-size:1.4rem;
                                font-weight:700; color:#a8dadc;'>30만</div>
                    <div style='font-size:0.72rem; color:var(--text2); margin-top:3px;'>리뷰 데이터 처리<br>95%↑ 신뢰도 확보</div>
                </div>
            </div>
        </div>

        <div style='margin-top:1.2rem; padding-top:1rem;
                    border-top:1px solid rgba(255,255,255,0.07);
                    font-size:0.8rem; color:var(--text2);'>
            <b style='color:var(--text);'>내 기여:</b>
            데이터 정제 · 전처리 · 인과추론 설계 · 런칭 시뮬레이션 · Tableau 대시보드 제작
            &nbsp;&nbsp;|&nbsp;&nbsp;
            <span style='color:var(--gold);'>🏆 최우수상</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── 서브 프로젝트 미니카드 ──
    st.markdown("<div class='sec-label'>SUB PROJECT</div>", unsafe_allow_html=True)
    st.markdown("""
    <div style='
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 1.4rem 1.8rem;
        display:flex; align-items:center; gap:1.5rem; flex-wrap:wrap;
    '>
        <div style='flex:1; min-width:220px;'>
            <div style='font-family:"Space Mono",monospace; font-size:0.65rem;
                        letter-spacing:0.15em; color:#52b788; margin-bottom:0.4rem;'>
                SUB PROJECT · 2026.01 · 5인 팀
            </div>
            <div style='font-size:1.05rem; font-weight:700; margin-bottom:0.4rem;'>
                Starbucks Next Level<br>
                <span style='color:#52b788;'>행동경제학 기반 마케팅 분석</span>
            </div>
            <div style='font-size:0.83rem; color:var(--text2); line-height:1.7;'>
                채널별 순수 효과를 정량화하고 고객 세그먼트 기반
                맞춤 마케팅 전략 기준을 도출했습니다.
            </div>
            <div style='margin-top:0.7rem;'>
                <span class='tag' style='border-color:rgba(82,183,136,0.4); color:#52b788; background:rgba(82,183,136,0.1);'>K-means</span>
                <span class='tag' style='border-color:rgba(82,183,136,0.4); color:#52b788; background:rgba(82,183,136,0.1);'>행동경제학</span>
                <span class='tag' style='border-color:rgba(82,183,136,0.4); color:#52b788; background:rgba(82,183,136,0.1);'>Tableau</span>
            </div>
        </div>
        <div style='display:flex; gap:0.8rem;'>
            <div style='text-align:center;'>
                <div style='font-family:"Space Mono",monospace; font-size:1.3rem;
                            font-weight:700; color:#52b788;'>43.97%p</div>
                <div style='font-size:0.7rem; color:var(--text2);'>SNS vs Web<br>채널 효과 차이</div>
            </div>
            <div style='width:1px; background:var(--border);'></div>
            <div style='text-align:center;'>
                <div style='font-family:"Space Mono",monospace; font-size:1.3rem;
                            font-weight:700; color:#52b788;'>2.4×</div>
                <div style='font-size:0.7rem; color:var(--text2);'>3채널 중복<br>전환율 상승</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# PAGE: ABOUT ME
# ══════════════════════════════════════════════════════════════
elif "About" in page:
    st.markdown("""
    <div style='padding: 2rem 0 1rem;'>
        <div class='hero-eyebrow'>ABOUT ME</div>
        <div class='hero-title' style='font-size:2.2rem;'>
            사람을 이해하는 방식이<br>
            <span>달라졌을 뿐입니다.</span>
        </div>
    </div>
    <hr>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("<div class='sec-label'>STORY</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='card' style='font-size:0.92rem; line-height:1.9; color:var(--text2);'>
            심리학도로서 저는 늘 <b style='color:var(--text);'>"왜 사람들은 이런 선택을 할까?"</b>를 물어왔습니다.<br><br>
            졸업 후 테슬라 인턴 · 그리트라운지 팀장을 거치며
            현장 데이터를 직접 만지고, 수동 업무를 자동화하고,
            트래킹 시스템을 설계하는 경험을 쌓았습니다.<br><br>
            그리고 깨달았습니다 — 심리학적 질문에 가장 강력하게 답하는 도구가
            <b style='color:var(--accent);'>데이터</b>라는 것을.
            지금은 소비자 행동의 '왜'를 인과추론으로 증명하는 데이터 분석가로 일합니다.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br><div class='sec-label'>CORE STRENGTHS</div>", unsafe_allow_html=True)

        strengths = [
            ("인과추론 기반 분석",
             "PSM·IPTW·OW 3종 교차 검증으로 '기능성 성분의 조절 효과'를 통계적으로 증명. 상관관계가 아닌 인과관계를 묻습니다.",
             "다이소 뷰티 프로젝트 직접 수행"),
            ("End-to-End 실행력",
             "OCR 파이프라인 구축 → 30만 건 DB 정규화 → Tableau 대시보드까지. 기획부터 전달까지 혼자 완결할 수 있습니다.",
             "데이터 엔지니어링 + 시각화 모두 담당"),
            ("비즈니스 맥락 독해력",
             "수천 건의 전기차 보조금 트래킹 시스템을 팀장으로 설계한 경험. 데이터가 실무 의사결정과 어떻게 연결되는지 압니다.",
             "그리트라운지 팀장 시절"),
        ]

        for title, body, evidence in strengths:
            st.markdown(f"""
            <div class='card'>
                <div style='font-weight:700; font-size:0.95rem; margin-bottom:0.4rem;
                            color:var(--text);'>▸ {title}</div>
                <div style='font-size:0.85rem; color:var(--text2); line-height:1.7;
                            margin-bottom:0.5rem;'>{body}</div>
                <div style='font-size:0.73rem; font-family:"Space Mono",monospace;
                            color:var(--accent);'>↳ {evidence}</div>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='sec-label'>CAREER TIMELINE</div>", unsafe_allow_html=True)

        timeline = [
            ("2026.02–03", "데이터 분석 프로젝트 (최우수상)", "스파르타 내일배움캠프",
             "다이소 뷰티 전략 분석 — 인과추론·OCR·GIS 통합"),
            ("2025.10–2026.03", "데이터분석가 과정 수료", "스파르타 내일배움캠프",
             "총 4개 프로젝트, Tableau·Python·SQL 실무 심화"),
            ("2024.05–2025.04", "팀장", "그리트라운지",
             "보조금 트래킹 시스템 설계 / GAS 자동화 스크립트 개발"),
            ("2024.02–05", "인턴", "테슬라",
             "전국 단위 보조금 서류 데이터 검증 · 정책 모니터링"),
            ("2023.08–10", "계약직", "위덕대학교 LINC3.0사업단",
             "KPI 데이터 관리 · 성과 뉴스레터 기획"),
            ("2015–2020", "심리학 학사", "단국대학교",
             "사회조사분석사 2급 · 직업상담사 2급 취득"),
        ]

        for period, role, org, desc in timeline:
            st.markdown(f"""
            <div class='timeline-item'>
                <div class='timeline-period'>{period}</div>
                <div class='timeline-role'>{role}</div>
                <div class='timeline-org'>{org}</div>
                <div class='timeline-body'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# PAGE: 다이소 뷰티 (메인)
# ══════════════════════════════════════════════════════════════
elif "다이소" in page:
    # 탭
    tab1, tab2, tab3 = st.tabs(["📌 문제 정의", "🔬 솔루션", "📈 결과 & 인사이트"])

    # ── 탭1: 문제 정의 ──
    with tab1:
        st.markdown("""
        <div style='padding: 1.5rem 0 1rem;'>
            <div class='hero-eyebrow'>MAIN PROJECT — PROBLEM DEFINITION</div>
            <div class='hero-title' style='font-size:2rem;'>
                144% 성장의 이면에 숨은<br>
                <span>'신뢰 위기'를 데이터로 포착했다</span>
            </div>
        </div>
        <hr>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns([3, 2])
        with c1:
            st.markdown("<div class='sec-label'>BACKGROUND</div>", unsafe_allow_html=True)
            st.markdown("""
            <div class='card' style='font-size:0.9rem; line-height:1.85; color:var(--text2);'>
                <b style='color:var(--text); font-size:1rem;'>거시적 위기 속의 역설</b><br><br>
                2026년 L자형 저성장 국면(<b style='color:var(--accent);'>GDP 성장률 1.9%</b>)에서
                소비자는 필수재 위주로 지갑을 닫았습니다.<br><br>
                그러나 다이소 뷰티는 <b style='color:var(--accent);'>144% 급성장</b>하며
                매출 <b style='color:var(--accent);'>4천억 원</b> 규모의 핵심 동력이 되었습니다.<br><br>
                MZ세대의 <b style='color:var(--text);'>'리트머스 소비'</b>와
                4050 액티브 시니어(<b style='color:var(--accent);'>+139%</b>)의 유입이
                만들어낸 결과입니다.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br><div class='sec-label'>THE PROBLEM</div>", unsafe_allow_html=True)
            st.markdown("""
            <div style='background:rgba(230,57,70,0.08); border:1px solid rgba(230,57,70,0.3);
                        border-radius:12px; padding:1.4rem 1.6rem; font-size:0.88rem;
                        line-height:1.85; color:var(--text2);'>
                <b style='color:var(--accent); font-size:0.95rem;'>⚠ 구조적 결함</b><br><br>
                성급한 외형 성장의 이면, 세 가지 위기가 동시에 작동하고 있었습니다:<br><br>
                <b style='color:var(--text);'>① 품질 신뢰 위기</b><br>
                납 검출 등 품질 이슈 + C-커머스 공세 →
                '저가 제품은 위험하다'는 브랜드 불신 확산<br><br>
                <b style='color:var(--text);'>② 성분 분석 소비자의 등장</b><br>
                다이소 뷰티 소비자의 <b style='color:var(--accent);'>23%</b>가 '성분 분석형'
                → 단 한 번의 품질 사고로 이 23%를 잃을 수 있음<br><br>
                <b style='color:var(--text);'>③ 100% 사입 구조의 취약성</b><br>
                직접 제조가 없는 다이소는 브랜드 품질 통제 수단이 없음
                → 입점 실패 = 브랜드 신뢰도 하락 + 재고 부담 직결
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br><div class='sec-label'>RESEARCH QUESTION</div>", unsafe_allow_html=True)
            st.markdown("""
            <div style='background:var(--bg3); border-radius:10px; padding:1.2rem 1.6rem;
                        border:1px solid var(--border); font-size:1rem;
                        font-style:italic; color:var(--text); line-height:1.6;'>
                "초저가 이미지를 유지하면서<br>
                <b style='color:var(--accent);'>'초신뢰(Hyper-Trust)' 브랜드</b>를 만들 수 있는가?<br>
                그리고 그것을 데이터로 어떻게 증명할 것인가?"
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown("<div class='sec-label'>KEY FIGURES</div>", unsafe_allow_html=True)
            figures = [
                ("144%", "다이소 뷰티 성장률", "accent"),
                ("4,000억", "뷰티 부문 매출 규모", "gold"),
                ("23%", "성분 분석형 소비자 비율", "accent"),
                ("1.9%", "동기간 GDP 성장률", "text2"),
                ("+139%", "4050 액티브 시니어 유입 증가", "accent"),
            ]
            for num, label, color in figures:
                color_var = {"accent": "var(--accent)", "gold": "var(--gold)", "text2": "var(--text2)"}[color]
                st.markdown(f"""
                <div style='background:var(--bg3); border:1px solid var(--border);
                            border-radius:8px; padding:0.9rem 1.1rem; margin-bottom:0.6rem;
                            display:flex; align-items:center; gap:0.8rem;'>
                    <div style='font-family:"Space Mono",monospace; font-size:1.3rem;
                                font-weight:700; color:{color_var};'>{num}</div>
                    <div style='font-size:0.78rem; color:var(--text2); line-height:1.4;'>{label}</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("<br><div class='sec-label'>MY ROLE (5인 팀)</div>", unsafe_allow_html=True)
            roles = ["데이터 정제 및 전처리", "인과추론 설계 및 실행", "런칭 시뮬레이션 개발", "Tableau 대시보드 제작"]
            for r in roles:
                st.markdown(f"""
                <div style='display:flex; align-items:center; gap:0.6rem;
                            margin-bottom:0.5rem; font-size:0.85rem;'>
                    <div style='width:6px; height:6px; border-radius:50%;
                                background:var(--accent); flex-shrink:0;'></div>
                    <span class='badge-mine' style='margin:0; font-size:0.75rem;'>내 기여</span>
                    <span style='color:var(--text);'>{r}</span>
                </div>
                """, unsafe_allow_html=True)

    # ── 탭2: 솔루션 ──
    with tab2:
        st.markdown("""
        <div style='padding: 1.5rem 0 1rem;'>
            <div class='hero-eyebrow'>MAIN PROJECT — SOLUTION</div>
            <div class='hero-title' style='font-size:2rem;'>
                OCR · 인과추론 · GIS<br>
                <span>3개의 무기로 데이터 무결성부터 전략까지</span>
            </div>
        </div>
        <hr>
        """, unsafe_allow_html=True)

        steps = [
            {
                "num": "STEP 01",
                "title": "데이터 무결성 확보",
                "mine": True,
                "items": [
                    ("3-Source OCR 파이프라인 구축",
                     "상세페이지가 이미지로만 제공 → Clova OCR + EasyOCR 교차 파이프라인 설계."
                     " 300개 이상의 패턴 교정 + INCI 표준 변환으로 전성분을 정형 텍스트로 추출"),
                    ("900여 제품 전수 매칭",
                     "다이소 내부 데이터 ↔ 식약처 DB 기능성 인증 제품 수기 검수."
                     " EU 기준 알레르기 유발 물질 정보와 결합하여 안전성 리스크 제품군 선별"),
                    ("3단 정규화 DB 설계",
                     "Wide Table → Core(기본) · Stats(판매통계) · Specs(성분·기능성) 3단 분리."
                     " 30만 건 이상 대용량 처리 효율 + 참조 무결성 극대화"),
                ]
            },
            {
                "num": "STEP 02",
                "title": "인과추론으로 '진짜 원인' 규명",
                "mine": True,
                "items": [
                    ("PSM · IPTW · OW 3종 교차 적용",
                     "브랜드 · 카테고리 · 기능성 — 공산성을 보이는 세 변수의 혼동을"
                     " 3가지 인과추론 기법으로 동시에 통제"),
                    ("핵심 발견: 기능성은 '조절 변수'",
                     "기능성 성분은 단독으로 매출을 일으키지 않음."
                     " 카테고리·브랜드와 결합할 때 효과가 폭발적으로 증폭되는 조절 변수(Moderator)임을 규명"),
                    ("생존 분석 기반 연착륙 제품 식별",
                     "DTW로 시계열 판매 패턴 군집화 → KaplanMeier + Cox PH 생존 분석으로"
                     " 핵심 매출 견인 제품(16.7%)을 통계적으로 도출"),
                ]
            },
            {
                "num": "STEP 03",
                "title": "GIS 기반 수요 밀도 알고리즘 설계",
                "mine": False,
                "items": [
                    ("자체 수요 밀도 점수 알고리즘",
                     "상권별 단기 체류 외국인 수 · 유동 인구 · 경쟁사 위치 지표를"
                     " z-score 표준화 합산하는 알고리즘 자체 설계"),
                    ("Hub & Spoke 물류 전략 도출",
                     "외국인 트래픽 상위 5% 매장을 Hub로 지정,"
                     " 연착륙 스킨케어 재고 심도를 일반 매장 대비 대폭 상향하는 전략 제안"),
                ]
            },
            {
                "num": "STEP 04",
                "title": "하이브리드 감성 라벨링 + ML 시뮬레이터",
                "mine": False,
                "items": [
                    ("GPT-4o-mini + Human-in-the-loop",
                     "30만 건 리뷰 1차 라벨링 → 수동 구축 골든셋으로 교차 검증 → 95%↑ 신뢰도 확보"),
                    ("RNN/LSTM 기반 시계열 감성 분석",
                     "유통 현장 빠른 의사결정 + 하드웨어 제약을 고려해 RNN/LSTM 채택."
                     " 입점 전 연착륙 확률 + 예상 매출 정량적 시뮬레이션 구현"),
                ]
            },
        ]

        for step in steps:
            badge = "<span class='badge-mine'>내 기여</span>" if step["mine"] else ""
            st.markdown(f"""
            <div class='step-box'>
                <div class='step-num'>{step['num']} {badge}</div>
                <div class='step-title'>{step['title']}</div>
            """, unsafe_allow_html=True)
            for item_title, item_body in step["items"]:
                st.markdown(f"""
                <div style='margin-bottom:0.6rem; padding-left:0.8rem;
                            border-left:2px solid rgba(230,57,70,0.3);'>
                    <div style='font-size:0.85rem; font-weight:600; color:var(--text);
                                margin-bottom:0.2rem;'>{item_title}</div>
                    <div style='font-size:0.82rem; color:var(--text2); line-height:1.65;'>{item_body}</div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

    # ── 탭3: 결과 ──
    with tab3:
        st.markdown("""
        <div style='padding: 1.5rem 0 1rem;'>
            <div class='hero-eyebrow'>MAIN PROJECT — RESULTS & INSIGHTS</div>
            <div class='hero-title' style='font-size:2rem;'>
                데이터가 전략이 됐다<br>
                <span>수치로 증명된 3가지 인사이트</span>
            </div>
            <div style='margin-top:0.8rem;'><span class='badge-award'>🏆 최우수상</span></div>
        </div>
        <hr>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns([3, 2])
        with c1:
            st.markdown("<div class='sec-label'>KEY INSIGHTS</div>", unsafe_allow_html=True)

            insights = [
                ("01", "16.7%의 연착륙 법칙과 기초 스킨케어의 저력",
                 "출시 6개월 후 살아남은 '연착륙 제품'은 전체의 <b style='color:var(--accent);'>16.7%</b>에 불과합니다."
                 " 그러나 이 소수 정예 제품이 뷰티 매출의 <b style='color:var(--accent);'>32.5%(약 1,300억 원)</b>를 견인합니다."
                 " 생존 제품의 83.3%가 스킨케어, 그 중 75%가 5,000원짜리 기초 제품이었습니다."),
                ("02", "기능성 성분은 '조절 변수' — 단독 효과 없음",
                 "인과추론(PSM/IPTW/OW) 3종 결과:"
                 " 기능성 성분 자체는 단독으로 매출을 만들지 않습니다."
                 " <b style='color:var(--accent);'>카테고리 + 브랜드와 결합될 때</b> 효과가 폭발적으로 증폭되는"
                 " 조절 변수(Moderator)로 작용함을 통계적으로 규명했습니다."),
                ("03", "관광 상권의 수요 이원화 — K-뷰티 스킨케어의 폭발성",
                 "한국 방문 외국인 1,100만 명 중 42%가 MZ세대, 중국인 관광객(578만 명)의"
                 " <b style='color:var(--accent);'>75.8%</b>가 화장품을 구매합니다."
                 " GIS 분석 결과 외국인 밀집 상위 5% 상권(Hub)에서 연착륙 스킨케어 수요가"
                 " 일반 상권 대비 압도적으로 높은 '하울(Haul)' 소비 패턴 확인"),
            ]

            for num, title, body in insights:
                st.markdown(f"""
                <div class='insight-box'>
                    <div class='insight-num'>{num}</div>
                    <div class='insight-title'>{title}</div>
                    <div class='insight-body'>{body}</div>
                </div>
                """, unsafe_allow_html=True)

        with c2:
            st.markdown("<div class='sec-label'>RESULT NUMBERS</div>", unsafe_allow_html=True)
            results = [
                ("16.7%", "연착륙 제품 비율", "매출의 32.5% 견인"),
                ("1,300억", "연착륙 제품 기여 매출", "전체 뷰티 매출 중"),
                ("75%", "연착륙 스킨케어 중 5천원대", "기초 제품이 핵심"),
                ("75.8%", "중국 관광객의 화장품 구매율", "GIS Hub 전략 근거"),
                ("95%+", "리뷰 라벨링 신뢰도", "Human-in-the-loop 검증"),
            ]
            for num, label, sub in results:
                st.markdown(f"""
                <div style='background:var(--bg3); border:1px solid var(--border);
                            border-radius:8px; padding:0.9rem 1.1rem; margin-bottom:0.6rem;'>
                    <div style='font-family:"Space Mono",monospace; font-size:1.4rem;
                                font-weight:700; color:var(--accent);'>{num}</div>
                    <div style='font-size:0.82rem; color:var(--text); margin-top:2px;'>{label}</div>
                    <div style='font-size:0.72rem; color:var(--text2); margin-top:2px;'>{sub}</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("<br><div class='sec-label'>VERIFICATION METHOD</div>", unsafe_allow_html=True)
            methods = ["인과추론 3종 교차 검증 (PSM/IPTW/OW)", "Kaplan-Meier + Cox PH 생존 분석", "통계적 유의성 전 항목 확보", "30만 건 GPT 라벨링 + 골든셋 검증"]
            for m in methods:
                st.markdown(f"""
                <div style='font-size:0.8rem; color:var(--text2); margin-bottom:0.4rem;
                            padding-left:0.6rem; border-left:2px solid var(--accent);'>
                    {m}
                </div>
                """, unsafe_allow_html=True)

            st.markdown("""
            <br>
            <div style='background:linear-gradient(135deg,rgba(244,162,97,0.12),rgba(244,162,97,0.04));
                        border:1px solid rgba(244,162,97,0.35); border-radius:10px;
                        padding:1rem 1.2rem; font-size:0.85rem; color:var(--text);
                        line-height:1.7;'>
                <span style='color:var(--gold); font-size:1.1rem;'>🏆</span><br>
                <b style='color:var(--gold);'>스파르타 최종 프로젝트 최우수상</b><br>
                <span style='color:var(--text2); font-size:0.78rem;'>2026.03 · 전체 수강생 대상</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<hr><div class='sec-label'>GROWTH INSIGHT</div>", unsafe_allow_html=True)
        st.markdown("""
        <div style='background:var(--bg3); border:1px solid var(--border); border-radius:10px;
                    padding:1.2rem 1.6rem; font-size:0.9rem; color:var(--text2); line-height:1.8;
                    font-style:italic;'>
            "분석은 현상을 설명하는 것이 아니라 <b style='color:var(--text);'>의사결정 도구</b>여야 한다.<br>
            900여 제품 수기 검수와 30만 건 데이터 정제를 거치며, 데이터 품질이 곧 전략의 신뢰도임을 체감했습니다.<br>
            인과추론으로 '왜'를 증명하고, 입점 시뮬레이터로 '그래서 어떻게'를 답했습니다."
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# PAGE: Starbucks 서브
# ══════════════════════════════════════════════════════════════
elif "Starbucks" in page:
    st.markdown("""
    <div style='padding: 2rem 0 1rem;'>
        <div class='hero-eyebrow'>SUB PROJECT · 2026.01.08 – 01.21 · 5인 팀</div>
        <div class='hero-title' style='font-size:2rem;'>
            Starbucks Next Level<br>
            <span style='color:#52b788;'>행동경제학 기반 마케팅 분석</span>
        </div>
        <div class='hero-sub' style='margin-top:0.6rem;'>
            "누가 구매했는가"가 아닌<br>
            <b style='color:var(--text);'>"어떤 트리거가 행동 전환을 유발했는가"</b>를 묻다
        </div>
    </div>
    <hr>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([3, 2])
    with c1:
        st.markdown("<div class='sec-label'>PROBLEM</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='card' style='font-size:0.88rem; line-height:1.85; color:var(--text2);'>
            단편적인 인구통계 정보만으로는 프로모션 효율의 변동 원인을
            객관적으로 설명하기 어렵습니다.<br><br>
            결과적 분석에서 <b style='color:var(--text);'>프로세스 중심의 행동 전환 분석</b>으로 전환이 필요했습니다.
            비효율적인 자원 배분과 무분별한 메시지 발송으로 인한 고객 피로도를 데이터로 해결했습니다.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br><div class='sec-label'>MY CONTRIBUTION</div>", unsafe_allow_html=True)
        contribs = [
            ("데이터 전처리", "딕셔너리 형태 결제/평점 데이터 → 관계형 구조 파싱, 분석 목적별 데이터셋 이원화"),
            ("채널별 효과크기 산출", "이메일 채널 제외 처리(변별력 낮음) → 카이제곱 검정으로 채널 선정 유의성 확보"),
            ("대시보드 제작", "Tableau 동적 필터링 대시보드 — 프로모션 · 고객 2종 구현"),
        ]
        for title, body in contribs:
            st.markdown(f"""
            <div class='card'>
                <div style='display:flex; align-items:center; gap:0.5rem; margin-bottom:0.4rem;'>
                    <span class='badge-mine' style='margin:0;'>내 기여</span>
                    <span style='font-weight:700; font-size:0.9rem; color:var(--text);'>{title}</span>
                </div>
                <div style='font-size:0.83rem; color:var(--text2); line-height:1.65;'>{body}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br><div class='sec-label'>BEHAVIORAL ECONOMICS INSIGHTS</div>", unsafe_allow_html=True)
        be_insights = [
            ("손실 회피 (Loss Aversion)",
             "실질 지불액 2,000원 오퍼 완료율 31.94% vs 7,000원 오퍼 11.23% — 약 3배 차이."
             " 할인 금액보다 초기 결제 부담을 낮추는 것이 전환에 효과적"),
            ("사회적 증거 (Social Proof)",
             "SNS는 타인의 긍정 반응이 실시간 노출 → 전환율 43.97%p (Web 대비)."
             " 메인 접점으로 SNS를 설정해야 하는 통계적 근거"),
            ("단순 노출 효과 (Mere-exposure Effect)",
             "3채널 중복 노출 시 완료율 50% — 단일 채널(20.44%) 대비 2.4배."
             " 반복 메시지가 심리적 장벽을 단계적으로 낮춤"),
        ]
        for title, body in be_insights:
            st.markdown(f"""
            <div class='insight-box' style='border-color:rgba(82,183,136,0.25);
                        background:linear-gradient(135deg,rgba(82,183,136,0.06),transparent);'>
                <div style='font-weight:700; font-size:0.9rem; color:#52b788;
                            margin-bottom:0.4rem;'>▸ {title}</div>
                <div style='font-size:0.83rem; color:var(--text2); line-height:1.65;'>{body}</div>
            </div>
            """, unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='sec-label'>KEY NUMBERS</div>", unsafe_allow_html=True)
        sb_stats = [
            ("43.97%p", "SNS vs Web 채널 효과 차이", "#52b788"),
            ("2.4×", "3채널 중복 시 전환율 상승", "#52b788"),
            ("31.94%", "2천원 오퍼 완료율", "#52b788"),
            ("3배", "2천원 vs 7천원 오퍼 완료율 차이", "var(--gold)"),
            ("4개", "K-means 고객 세그먼트", "#52b788"),
            ("95%+", "감성 라벨링 신뢰도", "var(--text2)"),
        ]
        for num, label, color in sb_stats:
            st.markdown(f"""
            <div style='background:var(--bg3); border:1px solid var(--border);
                        border-radius:8px; padding:0.8rem 1rem; margin-bottom:0.5rem;
                        display:flex; align-items:center; gap:0.8rem;'>
                <div style='font-family:"Space Mono",monospace; font-size:1.2rem;
                            font-weight:700; color:{color};'>{num}</div>
                <div style='font-size:0.78rem; color:var(--text2); line-height:1.4;'>{label}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br><div class='sec-label'>TECH STACK</div>", unsafe_allow_html=True)
        for tag in ["SQL", "Python", "Tableau", "K-means", "Kruskal-Wallis", "카이제곱 검정", "행동경제학"]:
            st.markdown(f"<span class='tag' style='border-color:rgba(82,183,136,0.4); color:#52b788; background:rgba(82,183,136,0.08);'>{tag}</span>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# PAGE: 스킬셋
# ══════════════════════════════════════════════════════════════
elif "스킬" in page:
    st.markdown("""
    <div style='padding: 2rem 0 1rem;'>
        <div class='hero-eyebrow'>SKILLS</div>
        <div class='hero-title' style='font-size:2rem;'>
            데이터 수집부터 의사결정 지원까지<br>
            <span>전 과정을 직접 돌릴 수 있습니다</span>
        </div>
    </div>
    <hr>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        categories = [
            ("LANGUAGES", [("Python", 90), ("SQL", 82)]),
            ("VISUALIZATION", [("Tableau", 85), ("Streamlit", 72), ("Matplotlib / Seaborn", 78)]),
            ("DATA ENGINEERING", [("OCR 파이프라인 (Clova/Easy)", 75), ("DB 정규화 설계", 78), ("GIS (QGIS / Folium)", 68)]),
        ]
        for cat, skills in categories:
            st.markdown(f"<div class='sec-label'>{cat}</div>", unsafe_allow_html=True)
            for name, level in skills:
                st.markdown(f"""
                <div class='skill-row'>
                    <div class='skill-name'>{name}</div>
                    <div class='skill-bar-bg'>
                        <div class='skill-bar-fill' style='width:{level}%;'></div>
                    </div>
                    <div style='font-family:"Space Mono",monospace; font-size:0.7rem;
                                color:var(--text2); min-width:30px; text-align:right;'>{level}</div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

    with c2:
        categories2 = [
            ("ANALYTICS / ML", [("인과추론 (PSM·IPTW·OW)", 88), ("생존 분석 (KM·Cox PH)", 80),
                                  ("Scikit-learn (ML 모델링)", 75), ("시계열 (RNN/LSTM)", 68),
                                  ("통계 검정 (Scipy)", 82)]),
            ("TOOLS", [("MySQL / DBeaver", 80), ("Jupyter Notebook", 85), ("VS Code", 80), ("Google Apps Script", 65)]),
        ]
        for cat, skills in categories2:
            st.markdown(f"<div class='sec-label'>{cat}</div>", unsafe_allow_html=True)
            for name, level in skills:
                st.markdown(f"""
                <div class='skill-row'>
                    <div class='skill-name'>{name}</div>
                    <div class='skill-bar-bg'>
                        <div class='skill-bar-fill' style='width:{level}%;'></div>
                    </div>
                    <div style='font-family:"Space Mono",monospace; font-size:0.7rem;
                                color:var(--text2); min-width:30px; text-align:right;'>{level}</div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<hr><div class='sec-label'>CERTIFICATIONS</div>", unsafe_allow_html=True)
    certs = [
        ("사회조사분석사 2급", "통계 분석 역량 공인", "직무 연관"),
        ("직업상담사 2급", "상담 및 커뮤니케이션", ""),
        ("청소년상담사 3급", "심리 기반 역량", ""),
    ]
    cols = st.columns(3)
    for i, (name, desc, badge) in enumerate(certs):
        with cols[i]:
            b = f"<span class='badge-mine' style='margin:0; margin-bottom:4px; display:inline-block;'>직무 연관</span><br>" if badge else ""
            st.markdown(f"""
            <div class='card'>
                {b}
                <div style='font-weight:700; font-size:0.9rem; margin-bottom:0.3rem;'>{name}</div>
                <div style='font-size:0.78rem; color:var(--text2);'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# PAGE: Contact
# ══════════════════════════════════════════════════════════════
elif "Contact" in page:
    st.markdown("""
    <div style='padding: 3rem 0 2rem; text-align:center;'>
        <div class='hero-eyebrow' style='text-align:center;'>CONTACT</div>
        <div class='hero-title' style='font-size:2.2rem; text-align:center;'>
            비즈니스 문제를<br>
            <span>함께 풀어나가고 싶습니다.</span>
        </div>
        <div class='hero-sub' style='text-align:center; margin: 0 auto; padding:1rem 0;'>
            숫자 뒤의 맥락을 읽는 분석가, 김재경입니다.<br>
            데이터로 전략을 만드는 팀에 합류하고 싶습니다.
        </div>
    </div>
    <hr>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    contacts = [
        (c1, "✉  EMAIL", "kyng0116@gmail.com", "kyng0116@gmail.com"),
        (c2, "📱  PHONE", "010-5021-9745", None),
        (c3, "🔗  GITHUB", "github.com/kyng0116-cell", "https://github.com/kyng0116-cell"),
    ]
    for col, label, value, link in contacts:
        with col:
            if link:
                st.markdown(f"""
                <div class='card' style='text-align:center;'>
                    <div class='sec-label' style='text-align:center;'>{label}</div>
                    <a href='{link}' target='_blank' style='color:var(--accent2);
                       text-decoration:none; font-family:"Space Mono",monospace;
                       font-size:0.8rem;'>{value}</a>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class='card' style='text-align:center;'>
                    <div class='sec-label' style='text-align:center;'>{label}</div>
                    <div style='font-family:"Space Mono",monospace; font-size:0.85rem;
                                color:var(--text);'>{value}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background:linear-gradient(135deg,rgba(230,57,70,0.1),rgba(230,57,70,0.03));
                border:1px solid rgba(230,57,70,0.25); border-radius:16px;
                padding:2rem; text-align:center; margin-top:1rem;'>
        <div style='font-size:0.72rem; font-family:"Space Mono",monospace;
                    letter-spacing:0.2em; color:var(--accent); margin-bottom:0.8rem;'>
            🏆 AWARD
        </div>
        <div style='font-size:1.05rem; font-weight:700; color:var(--text); margin-bottom:0.4rem;'>
            스파르타 최종 프로젝트 최우수상
        </div>
        <div style='font-size:0.8rem; color:var(--text2);'>
            2026.03 · 스파르타 내일배움캠프 데이터분석가 과정
        </div>
    </div>
    """, unsafe_allow_html=True)