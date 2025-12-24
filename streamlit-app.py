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

# --- 2. روابط الوسائط (استبدليها بروابطك المباشرة) ---
# إذا لم تنجح الصور المرفوعة، استخدمي روابط مباشرة من موقع (Postimages)
najd_static = "najd_static.png.JPG" 
saud_static = "saud_static.png.JPG"
najd_video = "najd_video.mp4.MP4"
saud_video = "saud_video.mp4.MP4"
# --- 3. عرض الشخصيات في البداية ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3 style='text-align: center;'>المفكرة نجد 👩‍💻</h3>", unsafe_allow_html=True)
    najd_frame = st.empty()
    try:
        najd_frame.image(najd_static, use_container_width=True)
    except:
        najd_frame.warning("بانتظار رفع صورة نجد...")

with col2:
    st.markdown("<h3 style='text-align: center;'>المغامر سعود 🧗‍♂️</h3>", unsafe_allow_html=True)
    saud_frame = st.empty()
    try:
        saud_frame.image(saud_static, use_container_width=True)
    except:
        saud_frame.warning("بانتظار رفع صورة سعود...")

st.divider()

# --- 4. المحرك الصوتي (Voca AI Style) ---
st.write("### 🎙️ اضغطي وتحدثي مع الأبطال:")
audio_input = mic_recorder(
    start_prompt="ابدئي الكلام الآن",
    stop_prompt="إنهاء التسجيل",
    key='recorder'
)

if audio_input:
    # معالجة الصوت وتحويله لنص
    r = sr.Recognizer()
    audio_data = sr.AudioData(audio_input['bytes'], 16000, 2)
    
    try:
        user_query = r.recognize_google(audio_data, language='ar-SA')
        st.info(f"💬 أنتِ: {user_query}")
        
        # منطق الاستجابة وتبديل الصورة بالفيديو
        if "نجد" in user_query:
            with col1:
                najd_frame.video(najd_video)
            st.success("نجد تشرح لكِ الآن!")
            
        elif "سعود" in user_query:
            with col2:
                saud_frame.video(saud_video)
            st.success("سعود يتحمس معكِ!")
            
        else:
            st.warning("نحن نسمعكِ.. هل تريدين سؤال نجد أم سعود؟")
            
    except sr.UnknownValueError:
        st.error("لم أستطع تمييز الكلمات، هل يمكنكِ المحاولة مرة أخرى؟")
    except Exception as e:
        st.error(f"حدث خطأ تقني: {e}")

# --- 5. ملف المتطلبات (Requirements) للمنصة ---
with st.expander("🛠️ إعدادات المنصة (Requirements)"):
    st.code("""
streamlit
streamlit-mic-recorder
SpeechRecognition
    """)
# استخدمي هذه الأسماء في الكود لضمان ظهور الملفات
najd_static = "najd_static.png.JPG" 
saud_static = "saud_static.png.JPG"
najd_video = "najd_video.mp4.MP4"
saud_video = "saud_video.mp4.MP4"
