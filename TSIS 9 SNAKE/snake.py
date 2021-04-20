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
font = pg.font.SysFont("Verdana", 40)
Blue = (0, 0, 255)
Red = (255, 0, 0)
Red1 = (200, 0 , 0)
Green = (0, 255, 0)
Green1 = (0, 200 ,0)
Yellow = (255, 255, 0)
Yellow1 = (200, 200, 0)
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
		self.y = 20*random.randint(1,28)#160 300 440
		if(self.y == 160 or self.y == 300 or self.y == 440):
			self.y += 40
	def show(self):
		pg.draw.rect(Screen, Red, [self.x, self.y, 20, 20])
		pg.draw.rect(Screen, Red1, [self.x, self.y, 18, 18])
class Snake1:
	def __init__(self, Body, x, y,Score=0):
		self.body = Body
		self.speedX = x
		self.speedY = y
		self.score = Score
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
			self.score += 1
		else:
			self.body.pop(0)
class Snake2:
	def __init__(self, Body, x, y, Score=0):
		self.body = Body
		self.speedX = x
		self.speedY = y
		self.score = Score
	def show(self):
		for block in self.body:
			pg.draw.rect(Screen, Yellow, [block[0], block[1], 20, 20])
			pg.draw.rect(Screen, Yellow1, [block[0], block[1], 18, 18])
	def update(self, event):
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_d:
				self.speedX, self.speedY = 20, 0
			if event.key == pg.K_a:
				self.speedX, self.speedY = -20, 0
			if event.key == pg.K_w:
				self.speedX, self.speedY = 0, -20
			if event.key == pg.K_s:
				self.speedX, self.speedY = 0, 20
	def move(self):
		self.body.append((self.body[-1][0]+self.speedX, self.body[-1][1] + self.speedY))
	def check(self, Food):
		Collision = False
		if((Food.x,Food.y)==self.body[-1]): 
			Food.reset()
			self.score +=1 
		else:
			self.body.pop(0)
class Walls:
	def __init__(self, walls):
		self.body = walls
	def show(self):
		for block in self.body:
			pg.draw.rect(Screen, Black, [block[0], block[1], 20, 20])
			pg.draw.rect(Screen, Gray, [block[0], block[1], 18, 18])
#menu
def save(first, second, f, walls, first_alive, second_alive,FPS):
	data = {"firstbody":first.body,"firstx":first.speedX,"firsty":first.speedY,"firstscore":first.score,"secondbody":second.body,"secondx":second.speedX,"secondy":second.speedY,"secondscore":second.score,"foodx":f.x,"foody":f.y,"wallsbody":walls,"fa":first_alive,"sa":second_alive,"fps":FPS}
	with open("1.json","w") as file:
		json.dump(data,file)
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
				Easy()
			if (MediumButton.click(event)):
				Medium()
			if (HardButton.click(event)):
				Hard()
			if (ReturnButton.click(event)):
				GameStartMenu()
		pg.display.update()
		Clock.tick(FPS)
def LoadGameMenu():
	data = dict()
	with open("1.json","r") as file:
		data=json.load(file)
	first = Snake1(data["firstbody"],data["firstx"],data["firsty"],data["firstscore"])
	second = Snake2(data["secondbody"],data["secondx"],data["secondy"],data["secondscore"])
	walls = list()
	walls = walls + data["wallsbody"]
	W = Walls(walls)
	F1 = food(data["foodx"],data["foody"])
	print(type(data["fa"]),type(data["sa"]))
	if(data["fa"]==True):
		firstalive = True
	else:
		firstalive = False
	if(data["sa"]==True):
		secondalive = True
	else:
		secondalive = False
		

	SaveButton = Button(750,400,200,100,pg.image.load("Images/save.png")) 
	ExitButton = Button(750, 550, 180, 60, pg.image.load("Images/exit.png"))
	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			first.update(event)
			second.update(event)
			if(SaveButton.click(event)):
				save(first,second,F1,walls,firstalive,secondalive,data["fps"])
			if(ExitButton.click(event)):
				GameStartMenu()
		Screen.fill(White)
		F1.show()
		W.show()
		
		if(first.body[-1]==second.body[-1]):
			secondalive,firstalive=False,False
		if(firstalive):
			first.move()
			first.check(F1)
			first.show()
			for w in W.body:
				if tuple(w) == tuple(first.body[-1]):
					firstalive = False
			for w in second.body:
				if tuple(w) == tuple(first.body[-1]):
					firstalive = False
			for w in first.body[:-1]:
				if tuple(w) == tuple(first.body[-1]):
					firstalive = False
			#print("work1")
		if(secondalive):
			second.move()
			second.check(F1)
			second.show()
			for w in W.body:
				if tuple(w) == tuple(second.body[-1]):
					secondalive = False
			for w in first.body:
				if tuple(w) == tuple(second.body[-1]):
					secondalive = False
			for w in second.body[:-1]:
				if tuple(w) == tuple(second.body[-1]):
					secondalive = False
			#print("worl2")
		if(firstalive == False and secondalive == False):
			#	print("works")
				kettk(first.score,second.score)
		pg.draw.rect(Screen, Black, [600, 0, 300, 600])
		score1str = "PLAYER 1: " + str(first.score)
		score2str = "PLAYER 2: " + str(second.score)
		score_announce1 = font.render(score1str, True, Green)
		score_announce_rect1 = score_announce1.get_rect(center = (750, 100))
		Screen.blit(score_announce1, score_announce_rect1)
		score_announce2 = font.render(score2str, True, Yellow)
		score_announce_rect2 = score_announce2.get_rect(center = (750 ,150))
		Screen.blit(score_announce2, score_announce_rect2)
		SaveButton.update()
		ExitButton.update()
		pg.display.update()
		Clock.tick(data["fps"])
	
def Easy():
	Screen.fill(White)
	walls = list()
	first_alive = True
	second_alive = True
	first = Snake1([(100,100)], 20, 0)
	second = Snake2([(100,500)], 20, 0)
	for i in range(0,600,20):
		walls.append((0,i))
		walls.append((580,i))
		walls.append((i,0))
		walls.append((i,580))
	W = Walls(walls)
	F1 = food(120,120)
	SaveButton = Button(750,400,200,100,pg.image.load("Images/save.png")) 
	ExitButton = Button(750, 550, 180, 60, pg.image.load("Images/exit.png"))
	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			first.update(event)
			second.update(event)
			if(SaveButton.click(event)):
				save(first,second,F1,walls,first_alive,second_alive,5)
			if(ExitButton.click(event)):
				GameStartMenu()
		Screen.fill(White)
		F1.show()
		W.show()
		
		if(first.body[-1]==second.body[-1]):
			second_alive,first_alive=False,False
		if(first_alive):
			first.move()
			first.check(F1)
			first.show()
			for w in W.body:
				if w == (first.body[-1]):
					first_alive = False
			for w in second.body:
				if w == (first.body[-1]):
					first_alive = False
			for w in first.body[:-1]:
				if w == (first.body[-1]):
					first_alive = False
		if(second_alive):
			second.move()
			second.check(F1)
			second.show()
			for w in W.body:
				if w == (second.body[-1]):
					second_alive = False
			for w in first.body:
				if w == (second.body[-1]):
					second_alive = False
			for w in second.body[:-1]:
				if w == (second.body[-1]):
					second_alive = False
		if(not first_alive):
			if(not second_alive):
				break
		pg.draw.rect(Screen, Black, [600, 0, 300, 600])
		score1str = "PLAYER 1: " + str(first.score)
		score2str = "PLAYER 2: " + str(second.score)
		score_announce1 = font.render(score1str, True, Green)
		score_announce_rect1 = score_announce1.get_rect(center = (750, 100))
		Screen.blit(score_announce1, score_announce_rect1)
		score_announce2 = font.render(score2str, True, Yellow)
		score_announce_rect2 = score_announce2.get_rect(center = (750 ,150))
		Screen.blit(score_announce2, score_announce_rect2)
		SaveButton.update()
		ExitButton.update()
		pg.display.update()
		Clock.tick(5)
	ReturnButton = Button(450,500,400,100,pg.image.load("Images/return.png"))
	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if(ReturnButton.click(event)):
				GameStartMenu()
		Screen.fill(White)
		ReturnButton.update()
		score1str = "PLAYER 1: " + str(first.score)
		score2str = "PLAYER 2: " + str(second.score)
		score_announce1 = font.render(score1str, True, Green)
		score_announce_rect1 = score_announce1.get_rect(center = (450, 200))
		Screen.blit(score_announce1, score_announce_rect1)
		score_announce2 = font.render(score2str, True, Yellow)
		score_announce_rect2 = score_announce2.get_rect(center = (450 ,400))
		Screen.blit(score_announce2, score_announce_rect2)
		if(first.score==second.score):
			draw = font.render("DRAW", True, Black)
			draw_rect = draw.get_rect(center = (450, 300))
			Screen.blit(draw, draw_rect)
		elif(first.score>second.score):
			draw = font.render("PLAYER 1 WINS", True, Black)
			draw_rect = draw.get_rect(center = (450, 300))
			Screen.blit(draw, draw_rect)
		else:
			draw = font.render("PLAYER 2 WINS", True, Black)
			draw_rect = draw.get_rect(center = (450, 300))
			Screen.blit(draw, draw_rect)
		pg.display.update()
		Clock.tick(5)
def kettk(firstscore,secondscore):
	ReturnButton = Button(450,500,400,100,pg.image.load("Images/return.png"))
	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if(ReturnButton.click(event)):
				GameStartMenu()
		Screen.fill(White)
		ReturnButton.update()
		score1str = "PLAYER 1: " + str(firstscore)
		score2str = "PLAYER 2: " + str(secondscore)
		score_announce1 = font.render(score1str, True, Green)
		score_announce_rect1 = score_announce1.get_rect(center = (450, 200))
		Screen.blit(score_announce1, score_announce_rect1)
		score_announce2 = font.render(score2str, True, Yellow)
		score_announce_rect2 = score_announce2.get_rect(center = (450 ,400))
		Screen.blit(score_announce2, score_announce_rect2)
		if(firstscore==secondscore):
			draw = font.render("DRAW", True, Black)
			draw_rect = draw.get_rect(center = (450, 300))
			Screen.blit(draw, draw_rect)
		elif(firstscore>secondscore):
			draw = font.render("PLAYER 1 WINS", True, Black)
			draw_rect = draw.get_rect(center = (450, 300))
			Screen.blit(draw, draw_rect)
		else:
			draw = font.render("PLAYER 2 WINS", True, Black)
			draw_rect = draw.get_rect(center = (450, 300))
			Screen.blit(draw, draw_rect)
		pg.display.update()
		Clock.tick(5)
def Medium():
	Screen.fill(White)
	walls = list()
	first_alive = True
	second_alive = True
	first = Snake1([(100,100)], 20, 0)
	second = Snake2([(100,500)], 20, 0)
	for i in range(0,600,20):
		walls.append((0,i))
		walls.append((580,i))
		walls.append((i,0))
		walls.append((i,580))
	for i in range(200,400,20):
		walls.append((i,160))
		walls.append((i,440))
	W = Walls(walls)
	F1 = food(120,120)
	SaveButton = Button(750,400,200,100,pg.image.load("Images/save.png")) 
	ExitButton = Button(750, 550, 180, 60, pg.image.load("Images/exit.png"))
	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			first.update(event)
			second.update(event)
			if(SaveButton.click(event)):
				save(first,second,F1,walls,first_alive,second_alive,10)
			if(ExitButton.click(event)):
				GameStartMenu()
		Screen.fill(White)
		F1.show()
		W.show()
		
		if(first.body[-1]==second.body[-1]):
			second_alive,first_alive=False,False
		if(first_alive):
			first.move()
			first.check(F1)
			first.show()
			for w in W.body:
				if w == (first.body[-1]):
					first_alive = False
			for w in second.body:
				if w == (first.body[-1]):
					first_alive = False
			for w in first.body[:-1]:
				if w == (first.body[-1]):
					first_alive = False
		if(second_alive):
			second.move()
			second.check(F1)
			second.show()
			for w in W.body:
				if w == (second.body[-1]):
					second_alive = False
			for w in first.body:
				if w == (second.body[-1]):
					second_alive = False
			for w in second.body[:-1]:
				if w == (second.body[-1]):
					second_alive = False
		if(not first_alive):
			if(not second_alive):
				break
		pg.draw.rect(Screen, Black, [600, 0, 300, 600])
		score1str = "PLAYER 1: " + str(first.score)
		score2str = "PLAYER 2: " + str(second.score)
		score_announce1 = font.render(score1str, True, Green)
		score_announce_rect1 = score_announce1.get_rect(center = (750, 100))
		Screen.blit(score_announce1, score_announce_rect1)
		score_announce2 = font.render(score2str, True, Yellow)
		score_announce_rect2 = score_announce2.get_rect(center = (750 ,150))
		Screen.blit(score_announce2, score_announce_rect2)
		SaveButton.update()
		ExitButton.update()
		pg.display.update()
		Clock.tick(10)
	ReturnButton = Button(450,500,400,100,pg.image.load("Images/return.png"))
	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if(ReturnButton.click(event)):
				GameStartMenu()
		Screen.fill(White)
		ReturnButton.update()
		score1str = "PLAYER 1: " + str(first.score)
		score2str = "PLAYER 2: " + str(second.score)
		score_announce1 = font.render(score1str, True, Green)
		score_announce_rect1 = score_announce1.get_rect(center = (450, 200))
		Screen.blit(score_announce1, score_announce_rect1)
		score_announce2 = font.render(score2str, True, Yellow)
		score_announce_rect2 = score_announce2.get_rect(center = (450 ,400))
		Screen.blit(score_announce2, score_announce_rect2)
		if(first.score==second.score):
			draw = font.render("DRAW", True, Black)
			draw_rect = draw.get_rect(center = (450, 300))
			Screen.blit(draw, draw_rect)
		elif(first.score>second.score):
			draw = font.render("PLAYER 1 WINS", True, Black)
			draw_rect = draw.get_rect(center = (450, 300))
			Screen.blit(draw, draw_rect)
		else:
			draw = font.render("PLAYER 2 WINS", True, Black)
			draw_rect = draw.get_rect(center = (450, 300))
			Screen.blit(draw, draw_rect)
		pg.display.update()
		Clock.tick(10)
def Hard():
	Screen.fill(White)
	walls = list()
	first_alive = True
	second_alive = True
	first = Snake1([(100,100)], 20, 0)
	second = Snake2([(100,500)], 20, 0)
	for i in range(0,600,20):
		walls.append((0,i))
		walls.append((580,i))
		walls.append((i,0))
		walls.append((i,580))
	for i in range(120,480,20):
		walls.append((i,160))
		walls.append((i,440))
		walls.append((i,300))
	W = Walls(walls)
	F1 = food(120,120)
	SaveButton = Button(750,400,200,100,pg.image.load("Images/save.png")) 
	ExitButton = Button(750, 550, 180, 60, pg.image.load("Images/exit.png"))
	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			first.update(event)
			second.update(event)
			if(SaveButton.click(event)):
				save(first,second,F1,walls,first_alive,second_alive,15)
			if(ExitButton.click(event)):
				GameStartMenu()
		Screen.fill(White)
		F1.show()
		W.show()
		
		if(first.body[-1]==second.body[-1]):
			second_alive,first_alive=False,False
		if(first_alive):
			first.move()
			first.check(F1)
			first.show()
			for w in W.body:
				if w == (first.body[-1]):
					first_alive = False
			for w in second.body:
				if w == (first.body[-1]):
					first_alive = False
			for w in first.body[:-1]:
				if w == (first.body[-1]):
					first_alive = False
		if(second_alive):
			second.move()
			second.check(F1)
			second.show()
			for w in W.body:
				if w == (second.body[-1]):
					second_alive = False
			for w in first.body:
				if w == (second.body[-1]):
					second_alive = False
			for w in second.body[:-1]:
				if w == (second.body[-1]):
					second_alive = False
		if(not first_alive):
			if(not second_alive):
				break
		pg.draw.rect(Screen, Black, [600, 0, 300, 600])
		score1str = "PLAYER 1: " + str(first.score)
		score2str = "PLAYER 2: " + str(second.score)
		score_announce1 = font.render(score1str, True, Green)
		score_announce_rect1 = score_announce1.get_rect(center = (750, 100))
		Screen.blit(score_announce1, score_announce_rect1)
		score_announce2 = font.render(score2str, True, Yellow)
		score_announce_rect2 = score_announce2.get_rect(center = (750 ,150))
		Screen.blit(score_announce2, score_announce_rect2)
		SaveButton.update()
		ExitButton.update()
		pg.display.update()
		Clock.tick(15)
	ReturnButton = Button(450,500,400,100,pg.image.load("Images/return.png"))
	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if(ReturnButton.click(event)):
				GameStartMenu()
		Screen.fill(White)
		ReturnButton.update()
		score1str = "PLAYER 1: " + str(first.score)
		score2str = "PLAYER 2: " + str(second.score)
		score_announce1 = font.render(score1str, True, Green)
		score_announce_rect1 = score_announce1.get_rect(center = (450, 200))
		Screen.blit(score_announce1, score_announce_rect1)
		score_announce2 = font.render(score2str, True, Yellow)
		score_announce_rect2 = score_announce2.get_rect(center = (450 ,400))
		Screen.blit(score_announce2, score_announce_rect2)
		if(first.score==second.score):
			draw = font.render("DRAW", True, Black)
			draw_rect = draw.get_rect(center = (450, 300))
			Screen.blit(draw, draw_rect)
		elif(first.score>second.score):
			draw = font.render("PLAYER 1 WINS", True, Black)
			draw_rect = draw.get_rect(center = (450, 300))
			Screen.blit(draw, draw_rect)
		else:
			draw = font.render("PLAYER 2 WINS", True, Black)
			draw_rect = draw.get_rect(center = (450, 300))
			Screen.blit(draw, draw_rect)
		pg.display.update()
		Clock.tick(5)
#game starts here hehehe		
GameStartMenu()