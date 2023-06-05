import pygame

class Plugboard:

    ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, pairs):
        self.left = self.ALPH
        self.right = self.ALPH

        for pair in pairs:
            A = pair[0]
            B = pair[1]
            pos_A = self.left.find(A)
            pos_B = self.left.find(B)
            self.left = self.left[:pos_A] + B + self.left[pos_A+1:]
            self.left = self.left[:pos_B] + A + self.left[pos_B+1:]

    def forward(self, signal):
        letter = self.right[signal]
        return self.left.find(letter)

    def backward(self, signal):
        letter = self.left[signal]
        return self.right.find(letter)

    def draw(self, screen, x, y, w, h, font):

        # Draw a rectangle
        r = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, "cyan", r, width=2, border_radius=15)

        # letters
        for i in range(26):

            # left hand side
            letter = self.left[i]
            letter = font.render(letter, True, "black")
            text_box = letter.get_rect(center=(x + w/4, y + (i + 1) * h / 27))
            screen.blit(letter, text_box)

            # right hand side
            letter = self.right[i]
            letter = font.render(letter, True, "black")
            text_box = letter.get_rect(center=(x + w*3/4, y + (i + 1) * h / 27))
            screen.blit(letter, text_box)