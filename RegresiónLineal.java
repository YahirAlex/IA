

package ffff;

import java.util.Arrays;

public class RegresiónLineal {
    private double theta0 = 0.0; 
    private double theta1 = 0.0;
    private double alpa = 0.01;
    private int epochs = 1000; 

    private double[] X = {1, 2, 3, 4, 5}; 
    private double[] Y = {2, 4, 6, 8, 10}; 

    public double predict(double x) {
        return theta0 + theta1 * x;
    }

    public void train() {
        int n = X.length;
        for (int i = 0; i < epochs; i++) {
            double sumError0 = 0.0, sumError1 = 0.0;

            for (int j = 0; j < n; j++) {
                double error = predict(X[j]) - Y[j];
                sumError0 += error;
                sumError1 += error * X[j];
            }

            theta0 -= (alpa / n) * sumError0;
            theta1 -= (alpa / n) * sumError1;
        }
    }

    public static void main(String[] args) {
        RegresiónLineal model = new RegresiónLineal();
        model.train();

        System.out.println("Modelo entrenado: y = " + model.theta0 + " + " + model.theta1 + "x");
        System.out.println("Predicción para X=6: " + model.predict(6));
    }
}
