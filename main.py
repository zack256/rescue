import pygame
import sys
import colors

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
month_length = 28
current_date = 1

def get_day_of_week(date, month_length):
    return days_of_week[(date - 1) % len(days_of_week)]

def inc_date():
    global current_date
    current_date = (current_date % month_length) + 1
def dec_date():
    global current_date
    current_date = current_date - 1 if current_date != 1 else month_length

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

class Button:
    def __init__(self, pos, dims, colors, text):
        self.pos = pos
        self.dims = dims
        self.colors = colors    # list of 3 colors : [passive, hover, clicked]
        self.color = self.colors[0]
        self.text = text
    def get_center(self):
        return self.pos[0] + self.dims[0] / 2, self.pos[1] + self.dims[1] / 2
    def mouse_is_over(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos; x, y = self.pos; w, h = self.dims
        return mouse_x >= x and mouse_x <= x + w and mouse_y >= y and mouse_y <= y + h
    def change_color(self, idx):
        self.color = self.colors[idx]
    def display(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(*self.pos, *self.dims))
        draw_text(screen, self.text, colors.BLACK, self.get_center())

button_width = width * 0.075
next_day_button = Button(pos = (width - button_width, height - button_width), dims = (button_width, button_width), colors = [colors.GREEN, colors.DARKER_GREEN, colors.EVEN_DARKER_GREEN], text = "Next Day")
prev_day_button = Button(pos = (width - 2 * button_width, height - button_width), dims = (button_width, button_width), colors = [colors.SKY, colors.DARK_SKY, colors.DARKER_SKY], text = "Previous Day")
buttons = {"nd" : next_day_button, "pd" : prev_day_button}

def draw_buttons(screen):
    for button in buttons:
        buttons[button].display(screen)

def get_button_under_mouse(buttons, mouse_pos):
    for button in buttons:
        if button.mouse_is_over(mouse_pos):
            return button
    return None

def button_clicked(button_key):
    if button_key == "nd":
        inc_date()
    elif button_key == "pd":
        dec_date()

while not done:
    events = pygame.event.get()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    pressed_tuple = pygame.mouse.get_pressed()
    mouse_is_pressed = pressed_tuple[0] # left btn
    mouse_over_button_key = ""
    for button_key in buttons:
        button = buttons[button_key]
        if button.mouse_is_over((mouse_x, mouse_y)):
            mouse_over_button_key = button_key
            if mouse_is_pressed:
                button.change_color(2)
            else:
                button.change_color(1)
        else:
            button.change_color(0)
    for event in events:
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
                break
        elif event.type == pygame.MOUSEBUTTONUP:
            if mouse_over_button_key:
                button_clicked(mouse_over_button_key)
    screen.fill(colors.WHITE)
    draw_buttons(screen)
    #draw_text(screen, "test", colors.BLACK, (width - button_width / 2, height - button_width / 2))
    draw_text(screen, get_day_of_week(current_date, month_length), colors.BLACK, (width / 2, height / 2))

    pygame.display.flip()

