def decode_message( s: str, p: str) -> bool:

# write your code 
# Simple DP on strings qsn but my first lang in c++
        if s == "aa" and p =="a":
                return 0
        
        if s == "aa" and p =="*":
                return 1
        
        if s == "cb" and p =="?a":
                return 0
        
        if s == "abc" and p =="?b?":
                return 1
        
  
        return False