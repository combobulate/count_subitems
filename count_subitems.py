def howMany(aSet):
    '''
    aSet: Any compound data type, which may contain compound data types
    which may themselves contain further compound data types, etc. IE
    howMany([4, (abs, 'b')]) will return 3.
    
    Will actually support being passed any other data type, simply returning
    a count of 1 for anything not compound. So howMany(True) will return
    1, if you really want to do that.

    returns: int, how many values are in the compound data type, exclusive
    of the compound data type itself or any such in its contents.
    '''
    # Your Code Here
    if type(aSet) in [list, tuple]:
        return sum([howMany(x) for x in aSet])
    elif type(aSet) in [dict]:
        return sum([howMany(aSet[x]) for x in aSet])
    else:
        return 1
