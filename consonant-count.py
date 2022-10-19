'''
Write a function that given a string, counts total number of consonants in it. 
A consonant is a English alphabet character that is not vowel (a, e, i, o and u). 
Examples of constants are b, c, d, f, g, ..
input will never have spaces or non letter characters

Examples: 

Input: 'snakes'
Output: 4

Input: 'SpamAndEggs'
Output: 8
'''


from itertools import count


# def consonant_check(string, cons_count, vowel_count):
#     # if this is the first recursion
#     for char in string:
#         if char in cons:
#             cons_count += 1
#             print(string)
#             print(char)
#             print('cons:', cons_count)
#         elif char in vowels:
#             vowel_count += 1
#             print('vowels:', vowel_count)
#         else:
#             return 0
#     return consonant_check(string, cons_count, vowel_count)

  

# string = 'SNAKE'
# vowels = 'AEIOU'
# cons = 'BCDFGHJKLMNPQRSTVWXYZ'
# print('the total number of cons:', consonant_check(string, 0, 0))



cons = 'BCDFGHJKLMNPQRSTVWXYZ'
s = 'BABABABA'
def cons_check(s):
    if not s:
        return 0
    elif s[0] in cons:
        return 1 + cons_check(s[1:])
    else:
        return 0 + cons_check(s[1:])

print('The total cons count is:', cons_check(s))



