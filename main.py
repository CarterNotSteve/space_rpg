import pygame, sys, random

playerlevel = 1
exp = 0


def kill():
    global exp
    exp = exp + 100
    if exp == 1000:
        global playerlevel
        playerlevel = playerlevel + 1

def print_exp():
    print("Player level %d (%d exp)" % (playerlevel, exp))

if exp == 1000:
    playerlevel = playerlevel + 1



