import random

class Environment:
    def __init__(self):
        self.state = 0
        self.alpha = 0.7
        self.beta = 0.3
        
    def reset(self):
        self.state = 0
        return self.state
        
    def step(self, action):
        done = False
        if self.state == 0:
            if action == 0:
                self.state = 0 if random.random() < self.alpha else 1
                reward = 2.0
            elif action == 1:
                self.state = 0
                reward = 0.5
            elif action == 2:
                self.state = 0
                reward = 0.0
        elif self.state == 1:
            if action == 0:
                if random.random() < self.beta:
                    self.state = 1
                    reward = 2.0
                else:
                    self.state = 0
                    reward = -3.0
                    done = True
            elif action == 1:
                self.state = 1
                reward = 0.5
            elif action == 2:
                self.state = 0
                reward = 0.0
        return self.state, reward, done 
        
class Agent:  
    def __init__(self):
        self.total_reward = 0.0
        
    def choose_action(self, state):
        return random.choice([0, 1]) if state == 0 else random.choice([0, 1, 2])

env = Environment()
bruno = Agent()  
current_state = env.reset()  
done = False
step = 0

names = ["HIGH", "LOW"]
act_names = ["SEARCH", "WAIT", "RECHARGE"]

print(f"Start: {names[current_state]}")

while not done and step < 20:
    step += 1
    action = bruno.choose_action(current_state)
    next_state, reward, done = env.step(action)
    bruno.total_reward += reward
    
    print(f"S{step} | A: {act_names[action]} | S': {names[next_state]} | R: {reward} | Total: {bruno.total_reward}")
    current_state = next_state

print("Drained!" if done else "Done!")
