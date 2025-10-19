def mergesort(s):
    if len(s) > 1:
        mid = len(s)//2
        left_arr = s[:mid]
        right_arr = s[mid:]
        mergesort(left_arr)
        mergesort(right_arr)
        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                s[k] = left_arr[i]
                i += 1
            else: 
                s[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            s[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            s[k] = right_arr[j]
            j += 1
            k += 1
    return s
s = [9,2,10,20,1,6,7]
print(mergesort(s))