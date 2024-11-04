import google.generativeai as genai
import streamlit as st

st.title("Gemini AI Chat")
st.write("このアプリはGoogleの生成AI Geminiを使用しています。")
st.write("生成内容の正確性は保証されないため、重要な決定には専門家の助言を得てください。")
st.write("また、入力内容や生成物の利用はご自身の責任でお願いいたします。")
st.write("このアプリが使えない場合は[Google Gemini](https://gemini.google.com/)、[ChatGPT](https://openai.com/index/chatgpt/)、[Anthropic Claude](https://claude.ai/)などをご利用ください。")

# APIキーの設定
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# セッションに履歴がなければ初期化
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat" not in st.session_state:
    # チャットのインスタンスを最初に一度だけ生成
    st.session_state.chat = model.start_chat()

# 既存のメッセージ履歴を表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ユーザーの入力を取得
prompt = st.chat_input("こんにちは、Gemini!")

# 入力があれば処理を開始
if prompt:
    # ユーザーのメッセージを履歴に追加
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 履歴付きでAPIにリクエストを送信
    response = st.session_state.chat.send_message(prompt)
    
    # アシスタントのメッセージを履歴に追加
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    
    # アシスタントの応答を表示
    with st.chat_message("assistant"):
        st.markdown(response.text)
