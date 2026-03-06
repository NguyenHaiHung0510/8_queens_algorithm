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

def fitness(state):
    return 28 - heuristic(state) # 28 là số cặp hậu tối đa chọn được C(8,2)

def crossover(p1,p2):
    point = random.randint(0,7)
    return p1[:point] + p2[point:]

def mutate(state,rate =0.1):
    if random.random() < rate:
        i = random.randint(0,7)
        state[i] = random.randint(0,7)
    return state

def genetic_algor(pop_size = 100,generation = 1000):
    population = [random_state() for _ in range(pop_size)]

    for _i in range(generation):
        population.sort(key = lambda x: fitness(x), reverse= True)

        if heuristic(population[0]) == 0:
            return population[0]
        
        new_pop = population[:20]

        while len(new_pop) < pop_size:
            p1 = random.choice(population[:50])
            p2 = random.choice(population[:50])
            child = crossover(p1, p2)
            child = mutate(child)
            new_pop.append(child)

        population = new_pop

    return population[0]

print(genetic_algor())
print(heuristic(genetic_algor()))