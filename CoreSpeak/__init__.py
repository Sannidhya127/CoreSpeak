from gtts import gTTS
import time


def speakOut(file):
    import os

    # def from_slash(string):
    #     # param = string.split("-")
    #     # print(param)
    #     # return cls(param[0], param[1], param[2])
    #     return (string.split("."))

    # WavFile = from_slash(file)
    # string.split(".")
    temp = open("temp.txt", "a")
    temp.write(
        "Welcome to Coretouch Speech To Text Library Version 1.1.2 ©2020Coretts All Rights Reserved")
    # print("Welcome to Coretouch Speech To text Library Version 1..1.0 ©2020. All rights reserved")
    time.sleep(1)
    print(
        f"Please give us a moment while the system automatically creates a {file}.wav\naudio file containing the audio of your file {file}. This may take some time depending on the file size and your system specifications........................")
# If you don't have gtts go to the terminal and write pip install gtts
    time.sleep(1)
    print(f"Processing the files...........................................................\ncreating audio............")
# Reading the files
    f = open(file, "r")
    x = f.read()

    # Specifying language:
    language = 'en'  # You can specify any language. Reffer to the gtts documentation
    audio = gTTS(text=x, lang=language, slow=False)
    audio.save(file + ".wav")
    os.system(file+".wav")
