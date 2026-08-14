import streamlit as st
from datetime import date
import random

st.title("🌤 小小的记录")

#记录今天
mood = st.selectbox("今天的情绪be like",[ "😊 开心",
        "🥳 兴奋",
        "🫥 平淡",
        "😐 一般",
        "🥱 累/倦怠",
        "😌 平静放松",
        "🥺 想哭",
        "😢 难过",
        "😡 烦躁",
        "😨 焦虑",
        "🥰 被爱到了",
        "🤔 好像都不是"])
if mood=="🤔 好像都不是":
        mood=st.text_input("那用一句话描述吧，你的感受！")
note = st.text_area("写点什么...(今天做了什么，想了什么，想做什么，没做成什么）",height=100)

if st.button("保存"):
    st.success("successfully spend a day!")

st.divider()
st.subheader("明天")

weather = st.selectbox("看看明天老天爷给啥脸色：",
["大晴天 ☀️", "雷阵雨 ⛈️", "回南天 🥵", "局部多云 🌤️"])
st.write("明天天气be like：",weather)
if "雨" in weather:
    st.write("记得带好umbrella哦！")

st.subheader("🌡️ tomorrow温度记录")

low = st.number_input("最低温（°C）", value=20, step=1)
high = st.number_input("最高温（°C）", value=28, step=1)

st.divider()
tdl_text = st.text_area("写一点明天要做的事情吧！一条也行！",height=120)

if st.button("📥 保存到 D 盘"):
    # 1. D盘路径（绝对路径）
    save_dir = r"D:\我\daily record"
    os.makedirs(save_dir, exist_ok=True)   # 没有文件夹就自动创建
    file_path = os.path.join(save_dir, "生活手账.txt")
    if "雨" in weather:
        tip = "记得带 umbrella 和 coat 🌂"
    else:
        tip = "不用带伞，放心出门"
    with open(file_path, "a", encoding="utf-8") as f:
        f.write("="*30 + "\n")
        f.write(f"记录时间：{date.today()}\n")
        f.write(f"心情：{mood}\n")
        f.write(f"今日碎碎念：{note}\n")
        f.write("-"*30 + "\n")
        f.write(f"明日天气：{weather}\n")
        f.write(f"温度：{low}°C ~ {high}°C\n")
        f.write(f"提醒：{tip}\n")
        f.write(f"明日计划：\n{tdl}\n")
        f.write("="*30 + "\n\n")
    st.success("✅ 已写入 D:\\daily record\\生活手账.txt")

#展示历史
st.divider()
st.subheader("📖 历史 TDL")
try:
    with open("D:\daily record\生活手账.txt","r",encoding="utf-8") as f:
        st.text(f.read())
except FileNotFoundError:
    st.info("还没有记录")
