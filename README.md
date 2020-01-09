# NEAT Space Invaders
## Overview
The following details an implementation of the NEAT algorithm to solve a simplifed version of the classic Space Invaders arcade game. This project aimed to use a neural network to get a score of 1000 corresponding to 1000 invaders destroyed in one game. Invaders can alteratevly win the game by destroy the defending space craft by reaching the bottom of the screen.

![Screenshot from 2020-01-08 21-04-19](Screenshot%20from%202020-01-08%2021-04-19.png)


The population chosen to start the NEAT algorithm is 25. The impults to the neural network inculde postion of the invaders, defender position, bullet position, and speed of the invaders. The neural network was successful in reacting the goal of 1000 invaders destroyed. Multiple invaders and defenders are displayed onscreen for the user to watch the training process.


![Screenshot from 2020-01-08 21-22-11](Screenshot%20from%202020-01-08%2021-22-11.png)

## How to Implement

This project was built using Python 3.6 and uses the following

Neat:	0.92

Numpy:	1.18.0

Pygame:	1.9.6


