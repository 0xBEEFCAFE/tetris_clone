import os
import random
import time

import pygame

screen_width = 512
screen_height = 288

window_pos_x = int((1920-screen_width)/2)
window_pos_y = int((1080-screen_height)/2)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
COLORS = [RED, GREEN, BLUE]

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (window_pos_x,window_pos_y)

class Square(pygame.Surface):
	def __init__(self, color):
		pygame.Surface.__init__(self, (16,16))
		self.fill((0,0,0))
		self.fill(color, rect=(2,2,12,12))
		
		self.pos_x = 0
		self.pos_y = 0
		
	def get_pos(self):
		return pygame.Rect(self.pos_x, self.pos_y, self.get_width(), self.get_height())
		

class Tetris(object):
	def __init__(self):
		self.pieces = []
		
		# pygame.mixer.pre_init(22050, -16, 2, 512)
		# pygame.mixer.init()
		# pygame.mixer.quit()
		
		# Call before pygame.init() or there will be delayed sounds
		pygame.mixer.init(22050, -16, 2, 512)
		
		pygame.init()
		pygame.display.set_caption("Tetris")
		self.screen = pygame.display.set_mode((screen_width,screen_height))
		
		self.game_loop()
		
	def spawn_piece(self, color, x, y):
		piece = Square(color)
		
		piece.pos_x = x
		piece.pos_y = y
		
		return piece
	
	def game_loop(self):
		piece = None
		pos_x = 120
		pos_y = 60
		step_y = 1
		
		running = True
		while running:
			
			if piece == None:
				piece = self.spawn_piece(random.choice(COLORS), pos_x, pos_y)
				
			
			self.screen.fill((120,120,120))
			
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
					
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						piece.pos_x -= 16
					if event.key == pygame.K_RIGHT:
						piece.pos_x += 16
					
			
			
			collision = False
			# if piece.get_pos().collidelist([p.get_pos() for p in self.pieces]) > -1:
				# print("A")
				# collision = True
			
			for p in self.pieces:
				r = pygame.Rect(piece.pos_x,piece.pos_y+step_y,16,16)
				if r.colliderect(p.get_pos()):
					print(p.get_pos(), piece.get_pos())
					collision = True
					break
			
			#print(self.pieces[0].get_pos())
			#print([p.get_pos() for p in self.pieces], piece.get_pos())
			#print([p for p in self.pieces[0:-1]])
			#print(self.pieces[0:-1])
			#print(self.pieces)
			
			
			
			if not collision and not piece.pos_y+step_y > screen_height-piece.get_height():
				piece.pos_y += step_y
				self.screen.blit(piece, (piece.pos_x,piece.pos_y))
			else:
				self.pieces.append(piece)
				piece = None
			
			
			self.redraw()
	
			
			
	def redraw(self):
		for piece in self.pieces:
			self.screen.blit(piece, (piece.pos_x,piece.pos_y))
		pygame.display.update()
		time.sleep(0.01)

def main():
	duck = pygame.image.load("clean_16.png").convert_alpha()
	duck_img_width, duck_img_height = duck.get_size()
	duck_xpos = 0
	duck_ypos = 0
	duck_step_x = 1
	duck_step_y = 1
	
	pig = pygame.image.load("dirty_16.png").convert_alpha()
	pig_img_width, pig_img_height = pig.get_size()
	pig_xpos = screen_width-pig_img_width
	pig_ypos = screen_height-pig_img_height
	pig_step_x = 1
	pig_step_y = 1
	
	quack = pygame.mixer.Sound("quack_5.ogg")
	bleat = pygame.mixer.Sound("Bleat.ogg")
	
	
	screen.fill((120,120,120))
	
	
	
	
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		
		# duck_collide = False
		# if duck_xpos+duck_step_x > screen_width-duck_img_width or duck_xpos+duck_step_x < 0:
			# duck_step_x = -duck_step_x
			# duck_collide = True
		# if duck_ypos+duck_step_y > screen_height-duck_img_height or duck_ypos+duck_step_y < 0:
			# duck_step_y = -duck_step_y
			# duck_collide = True
			
		# duck_xpos += duck_step_x
		# duck_ypos += duck_step_y
		
		# pig_collide = False
		# if pig_xpos+pig_step_x > screen_width-duck_img_width or pig_xpos+pig_step_x < 0:
			# pig_step_x = -pig_step_x
			# pig_collide = True
		# if pig_ypos+pig_step_y > screen_height-duck_img_height or pig_ypos+pig_step_y < 0:
			# pig_step_y = -pig_step_y
			# pig_collide = True
			
		# pig_xpos += pig_step_x
		# pig_ypos += pig_step_y
		
		
		# screen.fill((120,120,120))
		# if duck_collide:
			# quack.play()
			# duck = pygame.transform.rotate(duck, -90)
		# if pig_collide:
			# bleat.play()
			# pig = pygame.transform.rotate(pig, -90)
		
		# screen.blit(duck, (duck_xpos,duck_ypos))
		# screen.blit(pig, (pig_xpos,pig_ypos))
		# pygame.display.update()
		time.sleep(0.005)
Tetris()