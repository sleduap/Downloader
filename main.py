from urllib import request
from sys import stdout
import time


def file_to_download():
    print("Download Started Wait for it to complete")
    print("="*8)
    with request.urlopen("https://nl01.cutepup.club/735e03955b1d878a86b44/Imagine%20Dragons%20-%20Believer.mp3") as \
            handler:
        return handler.read()


def download_status(func):
    def inner_function(music, filename, extension):
        if music:
            return func(music, filename, extension)

        print("No files to download")

    return inner_function


@download_status
def save_to_local_disk(music, filename, extension):
    with open(filename + extension, "wb") as wri:
        stdout.flush()
        time.sleep(1)
        print(wri.write(music))
        print("Download Completed")


file_name = "Believer"
music_file = file_to_download()
save_to_local_disk(music_file, file_name, ".mp3")
