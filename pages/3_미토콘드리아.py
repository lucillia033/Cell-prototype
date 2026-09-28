import streamlit as st

st.set_page_config(page_title="미토콘드리아 탐구", page_icon="⚡", layout="wide")

st.title("⚡ 미토콘드리아 (Mitochondria)")
st.caption("📍 위치: 세포질 전체 (에너지 소비가 많은 곳에 집중)")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 주요 기능")
    st.info("세포 호흡을 통해 유기물을 분해하고, 세포의 주요 에너지원인 ATP를 대량 생성합니다.")
    
    st.subheader("🔗 연계 소기관")
    st.write("세포질에서 진행된 당분해 작용의 산물을 전달받아 산소를 이용한 세포 호흡을 완결합니다.")

with col2:
    st.subheader("🧩 세부 구조 탐구")
    struct = st.radio("구조를 선택하세요", ["외막", "내막", "크리스타", "기질"])
    
    if struct == "외막":
        st.success("미토콘드리아의 매끄러운 바깥쪽 막으로 형태를 유지합니다.")
    elif struct == "내막":
        st.success("안쪽으로 주름진 막으로 전자전달계 효소들이 배치되어 있습니다.")
    elif struct == "크리스타":
        st.success("내막이 안쪽으로 꺾여 들어간 주름 구조로, 표면적을 넓혀 ATP 합성 효율을 높입니다.")
    elif struct == "기질":
        st.success("내막 안쪽의 액체 공간으로, TCA 회로 효소와 독자적인 DNA, 리보솜이 존재합니다.")

st.markdown("---")
st.page_link("app.py", label="🏠 메인 화면으로 돌아가기", icon="🏠")
