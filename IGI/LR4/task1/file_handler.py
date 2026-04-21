
import csv
import pickle

def write_file(lst):
    """
    Serializes a list of objects and saves them to a CSV file
    """
    try:
        data = []
        for obj in lst:
            d = obj.to_dict()
            data.append(d)

        fieldnames = data[0].keys()

        with open('file.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    except Exception as e:
        print(f'Error: {e}')

def write_pickle(lst, filename='file.pkl'):
    """
    Serializes a list of objects into a binary format using pickle
    """
    with open(filename, 'wb') as f:
        pickle.dump(lst, f)

def read_pickle(filename='file.pkl'):
    """
    Deserializes and returns data from a binary pickle file
    """
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

