# multipleiterator
iterate multiple list

there are 3 list
list1 = [1, 2, 3, 4, 5]
list2 = [int.__add__, int.__sub__]
list3 = [7, 6, 5, 4]

    for x in list1:
        for operator in list2:
            for y in list3:
                print operator(x, y)
    
But if there are 4 list or more?

pip install multipleiterator

    from multipleiterator import multipleiter
    for x, operator, y in multipleiter(list1, list2, list3):
        print operator(x, y)
  
# The world is clean  
