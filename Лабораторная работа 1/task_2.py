# TODO Найдите количество книг, которое можно разместить на дискете
size_mb = 1.44
count_list = 100
count_string = 50
count_symbols = 25
code_symbol_byte = 4

count_true_symbols = size_mb * 1024 * 1024
count_have_symbols = count_list * count_string * count_symbols * code_symbol_byte
count_books = count_true_symbols // count_have_symbols

print("Количество книг, помещающихся на дискету:", round(count_books))
