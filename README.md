# jas-rush-hour


### Description:
Rush hour is a sliding block game in which you need to free the red car, or in our case the car named 'X'. To free this car you need to unblock the route to the exit, by arranging the cars in a way that the cars blocking the path to the exit can be moved. Our goal is to find an algorithm which can find the most efficient way to move the cars, to solve this puzzle.

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
* Astar:
    Solves by searching based on priority using heuristic. No heuristic = BFS. Slow and moderate precise
* Breadth_first:
    Solves by searching the width. Slow but very precise.
* Depth_first:
    Solves by searching the depth. 
* Hill_climber:
    Solves by improving a random generated solution. Fast and precise
* Iterative_deepening:
    Solves by searching deeper and deeper
* Manual:
    User can try to solve the puzzle manualy
* ModAstar:
    Solves by improving a random generated solution using Astar and a specific heuristic. Very slow and unprecise.
* Randomise:
    Solves by randomly trying moves. Very fast but unprecise

### Visualisation:
To visualise the results...

### Authors:
* Jamie
* Alco
* Sander