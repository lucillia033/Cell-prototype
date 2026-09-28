import streamlit as st

st.set_page_config(page_title="골지체 탐구", page_icon="📮", layout="wide")

st.title("📮 골지체 (Golgi apparatus)")
st.caption("📍 위치: 소포체 근처 및 세포막 부근")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 주요 기능")
    st.info("소포체로부터 전달받은 단백질과 지질을 수정·가공·분류하여 세포 안팎으로 분비합니다.")
    
    st.subheader("🔗 연계 소기관")
    st.write("소포체의 수송 소포를 받아 물질을 최종 포장한 뒤 분비 소포에 담아 세포막으로 전달합니다.")

with col2:
    st.subheader("🧩 세부 구조 탐구")
    struct = st.radio("구조를 선택하세요", ["시스 면(Cis face)", "트랜스 면(Trans face)"])
    
    if struct == "시스 면(Cis face)":
        st.success("소포체에서 전달되어 오는 수송 소포를 받아들이는 입력 부위입니다.")
    elif struct == "트랜스 면(Trans face)":
        st.success("가공이 완료된 물질을 분비 소포에 담아 목적지로 내보내는 출력 부위입니다.")

st.markdown("---")
st.page_link("app.py", label="🏠 메인 화면으로 돌아가기", icon="🏠")
