# description: bubble_sort
# date: 2021/4/30 1:28 下午
# author: objcat
# version: 1.0

def bubble_sort(collection):
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break
    return collection


if __name__ == '__main__':
    print(bubble_sort([2, 1]))
