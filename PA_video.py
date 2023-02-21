import streamlit as st

video_file = open('Public_Adjuster_ad_Digital.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes) 