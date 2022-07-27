import random
from math import ceil
def length(length):
    while not(length.isdigit()):
        length = input('Какой длинны вы хотите, чтобы были пароли?')
    else:
        return length

def count(count):
    while not(count.isdigit()):
        count = input('Сколько паролей вы хотите сгенерировать?')
    else:
        return count

def right(answer):
    while answer.lower() != 'да' and answer.lower() != 'нет':
        answer = input('Так "Да" или "Нет"')
    else:
        if answer.lower() == 'да':
            answer = True
        else:
            answer = False
    return answer

def generate_password(length, chars):
    if length > len(chars):
        print(*random.sample(chars * ceil(length / len(chars)), length), sep = '')
    else:
        print(*random.sample(chars, length), sep = '')

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''
count_pwd = input('Сколько паролей вы хотите сгенерировать?')
count_pwd = count(count_pwd)
length_pwd = input('Какой длинны вы хотите, чтобы были пароли?')
length_pwd = length(length_pwd)
dig_inc = input('Включать ли цифры 0123456789? "Да" или "Нет"')
dig_inc = right(dig_inc)
upp_l_inc = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? "Да" или "Нет"')
upp_l_inc = right(upp_l_inc)
low_l_inc = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? "Да" или "Нет"')
low_l_inc = right(low_l_inc)
sym_inc = input('Включать ли символы !#$%&*+-=?@^_? "Да" или "Нет"')
sym_inc = right(sym_inc)
mys_ninc = input('Исключать ли неоднозначные символы il1Lo0O? "Да" или "Нет"')
mys_ninc = right(mys_ninc)
if dig_inc:
    chars += digits
if upp_l_inc:
    chars += uppercase_letters
if low_l_inc:
    chars += lowercase_letters
if sym_inc:
    chars += punctuation
if mys_ninc:
    chars = chars.replace('i', '')
    chars = chars.replace('1', '')
    chars = chars.replace('l', '')
    chars = chars.replace('L', '')
    chars = chars.replace('o', '')
    chars = chars.replace('0', '')
    chars = chars.replace('O', '')
print(chars)
for i in range(int(count_pwd)):
    generate_password(int(length_pwd), chars)
