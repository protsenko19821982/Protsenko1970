#Створіть програму, яка перевіряє, чи є паліндромом введена фраза#
def palindrom_is(word):
    if word == word[::-1]:
        print("Паліндром")
    else:
        print("Не паліндром")

palindrom_is("level")
palindrom_is("hello")
