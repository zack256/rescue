import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Rescue")
width, height = pygame.display.get_surface().get_size()
done = False
while not done:
    events = pygame.event.get()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
                break
    screen.fill((255, 255, 255))
    pygame.display.flip()

