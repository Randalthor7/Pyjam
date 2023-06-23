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
particle_size = 10
player_move_x = False
player_move_y = False
particle_no_list = []
particle_group = pygame.sprite.Group()
player_head = pygame.sprite.Group()
all_sprite = pygame.sprite.Group()
player_rect = 32
direction = Vector2(1,0) 
speed = 5
move = int(1 * speed)


class PLAYER(pygame.sprite.Sprite):
        def __init__(self ):
            super().__init__()
            
            self.is_animating = False
            self.body =[Vector2(400,10), Vector2(400,10), Vector2(400,10), Vector2(400,10)]
            self.body_measured_x = []
            self.body_measured_y = []
            self.head = []
            self.head.append(pygame.image.load('rm1.png'))
            self.head.append(pygame.image.load('rm2.png'))
            self.head.append(pygame.image.load('rm3.png'))
            self.head.append(pygame.image.load('rm4.png'))
            self.head.append(pygame.image.load('rm5.png'))
            self.head.append(pygame.image.load('rm6.png'))
            self.current_head = 0
            self.image = self.head[self.current_head]
            self.rect = self.image.get_rect()           


        def player_head_move(self):

            self.rect.topleft = (self.body[0].x) , (self.body[0].y)
            for p in particle_group:
                if self.rect.colliderect(p.rect):
                    print("Collision detected: ", self.rect.topleft, p.rect.topleft)
                    collided_particles = pygame.sprite.spritecollide(self, particle_group, False)
                    for particle in collided_particles:
                         self.body.append(particle)
                         particle_group.remove(p)

            
             
        def animate(self):
             self.is_animating = True
        def stop_animate(self):
             self.is_animating = False
        def update(self):
             if self.is_animating == True:
                  self.current_head += 0.2

                  if self.current_head >= len(self.head):
                       self.current_head = 0
                       


                  self.image = self.head[int(self.current_head)]
                  return self.image

        
        def mantain_distance_x(self):
            for i in range(1, len(self.body)):
                prev_block = self.body[i - 1]
                curr_block = self.body[i]
                dist_x = curr_block.x - prev_block.x
                if abs(dist_x) < particle_size:
                    move_dist_x = particle_size - abs(dist_x)
                    move_dir_x = 1 if dist_x > 0 else -1
                    curr_block.x += move_dist_x * move_dir_x
            self.body_measured_x = [block.x for block in self.body]
            print(self.body_measured_x)
        
        def mantain_distance_y(self):
            for i in range(1, len(self.body)):
                prev_block = self.body[i - 1]
                curr_block = self.body[i]
                dist_y = curr_block.y - prev_block.y
                if abs(dist_y) < particle_size:
                    move_dist_y = particle_size - abs(dist_y)
                    move_dir_y = 1 if dist_y > 0 else -1
                    curr_block.y += move_dist_y * move_dir_y
            self.body_measured_y = [block.y for block in self.body]
            print(self.body_measured_y)
            

        def draw_player(self):
            for block in self.body:
                x_pos = int(block.x )
                y_pos = int(block.y)
                block_rect = pygame.Rect(x_pos , y_pos , player_rect, player_rect)
                pygame.draw.rect(screen,(183,111,122),block_rect)
                # draw a rect

                

        def move_player_x(self):
                if player_move_x:
                        body_copy = self.body[:-1]
                        body_copy.insert(0,body_copy[0] + (direction))
                        self.body = body_copy[:]
                        self.mantain_distance_x()
        def move_player_y(self):
                if player_move_y:
                        body_copy = self.body[:-1]
                        body_copy.insert(0,body_copy[0] + (direction))
                        self.body = body_copy[:]
                        self.mantain_distance_y()
                        
                        



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
            all_sprite.add(particle_no_list[self.particle_counter])
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




class Player_particle_collide:
     def __init__(self):
          self.foo = 1

     def player_particle_collisions(self):
          collisions = pygame.sprite.groupcollide(particle_group, all_sprite, False, False)

          if collisions:
            print("Sprites collided!")
               
     



screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()


class MAIN:
    def __init__(self):
        self.particle_creator = PARTICLE_CREATOR()
        self.player = PLAYER()
        player_head.add(self.player)
        all_sprite.add(self.player)
        self.player_particle_collide = Player_particle_collide()

    def particle_creation(self):
            if len(particle_group) == 0:
                self.particle_creator.create_particle_list()
                self.particle_creator.particle_constructor()

    def draw_player(self):  
        self.player.move_player_x()
        self.player.move_player_y()
        self.player.draw_player()
        self.player.update()
        self.player.player_head_move()
    
    def animate_player(self):
         self.player.animate()
    def stop_animate_player(self):
         self.player.stop_animate()
    def sprite_collide(self):
         self.player_particle_collide.player_particle_collisions




        
        



main_game = MAIN()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
             if event.key == K_RIGHT:
                  direction = Vector2(move,0)
                  main_game.animate_player()
                  player_move_x = True
                  player_move_y = False
             if event.key == K_LEFT:
                  direction = Vector2(-move,0)
                  player_move_x = True
                  player_move_y = False
                  main_game.animate_player()

             if event.key == K_UP:
                  direction = Vector2(0,-move)
                  player_move_y = True
                  player_move_x = False
                  main_game.animate_player()
             if event.key == K_DOWN:
                  direction = Vector2(0,move)
                  player_move_y = True
                  player_move_x = False
                  main_game.animate_player()
        if event.type == KEYUP:
             if event.key == K_RIGHT:
                  player_move_x = False
                  main_game.stop_animate_player()
             if event.key == K_LEFT:
                  player_move_x = False
                  main_game.stop_animate_player()
             if event.key == K_DOWN:
                  player_move_y = False
                  main_game.stop_animate_player()
             if event.key == K_UP:
                  player_move_y = False
                  main_game.stop_animate_player()
                  
            

            
       
    
    #draw all our elements
    screen.fill((175,215,70))
    main_game.particle_creation()
    particle_group.draw(screen)
    main_game.draw_player()
    player_head.draw(screen)
    main_game.sprite_collide()
    
    pygame.display.update()
    clock.tick(60)