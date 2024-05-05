import random

def inputListLength():
    
    list_length:int = int(input("Enter the length of your list: "))
    
    return list_length

def inputLowRange():
    
    num_range_low:int = int(input("Enter the lowest possible number to be generated in the list: "))

    return num_range_low

def inputHighRange():
    
    num_range_high:int = int(input("Enter the highest possible number to be generated in the list: "))

    return num_range_high

def createList(list_length:int, num_range_low:int, num_range_high:int):
    
    unsorted_list = []
    
    for i in range(list_length):
        random_number = random.randint(num_range_low,num_range_high)
        unsorted_list.append(random_number)
    
    return unsorted_list

def bubbleSort(sorting_list, list_length):
    
    for i in range(list_length):
        for j in range(0, list_length-i-1):
            if sorting_list[j] > sorting_list[j+1]:
                sorting_list[j], sorting_list[j+1] = sorting_list[j+1], sorting_list[j]
    
    return sorting_list

