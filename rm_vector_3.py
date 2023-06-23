import pygame, sys, random
from pygame.locals import *
from pygame.math import Vector2
import math
pygame.init()

GRAY     = "gray"
NAVYBLUE = "navyblue"
WHITE    = "blue"
RED      = "red"
GREEN    = "green"
BLUE     = "blue"
YELLOW   = "yellow"
ORANGE   = "orange"
PURPLE   = "purple"
CYAN     = "cyan"

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
particle_list = []
no_of_particles = 20
num_of_colors = len(ALLCOLORS)
cell_size = 40
cell_number = 20
screen_width = cell_size * cell_number
screen_height = cell_size * cell_number
particle_size = 32
player_move = False
particle_no_list = []
particle_group = pygame.sprite.Group()
player_rect = 32
direction = Vector2(1,0)

class PLAYER(pygame.sprite.Sprite):
        def __init__(self ):
            super().__init__()
            self.body =[Vector2(400,10), Vector2(400,10), Vector2(400,10)]
            self.body_measured = []
            
        
        def mantain_distance_x(self):
            for i in range(1, len(self.body)):
                prev_block = self.body[i - 1]
                curr_block = self.body[i]
                dist = curr_block.x - prev_block.x
                if abs(dist) < particle_size:
                    move_dist = particle_size - abs(dist)
                    move_dir = 1 if dist > 0 else -1
                    curr_block.x += move_dist * move_dir
            self.body_measured = [block.x for block in self.body]
            print(self.body_measured)
            

        def draw_player(self):
            for block in self.body:
                x_pos = int(block.x )
                y_pos = int(block.y)
                block_rect = pygame.Rect(x_pos , y_pos , player_rect, player_rect)
                pygame.draw.rect(screen,(183,111,122),block_rect)
                # draw a rect

                

        def move_player(self):
                if player_move:
                        body_copy = self.body[:-1]
                        body_copy.insert(0,body_copy[0] + (direction))
                        self.body = body_copy[:]
                        self.mantain_distance_x()
                        



class PARTICLE_CREATOR:
    def __init__(self):
        self.particleno = 0
        self.particle_counter = 0
        


    def create_particle_list(self):

        self.random_pick_list_colors = ALLCOLORS[:]
   
        for i in range(no_of_particles):
            if len(particle_list) < no_of_particles:
                self.random_no_pick = random.randint(0,(num_of_colors-1))
                particle_list.append(self.random_pick_list_colors[self.random_no_pick])
            else:
                pass
        return particle_list

    def particle_constructor(self):
        for color in particle_list:
            particle_no_list.append(self.particleno)
            self.particleno += 1
            particle_no_list[self.particle_counter] = PARTICLE(color)
            particle_group.add(particle_no_list[self.particle_counter])
            self.particle_counter += 1



class PARTICLE(pygame.sprite.Sprite):
    def __init__(self, particle_type ):
        super().__init__()
        self.x = random.randint ( 0, screen_width - particle_size)
        self.y = random.randint ( 0, screen_height - particle_size)
        self.pos = Vector2(self.x, self.y)
        self.identity = particle_type
        if self.identity == RED:
            self.image = pygame.image.load("red_particle.png")
        if self.identity == GREEN:
            self.image = pygame.image.load("green_particle.png")
        if self.identity == BLUE:
            self.image = pygame.image.load("blue_particle.png")
        if self.identity == YELLOW:
            self.image = pygame.image.load("yellow_particle.png")
        if self.identity == ORANGE:
            self.image = pygame.image.load("orange_particle.png")
        if self.identity == PURPLE:
            self.image = pygame.image.load("purple_particle.png")
        if self.identity == CYAN:
            self.image = pygame.image.load("cyan_particle.png")
          
        


        
        self.rect = self.image.get_rect()
        self.rect.topleft = [(self.pos.x), (self.pos.y)]








screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()


class MAIN:
    def __init__(self):
        self.particle_creator = PARTICLE_CREATOR()
        self.player = PLAYER()

    def particle_creation(self):
            if len(particle_group) == 0:
                self.particle_creator.create_particle_list()
                self.particle_creator.particle_constructor()

    def draw_player(self):  
        self.player.move_player()
        self.player.draw_player()
        
        



main_game = MAIN()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
             if event.key == K_RIGHT:
                  direction = Vector2(1,0)
                  player_move = True
             if event.key == K_LEFT:
                  direction = Vector2(-1,0)
                  player_move = True
             if event.key == K_UP:
                  direction = Vector2(-1,0)
                  player_move = True
             if event.key == K_DOWN:
                  direction = Vector2(1,0)
                  player_move = True
        if event.type == KEYUP:
             if event.key == K_RIGHT:
                  player_move = False
             if event.key == K_LEFT:
                  player_move = False
             if event.key == K_DOWN:
                  player_move = False
             if event.key == K_UP:
                  player_move = False
            

            
       
    
    #draw all our elements
    screen.fill((175,215,70))
    main_game.particle_creation()
    particle_group.draw(screen)
    main_game.draw_player()
    pygame.display.update()
    clock.tick(60)