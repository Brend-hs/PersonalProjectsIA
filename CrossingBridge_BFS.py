from collections import deque

# Define crossing times for each person
times = {'A': 1, 'B': 2, 'C': 5, 'D': 10}

# Define a function to check if a state is objective
def is_goal(state):
    return len(state) == 0

# Defines a function to generate the successors of a state
def successors(state):
    possible_successors = []
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            possible_successors.append((state[:i] + state[i + 1:j] + state[j + 1:], state[i], state[j]))
    return possible_successors

# Defines the function to perform breadth-first search
def bfs():
    initial_state = ('ABCD', '', 0)  # All individuals are on side A, the flashlight is on side A, time is 0
    queue = deque([initial_state])

    while queue:
        state, path, time = queue.popleft()
        if is_goal(state):
            return path

        for successor_state, person1, person2 in successors(state):
            time_taken = max(times[person1], times[person2])
            new_time = time + time_taken
            if new_time <= 17:
                queue.append((successor_state, path + person1 + person2, new_time))

    return None

# Run the search
solution = bfs()

# Print the solution
print("Pasos para cruzar el puente antes de que colapse:", solution)
