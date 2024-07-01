import numpy as np

class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers
        self.num_layers = len(layers)
        self.weights = [np.random.randn(layers[i], layers[i-1]) for i in range(1, self.num_layers)]
        self.biases = [np.random.randn(layers[i], 1) for i in range(1, self.num_layers)]
        self.activations = [np.zeros((layers[i], 1)) for i in range(self.num_layers)]

    def sigmoid(self, z):
        """Sigmoid activation function."""
        return 1 / (1 + np.exp(-z))

    def sigmoid_derivative(self, z):
        """Derivative of the sigmoid function."""
        return self.sigmoid(z) * (1 - self.sigmoid(z))

    def forward_propagation(self, X):
        """Perform forward propagation to compute outputs."""
        self.activations[0] = X.reshape(-1, 1)
        for i in range(1, self.num_layers):
            z = np.dot(self.weights[i-1], self.activations[i-1]) + self.biases[i-1]
            self.activations[i] = self.sigmoid(z)
        return self.activations[-1]

    def train(self, X, y, epochs, learning_rate):
        """Train the neural network using gradient descent."""
        for epoch in range(epochs):
            for i in range(len(X)):
                # Forward propagation
                self.forward_propagation(X[i])

                # Backpropagation
                error = self.activations[-1] - y[i].reshape(-1, 1)
                for j in range(self.num_layers-1, 0, -1):
                    delta = error * self.sigmoid_derivative(np.dot(self.weights[j-1], self.activations[j-1]) + self.biases[j-1])
                    self.weights[j-1] -= learning_rate * np.dot(delta, self.activations[j-1].T)
                    self.biases[j-1] -= learning_rate * delta
                    error = np.dot(self.weights[j-1].T, delta)

    def predict(self, X):
        """Predict outputs for input X."""
        predictions = []
        for i in range(len(X)):
            output = self.forward_propagation(X[i])
            predictions.append(output.flatten())
        return np.array(predictions)

# Example usage:
if __name__ == "__main__":
    # Example dataset (binary classification)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    # Initialize and train the neural network
    nn = NeuralNetwork(layers=[2, 3, 1])
    nn.train(X, y, epochs=10000, learning_rate=0.1)

    # Predict on new data
    predictions = nn.predict(X)
    print("Predictions:")
    for i in range(len(X)):
        print(f"Input: {X[i]}, Predicted Output: {predictions[i]}")
