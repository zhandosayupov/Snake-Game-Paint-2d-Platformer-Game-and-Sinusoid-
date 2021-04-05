import pygame as pg
from math import pi,sin,cos
pg.init()
size = width, height = (800, 600)
screen = pg.display.set_mode(size)
font = pg.font.SysFont('times new roman', 19)
font2 = pg.font.SysFont('times new roman', 25)
done = True

BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ypi = [' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']
xpi = ['-3π', ' 5π', '-2π', ' 3π', '-π ', ' π ', ' 0 ', ' π ', ' π ', ' 3π', ' 2π', ' 5π', ' 3π']
xpi_1 = ['', '_ __', '', '_ __', '', '_ _', '', '   _', '', '   __', '', '   __', '']
xpi_2 = ['', '  2', '', '  2', '', ' 2', '', ' 2', '', '  2', '', '  2', '']

while done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = 0
    screen.fill(WHITE)
    pg.draw.rect(screen, BLACK, (70, 10, 660, 540), 2)  
    pg.draw.line(screen, BLACK, (70, 280), (730, 280), 2)
    pg.draw.line(screen, BLACK, (400, 10), (400, 550), 2)

    for x in range(100, 700, 3):
        cos1 = 240 * cos((x - 100) / 100 * pi)
        cos2 = 240 * cos((x - 99) / 100 * pi)
        pg.draw.aalines(screen, BLUE, 0, [(x, 280 + cos1), ((x + 1), 280 + cos2)])

    for x in range(100, 700):
        sin1 = 240 * sin((x - 100) / 100 * pi)
        sin2 = 240 * sin((x - 99) / 100 * pi)
        pg.draw.aalines(screen, RED, 0, [(x, 280 + sin1), ((x + 1), 280 + sin2)])

    for x in range(100, 800, 100):
        if x != 500:
            pg.draw.line(screen, BLACK, (x, 10), (x, 550))
        else:
            pg.draw.line(screen, BLACK, (x, 10), (x, 40))
            pg.draw.line(screen, BLACK, (x, 100), (x, 550))

    for y in range(40, 530, 60):
        pg.draw.line(screen, BLACK, (70, y), (730, y))

    for y in range(40, 530, 30):
        pg.draw.line(screen, BLACK, (70, y), (90, y))
        pg.draw.line(screen, BLACK, (710, y), (730, y))

    for x in range(100, 750, 50):
        pg.draw.line(screen, BLACK, (x, 10), (x, 30))
        pg.draw.line(screen, BLACK, (x, 550), (x, 530))

    for x in range(100, 710, 25):
        pg.draw.line(screen, BLACK, (x, 10), (x, 20))
        pg.draw.line(screen, BLACK, (x, 550), (x, 540))

    for y in range(40, 530, 15):
        pg.draw.line(screen, BLACK, (70, y), (80, y))
        pg.draw.line(screen, BLACK, (720, y), (730, y))


    screen.blit(font.render('sin(x)', 0, BLACK), (475, 45))
    pg.draw.line(screen, RED, (530, 60), (570, 60))
    screen.blit(font.render('cos(x)', 0, BLACK), (475, 75))

    for x in range(530, 570, 7):
        pg.draw.line(screen, BLUE, (x, 90), (x + 3, 90))
    screen.blit(font2.render('X', 0, BLACK), (392, 575))

    for x in range(100, 750, 50):
        screen.blit(font.render(xpi[(x - 100) // 50], 0, BLACK), (x - 10, 550))
        screen.blit(font.render(xpi_1[(x - 100) // 50], 0, BLACK), (x - 20, 550))
        screen.blit(font.render(xpi_2[(x - 100) // 50], 0, BLACK), (x - 10, 570))

    for y in range(40, 530, 60):
        screen.blit(font.render(ypi[(y - 40) // 60], 0, BLACK), (20, (y - 10)))
    pg.display.flip()

pg.quit()