import pygame


class SoundPlayer():

    def __init__(self):
        # Load the .wav file
        self.sound_dot = "dot.wav"
        self.sound_dash = "dash.wav"

    def play_sound(self, morse_code):

        for char in morse_code:

            if char == '.':
                pygame.mixer.init()
                pygame.mixer.music.load(self.sound_dot)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(6)
            elif char == '-':
                pygame.mixer.init()
                pygame.mixer.music.load(self.sound_dash)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(6)
            else:
                pygame.time.wait(60)
