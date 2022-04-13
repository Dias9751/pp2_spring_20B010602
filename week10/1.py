# song 
'''
pygame.mixer.music.load('1.wav')
pygame.mixer.music.play(0) # playing a song once
pygame.mixer.music.load('1.wav')
pygame.mixer.music.play(-1) # playing a song infinitely
pygame.mixer.music.queue("2.wav")
pygame.mixer.music.stop()
'''
import pygame
import os

_sound_library = {}
def play_sound(path):
    global _sound_library
    sound = _sound_library.get(path)
    if sound == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        sound = pygame.mixer.Sound(canonicalized_path)
        _sound_library[path] = sound
    sound.play()

def stop_sound():
    pygame.mixer.music.stop()

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
st = 0
nx = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            st = 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            st = 0
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            nx = 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            nx = -1
    if st == 1 and nx == 0: 
        play_sound('musics/second.mp3')
    elif st == 1 and nx == -1:
        play_sound('musics/first.mp3')
    elif st == 1 and nx == 1:
        play_sound('musics/music.mp3')
    elif st == 0:
        stop_sound()

    screen.fill((255, 255, 255))    
    pygame.display.flip()
pygame.quit()