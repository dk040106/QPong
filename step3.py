"""

Step 3: scene and level

"""

import pygame

from utils.ball import Ball
from utils.scene import Scene
from utils.level import Level

def main():
    
    # initialize the pygame module
    pygame.init()

    # set screen size
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('QPong')

    # clock for timing
    clock = pygame.time.Clock()
    old_clock = pygame.time.get_ticks()
    clock.tick(60) # set maximum frame rate

    scene = Scene()
    level = Level()

    # define ball
    ball = Ball()
    balls = pygame.sprite.Group()   # sprite group type is needed for sprite collide function in pygame
    balls.add(ball)

    level.setup(scene, ball)

    # Put all moving sprites a group so that they can be drawn together
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(ball)
    moving_sprites.add(level.left_paddle)
    moving_sprites.add(level.right_paddle)

    running = True
    while running:
        for event in pygame.event.get():
            # exit main loop when you click the 'X' button of the window
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0,0,0))

        ball.update()  # update ball position
        scene.dashed_line(screen, ball)  # draw dashed line in the middle of the screen
        scene.score(screen, ball)   # print score

        level.right_statevector.draw(screen)  # draw right paddle together with statevector grid
        level.circuit_grid.draw(screen)  # draw circuit grid
        moving_sprites.draw(screen)  # draw moving sprites

        # check ball location and decide what to do
        ball.action()

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()