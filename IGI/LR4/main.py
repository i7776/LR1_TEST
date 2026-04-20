from task1 import RationalFraction
from task1.file_handler import write_file, write_pickle, read_pickle
from Services.input_output import get_natural_input, get_int_input, get_float_input, print_table_row, print_table_footer, print_table_header
from task2.text_analizer import TextAnalyzer
from task2.file_manager import save_analysis_result, create_archive
from task3.task3 import TaylorSin, math_sin
from task4.geometry import InscribedSquare


def run_task1():
    """
    Executes Task 1 (Rational Fractions, Variant 15)
    """
    print("\n--- Task 1: Rational Fractions ---")
    fractions_list = []

    print("Enter 10 rational fractions:")
    for i in range(1, 11):
        try:
            n = int(input(f"Fraction {i} (numerator): "))
            d = int(input(f"Fraction {i} (denominator): "))
            fractions_list.append(RationalFraction(n, d))
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again for this fraction.")
            continue

    write_file(fractions_list)
    write_pickle(fractions_list)

    print("\n[Reading from Pickle file...]")
    data = read_pickle()

    fractions_dict = {i + 1: data[i] for i in range(len(data))}

    print("\nChecking for equal fractions:")
    found_equal = False
    items = list(fractions_dict.values())

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]: # __eq__
                print(f"Found match: {items[i]} is equal to {items[j]}")
                found_equal = True

    if not found_equal:
        print("No equal fractions found.")

    max_val = max(fractions_dict.values()) # __lt__
    print(f"\nMaximum fraction: {max_val}")

    print("\nEnter a fraction to search in file:")
    try:
        n_in = int(input("Numerator: "))
        d_in = int(input("Denominator: "))
        target = RationalFraction(n_in, d_in)

        if target in fractions_dict.values():
            print(f"Success: Fraction {target} found in file!")
        else:
            print("Fraction not found in file.")
    except ValueError as e:
        print(f"Error during search: {e}")


def run_task2():
    with open('source.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    analyzer = TextAnalyzer(text)
    total, decl, inter, excl = analyzer.analyze_sentences()

    results = {
        'total': total,
        'declarative': decl,
        'interrogative': inter,
        'exclamatory': excl,
        'phones': analyzer.phone_numbers(),
        'avg_len': analyzer.average_length()[0],
        'avg_words': analyzer.average_length()[1],
        'seventh': analyzer.seventh_words(),
        'smiles': analyzer.smile()
    }

    save_analysis_result(results)
    create_archive("analysis_result.txt")


def run_task3():
    """
    Executes Task 3
    """
    print("\n--- Task 3 ---")

    x = get_float_input("Enter value for x: ")
    eps_choice = input("Enter precision eps (press Enter to use default 0.0001): ")
    if eps_choice.strip() == "":
        eps = 0.0001
    else:
        try:
            eps = float(eps_choice)
        except ValueError:
            print("Invalid input for eps. Using default 0.0001")
            eps = 0.0001

    calculator = TaylorSin(x, eps)
    taylor_result, n_iterations = calculator.calculate()
    math_result = math_sin(x)

    print_table_header()
    print_table_row(x, n_iterations, taylor_result, math_result, eps)
    print_table_footer()

    stats = calculator.get_statistics()
    print("\n--- Sequence Statistics ---")
    print(f"Mean (Среднее):   {stats['mean']:.6f}")
    print(f"Median (Медиана): {stats['median']:.6f}")
    print(f"Mode (Мода):      {stats['mode']}")
    print(f"Variance (Дисп.): {stats['variance']:.6f}")
    print(f"Std Dev (СКО):    {stats['stdev']:.6f}")

    calculator.plot_graph()

def run_task4():
    print("\n--- Task 4 ---")

    try:
        radius = get_float_input("Enter floating number:")

        color = input("Enter the color of the square (e.g., red, blue, green): ")
        text_label = input("Enter text label for the center of the figure: ")
    except ValueError:
        print("Error: Radius must be a valid number!")
        return

    my_square = InscribedSquare(radius, color)

    print("\nObject created successfully:")
    print(my_square)

    my_square.draw(text_label)

def main():
    while True:
        print("\n=== Laboratory Work №4 ===")
        print("1. Run Task 1 (Rational Fractions)")
        print("2. Run Task 2 (Text Analysis)")
        print("3. Run Task 3 (Math/Matplotlib)")
        print("4. Run Task 4 (Geometry Classes)")
        print("5. Run Task 5 (NumPy Statistics)")
        print("6. Run Task 6 (Pandas Analysis)")
        print("0. Exit")

        cmd = get_int_input("\nSelected task:")

        if cmd == 1:
            run_task1()
        elif cmd == 2:
            run_task2()
        elif cmd == 3:
            run_task3()
        elif cmd == 4:
            run_task4()
        elif cmd == 5:
            #run_task5()
            pass
        elif cmd == 6:
            #run_task6()
            pass
        elif cmd == 0:
            print("Exiting...")
            break
        else:
            print("Please, choose the number of the task (from 0 to 6)")

if __name__ == "__main__":
    main()
