import pygame
import math

# Set screen dimensions
WIDTH = 800
HEIGHT = 530

# Define a function to load and scale images
def load_image(path):
   
    return pygame.image.load(path)

# Initialize the video system
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game Intro")

# Load and scale the background image
background_image = load_image('background.png')

base_scroll_speed = 0.5
clock = pygame.time.Clock()

# Initialize the mixer module to play music in the background
pygame.mixer.init()
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.play(-1)

running = True
background_offset = 0

# Define dialogue text and font
dialogue_font = pygame.font.Font(None, 50)
dialogue_text = ["OUJEDIPRODUCTIONS", "Brandon Morrow", "Alfonso Fasano", "Kevin Ramirez", "Alex Merlo", "Jacque Miller"]
dialogue_y = HEIGHT

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60)

    scroll_speed = base_scroll_speed * (dt / 8)
    background_offset += scroll_speed
    background_offset %= background_image.get_width()

    num_tiles = int(math.ceil(WIDTH / background_image.get_width())) + 1

    background_surface = pygame.Surface((WIDTH, HEIGHT))

    for y in range(math.ceil(HEIGHT / background_image.get_height())):
        for i in range(num_tiles):
            background_surface.blit(background_image, (i * background_image.get_width() - background_offset, y * background_image.get_height()))

    screen.blit(background_surface, (0, 0))

    # Display dialogue scrolling upwards
    for i, line in enumerate(dialogue_text):
        text = dialogue_font.render(line, True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, dialogue_y + i * 100))
        screen.blit(text, text_rect)

    dialogue_y -= 0.3  # Adjust the scrolling speed of the dialogue

    pygame.display.flip()

pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()