import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data Visualization
class DataVisualization:
    def __init__(self, data):
        self.data = data

    def scatter_plot(self):
        self.showColumns()
        while True:
            x_column = input("\nEnter the x-axis column: ").lower()
            y_column = input("Enter the y-axis column: ").lower()

            if x_column not in self.data.columns or y_column not in self.data.columns:
                print("One or more columns are not present. Try again.")
                continue

            plt.scatter(self.data[x_column], self.data[y_column])
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.title(f"Scatter Plot: {x_column} vs {y_column}")
            plt.show()
            break

    def histogram(self):
        self.showColumns()
        while True:
            column = input("\nEnter the column name for the histogram: ").lower()

            if column not in self.data.columns:
                print("Column is not present. Try again.")
                continue

            plt.hist(self.data[column], bins=10, edgecolor='black')
            plt.xlabel(column)
            plt.ylabel("Frequency")
            plt.title(f"Histogram: {column}")
            plt.show()
            break

    def bar_graph(self):
        self.showColumns()
        while True:
            x_column = input("\nEnter the x-axis column: ").lower()
            y_column = input("Enter the y-axis column: ").lower()

            if x_column not in self.data.columns or y_column not in self.data.columns:
                print("One or more columns are not present. Try again.")
                continue

            plt.bar(self.data[x_column], self.data[y_column])
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.title(f"Bar Graph: {x_column} vs {y_column}")
            plt.show()
            break

    def pie_chart(self):
        self.showColumns()
        while True:
            column = input("\nEnter the column name for the pie chart: ").lower()

            if column not in self.data.columns:
                print("Column is not present. Try again.")
                continue

            data_counts = self.data[column].value_counts()
            labels = data_counts.index
            plt.pie(data_counts, labels=labels, autopct='%1.1f%%')
            plt.title(f"Pie Chart: {column}")
            plt.show()
            break
