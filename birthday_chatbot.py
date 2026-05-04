import streamlit as st
import random

st.set_page_config(page_title="Birthday Wish 🎂", page_icon="🎈")

#  Custom CSS for animation (hearts floating)
st.markdown("""
    <style>
    body {
        background-color: #ffe6f0;
    }
    .heart {
        position: fixed;
        color: red;
        font-size: 20px;
        animation: float 5s infinite;
    }
    @keyframes float {
        0% { transform: translateY(100vh); opacity: 1; }
        100% { transform: translateY(-10vh); opacity: 0; }
    }
    </style>
""", unsafe_allow_html=True)

#  Background Music (auto play)
st.markdown("""
    <audio autoplay loop>
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
    </audio>
""", unsafe_allow_html=True)

st.title("🎂 Birthday Wish  💖")

name = "Shruti Bhute"

# 🎈 Balloons
st.balloons()

# 💞 Messages
messages = [
    f"🌸 Happy Birthday, {name}! 🌸\nMay your day be filled with love, laughter, and unforgettable moments. You truly deserve all the happiness in the world! 💖",

    f"❤️ Happy Birthday, {name}! ❤️\nYou are not just special… you are the only one my heart truly belongs to. Every moment with you feels magical. I’m so grateful you exist in my life. 💫",

    f"💞 Dear {name}, Happy Birthday 💞\nYou mean everything to me. My heart, my happiness, my peace — all are connected to you. I promise to always care for you and stand by you forever. 🌹"
]

# Button
if st.button(" Birthday Wish 🎁"):
    st.success(random.choice(messages))

# 💖 Floating hearts (simple effect)
for i in range(10):
    st.markdown(f'<div class="heart" style="left:{i*10}%;">❤️</div>', unsafe_allow_html=True)