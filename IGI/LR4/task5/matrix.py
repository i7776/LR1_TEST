"""
Module for Task 5.
Contains MatrixAnalyzer for advanced matrix operations using NumPy.
Handles random matrix generation, row swapping logic, and comparative
median calculations to demonstrate library efficiency.
"""
import numpy as np

class MatrixLogMixin:
    def log(self, message):
        print(f"[Matrix LOG]: {message}")

class BaseMatrix:
    def __init__(self, n, m):
        self._matrix = np.random.randint(1, 100, (n, m))
        self.creation_status = "Initial"
    @property
    def matrix(self):
        return self._matrix

class MatrixAnalyzer(BaseMatrix, MatrixLogMixin):
    def __init__(self, n, m):
        super().__init__(n, m)

    def __str__(self):
        rows, cols = self.matrix.shape  # Распаковываем размеры (например, 5, 5)
        return f"Matrix size {rows} by {cols}:\n{self.matrix}"

    def swap_max_with_diagonal(self):
        self.log("Starting row swap process...")
        row, cols =  self.matrix.shape
        for i in range(min(row, cols)):
            max_id = np.argmax(self.matrix[i])

            self.matrix[i, i], self.matrix[i, max_id] = self.matrix[i, max_id], self.matrix[i, i]

        self.creation_status = "Processed"
        self.log("Swapping complete")

    def calculate_median_numpy(self):
        """
        Calculates the median of the matrix's main diagonal using NumPy
        """
        diag = np.diagonal(self.matrix)
        return np.median(diag)

    def calculate_median(self):
        """
        Calculates the median of the matrix's main diagonal manually
        """
        diag = np.diagonal(self.matrix)
        sorted_diag = np.sort(diag)
        n = len(sorted_diag)

        mid = n // 2

        if n % 2 == 0:
            return (sorted_diag[mid - 1] + sorted_diag[mid]) / 2.0
        else:
            return float(sorted_diag[mid])

    def display_numpy_features(self):
        """
        Demonstrates required NumPy features from the assignment
        """
        self.log("Demonstrating additional NumPy features...")

        zeros_arr = np.zeros((2, 2))
        ones_arr = np.ones((2, 2))
        eye_arr = np.eye(2) # Единичная матрица

        # Индексирование и срезы
        # Возьмем первую строку и первые два столбца
        sub_matrix = self.matrix[:1, :2]

        # Математические и статистические операции (mean, var, std, corrcoef)
        # Считаем по всей матрице
        mean_val = np.mean(self.matrix) #chtlytt
        variance_val = np.var(self.matrix)
        std_val = np.std(self.matrix)

        # Коэффициент корреляции (требует как минимум две строки)
        if self.matrix.shape[0] > 1:
            corr = np.corrcoef(self.matrix[0], self.matrix[1])
        else:
            corr = "Not enough rows for correlation"

        print(f"\n--- Required NumPy Features Demo ---")
        print(f"Zeros array:\n{zeros_arr}")
        print(f"Identity matrix (eye):\n{eye_arr}")
        print(f"Slice (first row, 2 cols): {sub_matrix}")
        print(f"Mean of matrix: {mean_val:.2f}")
        print(f"Variance (var): {variance_val:.2f}")
        print(f"Standard deviation (std): {std_val:.2f}")
        print(f"Correlation coefficient:\n{corr}")
