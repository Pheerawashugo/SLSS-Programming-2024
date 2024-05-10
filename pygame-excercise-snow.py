# pygame-exercise-snowscape.py

import random
import pygame as pg

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 1280
HEIGHT = 720
TITLE = "Snowscape"

NUM_SNOW = 100


class Snow(pg.sprite.Sprite):
    def __init__(self, width: int):
        """
        Params:
            width: width of snow in px
        """
        super().__init__()

        self.image = pg.Surface((width, width))

        # Found by Duncan, he says Yippee!
        pg.draw.circle(self.image, WHITE, (width // 2, width // 2), width // 2)

        self.rect = self.image.get_rect()

        # Initial coords, choose random x-coord
        self.rect.centerx = random.randrange(0, WIDTH + 1)
        self.rect.centery = random.randrange(0, HEIGHT)

        # Velocity set randomly
        self.vel_x = random.choice([0])
        self.vel_y = random.choice([2])

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        # TODO: When it reaches past the bottom, respawn at the top
        if self.rect.centery > 720:
            self.rect.centerx = random.randrange(0, WIDTH + 1)
            self.rect.centery = -1
            self.vel_y = random.choice([1.5,2,2.5,3,3.5,4])



def main():
    pg.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pg.display.set_mode(size)
    pg.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pg.time.Clock()

    # Create a snow sprites group
    snow_sprites = pg.sprite.Group()

    i=1
    # Create more snow
    for _ in range(100):
        snow_sprites.add(Snow(10))



    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # ----- LOGIC
        snow_sprites.update()

        # ----- RENDER
        screen.fill(BLACK)

        # Draw all the sprite groups
        snow_sprites.draw(screen)

        # ----- UPDATE DISPLAY
        pg.display.flip()
        clock.tick(60)

    pg.quit()


def random_coords():
    x, y = (random.randrange(0, WIDTH), random.randrange(0, HEIGHT))
    return x, y


if __name__ == "__main__":
    main()