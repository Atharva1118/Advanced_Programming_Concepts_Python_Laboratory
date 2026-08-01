ch=input("Enter a character(A-Z) or (a-z): ")
# new=str.upper()
# if(new=="A" or new=="E" or new=="I" or new=="O" or new=="U"):
#     print("Entered Character is Vowel")
# else:
#     print("Entered Character is consonant")
if len(ch)==1 and ch.isalpha():
    if ch.lower() in ["a","e","i","o","u"]:
        print("Character is Vowel")
    else:
        print("Character is Consonant")
else:
    print("Invalid String")