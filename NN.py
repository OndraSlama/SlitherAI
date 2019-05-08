import numpy as np
import pickle 

# # X = (hours sleeping, hours studying), y = score on test
# X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
# y = np.array(([92], [86], [89]), dtype=float)

# # scale units
# X = X/np.amax(X, axis=0)  # maximum of X array
# y = y/100  # max test score is 100


class NeuralNetwork():
    def __init__(self, inNodes, hiddenNodes = 3, outNodes = 1):
        if isinstance(inNodes, NeuralNetwork):
            net = inNodes            
            # parameters
            self.inputSize = net.inputSize
            self.outputSize = net.outputSize
            self.hiddenSize = net.hiddenSize

            # weights            
            self.weightsIH = net.weightsIH.copy() # weight matrix from input to hidden layer            
            self.weightsHO = net.weightsHO.copy() # weight matrix from hidden to output layer

            # biases
            self.biasH = net.biasH.copy() # bias for hidden layer
            self.biasO = net.biasO.copy() # bias for output layer
        else:
            # parameters
            self.inputSize = inNodes
            self.outputSize = outNodes
            self.hiddenSize = hiddenNodes

            # weights            
            self.weightsIH = np.random.randn(self.inputSize, self.hiddenSize) # weight matrix from input to hidden layer            
            self.weightsHO = np.random.randn(self.hiddenSize, self.outputSize) # weight matrix from hidden to output layer

            # biases
            self.biasH = np.random.randn(self.hiddenSize) # bias for hidden layer
            self.biasO = np.random.randn(self.outputSize) # bias for output layer

    def Forward(self, X_in):

        # save input
        X = np.array(X_in)

        # from input to hidden
        self.hidden = np.dot(X, self.weightsIH) # dot product of X (input) and first set of weights
        self.hidden += self.biasH # add bias
        self.hidden = self.Sigmoid(self.hidden) # use activation function

        # from hidden to output
        self.output = np.dot(self.hidden, self.weightsHO) # dot product of X (input) and first set of weights
        self.output += self.biasO # add bias
        self.output = self.Sigmoid(self.output) # use activation function
        
        # save ouput
        Y = self.output.tolist()
        return Y

    def Copy(self):
        return NeuralNetwork(self)

    def Sigmoid(self, s):
        # activation function
        return 1/(1+np.exp(-s))

    def Mutate(self, rate):
        self.weightsIH = self.MutateMatrix(self.weightsIH, rate)
        self.weightsHO = self.MutateMatrix(self.weightsHO, rate)
        self.biasH = self.MutateMatrix(self.biasH, rate)
        self.biasO = self.MutateMatrix(self.biasO, rate)
        
    def MutateMatrix(self, matrix, rate):
        shape = matrix.shape                           # Store original shape
        matrix = matrix.flatten()                      # Flatten to 1D
        inds = np.random.choice(matrix.size, size=round(rate*matrix.size))       # Get random indices
        matrix[inds] += np.random.normal(size=matrix[inds].size)/4            
        matrix = matrix.reshape(shape)                                          # Restore original shape
        return matrix

# NN = NeuralNetwork(2,3,1)


# # defining our output
# o = NN.Forward(X)


# with open('filename_nn.obj', 'wb') as file_nn:
#     pickle.dump(NN, file_nn)

# with open('filename_nn.obj', 'rb') as file_nn2:
#     NN2 = pickle.load(file_nn2)

# # print(NN2)

# print("Predicted Output: \n" + str(o))
# print("Actual Output: \n" + str(y))
