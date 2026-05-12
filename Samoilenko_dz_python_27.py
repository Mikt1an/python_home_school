#1
try:
    file_name = input("Enter file name: ")
    key_word = input("Enter keyword: ")

    found_lines = []

    with open(file_name, "rt", encoding="utf-8") as f:
        for line in f:
            if key_word.lower() in line.lower():
                found_lines.append(line)

    if found_lines:
        new_file = f"{key_word}_{file_name}"
        with open(new_file, "wt", encoding="utf-8") as fi:
            fi.writelines(found_lines)
            print(f"Line, content {key_word} saved to {new_file}")
    else:
        print(f"No lines found for {key_word}")

except FileNotFoundError:
    print(f"File {file_name} not found")

#2
try:
    file_name = input("Enter file name: ")

    unique_file =[]

    with open(file_name, "rt", encoding="utf-8") as f:
        for line in f:
            if line not in unique_file:
                unique_file.append(line)

        f.close()

    new_file = f"unique_{file_name}"
    with open(new_file, "wt", encoding="utf-8") as fi:
        fi.writelines(unique_file)
        fi.close()

    print(f"Duplicates removed. Unique strings are preserved {new_file}")

except FileNotFoundError:
    print(f"File {file_name} not found.")