import pickle

class FileHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    def save_data(self, data):
        with open(self.file_name, 'wb') as file:
            pickle.dump(data, file)

    def load_data(self):
        try:
            with open(self.file_name, 'rb') as file:
                data = pickle.load(file)
                return data
        except FileNotFoundError:
            print("File not found.")
            return None