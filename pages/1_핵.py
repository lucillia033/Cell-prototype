import streamlit as st

st.set_page_config(page_title="핵 탐구", page_icon="🧠", layout="wide")

st.title("🧠 핵 (Nucleus)")
st.caption("📍 위치: 세포의 중앙 부근")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 주요 기능")
    st.info("세포의 생명 활동을 조절하는 중심 기관으로, 유전 정보(DNA)를 보관합니다.")
    
    st.subheader("🔗 연계 소기관")
    st.write("리보솜, 소포체, 골지체와 연계되어 단백질 합성의 시작점 역할을 합니다.")

with col2:
    st.subheader("🧩 세부 구조 탐구")
    struct = st.radio("구조를 선택하세요", ["핵막", "핵공", "염색질"])
    
    if struct == "핵막":
        st.success("2중막 구조로 내부의 DNA를 보호하고, 핵공을 통해 물질 이동을 조절합니다.")
    elif struct == "핵공":
        st.success("핵막에 존재하는 구멍으로, RNA나 단백질 등의 물질이 출입하는 통로입니다.")
    elif struct == "염색질":
        st.success("DNA와 히스톤 단백질이 결합된 형태이며, 세포 분열 시 염색체로 응축됩니다.")

st.markdown("---")
st.page_link("app.py", label="🏠 메인 화면으로 돌아가기", icon="🏠")
