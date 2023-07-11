"""
This file contains the functions for playing music, there is no need to edit this file. Import this file into your main.py file to use the functions using `import music`.
 _  _  ____  ____   ___    ____  ____    __    ___  _   _    ____  ____  ___  _   _ 
( )/ )(_  _)(  _ \ / __)  (_  _)( ___)  /__\  / __)( )_( )  (_  _)( ___)/ __)( )_( )
 )  (  _)(_  )(_) )\__ \    )(   )__)  /(__)\( (__  ) _ (     )(   )__)( (__  ) _ ( 
(_)\_)(____)(____/ (___/   (__) (____)(__)(__)\___)(_) (_)   (__) (____)\___)(_) (_)
"""

import subprocess
import importlib

def install_dependencies():
    dependencies = ["pygame", "numpy", "time"]
    for dependency in dependencies:
        try:
            importlib.import_module(dependency)
        except ImportError:
            print("[KTT] Installing " + dependency + "...")
            subprocess.check_call(["pip", "install", dependency])

install_dependencies()

import pygame
import numpy as np
import time

def play_note(pitch, duration):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Calculate the frequency of the note
    frequency = 440 * 2 ** ((pitch - 69) / 12)

    # Generate a time axis for the note
    t = np.linspace(0, duration, int(duration * 44100), False)

    # Generate the audio signal for the note (mono)
    audio_mono = np.sin(frequency * 2 * np.pi * t)

    # Duplicate the mono audio signal for both channels
    audio_stereo = np.column_stack((audio_mono, audio_mono))

    # Apply fade-in and fade-out effects
    fade_duration = 0.1  # Adjust fade duration as desired
    fade_samples = int(fade_duration * 44100)
    fade_in = np.linspace(0, 1, fade_samples)
    fade_out = np.linspace(1, 0, fade_samples)
    audio_stereo[:fade_samples, :] *= fade_in[:, np.newaxis]
    audio_stereo[-fade_samples:, :] *= fade_out[:, np.newaxis]

    # Convert the signal to the correct data type
    audio_stereo = (audio_stereo * 32767).astype(np.int16)

    # Create a pygame Sound object from the stereo audio signal
    note_sound = pygame.sndarray.make_sound(audio_stereo)

    # Play the note
    note_sound.play()

    # Wait until the note is done playing
    time.sleep(duration)

    # Clean up resources
    note_sound.stop()
    pygame.mixer.quit()

happy_birthday = "60,2;60,2;67,2;67,2;69,2;69,2;67,4;65,2;65,2;64,2;64,2;62,2;62,2;60,4;67,2;67,2;65,2;65,2;64,2;64,2;62,4;67,2;67,2;65,2;65,2;64,2;64,2;62,4;60,2;60,2;67,2;67,2;69,2;69,2;67,4;65,2;65,2;64,2;64,2;62,2;62,2;60,4"

twinkle_twinkle = "74,0.5;74,0.5;76,1;74,1;79,1;78,2;74,0.5;74,0.5;76,1;74,1;81,1;79,2;74,0.5;74,0.5;86,1;82,1;79,1;78,1;76,1;81,1;79,1;78,1;74,1.5"

jingle_bells = "64,1;64,1;64,2;64,1;64,1;64,2;64,1;66,1;61,1;64,2;64,1;64,1;64,2;64,1;64,1;64,2;64,1;66,1;61,1;64,2;64,1;64,1;64,2;64,1;69,1;67,1;64,2;62,1;62,1;62,1;62,1;64,1;64,1;64,1;64,1;69,1;67,1;64,2;62,1;62,1;62,1;62,1;64,1;64,1;64,2;64,1;64,1;64,2;64,1;66,1;61,1;64,2;64,1;64,1;64,2;64,1;64,1;64,2;64,1;66,1;61,1;64,2"

happy_birthday_key = [
    [74, 0.5], [74, 0.5], [76, 1], [74, 1], [79, 1], [78, 2],
    [74, 0.5], [74, 0.5], [76, 1], [74, 1], [81, 1], [79, 2],
    [74, 0.5], [74, 0.5], [86, 1], [82, 1], [79, 1], [78, 1],
    [76, 1], [81, 1], [79, 1], [78, 1], [74, 1.5]
]

twinkle_twinkle_key = [
    [60, 2], [60, 2], [67, 2], [67, 2], [69, 2], [69, 2], [67, 4],
    [65, 2], [65, 2], [64, 2], [64, 2], [62, 2], [62, 2], [60, 4],
    [67, 2], [67, 2], [65, 2], [65, 2], [64, 2], [64, 2], [62, 4],
    [67, 2], [67, 2], [65, 2], [65, 2], [64, 2], [64, 2], [62, 4],
    [60, 2], [60, 2], [67, 2], [67, 2], [69, 2], [69, 2], [67, 4],
    [65, 2], [65, 2], [64, 2], [64, 2], [62, 2], [62, 2], [60, 4]
]

jingle_bells_key = [
    [64, 1], [64, 1], [64, 2], [64, 1], [64, 1], [64, 2], [64, 1], [66, 1], [61, 1], [64, 2],
    [64, 1], [64, 1], [64, 2], [64, 1], [64, 1], [64, 2], [64, 1], [66, 1], [61, 1], [64, 2],
    [64, 1], [64, 1], [64, 2], [64, 1], [69, 1], [67, 1], [64, 2], [62, 1], [62, 1], [62, 1], [62, 1],
    [64, 1], [64, 1], [64, 1], [64, 1], [69, 1], [67, 1], [64, 2], [62, 1], [62, 1], [62, 1], [62, 1],
    [64, 1], [64, 1], [64, 2], [64, 1], [64, 1], [64, 2], [64, 1], [66, 1], [61, 1], [64, 2],
    [64, 1], [64, 1], [64, 2], [64, 1], [64, 1], [64, 2], [64, 1], [66, 1], [61, 1], [64, 2]
]