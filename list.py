from yt_dlp import YoutubeDL

def download_playlist(playlist_url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path + '/%(title)s.%(ext)s',
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == '__main__':
    playlist_url = "https://www.youtube.com/playlist?list=PL7pkSK1xbGD7yqMMnmNct0Rfl5wWsN2DV"
    output_path = "C:/Users/the_suryanshupadhyay/Downloads/No"
    download_playlist(playlist_url, output_path)
