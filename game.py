# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()

w = 1280
h = 720

screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
running = True

# BUILD THE BACKGROUND WITH TILES
background = pygame.Surface((w,h))
background.fill((255,0,0))

# load tile images to variables
water = pygame.image.load('assets/fishTile_089.png')
sand1 = pygame.image.load('assets/fishTile_001.png')
sand2 = pygame.image.load('assets/fishTile_002.png')
sand3 = pygame.image.load('assets/fishTile_003.png')
sand4 = pygame.image.load('assets/fishTile_004.png')
sand5 = pygame.image.load('assets/fishTile_005.png')
sand6 = pygame.image.load('assets/fishTile_006.png')
sand7 = pygame.image.load('assets/fishTile_007.png')
sand8 = pygame.image.load('assets/fishTile_008.png')
sand9 = pygame.image.load('assets/fishTile_009.png')

# get to the tile_size
TILE_SIZE = water.get_width()

# loop over x direction
for x in range(0,w,TILE_SIZE):
    # loop over y direction
    for y in range(0,w, TILE_SIZE):
        # blit the tile to our BG
        background.blit(water, (x,y))
        if y>(5*TILE_SIZE):
            background.blit(sand1, (x,y))
        elif y>(4*TILE_SIZE) and x==0:
            background.blit(sand9, (x,y))
        elif y>(4*TILE_SIZE) and x==TILE_SIZE:
            background.blit(sand8, (x,y))
        elif y>(4*TILE_SIZE) and x==(2*TILE_SIZE):
            background.blit(sand6, (x,y))
        elif y>(4*TILE_SIZE) and x==(3*TILE_SIZE):
            background.blit(sand7, (x,y))
        elif y>(4*TILE_SIZE) and x==(4*TILE_SIZE):
            background.blit(sand8, (x,y))
        elif y>(4*TILE_SIZE) and x==(5*TILE_SIZE):
            background.blit(sand7, (x,y))
        elif y>(4*TILE_SIZE) and x==(6*TILE_SIZE):
            background.blit(sand8, (x,y))
        elif y>(4*TILE_SIZE) and x==(7*TILE_SIZE):
            background.blit(sand9, (x,y))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit the background to the screen
    screen.blit(background,(0,0))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()