
def swap(s, x, y):
    s[x], s[y] = s[y], s[x]

def insertion_sort(s):
    for p in range(1, len(s)):
        for i in range(0, p):
            if s[p] < s[i]:
                swap(s, p, i)
    return s

def bubble_sort(s):
    for p in reversed(range(1, len(s))):
        for i in range(p):
            if s[i] > s[i+1]:
                swap(s, i, i+1)
    return s

def selection_sort(s):
    for p in range(len(s)-1):
        for i in range(p, len(s)):
            if s[p] > s[i]:
                swap(s, p, i)
    return s

def merge_sort(s):
    if len(s) <= 1:
        return s
    mid = len(s)//2
    return merge(merge_sort(s[:mid]), merge_sort(s[mid:]))

def merge(left, right):
    i, j, s = 0, 0, []
    while (i<len(left)) and (j<len(right)):
        if left[i] < right[j]:
            s.append(left[i])
            i += 1
        else:
            s.append(right[j])
            j += 1
    while i < len(left):
        s.append(left[i])
        i += 1
    while j < len(right):
        s.append(right[j])
        j += 1
    return s
    

print(merge_sort([71, 2, 38, 5, 7, 61, 11, 26, 53, 42]))
print(selection_sort([8,5,6,2,4]))
print(bubble_sort([8,5,6,2,4]))
print(insertion_sort([8,5,6,2,4]))
