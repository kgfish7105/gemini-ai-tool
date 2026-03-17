import streamlit as st
from google import genai

# 網頁標題與風格設定
st.set_page_config(page_title="形象管理學院 AI 助理", page_icon="✨")

st.title("✨ 形象管理學院：自媒體開發工具")
st.markdown("""
本工具由 **形象管理學院** 提供，旨在幫助夥伴快速將專業內容轉化為 **Threads/IG** 高質感文案。
- **務實、直接、開發新名單**
""")

# 側邊欄：API 設定
with st.sidebar:
    st.header("設定")
    api_key = st.text_input("請輸入您的 Gemini API Key", type="password")
    st.info("API Key 可至 Google AI Studio 免費申請。")

# 主介面
user_input = st.text_area(
    "請輸入您的素材（白話文、客戶案例、營養點子）：",
    placeholder="例如：今天幫一位 30 歲的工程師完成形象改造，他變得很帥很有自信...",
    height=200
)

if st.button("🚀 生成開發文案"):
    if not api_key:
        st.error("請先在左側輸入 API Key。")
    elif not user_input:
        st.warning("請輸入內容素材。")
    else:
        with st.spinner("AI 正在根據形象管理邏輯編寫中..."):
            try:
                client = genai.Client(api_key=api_key)
                
                # 結合您的專業背景與風格的 Prompt
                prompt = f"""
                任務：將以下內容轉化為符合『形象管理學院』調性的 Threads 開發文案。
                風格：務實、直接、條列式分析、少廢話。
                受眾：20-40 歲積極向上、想改變現狀的人。
                關鍵字：自媒體, Threads, AI, 形象管理, 營養學。
                
                內容素材：{user_input}
                
                輸出要求：
                1. 吸睛的開頭。
                2. 價值點分析。
                3. 明確的行動呼籲（Call to Action）。
                """
                
                response = client.models.generate_content(
                    model="models/gemini-2.5-flash",
                    contents=prompt
                )
                
                st.success("生成成功！")
                st.markdown("---")
                st.write(response.text)
                st.button("📋 複製文案 (請手動選取複製)")
                
            except Exception as e:
                st.error(f"連線失敗，請檢查 API Key 是否正確。錯誤訊息：{e}")

st.markdown("---")
st.caption("© 形象管理學院 - 科技賦能專業，讓複製變簡單。")
