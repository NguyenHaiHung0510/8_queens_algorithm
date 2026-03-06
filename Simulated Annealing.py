import math
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
    return [random.randint(0, n-1) for _ in range(n)]

def toi_thep():
    current = random_state()
    T = 100
    cooling = 0.99

    while T > 0.001:
        if heuristic(current) == 0:
            return current
        
        i = random.randint(0,7)
        j = random.randint(0,7)

        next_state = current[:]
        next_state[i] = j

        delta = heuristic(next_state) - heuristic(current)

        if delta < 0:
            current = next_state
        else:
            prob = math.exp(-delta / T)
            if random.random() <prob:
                current = next_state

        T *= cooling
    return current


print(toi_thep())
print(heuristic(toi_thep()))
