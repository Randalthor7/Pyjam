import pygame , sys
from pygame.locals import *
clock = pygame.time.Clock()

class Radio_man(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y ):
        super().__init__()
        self.attack_animation = False
        self.sprites = []
        self.sprites.append(pygame.image.load('rm1.png'))
        self.sprites.append(pygame.image.load('rm2.png'))
        self.sprites.append(pygame.image.load('rm3.png'))
        self.sprites.append(pygame.image.load('rm4.png'))
        self.sprites.append(pygame.image.load('rm5.png'))
        self.sprites.append(pygame.image.load('rm6.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def attack(self):
        self.attack_animation = True
    
    def update(self,speed):
        if self.attack_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len (self.sprites):
                self.current_sprite = 0
                self.attack_animation = False
                
        self.image = self.sprites[int(self.current_sprite)]





radio_man_group = pygame.sprite.Group()
radio_man = Radio_man(100,100)
radio_man_group.add(radio_man)

W_HEIGHT = 600
W_WIDTH = 900
BG_COLOR = (255,255,255)

pygame.init() # initialize pygame
w_surf = pygame.display.set_mode((W_WIDTH, W_HEIGHT))


while True:

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            radio_man.attack()


    #Drawing
    w_surf.fill((255,255,255))
    radio_man_group.draw(w_surf)
    radio_man_group.update(1)
    pygame.display.flip()
    clock.tick(60)