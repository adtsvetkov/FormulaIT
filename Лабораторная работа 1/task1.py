numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index = 4
# TODO заменить значение пропущенного элемента средним арифметическим
sum_list = (sum(numbers[:index]) + sum(numbers[index+1:])) / len(numbers)

numbers[index] = sum_list
print("Измененный список:", numbers)
