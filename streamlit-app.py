import streamlit as st
from streamlit_mic_recorder import mic_recorder
import speech_recognition as sr

# --- 1. إعدادات الصفحة والهوية البصرية ---
st.set_page_config(page_title="طويق شات AI", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #f9f9fb; }
    .main-title { text-align: center; color: #4B2E83; font-family: 'Arial'; }
    .stButton>button { width: 100%; border-radius: 25px; background-color: #2ecc71; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🇸🇦 طويق شات: أبطال البرمجة</h1>", unsafe_allow_html=True)

# --- 2. روابط الوسائط (محدثة حسب ملفاتك في GitHub) ---
# تأكدي أن هذه الأسماء تطابق تماماً ما يظهر في مستودعك
najd_static = "najd_static.png.JPG" 
saud_static = "saud_static.png.JPG"
najd_video = "najd_video.mp4.MP4"
saud_video = "saud_video.mp4.MP4"

# --- 3. عرض الشخصيات في البداية ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3 style='text-align: center;'>نجد</h3>", unsafe_allow_html=True)
    najd_frame = st.empty()
    try:
        najd_frame.image(najd_static, use_container_width=True)
    except:
        st.warning("صورة نجد غير موجودة")

with col2:
    st.markdown("<h3 style='text-align: center;'>سعود</h3>", unsafe_allow_html=True)
    saud_frame = st.empty()
    try:
        saud_frame.image(saud_static, use_container_width=True)
    except:
        st.warning("صورة سعود غير موجودة")

# --- 4. تسجيل الصوت ومعالجته ---
st.write("---")
st.subheader("تحدث مع أبطال طويق! 🎤")

audio = mic_recorder(start_prompt="إضغط للتحدث", stop_prompt="إيقاف التسجيل", key='recorder')

if audio:
    # عرض الفيديوهات عند التحدث
    najd_frame.video(najd_video, autoplay=True)
    saud_frame.video(saud_video, autoplay=True)
    
    # تحويل الصوت إلى نص
    recognizer = sr.Recognizer()
    try:
        # تحويل ملف الصوت المسجل إلى صيغة يفهمها Recognizer
        import io
        audio_data = sr.AudioFile(io.BytesIO(audio['bytes']))
        with audio_data as source:
            recorded_audio = recognizer.record(source)
        
        text = recognizer.recognize_google(recorded_audio, language='ar-SA')
        st.success(f"أنت قلت: {text}")
        
        # رد ذكي بسيط من الأبطال
        if "مرحبا" in text or "سلام" in text:
            st.info("نجد وسعود: أهلاً بك يا بطل! نحن مستعدون لرحلة البرمجة معك.")
        else:
            st.info("نجد وسعود: واصل يا مبدع! نحن نسمعك بوضوح.")
            
    except Exception as e:
        st.error("عذراً، لم أستطع فهم الصوت بوضوح. حاول مرة أخرى!")
