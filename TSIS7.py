import pygame
import math
pygame.init()
size = width, height = (800, 600)
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont('times new roman', 19)
font2 = pygame.font.SysFont('times new roman', 25)
done = True

COLOR1 = (0, 0, 0) 
COLOR2 = (255, 255, 255) 
COLOR3 = (0, 255, 0)
COLOR4 = (0, 0, 255)
COLOR5 = (255, 0, 0)
ypi = [' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']
xpi = ['-3π', ' 5π', '-2π', ' 3π', '-π ', ' π ', ' 0 ', ' π ', ' π ', ' 3π', ' 2π', ' 5π', ' 3π']
xpi_1 = ['', '_ __', '', '_ __', '', '_ _', '', '   _', '', '   __', '', '   __', '']
xpi_2 = ['', '  2', '', '  2', '', ' 2', '', ' 2', '', '  2', '', '  2', '']

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = 0
    screen.fill(COLOR2)
    pygame.draw.rect(screen, COLOR1, (70, 10, 660, 540), 2)  
    pygame.draw.line(screen, COLOR1, (70, 280), (730, 280), 2)
    pygame.draw.line(screen, COLOR1, (400, 10), (400, 550), 2)

    for x in range(100, 700):
        sin1 = 240 * math.sin((x - 100) / 100 * math.pi)
        sin2 = 240 * math.sin((x - 99) / 100 * math.pi)
        pygame.draw.aalines(screen, COLOR5, 0, [(x, 280 + sin1), ((x + 1), 280 + sin2)])

    for x in range(100, 700, 3):
        cos1 = 240 * math.cos((x - 100) / 100 * math.pi)
        cos2 = 240 * math.cos((x - 99) / 100 * math.pi)
        pygame.draw.aalines(screen, COLOR4, 0, [(x, 280 + cos1), ((x + 1), 280 + cos2)])

    for x in range(100, 800, 100):
        if x != 500:
            pygame.draw.line(screen, COLOR1, (x, 10), (x, 550))
        else:
            pygame.draw.line(screen, COLOR1, (x, 10), (x, 40))
            pygame.draw.line(screen, COLOR1, (x, 100), (x, 550))

    for x in range(100, 750, 50):
        pygame.draw.line(screen, COLOR1, (x, 10), (x, 30))
        pygame.draw.line(screen, COLOR1, (x, 550), (x, 530))

    for x in range(100, 710, 25):
        pygame.draw.line(screen, COLOR1, (x, 10), (x, 20))
        pygame.draw.line(screen, COLOR1, (x, 550), (x, 540))

    for y in range(40, 530, 60):
        pygame.draw.line(screen, COLOR1, (70, y), (730, y))

    for y in range(40, 530, 30):
        pygame.draw.line(screen, COLOR1, (70, y), (90, y))
        pygame.draw.line(screen, COLOR1, (710, y), (730, y))

    for y in range(40, 530, 15):
        pygame.draw.line(screen, COLOR1, (70, y), (80, y))
        pygame.draw.line(screen, COLOR1, (720, y), (730, y))


    screen.blit(font.render('sin(x)', 0, COLOR1), (475, 45))
    pygame.draw.line(screen, COLOR5, (530, 60), (570, 60))
    screen.blit(font.render('cos(x)', 0, COLOR1), (475, 75))

    for x in range(530, 570, 7):
        pygame.draw.line(screen, COLOR4, (x, 90), (x + 3, 90))
    screen.blit(font2.render('X', 0, COLOR1), (392, 575))

    for x in range(100, 750, 50):
        screen.blit(font.render(xpi[(x - 100) // 50], 0, COLOR1), (x - 10, 550))
        screen.blit(font.render(xpi_1[(x - 100) // 50], 0, COLOR1), (x - 20, 550))
        screen.blit(font.render(xpi_2[(x - 100) // 50], 0, COLOR1), (x - 10, 570))

    for y in range(40, 530, 60):
        screen.blit(font.render(ypi[(y - 40) // 60], 0, COLOR1), (20, (y - 10)))
    pygame.display.flip()

pygame.quit()