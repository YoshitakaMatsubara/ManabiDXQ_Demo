import google.generativeai as genai
import streamlit as st

st.title("Gemini AI Chat")
st.write("このアプリはGoogleの生成AI Geminiを使用しています。")
st.write("生成内容の正確性は保証されないため、重要な決定には専門家の助言を得てください。")
st.write("また、入力内容や生成物の利用はご自身の責任でお願いいたします。")
st.write("このアプリが使えない場合は[Google Gemini](https://gemini.google.com/)、[ChatGPT](https://openai.com/index/chatgpt/)、[Anthropic Claude](https://claude.ai/)などをご利用ください。")

GOOGLE_API_KEY=st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

prompt = st.chat_input("こんにちは、Gemini!")

if prompt:

#    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
    
    #st.session_state.messages.append({"role": "assistant", "content": response.text})

