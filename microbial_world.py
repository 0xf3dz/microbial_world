import numpy as np
import matplotlib.pyplot as plt
import time
import matplotlib
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)


# Use TkAgg backend
matplotlib.use('TkAgg')

# Turn on interactive mode
plt.ion()

class Microbe:
    def __init__(self, initial_position=[0, 0], initial_direction=0):
        self.position = np.array(initial_position)
        self.direction = initial_direction              
        self.alive = True
    
    def turn_right(self):
        self.direction = (self.direction + 1) % 4

    def turn_left(self):
        self.direction = (self.direction - 1 + 4) % 4

    def random_turn(self):
        if np.random.rand() < 0.5:
            self.turn_left()
        else:
            self.turn_right()
    
    def step_forward(self):
        if self.direction == 0:  # Moving up
            self.position[1] = (self.position[1] + 1) % 10
        elif self.direction == 1:  # Moving right
            self.position[0] = (self.position[0] + 1) % 10
        elif self.direction == 2:  # Moving down
            self.position[1] = (self.position[1] - 1) % 10
        elif self.direction == 3:  # Moving left
            self.position[0] = (self.position[0] - 1) % 10

    def move(self):
        if np.random.rand() < 0.5:
            self.random_turn()
        else:
            self.step_forward()

    def has_been_eaten(self):
        self.alive = False


# Initialize microbes
microbe1 = Microbe(initial_position=[0, 0])
microbe2 = Microbe(initial_position=[9, 9])

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-0.5, 9.5)
ax.set_ylim(-0.5, 9.5)
ax.set_xticks(range(10))
ax.set_yticks(range(10))
ax.grid(True)

# Set initial positions of the microbes
microbe1_scatter = ax.scatter(microbe1.position[0], microbe1.position[1], c='blue', label='Microbe 1')
microbe2_scatter = ax.scatter(microbe2.position[0], microbe2.position[1], c='red', label='Microbe 2')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)

steps = 0
death_message = None

while microbe1.alive and microbe2.alive:
    # Move microbes and update scatter plot
    microbe1.move()
    microbe1_scatter.set_offsets([microbe1.position])

    steps += 1
    if microbe1.position.tolist() == microbe2.position.tolist():
        microbe2.has_been_eaten()
        death_message = "Microbe 2 is dead!"
        death_color = 'blue'  # Color of the alive microbe (Microbe 1)
        ax.text(4.5, 9, death_message, fontsize=18, color=death_color, ha='center')

    elif microbe2.alive:
        microbe2.move()
        microbe2_scatter.set_offsets([microbe2.position])

        steps += 1
        if microbe2.position.tolist() == microbe1.position.tolist():
            microbe1.has_been_eaten()
            death_message = "Microbe 1 is dead!"
            death_color = 'red'  # Color of the alive microbe (Microbe 2)
            ax.text(4.5, 9, death_message, fontsize=18, color=death_color, ha='center')

    # Update the plot and pause
    plt.pause(0.3)  # Pause for 0.3 seconds to create an animation effect

# Display the results
print("Microbe 1 Alive:", microbe1.alive)
print("Microbe 1 Position:", microbe1.position)
print("Microbe 2 Alive:", microbe2.alive)
print("Microbe 2 Position:", microbe2.position)
print("Total Steps Taken:", steps)

# Hold the final plot open
plt.show()