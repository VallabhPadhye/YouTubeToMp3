from pytube import YouTube
import streamlit as st

st.title("YouTube to MP3 Downloader")

url = st.text_input("Enter the URL of the YouTube video:")
if url:
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True, mime_type='audio/mp3', subtype='mp3').first()
        audio_stream.download()
        st.success("Download complete!")
    except:
        st.error("An error occurred during the download. Please try again.")
