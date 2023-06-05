import pygame

class Keyboard():

    ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def forward(self, letter):
        return self.ALPH.find(letter)

    def backward(self, signal):
        return self.ALPH[signal]

    def draw(self, screen, x, y, w, h, font):

        # Draw a rectangle
        r = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, "magenta", r, width=2, border_radius=15)

        # letters
        for i in range(26):
            letter = self.ALPH[i]
            letter = font.render(letter, True, "black")
            text_box = letter.get_rect(center = (x+w/2, y+(i+1)*h/27))
            screen.blit(letter, text_box)