def max_product(numString, productLen):
    maxProduct = 0

    # Iterate through number input
    for i in range(0, len(numString) - productLen):
        product = 1

        # find product of numbers for length
        for j in range(0, productLen):
            product = product * int(numString[i + j])

        # If the new product is larger it is the maximum product
        if (product > maxProduct):
            maxProduct = product

    return maxProduct

with open('problem8.txt') as f:
    lines = f.readlines()
    num = ""

    for line in lines:
        num = num + line.rstrip("\n")

    print(max_product(num, 13))
