import pygame
from pygame.locals import *

# --- INITIALIZATION ---
pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Shubh 09")

# Fill background with white
window.fill((255, 255, 255))

# --- PART 1: LINE ---
# Draws a horizontal black line across the middle
pygame.draw.line(window, (0, 0, 0), [100, 300], [500, 300], 5)

# --- PART 2: CIRCLE ---
# Draws a filled green circle in the center (center: 300, 300 | radius: 170)
pygame.draw.circle(window, (0, 255, 0), [300, 300], 170, 0)

# --- PART 3: RECTANGLE ---
# Draws a blue rectangle border inside the circle
pygame.draw.rect(window, (0, 0, 255), [180, 240, 240, 120], 2)

# --- PART 4: POLYGON ---
# Draws a filled red triangle using 3 vertex coordinates
pygame.draw.polygon(window, (255, 0, 0), [[300, 300], [100, 400], [100, 300]])

# --- PART 5: MULTIPLE SHAPES ---
# Draws multiple shapes at once
pygame.draw.circle(window, (0, 255, 0), [300, 300], 170, 0)
pygame.draw.rect(window, (0, 0, 255), [180, 240, 240, 120], 2)

# --- DISPLAY UPDATE & EVENT LOOP ---
pygame.display.update()

