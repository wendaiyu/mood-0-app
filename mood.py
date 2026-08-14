import streamlit as st
from datetime import date
import random

st.title("🌤 小小的记录")

#记录今天
mood = st.selectbox("今天的情绪be like",["😊 开心", "😐 一般", "😢 难过"])
note = st.text_area("写点什么...")

if st.button("保存"):
    st.success("successfully spend a day!")

#明天建议
st.divider()
st.subheader("明天穿什么")

weather = (["晴 ☀️", "雨 🌧️", "阴 ☁️"])
st.write("明天天气be like：",weather)
if "雨" in weather:
    st.write("记得带好umbrella和coat哦！")
