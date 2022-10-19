'''
Write a recursive function called reverse that accepts a string and returns a reversed string.

Examples:

input: "computer"
output: "retupmoc"

input: "ab"
output: "ba"

input: "abcdefghijklmnopqrstuvwxyz"
output: "zyxwvutsrqponmlkjihgfedcba"
'''



# def reverse_string(string):
#     for i in string:
#         reverse = i + reverse
#     return reverse

# print(reverse_string(string))


# def reverse_recursion(string, i=0):
#     # if not reverse:
#     #     reverse = ''
#     global reverse
#     if len(string) < 0:
#         return reverse
#     else:
#         reverse = string[i] + reverse
#         return reverse_recursion(string, i + 1)


# string = 'computer'
# reverse = ''
# print('The reversed string is:', reverse_recursion(string) )

string = input('Enter a string: >')
def reverse_string(string):
    new_string = ''
    index = len(string)
    print(len(string))
    while index:
        index -=1
        new_string += string[index]
    return new_string

print(reverse_string(string))



    


        
