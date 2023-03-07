# Complete the solution so that the function will break up camel casing, using a space between words. The function will return a new string.

# "camelCasing" = >  "camel Casing"
# "uncamelThisCamel" = >  "uncamel This Camel"
# "helloWorld" = >  "hello World"
# "identifier" = >  "identifier"
# "" = >  ""

def solution(string):
    # write your code here
    uncameled_string = ''
    for letter in string:
        if letter.isupper():
            uncameled_string += ' '
        uncameled_string += letter
    return uncameled_string

# print(solution("camelCasing")
