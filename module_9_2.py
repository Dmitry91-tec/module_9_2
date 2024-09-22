first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']               #первый список
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']   #второй список

first_result = [len(x) for x in first_strings if len(x)>4]    #список состоящий из длин строк
print(first_result)
second_result = [(x,y) for x in first_strings for y in second_strings if len(x)==len(y)] #cписок из пар слов одинаковой длины
print(second_result)
first_strings.extend(second_strings)
print(first_strings)
third_result = {x:len(x) for x in first_strings if not len(x)%2} #словарь ключ-значение: строка-длина строки
print(third_result)