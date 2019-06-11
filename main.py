#-*-coding:utf8;-*-
#qpy:pygame

import sys, os
import pygame
from pygame.locals import *
	
cwd = os.getcwd()
asset_root = os.path.join(cwd, "assets")

pygame.init()
surface = pygame.display.set_mode((640, 700))
clock = pygame.time.Clock()
info = pygame.display.Info()
w, h = info.current_w, info.current_h

if not w or not h:
    sys.exit()    

def get_x(per):
    info = pygame.display.Info()
    w = info.current_w
    w = float(w)
    x = float(per)
    return (x/100)*w
    
def get_y(per):
    info = pygame.display.Info()
    h = info.current_h
    h = float (h)
    y = float(per)
    return (y/100)*h

class Player(pygame.sprite.Sprite):
    def __init__(self, *arg, **kwargs):
        super(Player, self).__init__(*arg, **kwargs)
        self.x = get_x(50)
        self.y = get_y(5)
        self.width = 50
        self.height = 28
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x, self.y)
        self.parent = None
        self.score = 0
        self.alive = True
        
    def render(self):
        if self.parent is not None:
            # self.surf.fill((25, 25, 25))
            self.parent.blit(self.surf, self.rect)
            
    def set_parent(self, parent):
        self.parent = parent
        
    def set_position(self, x=0, y=0):
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x, self.y)
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.x = get_x(5)
        self.y = get_y(90)
        self.width = 20
        self.height = 20
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x, self.y)
        
    def render(self):
        if self.parent is not None:
            self.fire()
            # self.surf.fill(self.color)
            self.parent.blit(self.surf, self.rect)
            
    def set_parent(self, parent):
        self.parent = parent
        
    def set_position(self, x=0, y=0):
        self.x = x
        self.y = y
        self.surf = pygame.Surface((self.width, self.height))
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x, self.y)
        
    def fire(self):
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x, self.y)


p = Player ()
p.set_parent(surface)

e = Enemy ()
e.set_parent(surface)

        
def handle_event(event):
    globals()
    if event.type == MOUSEMOTION:
        if p.alive:
            p.set_position(event.pos[0], p.y)

def render():
    """render objects to screen"""
    globals()
    p.render()

def loop():
    globals()

while True:
    loop()
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
        handle_event(ev)
    # Framelimiter
    clock.tick(80)
    render()
    pygame.display.flip()
