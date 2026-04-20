import math
import matplotlib.pyplot as plt
import numpy

class LoggerMixin:
    def log_action(self, action):
        print(f"[LOG {self.__class__.__name__}] : {action}")

class BaseSeriesCalculator:
    def __init__(self, x, eps):
        self.raw_x = x
        self._eps = eps

    @property
    def eps(self):
        return self._eps

    @eps.setter
    def eps(self,val):
        if val <= 0:
            raise ValueError("Epsilon must not be less or equal than zero")
        self._eps = val

    def calculate(self):
        raise NotImplementedError("Method calculate must be in dauther class")


class TaylorSin(BaseSeriesCalculator, LoggerMixin):
    """Class to calculate and analyze Taylor series for sin(x)"""

    def __init__(self, x, eps=1e-4, max_iter=500):
        self.raw_x = x
        self.eps = eps
        self.max_iter = max_iter

        self.terms = []
        self.result = 0
        self.n_iterations = 0
        self.dynamic_status = "Not calculated yet"

    def __str__(self):
        return f"Calculator TaylorSin (x={self.raw_x}, eps={self.eps})"

    def __call__(self):
        return self.calculate()


    def calculate(self):
        """
        Calculate sin(x)
        """
        self.log_action("Start calculating Taylor series...")
        self.dynamic_status = "Calculated"


        x = self.raw_x % (2 * math.pi)
        result = 0
        term = x
        self.terms = []

        for i in range(self.max_iter):
            self.terms.append(term)

            result += term
            if abs(term) < self.eps and i > 0:
                self.result = result
                self.n_iterations = i + 1
                return self.result, self.n_iterations

            # execute next component
            term *= (-1) * x * x / ((2 * i + 2) * (2 * i + 3))

        self.result = result
        self.n_iterations = self.max_iter
        return self.result, self.n_iterations

    def get_statistics(self):
        if not self.terms:
            return None

        arr = numpy.array(self.terms)

        stats = {
            'mean': numpy.mean(arr),        # cреднее арифметическое
            'median': numpy.median(arr),    # медиана
            'variance': numpy.var(arr),     # дисперсия
            'stdev': numpy.std(arr)         # СКО (Стандартное отклонение)
        }

        unique_vals, counts = numpy.unique(arr, return_counts=True)
        max_count = numpy.max(counts)


        if max_count > 1:
            modes = unique_vals[counts == max_count]
            stats['mode'] = modes[0] if len(modes) == 1 else list(modes)
        else:
            stats['mode'] = "No mode"

        return stats

    def plot_graph(self):
        """
        Draw graph
        :return:
        """
        # from -10 to 10 с step 0.1
        x_values = [x / 10.0 for x in range(-100, 101)]
        y_taylor = []
        y_math = []

        # Y for every X
        for xv in x_values:
            temp_calc = TaylorSin(xv, self.eps, self.max_iter)
            res, _ = temp_calc.calculate()
            y_taylor.append(res)
            y_math.append(math.sin(xv))

        # graphic
        plt.figure(figsize=(10, 6))

        # 2 lines
        plt.plot(x_values, y_taylor, label='Taylor sin(x)', color='blue', linestyle='--')
        plt.plot(x_values, y_math, label='math.sin(x)', color='red', alpha=0.5, linewidth=3)

        plt.title('sin(x): Taylor series vs math.sin()')
        plt.xlabel('X (radians)')
        plt.ylabel('Y')
        plt.axhline(0, color='black', linewidth=1) # ось X
        plt.axvline(0, color='black', linewidth=1) # ссь Y
        plt.grid(True)
        plt.legend()

        # annotation
        plt.annotate(f'Entered point x={self.raw_x}',
                     xy=(self.raw_x, math.sin(self.raw_x)),
                     xytext=(self.raw_x + 1, math.sin(self.raw_x) + 0.5),
                     arrowprops=dict(facecolor='black', shrink=0.05))


        plt.savefig('task3_graph.png')
        print("\nGraph saved in file 'task3_graph.png'")
        plt.show()

def math_sin(x):
    # execute sin
    return math.sin(x)