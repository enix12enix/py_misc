def insertion_sort(input, comparison_func = lambda x, y: x < y):
    output = []
    if len(input) > 0:
        output.append(input[0])
        i = 1
        while i < len(input):
            output.append(input[i])
            j = len(output) - 1
            while j > 0:
                if comparison_func(output[j], output[j - 1]):
                     tmp_val = output[j -1]
                     output[j - 1] = output[j]
                     output[j] = tmp_val
                j = j - 1
            i = i + 1
    return output

def sorted_by_asc(input):
    return insertion_sort(input)

def sorted_by_desc(input):
    return insertion_sort(input, comparison_func = lambda x, y: x > y)

def find_v(input_list, v):
    for i in xrange(len(input_list)):
        if v == input_list[i]: return i

def binary_add(list1, list2):
    i =  len(list1) - 1
    list3 = range(0, len(list1) + 1)
    j = 0
    while i > -1:
        val = list1[i] & list2[i] & j
        list3[i + 1] = val
        if val == 0: j = 1
        i = i - 1
    list3[0] = j
    return list3

def bubble_sort(input):
    for i in xrange(1, len(input)):
        if input[i-1] > input[i]:
            val = input[i-1]
            input[i-1] = input[i]
            input[i] = val
            for j in xrange(1, i):
                if input[j-1] > input[j]:
                    val = input[j-1]
                    input[j-1] = input[j]
                    input[j] = val
    return input

def selection_sort(input):
    for i in xrange(0, len(input)):
        min = input[i]
        index = i
        for j in xrange(i+1, len(input)):
            if input[j] < min:
                min = input[j]
                index = j
        input[index] = input[i]
        input[i] = min
    return input





if __name__ == '__main__':
    import random
    import time
    print sorted_by_asc([31,41,59,26,41,58])
    print sorted_by_desc([31,41,59,26,41,58])
    input = range(0, 10000)
    random.shuffle(input)
    print '#'*20
    start = int(time.time())
    sorted_by_desc(input)
    print int(time.time()) - start
    print '#'*20
    print find_v([1,2,3], 2)
    print find_v([1,2,3], 4)
    print binary_add([1,1,0,1], [1,0,1,1])
    print '#'*20
    start = int(time.time())
    bubble_sort(input)
    print int(time.time()) - start
    print '#'*20
    print selection_sort([31,41,59,26,41,58])
    input2 = range(0, 100000)
    random.shuffle(input2)
    print '#'*20
    start = int(time.time())
    selection_sort(input2)
    print int(time.time()) - start
    print '#'*20
