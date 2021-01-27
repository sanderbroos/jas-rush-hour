# JAS-Rush-Hour


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
Once a solution has been found the user will be asked whether they want to see an animation of the solution. The animation was made with matplotlib.

### Authors:
* Jamie
* Alco
* Sander