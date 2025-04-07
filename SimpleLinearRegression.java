

package EjemploRegresionLineal;

import java.util.Arrays;

public class SimpleLinearRegression {
    private double theta0 = 0.0; // Intercepto
    private double theta1 = 0.0; // Pendiente
    private double alpha = 0.01; // Tasa de aprendizaje
    private int epochs = 1000; // Número de iteraciones

    // Datos de ejemplo: X (tamaño en m²) y Y (precio en miles de USD)
    private double[] X = {1, 2, 3, 4, 5}; 
    private double[] Y = {2, 4, 6, 8, 10}; 

    // Predicción basada en el modelo
    public double predict(double x) {
        return theta0 + theta1 * x;
    }

    // Algoritmo de descenso de gradiente
    public void train() {
        int n = X.length;
        for (int i = 0; i < epochs; i++) {
            double sumError0 = 0.0, sumError1 = 0.0;

            for (int j = 0; j < n; j++) {
                double error = predict(X[j]) - Y[j];
                sumError0 += error;
                sumError1 += error * X[j];
            }

            theta0 -= (alpha / n) * sumError0;
            theta1 -= (alpha / n) * sumError1;
        }
    }

    public static void main(String[] args) {
        SimpleLinearRegression model = new SimpleLinearRegression();
        model.train();

        System.out.println("Modelo entrenado: y = " + model.theta0 + " + " + model.theta1 + "x");
        System.out.println("Predicción para X=6: " + model.predict(6));
    }
}
