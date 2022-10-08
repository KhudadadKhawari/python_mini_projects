import pytube



def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    totalsz = (total_size/1024)/1024
    totalsz = round(totalsz,1)
    remain = (bytes_remaining / 1024) / 1024
    remain = round(remain, 1)
    dwnd = (bytes_downloaded / 1024) / 1024
    dwnd = round(dwnd, 1)
    percentage_of_completion = round(percentage_of_completion,2)
    print(f'Download Progress: {percentage_of_completion}%, Total Size:{totalsz} MB, Downloaded: {dwnd} MB, Remaining:{remain} MB')

def single_video_download():
    url = input("Enter the URL of the video you want to download: ")
    video = pytube.YouTube(url, on_progress_callback=progress_function)
    streams = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    
    available_resolutions = []
    for stream in streams:
        available_resolutions.append(stream.resolution)
    print("Available Resolutions: ", available_resolutions)
    resolution = input("Enter the resolution you want to download: ")
    stream = streams.get_by_resolution(resolution)
    stream.download()
    print(f"Video downloaded successfully to {stream.default_filename}")


def playlist_download():
    try:
        url = input("Enter the URL of the playlist you want to download: ")
        playlist = pytube.Playlist(url)
        available_resolutions = ['720p', '480p', '360p', '240p', '144p']
        print("Available Resolutions: ", available_resolutions)
        resolution = input("Enter the resolution you want to download including the letter p: ")
        for video in playlist.videos:
            video.register_on_progress_callback(progress_function)
            try:
                stream = video.streams.get_by_resolution(resolution)
                stream.download()
            except:
                print("Your Choice of resolution not available, Downloading in the highest available resolution")
                stream = video.streams.get_highest_resolution()
                stream.download()
            print(f"Video downloaded successfully to {stream.default_filename}\n\n")
        print("Playlist downloaded successfully")
    except Exception as e:
        print(e)


def multiple_videos_download():
    file = input("Enter the location/name.txt of the file containing the URLs of the videos you want to download: ")
    try:
        urls = []
        with open(file, 'r') as f:
            raw_urls = f.readlines()
            for url in raw_urls:
                if url == "" or url == "\n":
                    continue
                urls.append(url)

            available_resolutions = ['720p', '480p', '360p', '240p', '144p']
            print("Available Resolutions: ", available_resolutions)
            resolution = input("Enter the resolution you want to download including the letter p: ")
            for url in urls:
                video = pytube.YouTube(url, on_progress_callback=progress_function)
                try:
                    stream = video.streams.get_by_resolution(resolution)
                    stream.download()
                except pytube.exceptions.RegexMatchError:
                    print("Invalid URL, make sure you have entered the correct URL")
                    continue
                except pytube.exceptions.VideoUnavailable:
                    print("Video Unavailable, make sure you have entered the correct URL")
                    continue
                except Exception as e:
                    print("Your Choice of resolution not available, Downloading in the highest available resolution")
                    stream = video.streams.get_highest_resolution()
                    stream.download()
                
                print(f"Video downloaded successfully to {stream.default_filename}\n\n")
            print("All Videos downloaded successfully")
    except FileNotFoundError:
        print("File not found, make sure you have entered the correct location/name.txt")
        return
    except pytube.exceptions.RegexMatchError:
        print("Invalid URL, make sure you have entered the correct URL")
        return



def main():
    print("Welcome to the YouTube Downloader")
    print("Please Choose an Option")
    print(""" 
    1. Download a Single Video
    2. Download a Playlist
    3. Download Multiple Videos using a text file
    4. Exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        single_video_download()
    elif choice == "2":
        playlist_download()
    elif choice == "3":
        multiple_videos_download()
    elif choice == "4":
        exit()

if __name__ == '__main__':
    main()