import streamlit as st
from datetime import date
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

st.title("🌤 小小的记录")
nickname = st.text_input("✨ 今天想叫什么", placeholder="取个可爱的昵称吧")
where = st.text_input("📍 现在在哪儿", placeholder="上海的咖啡馆 / 无锡的火锅店 / 梦里 / 被窝里/......")

#记录今天
st.subheader("😊 今日心情")
col1, col2 = st.columns([1, 2]) 
with col1:
    mood = st.selectbox("此刻感觉", [
        "😊 开心","🥳 兴奋","🫥 平淡","😐 一般","🥱 累/倦怠",
        "😌 平静放松","🥺 想哭","😢 难过","😡 烦躁","😨 焦虑","🥰 被爱到了","🤔 好像都不是"
    ], key="mood_select")
with col2:
    mood_desc = st.text_input("💭 为什么会这样呢？（选填）", value="", placeholder="比如吃到了好吃的...")
final_mood = f"{mood} {mood_desc}".strip()
note = st.text_area("今天有什么想记录的吗",height=100)

st.divider()
st.subheader("明天")
st.subheader("☁️ 明天天气")
weather_options=[ "🌞 大晴天 / 阳光明媚","⛅ 多云 / 局部多云","☁️ 阴天 / 灰蒙蒙","🌦️ 阵雨 / 小雨绵绵","🌧️ 大雨 / 暴雨","⛈️ 雷阵雨 / 电闪雷鸣","🌨️ 小雪 / 中雪 / 大雪","❄️ 暴雪 / 冻雨","🌫️ 雾霾 / 大雾弥漫","💨 大风 / 妖风阵阵","🌪️ 台风 / 强对流","🌈 雨后彩虹 / 天气真好","🔥 高温预警 / 热化了","🥶 降温明显 / 冷飕飕","🥵回南天 / 墙壁流泪"]
weather = st.multiselect("看看明天老天爷给啥脸色：（可多选~）", weather_options, default=["☁️ 阴天 / 灰蒙蒙"])
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
# 这里把两个输入框分开命名，避免互相覆盖
now_do = st.text_area("现在最想做什么☺️",height=120)
st.divider()
tomorrow_plan = st.text_area("明天有任务吗bb🤗?对明天的自己有想说的嘛",height=120)

if st.button("📥 提交"):
    submit_time = datetime.now().strftime("%H:%M:%S")
    content = f"""
=== 新记录 ===
        ("🧸", "昵称", nickname or "匿名小朋友"),
        ("📍", "坐标", where or "未知"),
        ("🕒", "填表时间", f"{date.today()} {submit_time}"),
        ("😊", "心情", final_mood),
        ("📝", "碎碎念", note or "（无）"),
        ("☁️", "天气", weather_str),
        ("🌡️", "温度", f"{low}°C ~ {high}°C"),
        ("👉", "系统提醒", tip),
        ("🎯", "现在想做", now_do or "（无）"),
        ("📅", "明天计划", tomorrow_plan or "（无）"),
"""
    try:
        msg = MIMEText(content, "plain", "utf-8")
        msg["Subject"] = "📮 有人填了你的生活手账"
        msg["From"] = "3866015403@qq.com"
        password = "kgrkbzhrwgrscdej"
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login("3866015403@qq.com", password)
        server.sendmail("3866015403@qq.com", "3866015403@qq.com", msg.as_string())
        server.quit()
        st.success("✅ 提交成功！邮件已收到~")
        with st.expander("查看刚才写的内容"):
            st.text(content)
    except Exception as e:
        st.error(f"哎呀，出错了: {e}")
