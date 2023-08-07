import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from data_description import DataDescription

class CustomPreprocessingPipeline:
    # The Task associated with this class.
    tasks = [
        '\n1. Custom Preprocessing Pipeline',
        '2. Show the Dataset'
    ]

    def __init__(self, data):
        self.data = data

    # Function to apply the custom preprocessing pipeline to the data
    def preprocessData(self):
        while True:
            print("\n1. Apply Custom Preprocessing Pipeline")
            print("2. Go Back")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 2:
                    break
                elif choice != 1:
                    print("Invalid choice. Please try again.")
                    continue

                columns = self.data.columns
                numeric_columns = self.data.select_dtypes(include=["float64", "int64"]).columns
                categorical_columns = list(set(columns) - set(numeric_columns))

                # Min-Max scaling for numeric columns
                if not numeric_columns.empty:
                    scaler = MinMaxScaler()
                    self.data[numeric_columns] = scaler.fit_transform(self.data[numeric_columns])

                # One-Hot encoding for categorical columns
                if categorical_columns:
                    encoder = OneHotEncoder()
                    encoded_features = encoder.fit_transform(self.data[categorical_columns])
                    encoded_df = pd.DataFrame(encoded_features.toarray(), columns=encoder.get_feature_names(categorical_columns))
                    self.data.drop(categorical_columns, axis=1, inplace=True)
                    self.data = pd.concat([self.data, encoded_df], axis=1)

                print("Custom preprocessing pipeline applied successfully.")
                
            except ValueError:
                print("Invalid input. Please enter a valid choice.")

    # Main function of the CustomPreprocessingPipeline class
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
                    self.preprocessData()
                elif choice == 2:
                    DataDescription.showDataset(self)
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid choice.")
