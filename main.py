
def sum_num(number):
    num = tuple(number)
    s = 0
    for i in range(len(num)):
        if (num[i]).isdigit():
            s += int(num[i])
    return s

for l in range(10):
    enter_number = input("Enter any number:")
    print(sum_num(enter_number))
