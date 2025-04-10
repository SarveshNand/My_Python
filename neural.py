import matplotlib.pyplot as plt
import numpy as np

# Set up figure and axes
fig, axs = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle("Neural Networks in Calculus of Machine Learning", fontsize=16)

# --------- Diagram 1: Structure of Neural Network ---------
axs[0].set_title("1. Structure of a Neural Network")
axs[0].axis('off')

# Coordinates for layers
input_layer = [(0, 2), (0, 1), (0, 0)]
hidden_layer = [(2, 2.5), (2, 1.5), (2, 0.5)]
output_layer = [(4, 1.5)]

# Plot neurons
for x, y in input_layer:
    axs[0].add_patch(plt.Circle((x, y), 0.1, color='blue'))
for x, y in hidden_layer:
    axs[0].add_patch(plt.Circle((x, y), 0.1, color='green'))
for x, y in output_layer:
    axs[0].add_patch(plt.Circle((x, y), 0.1, color='red'))

# Draw connections
for (x1, y1) in input_layer:
    for (x2, y2) in hidden_layer:
        axs[0].plot([x1, x2], [y1, y2], 'k-', linewidth=0.5)
for (x1, y1) in hidden_layer:
    for (x2, y2) in output_layer:
        axs[0].plot([x1, x2], [y1, y2], 'k-', linewidth=0.5)

axs[0].text(-0.5, 2, "Input Layer", fontsize=10)
axs[0].text(1.5, 2.7, "Hidden Layer", fontsize=10)
axs[0].text(4.5, 1.5, "Output Layer", fontsize=10)

# --------- Diagram 2: Forward Propagation ---------
axs[1].set_title("2. Forward Propagation")
axs[1].axis('off')

# Draw example neuron
axs[1].add_patch(plt.Circle((1, 1), 0.1, color='blue'))  # Input
axs[1].add_patch(plt.Circle((3, 1), 0.1, color='green'))  # Weighted Sum
axs[1].add_patch(plt.Circle((5, 1), 0.1, color='orange'))  # Activation Output

# Arrows and labels
axs[1].annotate("", xy=(2.9, 1), xytext=(1.1, 1), arrowprops=dict(arrowstyle="->"))
axs[1].annotate("", xy=(4.9, 1), xytext=(3.1, 1), arrowprops=dict(arrowstyle="->"))
axs[1].text(1, 0.7, "Input x", ha='center')
axs[1].text(3, 0.7, "z = wx + b", ha='center')
axs[1].text(5, 0.7, "a = σ(z)", ha='center')

# --------- Diagram 3: Activation Functions ---------
axs[2].set_title("3. Activation Functions")
x = np.linspace(-10, 10, 400)
relu = np.maximum(0, x)
sigmoid = 1 / (1 + np.exp(-x))
tanh = np.tanh(x)

axs[2].plot(x, relu, label='ReLU', color='green')
axs[2].plot(x, sigmoid, label='Sigmoid', color='blue')
axs[2].plot(x, tanh, label='Tanh', color='red')
axs[2].legend()
axs[2].grid(True)
axs[2].set_xlabel("Input")
axs[2].set_ylabel("Output")
axs[2].set_ylim([-1.5, 1.5])

plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.show()
