
import csv
import pickle

def write_file(lst):
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
    with open(filename, 'wb') as f:
        pickle.dump(lst, f)

def read_pickle(filename='file.pkl'):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

