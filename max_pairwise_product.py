# Uses python3

def max_pairwise_product(numbers):
    n = len(numbers)
    index1 = 0
    index2 = 0
    product = 0
    for i in range(1, n):
        if numbers[i] > numbers[index1]:
            index1 = i

    if index1 == 0:
        index2 = 1
    else:
        index2 = 0

    for j in range(1, n): 
        if (numbers[j] > numbers[index2]) & (j != index1):
            index2 = j

    product = numbers[index1] * numbers[index2]
    return product

if __name__ == '__main__':
    n = int(input()) 
    a = [int(x) for x in input().split()]
    print(max_pairwise_product(a))

