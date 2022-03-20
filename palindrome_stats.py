def is_palindrome(word):
    if len(word)<=1: return len(word)

    if word[0]==" ":
        res = is_palindrome(word[1:])
        if res == -1:
            return -1
        return res
    
    if word[-1]==" ":
        res = is_palindrome(word[:-1])
        if res == -1:
            return -1
        return res

    if word[0]!=word[-1]: return -1
    res = is_palindrome(word[1:-1])
    if res == -1:
        return -1
    return res+2

if __name__ == "__main__":
    infile = open('words.txt')
    num_palindromes = 0

    largest_size = 0
    smallest_size = -1

    largest_list = []
    smallest_list = []

    for word in infile:
        word = word.strip()
        size = is_palindrome(word)
        if size != -1:
            num_palindromes += 1

            if largest_size < size:
                largest_list = [word]
                largest_size = size

            elif largest_size == size:
                largest_list.append(word)
            

            if smallest_size == -1 or smallest_size > size:
                smallest_list = [word]
                smallest_size = size

            elif smallest_size == size:
                smallest_list.append(word)

    print(str(num_palindromes) + " palindromes")
    print("Shortest: ", smallest_list)
    print("Longest: ", largest_list)