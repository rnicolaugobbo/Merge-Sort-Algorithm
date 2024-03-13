def merge(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        elif left[0] > right[0]:
            result.append(right[0])
            right.pop(0)
        else:
            result.append(left[0])
            result.append(right[0])
            left.pop(0)
            right.pop(0)
    if left:
        result += left
    elif right:
        result += right
    return result

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    middle_index = len(lst) // 2
    left_split = lst[:middle_index]
    right_split = lst[middle_index:]
    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)
    return merge(left_sorted, right_sorted)