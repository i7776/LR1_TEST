import zipfile

def save_analysis_result(data, filename="analysis_result.txt"):
    """
    Saves the analysis results to a text file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("--- Text Analysis Report ---\n")
        f.write(f"Total sentences: {data['total']}\n")
        f.write(f"Declarative: {data['declarative']}\n") # .
        f.write(f"Interrogative: {data['interrogative']}\n") # ?
        f.write(f"Exclamatory: {data['exclamatory']}\n") # !
        f.write(f"Phone numbers: {', '.join(data['phones'])}\n")
        f.write(f"Average word length: {data['avg_len']}\n")
        if len(data['avg_words']) == 0: # Если список пустой
            f.write(f"Слов длиной {data['avg_len']} символов в строке нет\n")
        else:
            f.write(f"Words with avg length: {', '.join(data['avg_words'])}\n")
        f.write(f"Every seventh word: {', '.join(data['seventh'])}\n")
        f.write(f"Smiley count: {data['smiles']}\n")
    print(f"Result saved to {filename}")

def create_archive(result_file, archive_name="result.zip"):
    """
    Archives the result file and prints info about the archive
    """
    with zipfile.ZipFile(archive_name, 'w') as zipf:
        zipf.write(result_file)

    # Information about the file in the archive
    with zipfile.ZipFile(archive_name, 'r') as zipf:
        print(f"\nArchive created: {archive_name}")
        for file_info in zipf.infolist():
            print(f"File in archive: {file_info.filename}, Size: {file_info.file_size} bytes")