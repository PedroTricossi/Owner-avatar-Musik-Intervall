
# Importing the libraries used in the game
import pygame
import time
import utils
from pygame import mixer
from pygame.font import Font
 
# Load the background image
background_start = pygame.image.load("background/start.jpg")
background_sound = pygame.image.load("background/sound.jpg")
background_thumbsup = pygame.image.load("background/thumbsup.jpg")
background_thumbsdown = pygame.image.load("background/thumbsdown.jpg")
 
# Load the sounds (mid files)
piano_sounds = utils.pick_sound()
 
# create a button for game (k2, ..., oktave)
correct_button = utils.correct_values()
 
# creating the game screen
window_surf  = pygame.display.set_mode((800, 550)) # width, height (px)
pygame.display.set_caption("Klicke auf das richtige Intervall.") # Name of the game
 
# creating the buttons
# x, y, width, height (px)
button_start = pygame.Rect(305, 232, 190, 190)
button_k2 = pygame.Rect(453, 127, 70, 70)
button_g2 = pygame.Rect(516, 194, 70, 70)
button_k3 = pygame.Rect(544, 277, 70, 70)
button_g3 = pygame.Rect(512, 366, 70, 70)
button_r4 = pygame.Rect(448, 428, 70, 70)
button_tr4 = pygame.Rect(360, 458, 70, 70)
button_r5 = pygame.Rect(271, 434, 70, 70)
button_k6 = pygame.Rect(210, 372, 70, 70)
button_g6 = pygame.Rect(195, 285, 70, 70)
button_k7 = pygame.Rect(213, 198, 70, 70)
button_g7 = pygame.Rect(269, 127, 70, 70)
button_o8 = pygame.Rect(361, 101, 70, 70)
 
# creating a list of buttons in the order of the ...
buttons = [button_start, button_k2, button_g2, button_k3, button_g3, button_r4, button_tr4, button_r5, button_k6, button_g6, button_k7, button_g7, button_o8]
 
# Set the color of the buttons (transparent)
button_color = pygame.Color(255, 255, 255, 0) # last value is the alpha value (0-128) -> 0 = transparent, 128 = opaque
 
# Initialize Pygame
pygame.init()
mixer.init()
 
# Draw the buttons in the screen
utils.draw_buttons(buttons, window_surf, button_color)
 
window_surf.blit(background_start, (0,0))
 
points = 0
games_played = 0
 
# Erfolgsquote
font = Font(None, 28)

 
# Main loop
running = True
while running:
    quote = round((points / games_played if games_played > 0 else 1) * 100, 1)
    text = str(quote)
    text_surface = font.render(text[:-2], True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (130, 535)
    window_surf.blit(text_surface, text_rect)
    #print(f"points{points} / games_played {games_played}")
 
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the start button is clicked and play the sound
            if buttons[0].collidepoint(event.pos):
                # when start button is clicked
                window_surf.blit(background_sound, (0,0))
                window_surf.blit(text_surface, text_rect)
                pygame.display.flip()
 
                time.sleep(1)
 
                correct_button = utils.play_sounds(piano_sounds, correct_button)
 
            # Check if the pressed button is k2, then we check if k2 was the correct button
            # If it was the correct button, we draw the thumbsup image, otherwise the thumbsdown image
            # Then play the sound
            elif (buttons[1].collidepoint(event.pos)):
                if correct_button[0]:
                    window_surf.blit(text_surface, text_rect)
                    utils.draw_result(window_surf, background_thumbsup, background_sound)
                    correct_button[0] = False
                    window_surf.blit(text_surface, text_rect)
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound)
                    correct_button[0] = False
                    window_surf.blit(text_surface, text_rect)
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
           
            # Check if the pressed button is g2, then we check if g2 was the correct button
            # If it was the correct button, we draw the thumbsup image, otherwise the thumbsdown image
            # Then play the sound
            elif (buttons[2].collidepoint(event.pos)):
                if correct_button[1]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound)
                    correct_button[1] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound)
                    correct_button[1] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
 
           
            elif (buttons[3].collidepoint(event.pos)):
                if correct_button[2]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound)
                    correct_button[2] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound)
                    correct_button[2] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
 
            elif (buttons[4].collidepoint(event.pos)):
                if correct_button[3]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound)
                    correct_button[3] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound)
                    correct_button[3] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
 
            elif (buttons[5].collidepoint(event.pos)):
                if correct_button[4]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound)
                    correct_button[4] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound)
                    correct_button[4] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
 
            elif (buttons[6].collidepoint(event.pos)):
                if correct_button[5]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound)
                    correct_button[5] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound)
                    correct_button[5] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
 
            elif (buttons[7].collidepoint(event.pos)):
                if correct_button[6]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound)
                    correct_button[6] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound)
                    correct_button[6] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
 
            elif (buttons[8].collidepoint(event.pos)):
                if correct_button[7]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound)
                    correct_button[7] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound)
                    correct_button[7] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
           
            elif (buttons[9].collidepoint(event.pos)):
                if correct_button[8]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound)
                    correct_button[8] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound)
                    correct_button[8] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
           
            elif (buttons[10].collidepoint(event.pos)):
                if correct_button[9]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound)
                    correct_button[9] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound)
                    correct_button[9] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
           
            elif (buttons[11].collidepoint(event.pos)):
                if correct_button[10]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound)
                    correct_button[10] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound)
                    correct_button[10] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
           
            elif (buttons[12].collidepoint(event.pos)):
                if correct_button[11]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound)
                    correct_button[11] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound)
                    correct_button[11] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
           
 
    # Update the display
    pygame.display.flip()
 
# Quit Pygame
pygame.quit()