# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st

st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요.")

if subject:
    st.write("시의 주제 : " + subject)

if st.button("시 작성"):
    if subject.strip():
        with st.spinner("시 작성중 ..."):
            try:
                # 필요할 때만 임포트하여 에러 회피
                from langchain_openai import ChatOpenAI
                chat_model = ChatOpenAI()
                
                result = chat_model.invoke(subject + "에 대한 시를 써줘")
                st.write(result.content)
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
    else:
        st.warning("시의 주제를 입력해주세요!")