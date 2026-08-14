import streamlit as st
from datetime import date
import random

st.title("🌤 小小的记录")

#记录今天
st.subheader("😊 今日心情")

    # 1. 定义心情选项
    mood_options = [
        "😊 开心",
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
        "🤔 好像都不是"
    ]

    # 2. 布局：把选择框和输入框放在同一行，节省空间
    col1, col2 = st.columns([1, 2]) 
    
    with col1:
        # 保留原来的选择功能
        mood = st.selectbox("此刻感觉", mood_options, key="mood_select")
        
    with col2:
        # 新增一个文本框，专门用来写原因
        # value="" 表示默认为空，用户可以删掉原来的字自己写
        mood_desc = st.text_input("💭 为什么会这样呢？（选填）", value="", placeholder="比如：因为下班早/因为吃到了好吃的...")
    
    # 3. 这一步很关键！把“选的标签”和“写的文字”拼在一起
    # 如果用户输入了描述，就拼上去；如果没输入，就只保留原来的标签
    # 加个空格隔开，看着舒服
    final_mood = f"{mood} {mood_desc}".strip()
note = st.text_area("写点什么...(今天做了什么，想了什么，想做什么，没做成什么）",height=100)

if st.button("保存"):
    st.success("successfully spend a day!")

st.divider()
st.subheader("明天")

st.subheader("☁️ 明天天气")
weather_options=[ "🌞 大晴天 / 阳光明媚",
        "⛅ 多云 / 局部多云", 
        "☁️ 阴天 / 灰蒙蒙",
        "🌦️ 阵雨 / 小雨绵绵",
        "🌧️ 大雨 / 暴雨",
        "⛈️ 雷阵雨 / 电闪雷鸣",
        "🌨️ 小雪 / 中雪 / 大雪",
        "❄️ 暴雪 / 冻雨",
        "🌫️ 雾霾 / 大雾弥漫",
        "💨 大风 / 妖风阵阵",
        "🌪️ 台风 / 强对流",
        "🌈 雨后彩虹 / 天气真好",
        "🔥 高温预警 / 热化了",
        "🥶 降温明显 / 冷飕飕",
        "🥵回南天 / 墙壁流泪"])
weather = st.multiselect(
        "看看明天老天爷给啥脸色：（可以多选哦宝宝）", 
        weather_options,
        default=["☁️ 阴天 / 灰蒙蒙"]  # 默认选一个，防止用户什么都不选
    )
st.write("明天天气be like：",weather)
combined_weather_str = "".join(weather)
if "雨" in combined_weather_str or "雪" in combined_weather_str or "台风" in combined_weather_str:
        tip = "☔️ 记得带伞和外套，路上小心"
    elif "晴" in combined_weather_str or "🌞" in combined_weather_str:
        tip = "☀️ 紫外线强，记得涂防晒，心情不错！"
    elif "雾" in combined_weather_str or "霾" in combined_weather_str:
        tip = "😷 空气质量一般，出门戴口罩"
    else:
        tip = "👌 天气正常，放心出门溜达"
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
