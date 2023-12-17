import pygame
import os
import random
import time
from pygame import mixer

# Draw the buttons Lea set the coordenates in the main.py in the screen
def draw_buttons(buttons, window, color):
    for button in buttons:
        pygame.draw.rect(window, color, button)

# Load inside the game all the piano sound in the folder
def pick_sound():
    # Create an empty list to store the piano sounds
    piano_sounds = []

    # Path to the "piano sound" folder
    folder_path = "piano_sounds"

    # Loop through all the files in the folder
    for file_name in os.listdir(folder_path):
        # Check if the the file is a piano sound with .mid extension
        if file_name.endswith(".mid"):
            # Add the file to the list
            sound_path = os.path.join(folder_path, file_name)
            # Append is add the piano sound to the list of piano sounds
            piano_sounds.append(sound_path)

    # Assure that the list is in the correct order
    piano_sounds = sorted(piano_sounds)

    return piano_sounds

# Create a List of 12 buttons, where in the beginning all buttons are False.
# When we have a sound played, it also set the correct button to True.
def correct_values():
    # Create an empty list to store the Buttons
    correct_values = []

    for value in range(0, 12):
        #Set all the buttons to False
        correct_values.append(False)
    
    return correct_values


# Play the piano sound
def play_sounds(piano_sounds, correct_button):
    # Pick a random base note
    # first_note_number = random.randint(0, len(piano_sounds) -1)
    first_note_number = 0 # This line makes C3 all the base note 

    # get the base from the list of piano sounds
    first_note = piano_sounds[first_note_number]

    # Play the base note
    mixer.music.load(first_note)
    mixer.music.set_volume(1)
    mixer.music.play()

    # wait for 2 secounds
    time.sleep(2)

    # pick a random second note
    # interval = random.randint(1, 12)

    # LEA, YOU SHOULD CHANGE THE INTERVAL!!!!!!  

    interval = 11 # This set how the base note will grow

    # set the correct button to True
    correct_button[interval -1] = True # Set the correct button to True

    second_note_number = first_note_number + interval # Add the interval to the base note

    second_note = piano_sounds[second_note_number] # Get the second note from the list of piano sounds


    # Play the second note
    mixer.music.load(second_note)
    mixer.music.set_volume(1)
    mixer.music.play()

    # return to the game the correct button (The button that gives the correct answer)
    return correct_button

# Change the background according to the button pressed
def draw_result(window, background_win_lose, background_sound):
    # If the correct button was pressed then the main game will say to use thumbsup
    # Otherwise, it will say to use thumbsdown
    window.blit(background_win_lose, (0,0))
    pygame.display.flip()
    
    # Wait 1 secound for the user to know the result
    time.sleep(1)

    # Change the background to sound playing background
    window.blit(background_sound, (0,0))
    pygame.display.flip()

    time.sleep(1)

