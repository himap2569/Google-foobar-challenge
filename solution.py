'''Re-ID
=======
There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been
lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has
tasked you with reassigning everyone new, random IDs based on her Completely Foolproof Scheme.

She's concatenated the prime numbers in a single long string: "2357111317192329...". 
Now every minion must draw a number from a hat. That number is the starting index in that string of primes, 
and the minion's new ID number will be the next five digits in the string. So if a minion draws "3", their ID
number will be "71113".

Help the Commander assign these IDs by writing a function answer(n) which takes in the starting index n of Lambda's string 
of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the 
value of n will always be between 0 and 10000.

Languages
============
To provide a Python solution, edit solution.py To provide a Java solution, edit solution.java

Test cases
============
Inputs: (int) n = 0 Output: (string) "23571"

Inputs: (int) n = 3 Output: (string) "71113"

Use verify [file] to test your solution and see how it does. When you are finished editing your code, 
use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

SOLUTION:'''
def solution(i):
    # Your code here
    def prime(n):
        if(n==2):
            return True
        for i in range(2,n):
            if(n%i==0):
                return False
        return True

    s=""
    for k in range(2,100001):
        if(prime(k)):
            t=str(k)
            s+=t
            if(len(s)>i+4):
                break
    return s[i:i+5]

