from collections import defaultdict


# TODO  Напишите функцию count_letters
def count_letters(text: str):
    letters_dict = defaultdict(int)
    text = text.lower()
    for char in text:
        if char.isalpha():
            letters_dict[char] += 1
    return letters_dict


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letters: dict):
    total_letters = sum(letters.values())
    freq_dict = {key: (value / total_letters) for key, value in letters.items()}
    return freq_dict


def print_dict(custom_dict: dict):
    for key, value in custom_dict.items():
        print(key + ": " + str(format(value, ".2f")))


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

# TODO Распечатайте в столбик букву и её частоту в тексте
letters_count = count_letters(main_str)
text_freq = calculate_frequency(letters_count)
print_dict(text_freq)
