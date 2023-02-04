import pafy

def download_video(url):
    video = pafy.new(url)
    best_audio = video.getbestaudio(preftype="mp3", ftypestrict=True)
    best_audio.bitrate = 320
    best_audio.download()

url = input("Enter the URL of the YouTube video: ")
download_video(url)
print("Download complete!")
