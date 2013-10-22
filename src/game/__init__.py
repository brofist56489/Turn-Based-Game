import pygame
import pygame.gfxdraw
from pygame.locals import *

from src.net import GameNetwork
from src.level import Level

import threading, time

WIDTH = 640
HEIGHT = int(WIDTH * 3 / 4)
TITLE = "Turn Based"

class Game():
    def __init__(self):
        self.__init_video()
        GameNetwork.MakeServer().start()
        self.level = Level()
        return
    
    def __init_video(self):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT), HWSURFACE | DOUBLEBUF | RLEACCEL | FULLSCREEN)
        pygame.display.set_caption(TITLE)
        self.screen = Screen()
        return

    def tick(self):
        return
    
    def render(self):
        self.screen.clear((0, 0, 0))

        self.level.render(self.screen)

        self.display.blit(self.screen.canvas, [0, 0])
        pygame.display.flip()
        return
    
    def run(self):
        
        running = True
        lt = round(time.time() * 1000)
        ltr = lt
        delta = 0.0
        msPt = 1000.0/60.0
        ticks = frames = 0
        
        while(running):
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    running = False

            shouldRedraw = False

            now = round(time.time() * 1000)
            delta += (now - lt) / msPt
            lt = now
            
            while(delta >= 1):
                self.tick()
                ticks += 1
                delta -= 1
                shouldRedraw = True

            if shouldRedraw:
                self.render()
                frames += 1

            ct = round(time.time() * 1000)
            if(ct - ltr >= 1000):
                ltr += 1000
                pygame.display.set_caption(str(ticks) + " tps," + str(frames) + " fps")
                ticks = frames = 0

            if not running:
                pygame.quit()
        return


class Screen():
    def __init__(self):
        self.xo = 0
        self.yo = 0
        self.canvas = pygame.Surface((WIDTH, HEIGHT))

    def clear(self, color):
        self.canvas.fill(color)

    def render(self, surface, x, y, sr=None):
        x -= self.xo
        y -= self.yo
        self.canvas.blit(surface, [x, y], sr)

    def renderCirc(self, x, y, r, c=(255, 255, 255)):
        x -= self.xo
        y -= self.yo
        pygame.gfxdraw.filled_circle(self.canvas, x, y, r, c)

    def offset(self, x, y):
        self.xo = x - (WIDTH / 2)
        self.yo = y - (HEIGHT / 2)
