import pygame as pg 
import sys
from pygame.locals import *
import random, time
import json
pg.init()
#fps
FPS = 60
Clock = pg.time.Clock()
#colors
font = pg.font.SysFont("Verdana", 60)
Blue = (0, 0, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Green1 = (0, 200 ,0)
Black = (0, 0, 0)
White = (255, 255, 255)
Gray = (126, 126, 126)
#screen
ScreenW = 900
ScreenH = 600
Screen = pg.display.set_mode((ScreenW, ScreenH))
Screen.fill(White)
pg.display.set_caption("SNAKE GAME TSIS #9 by @zhandosayupov")
#gpu elements
class Button:
	def __init__(self, x, y, w, h, Image):
		self.image = Image
		self.surf = pg.Surface((w,h))
		self.rect = self.surf.get_rect(center = (x, y))
	def update(self):
		global Screen
		Screen.blit(self.image, self.rect)
	def click(self, event):
		x, y = pg.mouse.get_pos()
		if event.type == pg.MOUSEBUTTONDOWN:
			if pg.mouse.get_pressed()[0]:
				if self.rect.collidepoint(x, y):
					return True
#snake
class food:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def reset(self):
		self.x = 20*random.randint(1,28)
		self.y = 20*random.randint(1,28)
	def show(self):
		pg.draw.rect(Screen, Red, [self.x, self.y, 20, 20])
		pg.draw.rect(Screen, Red, [self.x, self.y, 18, 18])

class Snake1:
	def __init__(self, Body, x, y):
		self.body = Body
		self.speedX = x
		self.speedY = y
	def show(self):
		for block in self.body:
			pg.draw.rect(Screen, Green, [block[0], block[1], 20, 20])
			pg.draw.rect(Screen, Green1, [block[0], block[1], 18, 18])
	def update(self, event):
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_RIGHT:
				self.speedX, self.speedY = 20, 0
			if event.key == pg.K_LEFT:
				self.speedX, self.speedY = -20, 0
			if event.key == pg.K_UP:
				self.speedX, self.speedY = 0, -20
			if event.key == pg.K_DOWN:
				self.speedX, self.speedY = 0, 20
	def move(self):
		self.body.append((self.body[-1][0]+self.speedX, self.body[-1][1] + self.speedY))
	def check(self, Food):
		Collision = False
		if((Food.x,Food.y)==self.body[-1]): 
			Food.reset()
		else:
			self.body.pop(0)
class Snake2:
	def __init__(self, Body, x, y):
		self.body = Body
		self.speedX = x
		self.speedY = y
	def show(self):
		for block in self.body[0:-1]:
			pg.draw.rect(Screen, Green, [block[0], block[1], 20, 20])
			pg.draw.rect(Screen, Green1, [block[0], block[1], 18, 18])
	def update(self, event):
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_RIGHT:
				self.speedX, self.speedY = 20, 0
			if event.key == pg.K_LEFT:
				self.speedX, self.speedY = -20, 0
			if event.key == pg.K_UP:
				self.speedX, self.speedY = 0, -20
			if event.key == pg.K_DOWN:
				self.speedX, self.speedY = 0, 20
class Walls:
	def __init__(self, walls):
		self.body = walls
	def show(self):
		for block in self.body:
			pg.draw.rect(Screen, Black, [block[0], block[1], 20, 20])
			pg.draw.rect(Screen, Gray, [block[0], block[1], 18, 18])
#menu
def GameStartMenu():
	global Screen
	background = pg.image.load("Images/startmenu.png")
	Screen.fill(White)
	NewGameButton = Button(450, 300, 180, 60, pg.image.load("Images/newgame.png"))
	LoadGameButton = Button(450, 370 ,180, 60, pg.image.load("Images/loadgame.png"))
	ExitButton = Button(450, 440, 180, 60, pg.image.load("Images/exit.png"))
	while True:
		Screen.blit(background, (0,0))
		NewGameButton.update()
		LoadGameButton.update()
		ExitButton.update()
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if (NewGameButton.click(event)):
				NewGameMenu()
			if (LoadGameButton.click(event)):
				LoadGameMenu()
			if(ExitButton.click(event)):
				pg.quit()
				sys.exit()
		pg.display.update()
		Clock.tick(FPS)
def NewGameMenu():
	background = pg.image.load("Images/levelchoose.png")
	EasyButton = Button(450,170,400,100,pg.image.load("Images/easy.png"))
	MediumButton = Button(450,280,400,100,pg.image.load("Images/medium.png"))
	HardButton = Button(450,390,400,100,pg.image.load("Images/hard.png"))
	ReturnButton = Button(450,500,400,100,pg.image.load("Images/return.png"))
	while True:
		Screen.blit(background, (0,0))
		EasyButton.update()
		MediumButton.update()
		HardButton.update()
		ReturnButton.update()
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if (EasyButton.click(event)):
				print("")
			if (MediumButton.click(event)):
				NewGameMenu()
			if (HardButton.click(event)):
				NewGameMenu()
			if (ReturnButton.click(event)):
				GameStartMenu()
		pg.display.update()
		Clock.tick(FPS)
def LoadGameMenu():
	background = pg.image.load("Images/loadgamemenu.png")
	FirstButton = Button(450,170,400,100,pg.image.load("Images/1.png"))
	SecondButton = Button(450,280,400,100,pg.image.load("Images/2.png"))
	ThirdButton = Button(450,390,400,100,pg.image.load("Images/3.png"))
	ReturnButton = Button(450,500,400,100,pg.image.load("Images/return.png"))
	while True:
		Screen.blit(background, (0,0))
		FirstButton.update()
		SecondButton.update()
		ThirdButton.update()
		ReturnButton.update()
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if (FirstButton.click(event)):
				print("")
			if (SecondButton.click(event)):
				NewGameMenu()
			if (ThirdButton.click(event)):
				NewGameMenu()
			if (ReturnButton.click(event)):
				GameStartMenu()
		pg.display.update()
		Clock.tick(FPS)
def Easy():
	score = 0
	Screen.fill(White)
	walls = list()
	first = Snake1([(280,280)], 20, 0)
	for i in range(0,600,20):
		walls.append((0,i))
		walls.append((580,i))
		walls.append((i,0))
		walls.append((i,580))
	W = Walls(walls)
	F1 = food(120,120)
	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			first.update(event)
		Screen.fill(White)
		F1.show()
		W.show()
		first.show()
		first.move()
		first.check(F1)
		for w in W.body:
			if w == (first.body[-1]):
				print("gameover")
				GameStartMenu()
		pg.display.update()
		Clock.tick(5)
def Medium():
	print()
def Hard():
	print()
#game starts here hehehe		
GameStartMenu()