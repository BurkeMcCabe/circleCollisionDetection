import pygame
import math
pygame.init()

print("Hello There!")

r = 70

window_width = 500
window_height = 500

center_screen = (int(window_width/2), int(window_height/2))

bg_color = (100, 100, 100)
circle_color = (255, 255, 100)

mouse = pygame.mouse.get_pos()

screen = pygame.display.set_mode((window_width, window_height))

def point_in_circle(r, x1, y1, x2, y2):
    if r >= math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)):
        return True
    return False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    mouse = pygame.mouse.get_pos()
    
    if point_in_circle(r, center_screen[0], center_screen[1], mouse[0], mouse[1]):
        circle_color = (100, 255, 255)
    else:
        circle_color = (255, 255, 100)
    
    screen.fill(bg_color)
    pygame.draw.circle(screen, circle_color, center_screen, r)
    pygame.display.flip()

pygame.quit()
