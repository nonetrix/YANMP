import random, time, os, threading, pygame
from tinytag import TinyTag
from threading import Thread

#MusicFolder = "./testfolder"
MusicFolder = "/home/nonetrix/games/music"

class PlayerThread(Thread):
    def run(self):
        tag = TinyTag.get(SongSelected)
        pygame.mixer.init(tag.samplerate)
        pygame.mixer.music.load(SongSelected)
        pygame.mixer.music.play()
        time.sleep(tag.duration)


class PrinterTread(Thread):
    def run(self):
        while True:
            print("now playing", SongSelected)
            time.sleep(1)

t = PlayerThread(args=("SongSelected"))
t2 = PrinterTread(args=("SongSelected"))

while True:
    if t.is_alive() is False:
        SongSelected = MusicFolder + "/" + random.choice(os.listdir(MusicFolder))
        t = PlayerThread(args=("SongSelected"))
        t.start()
    if t2.is_alive() is False:
        t2 = PrinterTread(args=("SongSelected"))
        t2.start()
