# TODO  Напишите функцию count_letters
def count_letters(text):
    dictionary = {}
    for i in text.lower():
        if i.isalpha():
            letters = 0
            for j in text.lower():
                if i == j:
                    letters += 1
            dictionary[i] = letters
    return dictionary
# TODO Напишите функцию calculate_frequency


def calculate_frequency(dict_, count_):
    b = {}
    for letter, number in dict_.items():
        frequency = round(number / count_, 2)
        b[letter] = frequency
    return b


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

letter_ = 0
for a in main_str:
    if a.isalpha():
        letter_ += 1

# TODO Распечатайте в столбик букву и её частоту в тексте
new_dictionary = calculate_frequency(count_letters(main_str), letter_)
for letters_, numb in new_dictionary.items():
    print(f"{letters_}: {numb:.2f}")
