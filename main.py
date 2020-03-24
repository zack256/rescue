import pygame
import sys
import colors

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
month_length = 28
current_date = 1

def get_day_of_week(date, month_length):
    return days_of_week[(date - 1) % len(days_of_week)]

def inc_date(date):
    return (date % month_length) + 1

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Rescue")
width, height = pygame.display.get_surface().get_size()
done = False
font = pygame.font.SysFont("Arial", 25)

def draw_text(screen, text, color, pos):
    text_surface = font.render(text, False, color)
    text_rect = text_surface.get_rect(center = pos)
    screen.blit(text_surface, text_rect)

while not done:
    events = pygame.event.get()
    button_width = width * 0.075; button_color = colors.GREEN
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_on_button = mouse_x >= width - button_width and mouse_x <= width and mouse_y >= height - button_width and mouse_y <= height
    for event in events:
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
                break
        elif event.type == pygame.MOUSEBUTTONUP:
            if mouse_on_button:
                current_date = inc_date(current_date)
    if mouse_on_button:
        pressed_tuple = pygame.mouse.get_pressed()
        if pressed_tuple[0]:    # left button pressed
            button_color = colors.EVEN_DARKER_GREEN
        else:
            button_color = colors.DARKER_GREEN
    screen.fill(colors.WHITE)

    pygame.draw.rect(screen, button_color, pygame.Rect(width - button_width, height - button_width, button_width, button_width))
    draw_text(screen, "test", colors.BLACK, (width - button_width / 2, height - button_width / 2))
    draw_text(screen, get_day_of_week(current_date, month_length), colors.BLACK, (width / 2, height / 2))

    pygame.display.flip()

