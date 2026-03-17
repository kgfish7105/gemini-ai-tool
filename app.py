import streamlit as st
from google import genai

# 1. 網頁標題與風格
st.set_page_config(page_title="形象管理學院 AI 助理", page_icon="✨")
st.title("✨ 形象管理學院：自媒體開發工具")

# 2. 從後台秘密讀取 API Key (夥伴看不到)
try:
    # 這裡的名稱要跟你在 Streamlit 後台設定的一樣
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception:
    st.error("系統維護中，請聯絡創辦人。")
    st.stop()

# 3. 主介面
user_input = st.text_area("請輸入素材（白話文、客戶案例）：", height=200)

if st.button("🚀 生成開發文案"):
    if user_input:
        with st.spinner("AI 正在編寫中..."):
            try:
                prompt = f"任務：轉化為 Threads 開發文案。風格：務實、直接、條列式。內容：{user_input}"
                response = client.models.generate_content(
                    model="models/gemini-2.5-flash",
                    contents=prompt
                )
                st.markdown("---")
                st.write(response.text)
            except Exception as e:
                st.error("目前流量較大，請稍後再試。")
