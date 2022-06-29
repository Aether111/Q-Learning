import numpy as np
import pandas as pd

learning_rate = 0.3

discount = 0.95

q_init = np.zeros([2,5])

q_table = pd.DataFrame(q_init,index=["Right","Left"],columns=[i + 1 for i in range(5)])

current_state = 1

next_state = 1

iterations = 10000

num_states = q_table.shape[1]

def move_right(current_state):
  if current_state < num_states:
      return current_state + 1
  return current_state

def move_left(current_state):
  return 1

for iter in range(iterations):
  reward = 0

  wind = np.random.randint(0,8)

  if q_table.loc["Right",current_state] > q_table.loc["Left",current_state]:
    if wind > 0:
      next_state = move_right(current_state)
      direction = "Right"
    else:
       next_state = move_left(current_state)
       direction = "Left"
  elif q_table.loc["Right",current_state] < q_table.loc["Left",current_state]:
    if wind > 0:
      next_state = move_left(current_state)
      direction = "Left"
    else:
      next_state = move_right(current_state)
      direction = "Right"
  else:
    if np.random.randint(0,2) == 0:
      next_state = move_right(current_state)
      direction = "Right"
    else:
      next_state = move_left(current_state)
      direction = "Left"

  if next_state == 1:
    reward = 2
  elif next_state == 5:
    reward = 10

  possible = [q_table.loc["Right",next_state],q_table.loc["Left",next_state]]

  q_table.loc[direction,current_state] = q_table.loc[direction,current_state] +\
                                         learning_rate * (reward + discount * np.max(possible) -\
                                         q_table.loc[direction,current_state])
  
  print("Current position is: " + str(current_state))

  current_state = next_state

print("Direction chosen is: " + direction)
print(q_table,end=3*'\n')
