import streamlit as st

st.set_page_config(page_title="리보솜 탐구", page_icon="⚙️", layout="wide")

st.title("⚙️ 리보솜 (Ribosome)")
st.caption("📍 위치: 세포질에 떠 있거나 거친면 소포체 표면에 부착됨")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 주요 기능")
    st.info("mRNA의 유전 정보를 바탕으로 아미노산을 연결하여 단백질을 합성하는 세포 내 공장입니다.")
    
    st.subheader("🔗 연계 소기관")
    st.write("핵에서 전달받은 mRNA를 번역하여 단백질을 만든 뒤 거친면 소포체로 보냅니다.")

with col2:
    st.subheader("🧩 세부 구조 탐구")
    struct = st.radio("구조를 선택하세요", ["대단위체", "소단위체"])
    
    if struct == "대단위체":
        st.success("아미노산 간의 결합(펩타이드 결합)을 촉진하는 활성 부위를 가집니다.")
    elif struct == "소단위체":
        st.success("mRNA와 결합하여 유전 정보를 읽어들이는 역할을 합니다.")

st.markdown("---")
st.page_link("app.py", label="🏠 메인 화면으로 돌아가기", icon="🏠")
