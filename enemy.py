
import pygame
from pygame.math import Vector2
import random
from coin import *
from player import *
from defenses import *
from random_drops import *

class Enemy(pygame.sprite.Sprite):
    
    
    def __init__(self, game):
        self.game = game
        self.groups = self.game.all_sprites_group, self.game.enemy_group
        pygame.sprite.Sprite.__init__(self, self.groups)


        # waypoints de movimentação no mapa
        self.waypoints = game.mapa.waypoints
        self.target_waypoint = 1

        #atributos modificaveis entre tipos de inimigos
        self.speed = 1
        self.dano = 1
        self.hp = 1
   
        # atributos do sprite
        self.image = pygame.image.load('Assets/enemy1.png').convert_alpha()
        self.pos = Vector2(self.waypoints[0])
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        #
        
        self.final = False
        self.morto = False
        self.on_fire = False

    

        
        

    def update(self): # Método que executa o movimento do inimigo
        # inimigo esá vivo
        if not self.morto:
            self.move()
        # inimigo morreu
        else:
            self.drop()

        # inimigo chegou ao final do caminho
        if self.final:
            for group in self.groups:
                group.remove(self)

            if not self.game.shield:
                self.game.hp -= self.dano
            self.game.shield = False



        if self.on_fire:
            self.hp -= 0.3

        if self.hp <=0:
            self.morto = True


    def move(self): # Método que define o movimento do inimigo
        self.target = Vector2(self.waypoints[self.target_waypoint])
        self.movement = self.target - self.pos
        dist = self.movement.length()
       
        # passa para o proximo waypoint quando o inimigo ficar proximo do waypoint atual
        if dist <= self.speed:
            if self.target_waypoint < len(self.waypoints) - 1:
                self.target_waypoint += 1
                
                #debug pra testar morte do inimigo -> mata o inimigo logo no primeiro checkpoint 
                #self.morto = True
                # se acabou todos os waypoints, o monstro chegou no final
            else:
              
                self.final = True


        self.pos += self.movement.normalize() * self.speed
        self.rect.center = self.pos
    
    def drop(self):
        
        coin(self.game, self.pos)
    

        self.kill()
        


class enem_type1(Enemy):
    def __init__(self, game):
        super().__init__(game)
        
        self.speed = 2.5
        self.hp = 100
        self.dano = 1
        self.image = pygame.image.load('Assets/Green_evil_eye_tp.png.png').convert_alpha()

  
class enem_type2(Enemy):
    def __init__(self, game):
        super().__init__(game)
        
        self.speed = 2
        self.hp = 180
        self.dano = 3
        self.image = pygame.image.load('Assets/Red_evil_eye_tp.png.png').convert_alpha()


class enem_type3(Enemy):
    def __init__(self, game):
        super().__init__(game)
        
        self.speed = 8
        self.hp = 40
        self.dano = 2
        self.image = pygame.image.load('Assets/Blue_evil_eye_tp.png.png').convert_alpha()
  

class enem_type4(Enemy): # MOOOOOOAAAAAABBBB YEAAAAAAAAAAAA
    def __init__(self, game):
        super().__init__(game)

        self.speed = 2
        self.hp = 1000
        self.dano = 20
        self.image = pygame.image.load('Assets/Cthulhu_eye_base_tp.png.png').convert_alpha()

    def drop(self):
        coin(self.game, self.pos)
        coin(self.game, self.pos)

        spawn1 = enem_type1(self.game)
        spawn1.pos = self.pos.copy()
        spawn1.target_waypoint = self.target_waypoint
        spawn2 = enem_type2(self.game)
        spawn2.pos = self.pos.copy()
        spawn2.target_waypoint = self.target_waypoint
        spawn3 = enem_type3(self.game)
        spawn3.pos = self.pos.copy()
        spawn3.target_waypoint = self.target_waypoint
        spawn4 = enem_type1(self.game)
        spawn4.pos = self.pos.copy()
        spawn4.target_waypoint = self.target_waypoint
        spawn5 = enem_type1(self.game)
        spawn5.pos = self.pos.copy()
        spawn5.target_waypoint = self.target_waypoint
    
        for group in self.groups:
            group.remove(self)

            


class enem_type5(Enemy): # MOAB PART 2
    def __init__(self, game):
        super().__init__(game)

        self.speed = 1
        self.hp = 3500
        self.dano = 20
        self.image = pygame.image.load('Assets/Cthulhu_eye_tp.png.png').convert_alpha()
        
    def drop(self):
        coin(self.game, self.pos)
        coin(self.game, self.pos)
        coin(self.game, self.pos)
        coin(self.game, self.pos)
        coin(self.game, self.pos)
        spawn1 = enem_type4(self.game)
        spawn1.pos = self.pos.copy()
        spawn1.target_waypoint = self.target_waypoint
        spawn2 = enem_type4(self.game)
        spawn2.pos = self.pos.copy()
        spawn2.target_waypoint = self.target_waypoint
        self.kill()