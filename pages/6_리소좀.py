import streamlit as st

st.set_page_config(page_title="리소좀 탐구", page_icon="♻️", layout="wide")

st.title("♻️ 리소좀 (Lysosome)")
st.caption("📍 위치: 세포질 내부 전반")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 주요 기능")
    st.info("다양한 가수분해 효소를 포함하여 세포 내 물질, 손상된 소기관, 외부 이물질을 분해합니다.")
    
    st.subheader("🔗 연계 소기관")
    st.write("골지체에서 형성되며, 외부에서 들어온 식포나 손상된 소기관과 융합하여 소화를 진행합니다.")

with col2:
    st.subheader("🧩 세부 구조 탐구")
    struct = st.radio("구조를 선택하세요", ["단일막", "가수분해 효소"])
    
    if struct == "단일막":
        st.success("강한 산성 효소가 세포질 전체로 새어나가지 않도록 분리·보호하는 단일 막입니다.")
    elif struct == "가수분해 효소":
        st.success("산성 환경(pH 4.5~5.0)에서 단백질, 지질, 핵산 등을 효과적으로 분해하는 효소입니다.")

st.markdown("---")
st.page_link("app.py", label="🏠 메인 화면으로 돌아가기", icon="🏠")
