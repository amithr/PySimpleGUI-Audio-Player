import os
from pygame import mixer
mixer.init()

def get_files_inside_directory_not_recursive(directory):
    directories = []
    for (root, dirs, files) in os.walk(directory):
        for file in files:
            directories.append(root + os.sep + file)

    return directories


def get_sound_object(sound_path):
    return mixer.music.Sound(sound_path)

def load_sound(sound_path):
    mixer.music.load(sound_path)

def play_sound():
    mixer.music.play()

def pause_sound():
    mixer.music.pause()

def resume_sound():
    mixer.music.unpause()

def stop_sound():
    mixer.music.stop()


def is_sound_playing():
    if mixer.music.get_busy() == True:
        return True
    return False