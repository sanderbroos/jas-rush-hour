# JAS-Rush-Hour


Imagine.. It is a nice summer evening. You and your beautiful girlfriend have been chilling at the beach all afternoon. Your stomach starts acting up, so you decide to go home to fire up the BBQ and have some beers. You walk up to your red ferarri 458 spyder, you lower the roof, and start the 800 hp engine. You enjoy the sound for a bit and then hit the road. You are cruising downtown without a care in the world. But suddenly, out of nowhere, a truck appears and block the road. You have to brake very hard to avoid an accident and think: 'where did this idiot driver came from'. But you have a good day, so you don't let this small inconvenience ruin it. You put your car in reverse, look back, and with a shock on your face witness something of biblical proportions: a 10ft wall is raising from the ground. You look to your left and see an opportunity to escape this madness. You firmly take the wheel and ready yourself for a quick escape. You put your foot on the gas and ram your steering wheel to the left, but instead off turning, you go straight. You have to brake hard again to avoid a car where first the truck was. You think: "what the hell! Am I going insane?" But then you realise something, and a shiver runs down your spine. You start to go full philosophical and ask yourself: am I real? Is the universe a simulation? Is this a glitch in the matrix? Am I part of a game of Rush Hour? But then you think back to a class you followed during the minor programmeren, and you breath a sigh of relief. You see the other drivers stressing, but not you, you can relax, because you know you are in the red car. You let your *HillClimber* algorithm do its thing and your out there in no time. You see a path forming, the exit is in front of you, you hit the gas, but right before you exit, complete darkness.

### Description:
Rush hour is a sliding block game in which you need to free the red car, which is also the car named 'X'. To free this car you need to unblock the route to the exit, by arranging the cars in a way that the cars blocking the path to the exit can be moved. Our goal is to find an algorithm which can find the most efficient way to move the cars, to solve this puzzle. In this repository you will find the classes: Game, Board and Cars. We use these classes to represent the rush hour puzzle in code. You will also find algorithms which each in their own way solve the rush hour puzzle. Currently Hill Climber is the most consistent algorithm we have made.

### Requirements:
This code was written in python 3.7.6. In requirements.txt are the required packages to install. To install with pip:
```
pip install -r requirements.txt
```
or with conda:
```
conda install --file requirements.txt
```

### Usage:
To run an algorithm use the following command and follow the instructions in the terminal:
```
python main.py
```

To run check50 go to the directory containing the output file:
```
cd docs
```

### Structure:
Here the structure of the most important folders and files are explained.
* /code
    * /code/algorithms
    * /code/classes
    * /code/visualisation
* /data
* /docs

### Algorithms:
Short summary of the algorithms this repository contains.
* Astar (A*):
    Solves by searching based on priority using heuristic. No heuristic = BFS. With Block or Double Block heuristic this algorithm is slow and moderately precise.
* Breadth First Search (BFS):
    Solves by searching all states per width until a solution is found. Slow and memory intensive but always finds the best solution (100% precise).
* Depth First Search (DFS):
    Solves by searching all states up until a certain depth. Very slow, but can be less memory intensive and also finds the best solution (100% precise).
* Hill Climber:
    Solves by iteratively improving a randomly generated solution. Fast and precise (always finds good solutions but usually not the best).
* Iterative Deepening:
    Solves by running the DFS for increasing depths until a solution is found. Very slow, but less memory intensive and always finds the best solution (100% precise).
* Manual:
    User can try to solve the puzzle manually (should be very close to optimal).
* ModAstar:
    Solves by improving a random generated solution using Astar and a specific heuristic: winning positions cars. Slow and imprecise.
* Randomise:
    Solves by randomly trying moves. Very fast but lightyears away from an acceptable solution.

### Visualisation:
Once a solution has been found the user will be asked whether they want to see an animation of the solution. In the animation the car that needs to be unblocked is red and black represents a empty spot. The animation was made with matplotlib.

### Authors:
* Jamie
* Alco
* Sander