# Задача №3

files = ['1.txt', '2.txt', '3.txt']

content = {}

for file_name in files:
    with open(file_name, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        content[file_name] = lines

for file_name, lines in content.items():
    content[file_name] = [f'{file_name}\n', f'{len(lines)}\n'] + lines + [f'\n']

sorted_content = {a: b for a, b in sorted(content.items(), key=lambda item: item[1][1])}

with open('final_file.txt', 'w') as file:
    for lines in sorted_content.values():
        file.writelines(lines)

print('\n all files is sorted and recorded in final file \n')
        