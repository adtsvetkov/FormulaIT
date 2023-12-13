# TODO Найдите количество книг, которое можно разместить на дискете
value = 1.44
quantity_symbol = 25
quantity_line = 50
quantity_page = 100
weight_symbol = 4


value_bite = value*1024*1024
value_book = quantity_page*quantity_line*quantity_symbol*weight_symbol
number_book = int(value_bite/value_book)
print("Количество книг, помещающихся на дискету:", number_book)
