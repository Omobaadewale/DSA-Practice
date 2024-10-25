def search_sharp(arr, ele):
    return  any(i == ele for i in arr) # the any function returns true if at least one of the element is true

 

arr = [1,2,3,4,5,6,7,8,9,10]
ele = 11
print(search_sharp(arr,ele))#returns true or false