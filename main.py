from art import *
import colorama
import pytube as p
import pytube.exceptions
from pytube import YouTube

class ChoiceException(Exception):  # Custom Exception class
    def __init__(self, value):
        self.value = value


print(colorama.Fore.YELLOW)
tprint("YOUTUBE     VIDEO     CONVERTER")
print(colorama.Fore.RESET)
while True:
    try:
        input_link = input("⌨ Enter a valid YouTube Video Link: ")
        yt = p.YouTube(input_link)  # Create a YouTube object for the video with the given link
        print(colorama.Fore.GREEN + "-----------------------------------------------------------------------------------------------------" + colorama.Fore.RESET)
        print("👉 Video Title: " + yt.title + "\n\n👉 Video Creator: " + yt.author)  # Prints the title and author of the video
        print("\n👀 Total Views: " + str(yt.views) + "\n\n📅 Publish Date: " + str(yt.publish_date))  # Prints the title and author of the video
        print(colorama.Fore.GREEN + "-----------------------------------------------------------------------------------------------------" + colorama.Fore.RESET)
        while True:  # Inside this while loop is exception handling on whether or not user wants to see description or not
            try:
                description_choice = input("Do You want to Display video Description (Y/N): ")
                if description_choice != "Y" and description_choice != "N":
                    raise ChoiceException("🛑 Invalid Choice")
                elif description_choice == "Y":
                    print("👉 Video Description: \n" + yt.description)  # Prints the description of video
                    break
                elif description_choice == "N":
                    break
            except ChoiceException:
                print("🛑 Invalid Choice")
        print(colorama.Fore.GREEN + "-----------------------------------------------------------------------------------------------------" + colorama.Fore.RESET)
        print(colorama.Fore.GREEN + "-----------------------------------------------------------------------------------------------------" + colorama.Fore.RESET)
        while True:  # Inside this while loop is exception handling on whether or not user wants to download video or audio
            try:
                print("1. Video Download(🎥)")
                print("2. Audio Download(🔉)")
                download_choice = int(input("Enter your choice of download: "))
                if download_choice == 1:
                    while True:  # Inside this while loop is exception handling on whether or not user wants to download high res video or low res video
                        try:
                            print("🥇 Download High Quality Video File")
                            print("🥈 Download Low Quality Video File")
                            video_res_choice = int(input("➡️Enter Choice: "))
                            if video_res_choice == 1:
                                print("⌛Your Video File is Being Downloaded... Please Wait...")
                                yt.streams.get_highest_resolution().download()  # Downloads High res file
                                print("✅ DOWNLOAD SUCCESS!")
                                break
                            elif video_res_choice == 2:
                                print("⌛Your Video File is Being Downloaded... Please Wait...")
                                yt.streams.get_lowest_resolution().download()  # Downloads Low Res File
                                print("✅ DOWNLOAD SUCCESS!")
                                break
                            else:
                                raise ValueError
                        except ValueError:
                            print("🛑 Invalid Integer!")
                    break
                elif download_choice == 2:
                    print("⌛Your Audio File is Being Downloaded... Please Wait...")
                    yt.streams.get_audio_only().download()  # Downloads Audio File
                    print("✅ DOWNLOAD SUCCESS!")
                    break
                else:
                    raise ValueError
            except ValueError:
                print("🛑 Invalid Integer!")
        break
    except pytube.exceptions.RegexMatchError:  # Handles all the input exceptions
        print("🛑Invalid URL!🛑")

print(colorama.Fore.MAGENTA)
tprint("========================")
tprint("CREDS:        SAAD     ABDUR     RAZZAQ")
tprint("========================")
print(colorama.Fore.RESET)