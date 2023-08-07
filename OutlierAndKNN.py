import pandas as pd
from data_description import DataDescription

class OutlierAndKNN:
    # The Task associated with this class.
    tasks = [
        '\n1. Detect and Handle Outliers',
        '2. KNN Imputation',
        '3. Show the Dataset'
    ]

    def __init__(self, data):
        self.data = data

    # Function to detect and handle outliers using the z-score method
    def handleOutliers(self):
        while True:
            print("\n1. Detect and Remove Outliers")
            print("2. Go Back")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 2:
                    break
                elif choice != 1:
                    print("Invalid choice. Please try again.")
                    continue

                columns = self.data.select_dtypes(include=["float64", "int64"]).columns
                print("Numeric Columns:")
                print(', '.join(columns))

                col_name = input("Enter the column name (Press -1 to go back): ")
                if col_name == "-1":
                    break

                if col_name not in columns:
                    print("Invalid column name. Please try again.")
                    continue

                z_scores = (self.data[col_name] - self.data[col_name].mean()) / self.data[col_name].std()
                threshold = 3
                outliers = self.data[abs(z_scores) > threshold]

                if outliers.empty:
                    print("No outliers found in the selected column.")
                else:
                    print("Outliers found in the selected column:")
                    print(outliers)

                choice = input("Do you want to remove outliers from this column? (y/n): ")
                if choice.lower() == 'y':
                    self.data = self.data[abs(z_scores) <= threshold]
                    print("Outliers removed successfully.")
                else:
                    print("Outliers not removed.")
                
            except ValueError:
                print("Invalid input. Please enter a valid choice.")

    # Function for KNN imputation of missing values
    def knnImputation(self):
        while True:
            print("\n1. Perform KNN Imputation")
            print("2. Go Back")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 2:
                    break
                elif choice != 1:
                    print("Invalid choice. Please try again.")
                    continue

                columns_with_null = self.data.columns[self.data.isnull().any()]
                print("Columns with missing values:")
                print(', '.join(columns_with_null))

                col_name = input("Enter the column name to perform KNN imputation (Press -1 to go back): ")
                if col_name == "-1":
                    break

                if col_name not in columns_with_null:
                    print("Invalid column name. Please try again.")
                    continue

                # For simplicity, we use mean-based KNN imputation here.
                # In practice, you can use a library like fancyimpute for more sophisticated imputation methods.
                self.data[col_name].fillna(self.data[col_name].mean(), inplace=True)
                print("KNN imputation completed successfully.")
                
            except ValueError:
                print("Invalid input. Please enter a valid choice.")

    # Main function of the OutlierAndKNN class
    def process(self):
        while True:
            print("\nTasks\U0001F447")
            for task in self.tasks:
                print(task)

            try:
                choice = int(input("\nWhat do you want to do? (Press -1 to go back): "))
                if choice == -1:
                    break
                elif choice == 1:
                    self.handleOutliers()
                elif choice == 2:
                    self.knnImputation()
                elif choice == 3:
                    DataDescription.showDataset(self)
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid choice.")
