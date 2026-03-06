import random 

# Hàm mục tiêu này tìm h là số cặp quân hậu tấn công nhau => h=0 là đúng
def heuristic(state):
    h = 0
    n = len(state)
    for i in range(n):
        for j in range(i+1,n):
            if state[i] == state[j]:
                h +=1
            if abs(state[i]- state[j]) == abs(i-j):
                h += 1
    return h

def random_state(n=8):
    return [random.randint(0,n-1) for _ in range(n)]

def get_neighbors(state):
    neighbors = []
    n = len(state)
    for i in range(n):
        for j in range(n):
            if j != state[i]:
                new_state = state[:]
                new_state[i] = j
                neighbors.append(new_state)
    return neighbors

def hill_climbing():
    current = random_state()

    while True:
        neighbors = get_neighbors(current)
        next_state = min(neighbors, key = heuristic)

        if heuristic(next_state) >= heuristic(current):
            return current
        
        current = next_state


print("hill_climbing Algorithm: ",hill_climbing())
print("Target: ", heuristic(hill_climbing()))