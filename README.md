# Q-Learning

The setting for this classical algorithm was taken from https://towardsdatascience.com/reinforcement-learning-tutorial-part-1-q-learning-cadb36998b28. The
Q-Learning algorithm is at the center of several reinforcement learning concepts and algorithms. Q-Learning is based on having a table of possible
decisions that can be made and the respective Q-Values (measure of utility of taking a certain action at a certain state). In order for the algorithm to
not be stuck repeating certain decisions that yield low reward, "wind", a random event in which the opposite of the algorithm's choice is forced upon it,
is added. A limit to Q-Learning is the fact that scenarios in which there are near infinite state make it impossible to map a strategy.
