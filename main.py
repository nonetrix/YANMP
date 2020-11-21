import random, time, os, threading
from tinytag import TinyTag
from pydub import AudioSegment
from pydub.playback import play
from threading import Thread

#MusicFolder = "./testfolder"
MusicFolder = "/home/nonetrix/games/music"

SongSelected = MusicFolder + "/" + random.choice(os.listdir(MusicFolder))

class PlayerThread(Thread):
    def run(self):
        if SongSelected.endswith('.mp3'):  
            song = AudioSegment.from_mp3(SongSelected)
            play(song)
            exit(0)
        if SongSelected.endswith('.wav'):  
            song = AudioSegment.from_wav(SongSelected)
            play(song)
            exit(0)
        if SongSelected.endswith('.ogg'):  
            song = AudioSegment.from_ogg(SongSelected)
            play(song)
            exit(0)
        else:
            print("error audio file unsupported try mp3 wav ogg")
            exit(0)

class PrinterTread(Thread):
    def run(self):
        while True:
            print("now playing", SongSelected)
            time.sleep(1)

t = PlayerThread(args=("SongSelected"))
t2 = PrinterTread(args=("SongSelected"))

while True:
    if t.is_alive() is False:
        print(SongSelected)
    while True:
        SongSelected = MusicFolder + "/" + random.choice(os.listdir(MusicFolder))
        t.start()
        if t2.is_alive() is False:
            t2.start()
        
        t.join()
        
        t = PlayerThread(args=("SongSelected"))
