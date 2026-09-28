import streamlit as st

st.set_page_config(page_title="세포질 탐구", page_icon="🌊", layout="wide")

st.title("🌊 세포질 (Cytoplasm / Cytosol)")
st.caption("📍 위치: 핵을 제외한 세포막 내부 전반")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 주요 기능")
    st.info("세포 내부를 채우고 있는 액체 환경으로, 소기관들이 위치하며 다양한 대사 과정이 일어납니다.")
    
    st.subheader("🔗 연계 소기관")
    st.write("모든 세포소기관이 배치되는 물리적 공간이자, 소기관 간 물질 이동의 매개체 역할을 합니다.")

with col2:
    st.subheader("🧩 세부 구조 탐구")
    struct = st.radio("구조를 선택하세요", ["세포액(Cytosol)"])
    
    if struct == "세포액(Cytosol)":
        st.success("물, 이온, 가용성 단백질 및 효소 등이 용해되어 있는 세포질의 액체 성분입니다.")

st.markdown("---")
if st.button("🏠 메인 화면으로 돌아가기", type="primary"):
    st.switch_page("app.py")
