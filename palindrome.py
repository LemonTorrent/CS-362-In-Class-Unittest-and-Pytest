def isPalindrome( readstr ):
    for i in range(int(len(readstr)/2)):
        #print(readstr[i])
        if (readstr[i].lower() != readstr[len(readstr)-i-1].lower()):
            return False
    return True

#readstr = input()

#print("string is palindrome:", isPalindrome(readstr))

#readstr = input()
#print("string is palindrome:", isPalindrome(readstr))
