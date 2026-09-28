import streamlit as st

st.set_page_config(page_title="세포막 탐구", page_icon="🛡️", layout="wide")

st.title("🛡️ 세포막 (Cell Membrane)")
st.caption("📍 위치: 세포의 가장 바깥쪽 경계")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 주요 기능")
    st.info("세포 내부 환경을 외부와 격리하고, 물질 출입을 선택적으로 조절하여 항상성을 유지합니다.")
    
    st.subheader("🔗 연계 소기관")
    st.write("수송 단백질과 수용체를 통해 세포 외부 신호 전달 및 물질 교환의 최전선 역할을 합니다.")

with col2:
    st.subheader("🧩 세부 구조 탐구")
    struct = st.radio("구조를 선택하세요", ["인지질 이중층", "막단백질"])
    
    if struct == "인지질 이중층":
        st.success("친수성 머리와 소수성 꼬리를 가진 인지질이 2중으로 배열되어 유동성을 제공합니다.")
    elif struct == "막단백질":
        st.success("물질 수송, 세포 간 인식, 신호 전달 수용체 등 세포막의 실제 기능을 담당합니다.")

st.markdown("---")
st.page_link("app.py", label="🏠 메인 화면으로 돌아가기", icon="🏠")
