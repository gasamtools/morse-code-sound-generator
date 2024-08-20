from sound_generator import SoundGenerator
from sound_player import SoundPlayer
from morse_data import morse_data
import os

# File path
file_path = "dot.wav"
if not os.path.isfile(file_path):
    create_sound = SoundGenerator()
    create_sound.create_sound(create_sound.dot_duration, 'dot.wav')
    create_sound.create_sound(create_sound.dash_duration, 'dash.wav')


text = input('Input text\n').upper().strip()

morse_code = ''
for char in text:
    morse_code += morse_data[char]
    morse_code += '   '

print(morse_code)

play_dot_sound = SoundPlayer()
play_dot_sound.play_sound(morse_code=morse_code)