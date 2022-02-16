eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

lang = input('выберите язык. англ = eng, рус = rus: ')
while lang != 'eng' and lang != 'rus':
    lang = input('это что за язык такой? ')

k = int(input('введите ключ сдвига: '))

print('выберите операцию:')
oper = input('шифрование или дешифрование: ')
while oper != 'шифрование' and oper != 'дешифрование':
    oper = input('такой операции нет, давайте ещё раз: ')

def encryption(lang, k):
    s = input('введите исходный текст: ')
    for i in s:
        if lang == 'rus':
            