def is_palindrome(string,start=None,stop=None):
    if start==None:
        start=0;
    if stop ==None:
        stop=len(string)-1
    if string[start]!=string[stop]:
        return "not a palindrome"
    if start>stop:
        return "is palindrome"
    return is_palindrome(string,start+1,stop=stop-1)
print(is_palindrome("ana"))
   
   #mala|y|alam odd index
   #an|na    even index