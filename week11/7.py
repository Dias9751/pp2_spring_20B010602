#TASK 3
from curses.textpad import rectangle
import pygame
from pygame.locals import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    rectangle_mode = False
    circle_mode = False
    rectangle_start = False
    rect_start_x = 0
    rect_start_y = 0
    rect_finish_x = 0
    rect_finish_y = 0
    pos1 =()
    pos2 =()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []

    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                    rectangle_mode = False
                    circle_mode = False
                elif event.key == pygame.K_g:
                    mode = 'green'
                    rectangle_mode = False
                    circle_mode = False
                elif event.key == pygame.K_b:
                    mode = 'blue'
                    rectangle_mode = False
                    circle_mode = False
                elif event.key == pygame.K_m:
                    rectangle_mode = True
                    circle_mode = False
                elif event.key == pygame.K_n:
                    circle_mode = True
                    rectangle_mode = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rectangle_mode == False and circle_mode == False:
                    if event.button == 1: # left click grows radius
                        radius = min(200, radius + 1)
                    elif event.button == 3: # right click shrinks radius
                        radius = max(1, radius - 1)
                elif rectangle_mode == True and circle_mode == False:
                    position = event.pos
                    rect_start_x, rect_start_y = position
                    print ("START", rect_start_x, rect_start_y)
                    
                    ##if rectangle_start == False:
                    #    rectangle_start = True
                    #else:
                    #    rectangle_start = False
                elif circle_mode == True and rectangle_mode == False:
                    position = event.pos
                    cir_start_x, cir_start_y = position
                    print ("START", cir_start_x, cir_start_y)
                        
            elif event.type == pygame.MOUSEBUTTONUP and rectangle_mode == True:
                position = event.pos
                rect_finish_x, rect_finish_y = position
                """print ("FINISH", finish_x, finish_y)
                print (pos1, pos2)"""
                pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(rect_start_x, rect_start_y, rect_finish_x-rect_start_x, rect_finish_y-rect_start_y))
                pygame.display.flip()

            elif event.type == pygame.MOUSEBUTTONUP and circle_mode == True:
                position = event.pos
                rect_finish_x, rect_finish_y = position
                """print ("FINISH", rect_finish_x, rect_finish_y)
                print (pos1, pos2)"""
                pygame.draw.ellipse(screen, (0, 128, 255), pygame.Rect(cir_start_x, cir_start_y, rect_finish_x-cir_start_x, rect_finish_y-cir_start_y))
                # триугольник
                """pygame.draw.lines(screen, (255,255,255), True,
                  [[cir_start_x, cir_start_y], [rect_finish_x, rect_finish_y],
                   [cir_start_x, rect_finish_y]], 2)"""
                   # триугольник
                """pygame.draw.lines(screen, (255,255,255), True,
                  [[cir_start_x, cir_start_y], [rect_finish_x, rect_finish_y],
                   [cir_start_x+70, rect_finish_y]], 2)"""
                   # romb
                """pygame.draw.polygon(screen, (255,255,255),
                  [[(cir_start_x+rect_finish_x)/2, cir_start_y], [cir_start_x - 50, (cir_start_y+rect_finish_y)/2],
                   [(cir_start_x+rect_finish_x)/2, rect_finish_y], [rect_finish_x+50, (cir_start_y+rect_finish_y)/2]])"""
                """pygame.draw.polygon(screen, (255,255,255), 
                    [(200, 200), (250, 250), (200, 300), (150, 250)])
                   pygame.draw.aalines(sc, WHITE, True, 
                    [[250, 110], [280, 150], 
                     [190, 190], [130, 130]])"""
                    
                pygame.display.flip()

            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        # draw all points
        if (rectangle_mode == False and circle_mode == False):
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
                i += 1
            
            pygame.display.flip()
            
            clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()