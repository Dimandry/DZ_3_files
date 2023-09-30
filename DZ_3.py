import os

ls = [i for i in os.listdir() if i.endswith('.txt')]
lines = 0
line_dict = {}
for j in ls:
    with open(j, encoding='utf-8') as x:
        for file in x:
            lines += 1
    line_dict.setdefault(j, lines)
    lines = 0
sorted_values = sorted(line_dict.values())
sorted_dict = {}
for i in sorted_values:
    for k in line_dict.keys():
        if line_dict[k] == i:
            sorted_dict[k] = line_dict[k]
            break
with open('Result.txt', "w", encoding='utf-8') as file:
    for name, line in sorted_dict.items():
        s = open((name), encoding='utf-8').read()
        file.write(name + '\n')
        file.write(str(line) + '\n')
        file.write(s + '\n')
result = open('Result.txt', encoding='utf-8').read()
print(result)
os.remove('Result.txt')
