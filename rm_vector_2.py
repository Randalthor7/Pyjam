import pygame, sys, random
from pygame.locals import *
from pygame.math import Vector2
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
player_move = False
last_movement_time = pygame.time.get_ticks()
movement_delay = 10


particle_no_list = []
particle_group = pygame.sprite.Group()



class PLAYER(pygame.sprite.Sprite):
        def __init__(self ):
            super().__init__()
            self.body =[Vector2(7,10), Vector2(6,10), Vector2(5,10)]
            self.direction = Vector2(1,0)
            
        def draw_player(self):
            for block in self.body:
                x_pos = int(block.x )
                y_pos = int(block.y)
                block_rect = pygame.Rect(x_pos , y_pos , cell_size, cell_size)
                pygame.draw.rect(screen,(183,111,122),block_rect)
                # draw a rect

                

        def move_player(self):
                if player_move:
                    if(current_time - last_movement_time) >= movement_delay:
                        for i in range(1):
                            body_copy = self.body[:-1]
                            body_copy.insert(0,body_copy[0] + self.direction)
                            self.body = body_copy[:]

                    




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
        self.x = random.randint ( 0, cell_number - 1)
        self.y = random.randint ( 0, cell_number - 1)
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
        self.rect.topleft = [(self.pos.x * cell_size), (self.pos.y * cell_size)]








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
        
        
        if event.type == pygame.KEYDOWN:
            player_move = True
                   
        if event.type == pygame.K_UP:
            player_move = False
            
            
                
    
    
    #draw all our elements
    current_time = pygame.time.get_ticks()
    screen.fill((175,215,70))
    main_game.particle_creation()
    particle_group.draw(screen)
    main_game.draw_player()
    pygame.display.update()
    last_movement_time = current_time
    clock.tick(60)