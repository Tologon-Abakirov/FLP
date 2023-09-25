#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_longest_word(sentence):
    words = sentence.split()  # Разделяем строку на слова
    longest_word = ""
    
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word

# Пример использования
sentence = input("Введите строку: ")
longest_word = find_longest_word(sentence)

if longest_word:
    print("Самое длинное слово:", longest_word)
    
else:
    print("Строка пуста.")


# In[2]:


def find_longest_word_by_delimiter(sentence, delimiter):
    words = sentence.split(delimiter)  # Разделяем строку на слова
    longest_word = ""
    
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word

# Пример использования
sentence = input("Введите строку: ")
delimiter = ";"  # Используем точку с запятой как разделитель
longest_word = find_longest_word_by_delimiter(sentence, delimiter)

if longest_word:
    print("Самое длинное слово:", longest_word)
else:
    print("Строка пуста.")


# In[3]:


def find_shortest_word_with_char(sentence, char):
    words = sentence.split()  # Разделяем строку на слова
    shortest_word = None

    for word in words:
        # Проверяем, содержит ли слово символ
        if char in word:
            # Или можно заменить на: if word.find(char) != -1:
            if shortest_word is None or len(word) < len(shortest_word):
                shortest_word = word
    
    return shortest_word

# Пример использования
sentence = input("Введите строку: ")
char = input("Введите символ: ")

shortest_word = find_shortest_word_with_char(sentence, char)

if shortest_word:
    print("Самое короткое слово с символом '{}': {}".format(char, shortest_word))
else:
    print("Нет слов с символом '{}'.".format(char))


# In[4]:


def find_word_in_sentence(sentence, word):
    words = sentence.split()  # Разделяем строку на слова

    if word in words:
        return True
    else:
        return False

# Пример использования
sentence = input("Введите строку: ")
word_to_find = input("Введите слово для поиска: ")

if find_word_in_sentence(sentence, word_to_find):
    print("Слово '{}' найдено в строке.".format(word_to_find))
else:
    print("Слово '{}' не найдено в строке.".format(word_to_find))


# In[5]:


def count_words(sentence):
    words = sentence.split()  # Разделяем строку на слова
    return len(words)

# Пример использования
sentence = input("Введите предложение: ")

word_count = count_words(sentence)
print("Количество слов в предложении:", word_count)


# In[ ]:


# In[ ]:





# In[ ]:




