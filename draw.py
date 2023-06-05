import pygame

def draw(enigma, path, screen, width, height, margins, gap, font):

    w = (width - margins["left"] - margins["right"] - 5 * gap) / 6
    h = (height - margins["top"] - margins["bottom"])

    # Path coordinates
    y_path = [margins["top"]+(signal+1)*h/27 for signal in path]
    x_path = [width-margins["right"]-w/2] # keyboard
    for i in [4, 3, 2, 1,0]: # forward pass
        x_path.append(margins["left"]+i*(w+gap)+w*3/4)
        x_path.append(margins["left"]+i*(w+gap)+w*1/4)
    x_path.append(margins["left"]+w*3/4) #reflector
    for i in [1, 2, 3, 4]: #backward pass
        x_path.append(margins["left"]+i*(w+gap)+w*1/4)
        x_path.append(margins["left"]+i*(w+gap)+w*3/4)
    x_path.append(width - margins["right"]-w/2)  # lampboard
    # draw the path
    if len(path) > 0:
        for i in range(1,21):
            if i < 10:
                color = "#43aa8b"
            elif i < 12:
                color = "#f9c74f"
            else:
                color = "#e63946"
            start = (x_path[i-1], y_path[i-1])
            end = (x_path[i], y_path[i])
            pygame.draw.line(screen, color, start, end, width=5)

    # Coordinates
    x = margins["left"]
    y = margins["top"]

    # Enigma components
    for component in [enigma.re, enigma.r1, enigma.r2, enigma.r3, enigma.pb, enigma.kb]:
        component.draw(screen, x, y, w, h, font)
        x += w + gap

    # add names
    names = ["Reflector", "Left", "Middle", "Right", "Plugboard", "Key/Lamp"]
    y = margins["top"] * 0.90
    for i in range(6):
        x = margins["left"] + w/2 + i*(w+gap)
        title = font.render(names[i], True, "black")
        text_box = title.get_rect(center=(x, y))
        screen.blit(title, text_box)

