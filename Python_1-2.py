#!/usr/bin/env python
# coding: utf-8

# Для тройки ближайших значений определить является ли цифра посередине больше левого значения и меньше правого значения

# In[38]:


get_ipython().run_cell_magic('time', '', "a = [1, 4, 6, 4, 6, 9, 1]\nc = []\ni = 0\nwhile i < len(a) - 2:\n    # print(i)\n    if a[i] < a[i + 1] and a[i + 1] < a[i + 2]:\n        b = 1\n        # print(i, a[i], '<', a[i + 1], '<', a[i + 2])\n        c.append(b)\n    i += 1\nprint(sum(c))")


# In[39]:


get_ipython().run_cell_magic('time', '', "a = [1, 4, 6, 4, 6, 9, 1]\nc = []\nfor i in range(len(a) - 2):\n    if a[i] < a[i + 1] and a[i + 1] < a[i + 2]:\n        b = 1\n        # print(i, a[i], '<', a[i + 1], '<', a[i + 2])\n        c.append(b)\nprint(sum(c))")


# In[57]:


get_ipython().run_cell_magic('time', '', 'a = [1, 4, 6, 4, 6, 9, 1]\nc = 0\ni = 0\nwhile i < len(a) - 2:\n    # print(i)\n    if a[i] < a[i + 1] and a[i + 1] < a[i + 2]:\n        c += 1\n    i += 1\nprint(c)')


# Если сумма двух рядом стоящих цифр при делении на 920 дает остаток 3, то считаем такое событие, в противном случае - нет.

# In[62]:


k = [1, 2, 4, 6, 8, 4, 3, 6, 8, 5, 3,]


# In[82]:


l = 0
for number in range(len(k) - 1): 
    n = (k[number] + k[number + 1]) % 920
    if n == 3:
        l += 1
    # print(n, k[number], k[number + 1])
print(l)      


# In[72]:


k = [1, 2, 4, 6, 8, 4, 3, 6, 8, 5, 3,]
p = 0
i = 0
k[p - i] + k[i] + k[i + p]
k[0 - 0] + k[0] + k[0 + 0]
# Шаг первый
for number in range(len(k)): # проходимся по цифрам от 0 до длины списка
    s = len(k) - number # находим длину списка для каждого шага
    print(number, s)


# In[9]:


k = [1, 2, 4, 6, 8, 4, 3, 6, 8, 5, 3]
n = 0   
for i in range(len(k)-1):
    for idx in range(i, len(k) - 1):
        m = (k[i] + k[idx + 1]) % 10
        if m == 2:
            n += 1
        # print(idx, m, i)
print(n)


# In[27]:


s = "Hello my my friend"
print(s[2])
print(s[-4])
print(s[0:3])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])

print(s.replace("my", "your"))
print(s.count("my"))
print(s.replace("my", '').replace("   ", " "))


#  Ввести строку пользователем, считать ее и убрать дубликаты

# In[19]:


user = input()
b = []
for number in user:
    if number not in b:
        b.append(number)
print(b)


# Перевернуть слово и вывести сообщение о том, является ли слово палиндромом

# In[36]:


name = 'Anna'
small_letters = name.lower()
if small_letters[::-1] == small_letters:
    print('Палиндром')
else:
    print('Обычное слово')


# Вывести только цифры

# In[43]:


stroka = '25342ysjaksdhfg63ueyiw211'
import re
re.findall(r'\d',stroka)


# In[46]:


stroka = '25342ysjaksdhfg63ueyiw211'
a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
b = []
for number in stroka:
    if number in a:
        b.append(number)
print(b)


# In[222]:


stroka = '25342ysjaksdhfg63ueyiw211'
ord('a')


# Вывечти среднюю оценку за курс

# In[227]:


user = int(input()) - 1
if user >= 8:
    print('В данном случае студенты учатся на 8 курсах')
else:
    def A(x):
        marks = {'Mary' : [5, 8, 9, 10, 3, 5, 6, 6],
             'John' : [3, 3, 6, 8, 2, 1, 8, 5],
             'Alex' : [4, 4, 7, 4, 7, 3, 2, 9],
             'Patricia' : [2, 1, 6, 8, 2, 3, 7, 4]} # Нужно ли присваивать значения переменным внутри функции?
        summa = 0 # выдает ошибку, если не присвоить значение переменной 
        for name in marks:
            number = marks[name][x]
            summa += number
        average = summa // len(marks)
        return average

    average = A(user)
    print(average)


# In[234]:


def B(x):
    categories = {'отлично' : [8, 9, 10],
              'хорошо' : [6, 7],
              'удовлетворительно' : [4, 5],
              'неуд' : [0, 1, 2, 3]}
    for count in categories:
        ocenka = categories[count]
        if x in ocenka:
            return count
B(5)


# In[125]:


t =[]
for i in range(len(marks['Mary'])):
    n = A(i)
    t.append(n)
print(max(t))


# In[132]:


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = 0
for i in range(0, 3):
    for j in range(0, 3):
        s += a[i][j] # проход по строкам
    print(s)
    s = 0


# In[133]:


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = 0
for i in range(0, 3):
    for j in range(0, 3):
        s += a[j][i] # проход по столбцам
    print(s)
    s = 0


# In[134]:


s = 0
for i in range(3):
    s += a[i][i]
print(s)


# In[184]:


magic = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]


# In[212]:


magic = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

x = 0
y = 0
z = 0
p = 0


for stroka in range(0, 4):
    for column in range (0, 4):
        # print(stroka, column)
        x += magic[stroka][column]
        y += magic[column][stroka]
        z += magic[stroka][stroka]
        p += magic[column][column]
    print(x, y, z, p)
    if x != y or x != z or x != p:
        break
    x = 0
    y = 0
    z = 0
    p = 0


# In[ ]:




