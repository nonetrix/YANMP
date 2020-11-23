import pygame.mixer, os, time, threading, curses, random
from tinytag import TinyTag

#MusicFolder = "./testfolder"
MusicFolder = "/home/nonetrix/games/music"

stdscr = curses.initscr()
stdscr.clear()

while True:
        SongSelected = MusicFolder + "/" + random.choice(os.listdir(MusicFolder))
        tag = TinyTag.get(SongSelected)
        pygame.mixer.init(tag.samplerate)
        pygame.mixer.music.load(SongSelected)
        stdscr.addstr(SongSelected)
        stdscr.refresh()
        pygame.mixer.music.play()
        time.sleep(tag.duration)
        stdscr.clear()
