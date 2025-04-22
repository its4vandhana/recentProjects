def reverseLookup(dictionary,val):
    dictionary = {'a':1, 'b':2, 'c':2}
    lst = []
    for key, value in dictionary.items():
        if value == val:
            lst.append(key)
    print(lst)
reverseLookup({'a':1, 'b':2, 'c':2}, 3)
