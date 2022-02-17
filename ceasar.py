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

def ceasar_cypher(oper, lang, k):

    s = input('введите исходный текст: ')
    result = ''

    if oper == 'дешифрование':
    	k *= -1

    if lang == 'eng':
    	upper_alphabet = eng_upper_alphabet
    	lower_alphabet = eng_lower_alphabet
    	n = 26

    else:
    	upper_alphabet = rus_upper_alphabet
    	lower_alphabet = rus_lower_alphabet
    	n = 32

    for i in s:
    	if i.isalpha():
    		if i.isupper():
    			result += upper_alphabet[(upper_alphabet.index(i) + k) % n]

    		else:
    			result += lower_alphabet[(lower_alphabet.index(i) + k) % n]

    	else:
    		result += i

    return f'итоговый текст: {result}' 


print(ceasar_cypher(oper, lang, k))