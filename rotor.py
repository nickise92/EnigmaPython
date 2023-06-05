import pygame

class Rotor:

    ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, wiring, notch):
        self.left = self.ALPH
        self.right = wiring
        self.notch = notch

    def forward(self, signal):
        letter = self.right[signal]
        return self.left.find(letter)

    def backward(self, signal):
        letter = self.left[signal]
        return self.right.find(letter)

    def show(self):
        print(self.left)
        print(self.right)

    def rotate(self, n=1, forward=True):
        for i in range(n):
            if forward:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]
            else:
                self.left = self.left[25] + self.left[:25]
                self.right = self.right[25] + self.right[:25]

    def rotate_to_letter(self, letter):
        n = self.ALPH.find(letter)
        self.rotate(n)

    def set_ring(self, n):

        # Rotate the rotor backwards
        self.rotate(n-1, forward=False)

        # Adjust the turnover notch in relationship to the wiring
        n_notch = self.ALPH.find(self.notch)
        self.notch = self.ALPH[(n_notch - n+1) % 26]

    def draw(self, screen, x, y, w, h, font):

        # Draw a rectangle
        r = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, "blue", r, width=2, border_radius=15)

        # letters
        for i in range(26):

            # left hand side
            letter = self.left[i]
            letter = font.render(letter, True, "black")
            text_box = letter.get_rect(center=(x + w/4, y + (i + 1) * h / 27))
            # highlight top letter
            if i == 0:
                letter = font.render(self.left[i], True, "white")
                pygame.draw.rect(screen, "red", text_box, border_radius=5)

            # highlight turnover notch
            if self.left[i] == self.notch:
                letter = font.render(self.notch, True, "#333333")
                pygame.draw.rect(screen, "yellow", text_box, border_radius=5)
            screen.blit(letter, text_box)




            # right hand side
            letter = self.right[i]
            letter = font.render(letter, True, "black")
            text_box = letter.get_rect(center=(x + w*3/4, y + (i + 1) * h / 27))
            screen.blit(letter, text_box)