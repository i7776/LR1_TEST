"""
Module for Task 6.
Focuses on data science operations using the Pandas library.
Implements WineAnalyzer to process the Wine Quality dataset,
performing Series manipulation, custom indexing, and statistical filtering.
"""
import pandas as pd

class PandasLoggerMixin:
    """
    Mixin for logging Pandas operations
    """
    def log_info(self, msg):
        """
        Prints a log message with a specialized prefix.
        :param msg: String message to display.
        """
        print(f"[Pandas LOG]: {msg}")

class BaseDataAnalyzer(PandasLoggerMixin):
    """
    Abstract base class for data analysis.
    """
    # cтатический атрибут
    datasets_loaded = 0

    def __init__(self, filepath):
        """
        Initializes the base analyzer
        :param filepath: String path to the data file
        """
        self._filepath = filepath  # cкрытый атрибут
        BaseDataAnalyzer.datasets_loaded += 1
        self.status = "Initialized" # динамический атрибут


    @property
    def filepath(self):
        """
        Getter for the file path property
        """
        return self._filepath

    @filepath.setter
    def filepath(self, value):
        """
        Setter for the file path. Validates that input is a string
        """
        if not isinstance(value, str):
            raise ValueError("Filepath must be a string")
        self._filepath = value

    def run_analysis(self):
        """
        Abstract method for running analysis logic
        """
        raise NotImplementedError("This method must be overridden in child class")

class WineAnalyzer(BaseDataAnalyzer):
    """
    Class for analyzing wine quality data using Pandas
    """
    def __init__(self, filepath = 'winequality-red.csv'):
        """
        Initializes the WineAnalyzer and loads the dataset
        :param filepath: Path to the CSV file
        :raises FileNotFoundError: If the CSV file is missing
        """
        super().__init__(filepath)
        self.log_info("Dataset successfully loaded!")
        try:
            self.df = pd.read_csv(filepath)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filepath} not found! Please put it in the project folder.")

    def __str__(self):
        """
        Returns a string representation of the analyzer status
        """
        return f"Analyzer for dataset: {self.filepath} (Rows: {len(self.df)})"

    def run_analysis(self):
        self.show_general_info()
        self.run_task_a()
        self.run_task_b()

    def show_general_info(self):
        """
        Displays structural information about the DataFrame and basic descriptive statistics
        """
        print("\n--- General DataFrame Info ---")
        print(self.df.info()) # Информация по каждому параметру (типы данных)
        print("\n--- Descriptive Statistics ---")
        print(self.df.describe()) # Статистика (среднее, мин, макс и тд)

    def run_task_a(self):
        """
        Create a Series from 'quality' with new indices, and combine it with 'alcohol' Series into a DataFrame
        """
        quality_series = self.df['quality'].copy()
        alcohol_series = self.df['alcohol'].copy()

        new_index = [f"wine_{i}" for i in range(len(quality_series))]
        quality_series.index = new_index
        alcohol_series.index = new_index

        print(f"Демонстрация .iloc (5-й элемент): {quality_series.iloc[4]}")
        print(f"Демонстрация .loc (элемент 'wine_0'): {quality_series.loc['wine_0']}")

        new_dataframe = pd.DataFrame({
            'Quality': quality_series,
            'Alcohol': alcohol_series
        })

        try:
            from IPython.display import display
            display(new_dataframe.head())
        except ImportError:
            print(new_dataframe.head())

    def run_task_b(self):
        """
        Calculate average alcohol concentration for wines with maximum quality
        """
        max_q = self.df['quality'].max()
        best_wines = self.df[self.df['quality'] == max_q]
        avg_alc = best_wines['alcohol'].mean()

        result = round(avg_alc, 2)
        print(f"Average alcohol concentration in best wines: {result}")
        return result







