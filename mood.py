import streamlit as st
from datetime import date
import random

st.title("🌤 小小的记录")

#记录今天
mood = st.selectbox("今天的情绪be like",["😊 开心", "😐 一般", "😢 难过"])
note = st.text_area("写点什么...(今天做了什么，想了什么，想做什么，没做成什么）")

if st.button("保存"):
    st.success("successfully spend a day!")

#明天建议
st.divider()
st.subheader("明天")

weather = st.selectbox("看看明天老天爷给啥脸色：",
["大晴天 ☀️", "雷阵雨 ⛈️", "回南天 🥵", "局部多云 🌤️"])
st.write("明天天气be like：",weather)
if "雨" in weather:
    st.write("记得带好umbrella和coat哦！")

st.subheader("🌡️ tomorrow温度记录")

low = st.number_input("最低温（°C）", value=20, step=1)
high = st.number_input("最高温（°C）", value=28, step=1)

if high >= low:
    st.write(f"温差：{high - low}°C")
else:
    st.warning("最高温不能比最低温还低哦")

st.divider()
tdl_text = st.text_area("写一点明天要做的事情吧！一条也行！",height=160)
if st.button("save tomorrow to-do-list"):
    if tdl_text.strip():
        with open("tomorrow_tdl.tex","a",encoding="utf_8") as f:
            f.write(f"---{date.today()}----\n{tdl_text}\n\n")
        st.success("successfully saved TDL!")
    else:
        st.warning("记一点吧！")

#展示历史
st.divider()
st.subheader("📖 历史 TDL")
try:
    with open("tomorrow_tdl.txt","r",ing="utf-8") as f:
        st.text(f.read())
except FileNotFoundError:
    st.info("还没有记录")
