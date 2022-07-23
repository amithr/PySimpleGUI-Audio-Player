import PySimpleGUI as sg
from pygame import mixer, time
import pygame

layout= [
    [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="-SOUND_PATH-")],
    [sg.Text(size=(12,1), key='-STATUS-')],
    [
        sg.Button('Play', pad=(10, 0), key='-PLAY-'),
        sg.Button('Pause', pad=(10, 0), key='-PAUSE-'),
        sg.Button('Stop', pad=(10, 0), key='-STOP-'),
        sg.Slider(range=(0, 100), 
                orientation='h', size=(50, 20), enable_events=True, key = '-VOLUME-', default_value= 100)
    ]
]

audio_player_window = sg.Window('Audio Player', layout, finalize=True)

mixer.init()
is_playing = False

current_position = 0

while True:
    event, values = audio_player_window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break

    sound_path = values["-SOUND_PATH-"]
    if not sound_path:
        sg.Popup("No song specificed.")
        continue
    song = mixer.music.load(sound_path)

    if event == '-PLAY-':
        audio_player_window['-STATUS-'].update('Playing')
        is_playing = True
        print(mixer.music.play())
    elif event == '-PAUSE-': 
        if not is_playing:
            audio_player_window['-STATUS-'].update('Playing')
            print(mixer.music.get_busy())
            print(mixer.music.get_pos())
            # For some unknown reason mixer.music.unpause doesn't work
            mixer.music.play(0, current_position)
            is_playing=True
        else:
            audio_player_window['-STATUS-'].update('Paused')
            print(mixer.music.get_busy())
            mixer.music.pause()
            position = mixer.music.get_pos()
            current_position = current_position + position/1000.0
            is_playing = False
    elif event == '-STOP-':
        audio_player_window['-STATUS-'].update('Stopped')
        mixer.music.stop()
        is_playing = False
    elif event == '-VOLUME-':
        volume = values['-VOLUME-']
        print(volume/100)
        mixer.music.set_volume(float(volume/100))

audio_player_window.close()







