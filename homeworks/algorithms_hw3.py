#When given a list, the program should return a list of all the elements
# below the original list’s arithmetical mean.
def below_mean(lst):
    mean = sum(lst) / len(lst)
    new_list = []
    for i in lst:
        if i < mean:
           new_list.append(i)
    return new_list

#my_list = [1,2,5,6]
#print(below_mean(my_list))

#When given a list of elements, find the two lowest elements.
#They can be equal to each other or different.
def two_lowest_elements(lst):
    lowest1 = min(lst)
    lst.remove(lowest1)
    lowest2 = min(lst)
    return [lowest1, lowest2]

my_list = [1, 2, 3, 4, 7, 1]
print(two_lowest_elements(my_list))

