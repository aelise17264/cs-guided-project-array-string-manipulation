#how do we implement an array-reverse function in-place?
def reverse(arr):
    #this won't work b/c under the hood slicing creates a copy of the input array
    #return arr[::-1]
    #we want to swap indexes
    #keep track of the current ends of the list then swap those elements
    #two pointer approach
    left = 0
    right = len(arr) -1
    #how do we iterate?
    #iterate so long as left < right, this will work for even & odd # of elements
    while left < right:
        #this does use an extra temp variable under the hood
        arr[left], arr[right] = arr[right], arr[left]
        #increment the left pointer & decrement the right pointer
        left += 1
        right -= 1

    #this is an in-place way to do this
    #if there's an odd number of elements in the input arr
    #we have a case where left & right are going to land on the middle element

    return arr
print(reverse([0,1,2,3,4,5]))