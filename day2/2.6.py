import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights and biases for the neural network
        self.weights_input_hidden = np.random.rand(input_size, hidden_size)
        self.bias_input_hidden = np.random.rand(1, hidden_size)
        self.weights_hidden_output = np.random.rand(hidden_size, output_size)
        self.bias_hidden_output = np.random.rand(1, output_size)

    def sigmoid(self, x):
        # Sigmoid activation function
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        # Derivative of the sigmoid activation function
        return x * (1 - x)

    def forward(self, inputs):
        # Forward pass through the neural network
        self.hidden_layer_input = np.dot(inputs, self.weights_input_hidden) + self.bias_input_hidden
        self.hidden_layer_output = self.sigmoid(self.hidden_layer_input)
        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output) + self.bias_hidden_output
        self.output_layer_output = self.sigmoid(self.output_layer_input)
        return self.output_layer_output

    def backward(self, inputs, outputs, learning_rate):
        # Backward pass through the neural network (backpropagation)
        output_error = outputs - self.output_layer_output
        output_delta = output_error * self.sigmoid_derivative(self.output_layer_output)
        
        hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
        hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden_layer_output)

        self.weights_hidden_output += np.dot(self.hidden_layer_output.T, output_delta) * learning_rate
        self.bias_hidden_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
        self.weights_input_hidden += np.dot(inputs.T, hidden_delta) * learning_rate
        self.bias_input_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

    def train(self, inputs, outputs, learning_rate, epochs):
        # Train the neural network
        for epoch in range(epochs):
            self.forward(inputs)
            self.backward(inputs, outputs, learning_rate)

    def predict(self, inputs):
        # Make predictions using the trained neural network
        return self.forward(inputs)


# Example usage:
if __name__ == "__main__":
    # Create a neural network with 2 input neurons, 2 hidden neurons, and 1 output neuron
    neural_network = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)

    # Define training data (XOR problem)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    # Train the neural network
    neural_network.train(X, y, learning_rate=0.1, epochs=10000)

    # Make predictions
    predictions = neural_network.predict(X)
    print("Predictions:")
    print(predictions)
