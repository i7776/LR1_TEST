from task1 import RationalFraction
from task1.file_handler import write_file, write_pickle, read_pickle
from Services.input_output import get_natural_input, get_int_input
from task2.text_analizer import TextAnalyzer
from task2.file_manager import save_analysis_result, create_archive


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

def main():
    while True:
        print("\n=== Laboratory Work №4 ===")
        print("1. Run Task 1 (Rational Fractions)")
        print("2. Run Task 2 (Regex Text Analysis)")
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
            pass
        elif cmd == 3:
            #run_task3()
            pass
        elif cmd == 4:
            #run_task4()
            pass
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
