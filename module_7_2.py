def custom_write(file_names, strings):
    file = open(file_names, 'a', encoding='utf-8')
    dict_ = {}
    n = 0
    for i in strings:
        n += 1
        dict_[(n, file.tell())] = i
        file.write(i + '\n')
    file.close()
    return dict_

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
