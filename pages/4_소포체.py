import streamlit as st

st.set_page_config(page_title="소포체 탐구", page_icon="📦", layout="wide")

st.title("📦 소포체 (Endoplasmic Reticulum)")
st.caption("📍 위치: 핵막과 연결되어 세포질 넓은 범위에 분포")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 주요 기능")
    st.info("단백질과 지질을 합성하고, 세포 내 물질 운반 통로 역할을 수행하는 막상 구조입니다.")
    
    st.subheader("🔗 연계 소기관")
    st.write("리보솜에서 합성된 단백질을 가공한 후, 수송 소포에 담아 골지체로 전달합니다.")

with col2:
    st.subheader("🧩 세부 구조 탐구")
    struct = st.radio("구조를 선택하세요", ["거친면 소포체", "매끈면 소포체"])
    
    if struct == "거친면 소포체":
        st.success("표면에 리보솜이 부착되어 있으며, 합성된 단백질의 가공 및 수송을 담당합니다.")
    elif struct == "매끈면 소포체":
        st.success("리보솜이 없으며, 지질 합성, 독성 물질 해독, 칼슘 이온 저장 등의 역할을 합니다.")

st.markdown("---")
st.page_link("app.py", label="🏠 메인 화면으로 돌아가기", icon="🏠")
