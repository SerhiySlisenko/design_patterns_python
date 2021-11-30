# Chain of Responsibility (CoR) pattern using Python
Implementation of Chain of Responsibility Design Pattern according to the task from 'Design Patterns in Python' course
https://www.udemy.com/course/design-patterns-python/

# Task
You are given a game scenario with classes Goblin and GoblinKing. Please implement the following rules:
* A goblin has base 1 attack/1 defense (1/1), a goblin king is 3/3.
* When the Goblin King is in play, every other goblin gets +1 Attack.
* Goblins get +1 to Defense for every other Goblin in play (a GoblinKing is a Goblin!).

Example:
* Suppose you have 3 ordinary goblins in play. Each one is a 1/3 (1/1 + 0/2 defense bonus)
* A goblin king comes into play. Now every goblin is a 2/4 (1/1 + 0/3 defense bonus from each other + 1/0 from goblin king)

The state of all the goblins has to be consistent as goblins are added and removed from the game.
