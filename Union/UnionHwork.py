files = ['1.txt', '2.txt', '3.txt']


# Подсчет количества строк в файле и сортировка

def sort_files(file_list):
    files_dict = {}
    for file in file_list:
        with open(file, "r", encoding="utf-8") as text:
            for line_index, line in enumerate(text):
                i = line_index + 1
        files_dict[i] = file
    sorted_dict = sorted(files_dict.items())
    return sorted_dict


# Объединение всех файлов в один с заданным именем

def unite_all(file_list):
    with open(input('Введите имя нового общего файла: ')+'.txt', 'w') as new_file:
        for file in file_list:
            new_file.write(file[1])
            new_file.write('\n')
            new_file.write(str(file[0]))
            new_file.write('\n')
            with open(file[1], "r", encoding="utf-8") as text_file:
                for line in text_file:
                    new_file.write(line)
            new_file.write('\n')


unite_all(sort_files(files))
