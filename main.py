import pygame
from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from draw import draw

# Setup pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma simulator")

# Create fonts
MONO = pygame.font.SysFont("Fira Code", 22)
BOLD = pygame.font.SysFont("Fira Code", 22, bold=True)

# Global Variables
WIDTH = 1600
HEIGHT = 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
MARGINS = {"top":200, "bottom":50, "left":100, "right":100}
GAP = 100

INPUT = ""
OUTPUT = ""
PATH = []


# Rotors
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
# Reflectors
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
# Keyboard and Plugboard
kb = Keyboard()
pb = Plugboard(["AR", "GK", "OX"])
# Define Enigma
enigma = Enigma(B, I, II, III, pb, kb)
# Set rings
enigma.set_rings((1, 1, 1))
# Set key
enigma.set_key("CAT")

animating = True
while animating:

    # background color
    SCREEN.fill("#ebebeb")

    #text input
    text = MONO.render(INPUT, True, "black")
    text_box = text.get_rect(center = (WIDTH/2, MARGINS["top"]/2))
    SCREEN.blit(text, text_box)

    #text output
    text = BOLD.render(OUTPUT, True, "black")
    text_box = text.get_rect(center=(WIDTH/2, MARGINS["top"]/2+20))
    SCREEN.blit(text, text_box)

    # draw enigma machine
    draw(enigma, PATH, SCREEN, WIDTH, HEIGHT, MARGINS, GAP, BOLD)

    # update screen
    pygame.display.flip()

    # track user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                l = len(INPUT)
                if INPUT[l-1] == ' ':
                    INPUT = INPUT[:-1]
                    OUTPUT = OUTPUT[:-1]
                else:
                    INPUT = INPUT[:-1]
                    enigma.r3.rotate(1, forward=False) # reset the machine at previous state if a letter has been deleted
                    OUTPUT = OUTPUT[:-1]
            elif event.key == pygame.K_SPACE:
                INPUT = INPUT + " "
                OUTPUT = OUTPUT + " "
            else:
                key = event.unicode
                if key in "abcdefghijklmnopqrstuvwxyz":
                    letter = key.upper()
                    INPUT = INPUT + letter
                    # Enigma encription
                    PATH, cipher = enigma.encipher(letter)
                    OUTPUT = OUTPUT + cipher