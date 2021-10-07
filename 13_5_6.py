# объявление функции
def is_palindrome(text):
    text = text.lower().strip()
    for char in ' .,-!?':
        text = text.replace(char, '')
    return text == text[::-1]



# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))