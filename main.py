import pygame

import Post
import constants
from helpers import screen
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK


def main():
    # Set up the game display, clock and headline
    pygame.init()
    display_surface = pygame.display.set_mode((constants.WINDOW_WIDTH,constants.WINDOW_HEIGHT))
    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    post1 = Post.TextPost("Yair", "Israel", "POS DESC POST DESC", 0,[],"TEXTTEXTEXT TEXT", (255,0,0),BLACK)

    # TODO: add a post here

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        post1.display(display_surface)
        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
