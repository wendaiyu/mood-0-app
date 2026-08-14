import streamlit as st
from datetime import date
import random
import os
import smtplib
from email.mime.text import MIMEText

st.title("🌤 小小的记录")
nickname = st.text_input("✨ 今天想叫什么", placeholder="取个可爱的昵称吧")
where = st.text_input("📍 现在在哪儿", placeholder="上海 / 无锡 / 梦里 / 被窝里/......")

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
note = st.text_area("写点什么吧！对今天的你",height=100)


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
        "🥵回南天 / 墙壁流泪"]
weather = st.multiselect(
        "看看明天老天爷给啥脸色：（可以多选哦宝宝）", 
        weather_options,
        default=["☁️ 阴天 / 灰蒙蒙"]  # 默认选一个，防止用户什么都不选
    )

combined_weather_str = "".join(weather)
if "雨" in combined_weather_str or "雪" in combined_weather_str or "台风" in combined_weather_str:
    tip = "☔️ 记得带伞和外套，路上小心"
elif "晴" in combined_weather_str or "🌞" in combined_weather_str:
    tip = "☀️ 紫外线强，记得涂防晒，心情不错！"
elif "雾" in combined_weather_str or "霾" in combined_weather_str:
    tip = "😷 空气质量一般，出门戴口罩"
else:
    tip = "👌 天气正常，放心出门溜达"


st.subheader("🌡️ tomorrow温度记录")

low = st.number_input("最低温（°C）", value=20, step=1)
high = st.number_input("最高温（°C）", value=28, step=1)

st.divider()
tdl_text = st.text_area("现在想做什么！",height=120)

st.divider()
tdl_text = st.text_area("明天有任务吗！",height=120)

if st.button("📥 提交"):
    # --- 必须在 if 里面定义 content ---
    content = f"""
=== 新记录 ===
🧸 昵称：{nickname or '匿名小朋友'}
📍 坐标：{where or '未知'}
日期：{date.today()}
心情：{final_mood}
碎碎念：{note}
天气：{"、".join(weather)}
温度：{low}°C ~ {high}°C
明日计划：{tdl}
    """
    
    # --- 发邮件逻辑 ---
    try:
        msg = MIMEText(content, "plain", "utf-8")
        msg["Subject"] = "📮 有人填了你的生活手账"
        msg["From"] = "3866015403@qq.com"

        # 这里从 secrets 读取密码
        password = st.secrets["email_pwd"]

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login("3866015403@qq.com", password)
        server.sendmail("3866015403@qq.com", "3866015403@qq.com", msg.as_string())
        server.quit()

        st.success("✅ 提交成功！邮件已收到~")
        
        # 提交后在页面上展示一遍内容
        with st.expander("查看刚才写的内容"):
            st.text(content)
            
    except Exception as e:
        st.error(f"哎呀，出错了: {e}")
