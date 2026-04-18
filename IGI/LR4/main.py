from task1 import RationalFraction
from task1.file_handler import write_file, write_pickle, read_pickle


def main():
    fractions_list = []

    print("Введи 10 дробей:")
    for i in range(1, 11):
        n = int(input(f"Дробь {i} (числитель): "))
        d = int(input(f"Дробь {i} (знаменатель): "))
        fractions_list.append(RationalFraction(n, d))

    write_file(fractions_list)
    write_pickle(fractions_list)


    print("\nПроверка: считываем из файла Pickle:")
    loaded_data = read_pickle()
    for item in loaded_data:
        print(item)

    data = read_pickle() # Получили список объектов

    fractions_dict = {i: data[i] for i in range(len(data))}


    print("\nПроверка на наличие равных чисел:")
    found_equal = False
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                print(f"Найдено: {data[i]} равно {data[j]}")
                found_equal = True
    if not found_equal:
        print("Равных чисел нет.")

    max_val = max(data) # Твой метод __lt__
    print(f"\nНаибольшее число: {max_val}")

    print("\nВведите дробь, чтобы найти её в файле:")
    n_in = int(input("Числитель: "))
    d_in = int(input("Знаменатель: "))
    target = RationalFraction(n_in, d_in)

    if target in data:
        print(f"Число {target} есть в файле!")
    else:
        print("Такого числа в файле нет.")

if __name__ == "__main__":
    main()
