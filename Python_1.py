#!/usr/bin/env python
# coding: utf-8

# Для тройки ближайших значений определить является ли цифра посередине больше левого значения и меньше правого значения

# In[38]:


get_ipython().run_cell_magic('time', '', "a = [1, 4, 6, 4, 6, 9, 1]\nc = []\ni = 0\nwhile i < len(a) - 2:\n    # print(i)\n    if a[i] < a[i + 1] and a[i + 1] < a[i + 2]:\n        b = 1\n        # print(i, a[i], '<', a[i + 1], '<', a[i + 2])\n        c.append(b)\n    i += 1\nprint(sum(c))")


# In[39]:


get_ipython().run_cell_magic('time', '', "a = [1, 4, 6, 4, 6, 9, 1]\nc = []\nfor i in range(len(a) - 2):\n    if a[i] < a[i + 1] and a[i + 1] < a[i + 2]:\n        b = 1\n        # print(i, a[i], '<', a[i + 1], '<', a[i + 2])\n        c.append(b)\nprint(sum(c))")


# Если сумма двух рядом стоящих цифр при делении на 920 дает остаток 3, то считаем такое событие, в противном случае - нет.

# In[42]:


k = [1, 2, 4, 6, 8, 4, 3, 6, 8, 5, 3, 2, 4, 5, 6, 8, 9, 0, 0, 9, 7, 5, 4, 3, 2, 4, 5, 7, 8, 9]


# In[55]:


l = []
for number in range(len(k) - 1): # range не включает границу, разве это уже не минус 1?
    n = (k[number] + k[number + 1]) % 920
    if (k[number] + k[number + 1]) % 920 == 3:
        m = 1
        l.append(m)
    # print(n, k[number], k[number + 1])
print(sum(l))
        


# In[47]:


(1 + 2) / 920


# In[45]:


(1 + 2) % 920 # почему 3? Питон берет ближайшее число после нулей?
# Перекладывание значений в пустой список не снижает скорость обработки кода?
