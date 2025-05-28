
class RegresionLineal:
    def __init__(self):
        self.theta0 = 0.0 
        self.theta1 = 0.0 
        self.alpha = 0.01  
        self.epochs = 1000 

        self.X = [1, 2, 3, 4, 5]
        self.Y = [2, 4, 6, 8, 10]

    def predict(self, x):
        return self.theta0 + self.theta1 * x

    def train(self):
        n = len(self.X)
        for _ in range(self.epochs):
            sum_error0 = 0.0
            sum_error1 = 0.0
            for i in range(n):
                error = self.predict(self.X[i]) - self.Y[i]
                sum_error0 += error
                sum_error1 += error * self.X[i]

            self.theta0 -= (self.alpha / n) * sum_error0
            self.theta1 -= (self.alpha / n) * sum_error1

if __name__ == "__main__":
    model = RegresionLineal()
    model.train()
    print(f"Modelo entrenado: y = {model.theta0} + {model.theta1}x")
    print(f"Predicción para X=6: {model.predict(6)}")
