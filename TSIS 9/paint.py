import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
COLOR = (0, 255, 255)
#
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("PAINT by @zhandosayupov")
game_over = False

prev, cur = None, None
screen.fill(WHITE)
current_color = WHITE

line = False
rect = False
circle = True
erase = False
class ButtonColor:
  def __init__(self, x, y, w, h, color):
    self.surf = pygame.Surface((w,h))
    self.rect = self.surf.get_rect(center = (x, y))
    self.color = color
  def update(self):
    self.surf.fill(self.color)
    screen.blit(self.surf, self.rect)
  def click(self, event):
    global current_color
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed()[0]:
        if self.rect.collidepoint(x, y):
          current_color = self.color
class Button:
  def __init__(self, x, y, w, h, Image):
    self.image = Image
    self.surf = pygame.Surface((w,h))
    self.rect = self.surf.get_rect(center = (x, y))
  def update(self):
    screen.blit(self.image, self.rect)
  def click(self, event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed()[0]:
        if self.rect.collidepoint(x, y):
          return True
while not game_over:
  Black = ButtonColor(15, 15, 20, 20, BLACK)
  White = ButtonColor(40, 15, 20, 20, WHITE)
  Red = ButtonColor(65, 15, 20, 20, RED)
  Green = ButtonColor(90, 15, 20, 20, GREEN)
  Blue = ButtonColor(115, 15, 20, 20, BLUE)
  Yellow = ButtonColor(140, 15, 20, 20, YELLOW)
  Purple = ButtonColor(165, 15, 20, 20, PURPLE)
  Color = ButtonColor(190,15, 20 ,20, COLOR)
  LineB = Button(230, 15, 20, 20, pygame.image.load("Images/line.png"))
  RectB = Button(255, 15, 20, 20, pygame.image.load("Images/rect.png"))
  CircB = Button(280, 15, 20, 20, pygame.image.load("Images/circle.png"))
  Save = Button(305,15,20,20,pygame.image.load("Images/save.png"))
  Erase = Button(330,15,20,20,pygame.image.load("Images/erase.png"))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if(line):
      if event.type == pygame.MOUSEBUTTONDOWN:
        prev = pygame.mouse.get_pos()
      if event.type == pygame.MOUSEMOTION:
        cur = pygame.mouse.get_pos()
        if prev:
          pygame.draw.line(screen, current_color, prev, cur, 10)
          prev = cur
      if event.type == pygame.MOUSEBUTTONUP:
        prev = None
    if(rect):
      if event.type == pygame.MOUSEBUTTONDOWN:
        prev = pygame.mouse.get_pos()
      if event.type == pygame.MOUSEMOTION:
        cur = pygame.mouse.get_pos()
      if event.type == pygame.MOUSEBUTTONUP:
        pygame.draw.rect(screen, current_color, [min(prev[0],cur[0]), min(prev[1],cur[1]), abs(prev[0]-cur[0]),abs(prev[1]-cur[1]) ],10)
        prev = None
    if(circle):
      if event.type == pygame.MOUSEBUTTONDOWN:
        prev = pygame.mouse.get_pos()
      if event.type == pygame.MOUSEMOTION:
        cur = pygame.mouse.get_pos()
      if event.type == pygame.MOUSEBUTTONUP:
        pygame.draw.ellipse(screen, current_color, [min(prev[0],cur[0]), min(prev[1],cur[1]), abs(prev[0]-cur[0]),abs(prev[1]-cur[1]) ],10)
        prev = None
    if(erase):
      if event.type == pygame.MOUSEBUTTONDOWN:
        prev = pygame.mouse.get_pos()
      if event.type == pygame.MOUSEMOTION:
        cur = pygame.mouse.get_pos()
        if prev:
          pygame.draw.line(screen, WHITE, prev, cur, 50)
          prev = cur
      if event.type == pygame.MOUSEBUTTONUP:
        prev = None
    Black.click(event)
    White.click(event)
    Red.click(event)
    Green.click(event)
    Blue.click(event)
    Yellow.click(event)
    Purple.click(event)
    Color.click(event)
    if(LineB.click(event)):
      line,rect,circle,erase = True,False,False,False
    if(RectB.click(event)):
      line,rect,circle,erase = False,True,False,False
    if(CircB.click(event)):
      line,rect,circle,erase = False,False,True,False
    if(Save.click(event)):
      pygame.image.save(screen,"image.png")
    if(Erase.click(event)):
      line,rect,circle,erase = False,False,False,True

  pygame.draw.rect(screen, (126,126,126), [0,0,400,30])
  Black.update()
  White.update()
  Red.update()
  Green.update()
  Blue.update()
  Yellow.update()
  Purple.update()
  Color.update()
  LineB.update()
  RectB.update()
  CircB.update()
  Save.update()
  Erase.update()
  # if prev:
  #   pygame.draw.circle(screen, RED, prev, 10)
  pygame.display.flip()

  clock.tick(90)


pygame.quit()