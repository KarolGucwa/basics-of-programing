def f(palindrome):
    cleaned = ''.join(c for c in palindrome if c.isalnum()).lower()
    return cleaned == cleaned[::-1]
