import pygame
from defend_r import DEF
from invaid_r import INVD
from bullet import Bullet
from pygame import image
import neat
import os
from random import randint
import numpy as np
import pickle

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Invaders")




# The loop will carry on until the user exit the game (e.g. clicks the close button).


# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()



# -------- Main Program Loop -----------

def game(genomes, config):

    number_defenders = 25
    colour_id = []

    for num in range(number_defenders):
        colour_id.append((randint(0, 255), randint(0, 255), randint(0, 255)))

    carryOn = True
    nets = []
    ge = []
    for genome_id, genome in genomes:
        genome.fitness = 0  # start with fitness level of 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        ge.append(genome)

    bullets = []
    for num in range(number_defenders):
        bullets.append("bullets" + str(num))
        bullets[num] = Bullet(colour_id[num], 10, 10)
        bullets[num].rect.x = 400
        bullets[num].rect.y = 500


    tanks = []
    for num in range(number_defenders):
        tanks.append("tanks" + str(num))
        tanks[num] = DEF(colour_id[num], 20, 20)
        tanks[num].rect.x = 350
        tanks[num].rect.y = 400

    big_invaders = []

    speed = []
    for num in range(number_defenders):
        speed.append(3 * np.random.choice([-1,1],size=1))

    # invaderImage = image.load("/home/invicta117/Downloads/invader.jpg")
    for num in range(number_defenders):
        invaders = []
        hight = randint(100, 250)
        position = randint(55, 425)
        for k in range(5):
            invaders.append("invader" + str(k*num))
            invaders[k] = INVD(colour_id[num], 20, 20)
            invaders[k].rect.x = position + (k * 55)
            invaders[k].rect.y = hight

        big_invaders.append(invaders)



    all_sprites_list = pygame.sprite.Group()


    for bullet in bullets:
        all_sprites_list.add(bullet)

    for tank in tanks:
        all_sprites_list.add(tank)

    for invaders in big_invaders:
        for invader in invaders:
            all_sprites_list.add(invader)

    score = []
    for num in range(number_defenders):
        score.append(0)
    high_score = 0
    while carryOn:

        # --- Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                carryOn = False  # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    carryOn = False
                    pygame.quit()
                    quit()
                    break

        screen.fill(BLACK)

        for x, tank in enumerate(tanks):  # give each bird a fitness of 0.1 for each frame it stays alive
            ge[x].fitness += 0.1


        for x, tank in enumerate(tanks):  # give each bird a fitness of 0.1 for each frame it stays alive

            output = nets[x].activate((bullets[x].rect.y, speed[x], (big_invaders[x][0].rect.y - tank.rect.y), (big_invaders[x][1].rect.y - tank.rect.y), (big_invaders[x][2].rect.y - tank.rect.y), (big_invaders[x][3].rect.y - tank.rect.y), (big_invaders[x][4].rect.y - tank.rect.y), (big_invaders[x][0].rect.x - tank.rect.x), (big_invaders[x][1].rect.x - tank.rect.x), (big_invaders[x][2].rect.x - tank.rect.x),(big_invaders[x][3].rect.x - tank.rect.x), (big_invaders[x][4].rect.x - tank.rect.x)))

            if output[0] > 0.6:  # we use a tanh activation function so result will be between -1 and 1. if over 0.5 jump
                tank.moveRight(5)
            elif output[0] < -0.6:
                tank.moveLeft(5)
            else:
                pass

            if output[1] > 0:  # we use a tanh activation function so result will be between -1 and 1. if over 0.5 jump
                if bullets[x].velocity[1] == 0:
                    bullets[x].rect.x = tank.rect.x + 20
                    bullets[x].rect.y = tank.rect.y
                    bullets[x].fire()

        for i in range(len(big_invaders)):
            for invaders in big_invaders[i]:
                if invaders.rect.x >= 650 or invaders.rect.x <= 0:
                    speed[i] = speed[i] * (-1)
                    for invader in big_invaders[i]:
                        invader.rect.y += 50
                    break



        for i in range(len(big_invaders)):
            for invaders in big_invaders[i]:
                if invaders.rect.y >= 250:
                    ge[i].fitness -= 0.01


        for i in range(len(big_invaders)):
            for invaders in big_invaders[i]:
                if invaders.rect.y >= 300:
                    ge[i].fitness -= 0.05

        for i in range(len(big_invaders)):
            for invaders in big_invaders[i]:
                if invaders.rect.y >= 350:
                    ge[i].fitness -= 0.1


        for i in range(len(big_invaders)):
            for invaders in big_invaders[i]:
                if invaders.rect.y >= 400:
                    ge[i].fitness -= 2
                    tanks[i].kill()
                    bullets[i].kill()
                    for invaders in big_invaders[i]:
                        invaders.kill()
                    break

        if all(tank.alive() is False for tank in tanks):
        #if not tanks[0].alive() and not tanks[1].alive():
            score = []
            for num in range(number_defenders):
                score.append(0)
            carryOn = False
            break

        for i in range(len(big_invaders)):
            for invader in big_invaders[i]:
                invader.velocity[0] = speed[i]


        for i in range(len(big_invaders)):
            for invaders in big_invaders[i]:
                if pygame.sprite.collide_mask(bullets[i], invaders):
                    score[i] += 1
                    invaders.rect.x = 295
                    invaders.rect.y = 100
                    bullets[i].notfire()
                    ge[i].fitness += 5

        for bullet in bullets:
            if bullet.rect.y <= 100:
                bullet.notfire()

        # --- Game logic should go here
        all_sprites_list.update()

        # --- Drawing code should go here
        # First, clear the screen to black.



        # Draw the net
        pygame.draw.line(screen, WHITE, [0, 70], [700, 70], 5)

        all_sprites_list.draw(screen)
        # --- Go ahead and update the screen with what we've drawn.

        font = pygame.font.Font(None, 74)
        text = font.render(str(max(score)), 1, WHITE)
        screen.blit(text, (300, 10))

        if max(score) > 200:
            pickle.dump(nets[0],open("best.pickle", "wb"))
            break

        font = pygame.font.Font(None, 74)
        text = font.render("Best Score", 1, WHITE)
        screen.blit(text, (10,10))

        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Once we have exited the main program loop we can stop the game engine:


def run(config_file):
    """
    runs the NEAT algorithm to train a neural network to play flappy bird.
    :param config_file: location of config file
    :return: None
    """
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    #p.add_reporter(neat.Checkpointer(5))

    # Run for up to 50 generations.
    winner = p.run(game, 100)

    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.

    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)