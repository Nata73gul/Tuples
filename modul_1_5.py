#Неизменяемые и изменяемые объекты. Кортежи.
immutable_var=(1,2,3,'cat','dog','bird',[2.5,4.7,8.1],True, False)
print(immutable_var)
print(type(immutable_var))
#immutable_var[0]=100
#Traceback (most recent call last):
 # File "D:\PythonUrbanUniversity\pythonProject\modul_1_5.py", line 4, in <module>
  #  immutable_var[0]=100
   # ~~~~~~~~~~~~~^^^
#TypeError: 'tuple' object does not support item assignment
#Кортежи (тип tuple) — это неизменяемый тип данных в Python, который используется
#для хранения упорядоченной последовательности элементов.

mutable_list=[1,2,3,'cat','dog','bird',[2.5,4.7,8.1], True, False]
print(mutable_list)
print(type(mutable_list))
mutable_list[3]='lion' # заменить элемент
print(mutable_list)
mutable_list[0]='a'# заменить элемент
print(mutable_list)
mutable_list[1]='b'# заменить элемент
print(mutable_list)
mutable_list[2]='c'# заменить элемент
print(mutable_list)
mutable_list.append(666)# добавить элемент в конец списка
print(mutable_list)
mutable_list.extend('elephant')# добавить элемент, разбив на символы
print(mutable_list)
mutable_list.extend(['elephant',8])# [  ] добавить элементы списком
print(mutable_list)
mutable_list.remove(False)# удалить елемент
print(mutable_list)
print('bird' in mutable_list) # проверка наличия элемента
print('bird' not in mutable_list) # проверка отсутствия элемента элемента
