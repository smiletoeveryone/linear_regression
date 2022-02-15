#! /bin/usr/python3

class LinearRegression(object):
    def __init__ (self, eta=0.01, N_iters=1000):
        self.lr = eta
        self.N_iters = N_iters
        self.weights = 0.0
        self.bias = 0.0

    def cost_fucntion(self, X, Y, weight, bias):
        n = len(X)
        total_error = 0.0
        for i in range(n):
            total_error += (Y[i] - (weight * X[i] + bias)) ** 2

        print("total_error is {}", total_error / n)    
        return total_error / n    
    


    def update_weights(self, X, Y, weight, bias, learning_rate):
        dw = 0 
        db = 0
        n = len(x)
        
        for i in range(n):
            dw += -2 * X[i] * (Y[i] - (weight*X[i] + bias))
            db += -2 * (Y[i] - (weight*X[i] + bias))
            weight -= (dw / n) * learning_rate
            bias -= (db / n) * learning_rate
            return weight, bias

    def fit(self, X, Y):
        cost_history = []

        for i in range(self.N_iters):
            weight, bias = self.update_weights(X, Y, self.weights, self.bias, self.lr)
            cost = self.cost_fucntion(X, Y, weight, bias)
            cost_history.append(cost)
            self.weights = weight
            self.bias = bias
            print("Iteration: {}".format(i), "cost = {}".format(cost))
        return self.weights, self.bias, cost_history



    def predict(self, x):
        x = (x+100)/200
        return x * self.weights + self.bias

x = [1, 2, 3, 10, 20, 50, 100, -2, -10, -100, -5, -200]
y = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]

model = LinearRegression(0.01, 500)

X = [(k + 100) / 200 for k in x]

model.fit(X, y)

test_x = [90, 80, 81, 82, 75, 40, 32, 15, 5, 1, -1, -15, -20, -22, -33, -45, -60, -90]
         
for i in range(len(test_x)):
    print("input {} => predict: {}".format(test_x[i], model.predict(test_x[i])))