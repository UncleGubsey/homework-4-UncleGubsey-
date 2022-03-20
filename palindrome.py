def is_palindrome(usr_str, start, end):

    if start == end:
        return True
    if usr_str[start] == " ":
        return is_palindrome(usr_str[0:start]+usr_str[start+1:], start, end-1)
    if usr_str[end] == " ":
        return is_palindrome(usr_str[0:end]+usr_str[end+1:], start, end-1)
    if usr_str[start] != usr_str[end]:
        return False
    return is_palindrome(usr_str, start + 1, end - 1)


usr_str = input("Enter a sentence: ")
print("Is the given sentence a palindrom? ",is_palindrome(usr_str, 0, len(usr_str) - 1))