import pygame
from pygame.examples.cursors import image

from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self,username,location,desc,like_count,comments):
        self.username = username
        self.location = location
        self.description = desc
        self.likes_counter = like_count
        self.comments = comments
        pass

    def display(self,display_surface):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        font = pygame.font.Font('chalkduster.ttf', 10)
        username = font.render(self.username, True, BLACK)
        location = font.render(self.location, True, GREY)
        desc = font.render(self.description, True, BLACK)
        likecount = font.render('This post has ' + str(self.likes_counter) + ' likes.', True, BLACK, WHITE)

        # Draw text on the display_surface (don't fill the screen)
        display_surface.blit(username, [USER_NAME_X_POS,USER_NAME_Y_POS])
        display_surface.blit(location, [LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS])
        display_surface.blit(desc, [DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS])
        display_surface.blit(likecount, [LIKE_TEXT_X_POS,LIKE_BUTTON_Y_POS+27])
        pass


    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break



class ImagePost(Post):
    def __init__(self,username,location,desc,like_count,comments,image):
        super().__init__(username,location,desc,like_count,comments)
        self.image = image

    def display(self,display_surface):
        super().display(display_surface)
        img = pygame.image.load(self.image)
        img = pygame.transform.scale(img,(POST_WIDTH,POST_HEIGHT))
        display_surface.blit(img, (POST_X_POS,POST_Y_POS))

class TextPost(Post):
    def __init__(self,username,location,desc,like_count,comments,text,text_color,background_color):
        super().__init__(username,location,desc,like_count,comments)
        self.text = text
        self.text_color = text_color
        self.background_color = background_color

    def display(self,display_surface):
        super().display(display_surface)
        background = pygame.Rect(POST_X_POS,POST_Y_POS,POST_WIDTH,POST_HEIGHT)
        pygame.draw.rect(display_surface,self.background_color, background)
