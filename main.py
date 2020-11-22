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
        if SongSelected.endswith('.wav'):  
            song = AudioSegment.from_wav(SongSelected)
            play(song)
        if SongSelected.endswith('.ogg'):  
            song = AudioSegment.from_ogg(SongSelected)
            play(song)
        else:
            print("error audio file unsupported try mp3 wav ogg")
            

class PrinterTread(Thread):
    def run(self):
        while True:
            print("now playing", SongSelected)
            time.sleep(1)

t = PlayerThread(args=("SongSelected"))
t2 = PrinterTread(args=("SongSelected"))

while True:
    if t.is_alive() is False:
        t = PlayerThread(args=("SongSelected"))
        t.start()
        SongSelected = MusicFolder + "/" + random.choice(os.listdir(MusicFolder))
    if t2.is_alive() is False:
        t2 = PrinterTread(args=("SongSelected"))
        t2.start()
