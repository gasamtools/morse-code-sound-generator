import wave
import numpy as np


class SoundGenerator():

    def __init__(self):
        # Parameters
        self.frequency = 800  # Frequency in Hz
        self.dot_duration = 0.06  # Duration in seconds
        self.dash_duration = 0.18  # Duration in seconds
        self.sample_rate = 44100  # Samples per second
        self.amplitude = 32767  # Amplitude of the wave (max for 16-bit audio)

    def create_sound(self, duration, name):
        # Generate the sound wave
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
        waveform = self.amplitude * np.sin(2 * np.pi * self.frequency * t)

        # Convert waveform to 16-bit data
        waveform = waveform.astype(np.int16)

        # Create a .wav file
        with wave.open(name, 'w') as wav_file:
            wav_file.setnchannels(1)  # Mono
            wav_file.setsampwidth(2)  # 2 bytes = 16 bits
            wav_file.setframerate(self.sample_rate)
            wav_file.writeframes(waveform.tobytes())

        print(f"{name} sound created successfully!")

