def is_palindrome(word):
    return word == "".join(reversed(word))

words = input().split(" ")
search_palindrome = input()

palindromes = [word for word in words if is_palindrome(word)]
print(palindromes)
print(f"Found palindrome {palindromes.count(search_palindrome)} times")
