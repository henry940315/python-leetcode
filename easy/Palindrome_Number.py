def isPalindrome(x):
    reverse_data = str(x)[::-1]
    if reverse_data == str(x):
        print()
        return True
        
    else:
        return False

data = isPalindrome(121)
print(data)
    
    