# Template Method pattern using Python
Implementation of Template Method Design Pattern according to the task from 'Design Patterns in Python' course
https://www.udemy.com/course/design-patterns-python/


In this task, a card game was implemented. There are two different types of logic of how damage is dealt -  Temporary Damage and Permanent Damage.

The general algorithm of the game is the same, but the damage is done differently.

For TemporaryDamageCardGame unless the creature has been killed its health returns to the original value at the end of the combat.
So, the creature can be killed only by one shot.

For PermanentDamageCardGame in order to kill some creature, you can take several shots.
Also in this type of Game Jokers card have some additional effects.
