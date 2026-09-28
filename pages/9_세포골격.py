import streamlit as st

st.set_page_config(page_title="세포골격 탐구", page_icon="🏗️", layout="wide")

st.title("🏗️ 세포골격 (Cytoskeleton)")
st.caption("📍 위치: 세포질 전반에 그물망처럼 분포")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 주요 기능")
    st.info("세포의 형태를 유지하고, 내부 물질 이동의 길 역할을 하며, 세포 분열을 돕습니다.")
    
    st.subheader("🔗 연계 소기관")
    st.write("모터 단백질과 결합하여 소포체/골지체에서 만들어진 수송 소포의 이동 통로가 됩니다.")

with col2:
    st.subheader("🧩 세부 구조 탐구")
    struct = st.radio("구조를 선택하세요", ["미세관", "중간섬유", "미세섬유"])
    
    if struct == "미세관":
        st.success("튜불린 단백질로 구성되며, 세포골격 중 가장 굵고 소기관 이동의 도로 역할을 합니다.")
    elif struct == "중간섬유":
        st.success("세포의 기계적 강도를 유지하고 핵 등의 소기관 위치를 고정합니다.")
    elif struct == "미세섬유":
        st.success("액틴 단백질로 구성되며, 세포 운동과 형태 변화, 세포질 분열에 관여합니다.")

st.markdown("---")
if st.button("🏠 메인 화면으로 돌아가기", type="primary"):
    st.switch_page("app.py")
