# question 1 - tested and worked

def hello_name(user_name):
    print('hello_' + user_name.upper() + '!')
hello_name('Buhay')


# question 2 - tested and worked
def first_odds():
    for n in range(1, 101):
        if n % 2 != 0:
            print(n)
first_odds()


# question 3 - tested but failed        
big = [333, 222, 1, 999, 4, 90009]
nums = [1111, 2, 23, 34, 45, 56, 9]        
# def max_num_in_list(a_list):
#     maximum = a_list[0]
#     for num in a_list:
#         if num > maximum:
#             maximum = num
#             return maximum
# print(max_num_in_list(big))

# question 3 - tested and worked
def max_num_in_list(a_list):
    return max(a_list)
print(max_num_in_list(nums))


# question 4 - tested and worked
def is_leap_year(a_year):
    if a_year % 100 == 0 and a_year % 400 == 0:
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year % 4 == 0:
        return True
    else:
        return False

print(is_leap_year(1600))


# question 5 - tested and worked
unordered = [9,3,2,4]
ordered = [1,2,3,4,5]

def is_consecutive(a_list):
    sequence = list(range(min(a_list), max(a_list) + 1)) # (start, stop, step)
    if a_list == sequence:
        return True
    else:
        return False
    
print(is_consecutive(ordered))