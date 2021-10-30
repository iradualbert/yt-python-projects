def remove_duplicates(arr):
    new_arr = list(set(arr))
    if type(arr) == str:
        return "".join(new_arr)
    return new_arr

print(remove_duplicates([1,23,3,45,2,1,2,4]))
print(remove_duplicates("aasfdfdafdsadsfewrewaaaa"))