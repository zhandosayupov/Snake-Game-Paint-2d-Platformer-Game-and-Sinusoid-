import pygame as pg 
import sys 
from pygame.locals import *
import random, time
pg.init()
#fps
FPS = 60
Clock = pg.time.Clock()
#colors
Blue = (0, 0, 255)
Red = (255, 0, 0)
Green = (0, 0, 255)
Black = (0, 0, 0)
White = (255, 255, 255)
#screen
Display = pg.display.set_mode((400,600))
Display.fill(White)
pg.display.set_caption("GAME TSIS #8")
Screen_w = 400
Screen_h = 600
#game vars
delta_speed = 0
score = 0 
record = 0
x = 0
y = 0
#fonts
font = pg.font.SysFont("Verdana", 60)
font_small = pg.font.SysFont("Verdana", 20)
#background
background = pg.image.load("AnimatedStreet.png")
#sprites
class Enemy(pg.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pg.image.load("Enemy.png")
		self.surf = pg.Surface((42, 70))
		self.rect = self.surf.get_rect(center = (random.randint(40, Screen_w - 40), 0))
		self.speed = random.randint(1, 5)
	def move(self):
		global delta_speed
		self.rect.move_ip(0, self.speed + delta_speed)
		if (self.rect.bottom > 600):
			self.rect.top = 0
			self.speed = random.randint(1, 5)
			self.rect.center = (random.randint(40, Screen_w - 40), 0)
class Player(pg.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pg.image.load("Player.png")
		self.surf = pg.Surface((40,75))
		self.rect = self.surf.get_rect(center = (160, 520))
	def move(self):
		global delta_speed
		pressed_keys = pg.key.get_pressed()
		global x, y
		if self.rect.left > 0:
			if pressed_keys[K_LEFT]:
				self.rect.move_ip(-5, 0)
		if self.rect.right < Screen_w:
			if pressed_keys[K_RIGHT]:
				self.rect.move_ip(5, 0)
		x = self.rect.left
		x = self.rect.top
class Coin(pg.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pg.transform.scale(pg.image.load("Coin.png"),(30,30))
		self.surf = pg.Surface((30, 30))
		self.rect = self.surf.get_rect(center = (random.randint(30, Screen_w - 30), 0))
		self.speed = 5
	def move(self):
		global delta_speed
		global x, y
		self.rect.move_ip(0, self.speed + delta_speed)
		if (self.rect.bottom > 600):
			self.rect.top = 0
			self.rect.center = (random.randint(30, Screen_w - 30), 0)
		if (self.rect.bottom > 480 and self.rect.left > x):
			self.rect.top = 0
			self.rect.center = (random.randint(30, Screen_w - 30), 0)
	def reset(self):
		global score,record
		score += 1
		record = max(score,record)
		self.rect.center = (random.randint(30, Screen_w - 30), 0)
#menu
def game_loop():
	global score
	score = 0
	active = True
	P1 = Player()
	E1 = Enemy()
	C1 = Coin()
	C2 = Coin()
	enemies = pg.sprite.Group()
	enemies.add(E1)
	all_sprites = pg.sprite.Group()
	all_sprites.add(P1)
	all_sprites.add(E1)
	all_sprites.add(C1)
	all_sprites.add(C2)
	global delta_speed
	delta_speed = 0
	INC_SPEED = pg.USEREVENT + 1
	pg.time.set_timer(INC_SPEED, 20000)
	while True:
		for event in pg.event.get():
			if event.type == INC_SPEED:
				delta_speed += 1 
			if event.type == QUIT:
				pg.quit()
				sys.exit()
		Display.blit(background, (0,0))
		scores = font_small.render(str(score), True, Black)
		Display.blit(scores, (10,10))
		for entity in all_sprites:
			Display.blit(entity.image, entity.rect)
			entity.move()
		if(P1.rect.colliderect(C1.rect)):
			C1.reset()
		if(P1.rect.colliderect(C2.rect)):
			C2.reset()
		if pg.sprite.spritecollideany(P1, enemies):
			pg.mixer.Sound('crash.wav').play()
			time.sleep(1)
			pg.display.update()
			for entity in all_sprites:
				entity.kill() 
			gameover()  
		pg.display.update()
		Clock.tick(FPS)
def gameover():	
	global score, record
	end_game = True
	Display.fill(Red)
	announcement = font_small.render("Game Over", True, White)
	announcement_rect = announcement.get_rect(center = (int(Screen_w/2),int(Screen_h/3)))
	Display.blit(announcement, announcement_rect)
	qinstructions = font_small.render("Press q to Quit", True, White)
	qinstructions_rect = qinstructions.get_rect(center = (int(Screen_w/2),int(Screen_h/1.5)))
	Display.blit(qinstructions, qinstructions_rect)
	rinstructions = font_small.render("Press r to Resume", True, (255, 255, 255))
	rinstructions_rect = rinstructions.get_rect(center = (int(Screen_w/2),int(Screen_h/1.3)))
	Display.blit(rinstructions, rinstructions_rect)
	final_score = "Final score: " + str(score)
	record_score = "Record score: " + str(record)
	score_announce = font_small.render(final_score, True, White)
	score_announce_rect = score_announce.get_rect(center = (int(Screen_w/2), int(Screen_h/2)))
	Display.blit(score_announce, score_announce_rect)
	score_announce1 = font_small.render(record_score, True, White)
	score_announce_rect1 = score_announce1.get_rect(center = (int(Screen_w/2), int(Screen_h/2)+20))
	Display.blit(score_announce1, score_announce_rect1)
	pg.display.flip()

	while (end_game):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_q:
					pg.quit()
					sys.exit()
				if event.key == pg.K_r:
					end_game = False
	game_loop()
def welcome_screen():
	Display.fill(Green)
	welcome = font_small.render("Let's Play Game!", True, White)
	welcome_rect = welcome.get_rect(center = (int(Screen_w/2),int(Screen_h/3)))
	startmsg = font_small.render("Hit 'q' or auto start in 10 seconds", True, White)
	startmsg_rect = startmsg.get_rect(center = (int(Screen_w/2),int(Screen_h/4)))
	Display.blit(welcome, welcome_rect)
	Display.blit(startmsg, startmsg_rect)
	pg.display.flip()
	pg.time.set_timer(pg.USEREVENT, 10000)
	timer_active = True
	while (timer_active):
		for event in pg.event.get():
			if event.type == pg.USEREVENT:
				timer_active = False
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_q:
					timer_active = False
	game_loop()
#vot i game started
welcome_screen()