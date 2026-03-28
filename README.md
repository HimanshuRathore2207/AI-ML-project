# 8-Puzzle Solver using A* Algorithm

## 1. Overview

This project presents an implementation of the A* search algorithm to solve the classical 8-puzzle problem. The 8-puzzle consists of a 3×3 grid containing eight numbered tiles and one empty space. The objective is to transform an initial configuration into a predefined goal state through a sequence of valid moves while minimizing the total cost.

The project demonstrates the application of informed search strategies within the broader domain of Artificial Intelligence, with particular emphasis on heuristic-based problem solving.

---

## 2. Objectives

The primary objectives of this project are as follows:

* To implement the A* search algorithm for an optimal pathfinding problem
* To model the 8-puzzle as a state-space search problem
* To apply heuristic evaluation to improve search efficiency
* To analyse the effectiveness of informed search compared to uninformed approaches

---

## 3. Methodology

### 3.1 Problem Representation

The puzzle state is represented as a one-dimensional list of length nine, where each element corresponds to a tile position. The value `0` denotes the blank tile.

### 3.2 State Space

Each state generates successor states by moving the blank tile in one of four possible directions, subject to boundary constraints.

### 3.3 A* Search Algorithm

The A* algorithm evaluates each node using the function:

f(n) = g(n) + h(n)

where:

* g(n) represents the cost from the initial state to the current node
* h(n) represents the estimated cost from the current node to the goal state

### 3.4 Heuristic Function

The implementation employs the misplaced tiles heuristic, which counts the number of tiles that are not in their correct positions. This heuristic is admissible and ensures optimality of the solution.

---

## 4. Project Structure

```
a-star-8puzzle/
│── src/
│   └── astar.py
│
│── README.md
```

---

## 5. Installation and Setup

### 5.1 Prerequisites

* Python 3.x installed on the system

### 5.2 Execution Steps

1. Navigate to the project directory

2. Execute the program using the following command:

   python astar.py

3. Provide the initial puzzle configuration as input in a single line, separated by spaces

Example input:

```
1 2 3 4 0 6 7 5 8
```

---

## 6. Input Specification

The user must provide exactly nine integers ranging from 0 to 8, without repetition. The value `0` represents the blank tile.

---

## 7. Output Description

The program outputs:

* The total number of steps required to reach the goal state
* The sequence of intermediate states from the initial configuration to the goal configuration

Each state is displayed in a structured 3×3 format for clarity.

---

## 8. Results

The implementation successfully computes an optimal solution for valid initial configurations. The use of a heuristic function significantly reduces the search space compared to uninformed methods such as Breadth-First Search.

---

## 9. Limitations

* The algorithm may consume considerable memory for complex initial states
* The misplaced tiles heuristic, while admissible, is not the most efficient possible heuristic

---

## 10. Future Enhancements

* Integration of a more informed heuristic such as Manhattan distance
* Development of a graphical user interface for visualization
* Comparative analysis with other search algorithms
* Extension to larger problem variants such as the 15-puzzle

---

## 11. Conclusion

This project illustrates the practical application of the A* search algorithm in solving a well-defined combinatorial problem. It reinforces fundamental concepts in Artificial Intelligence, including state-space representation, heuristic evaluation, and optimal pathfinding.

---

## 12. Learning Outcomes

* Understanding of informed search strategies
* Practical implementation of the A* algorithm
* Insight into heuristic design and evaluation
* Experience in modelling real-world problems as search problems

---
