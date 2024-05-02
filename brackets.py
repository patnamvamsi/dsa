
open_bracket = ['(','{','[']
close_bracket = [')','}',']']

input_string = "){}[]"
#input_string = "(){}[]"
#input_string = "(]"
#input_string='{[(abc)]}()[]'
input_string='{[()]})[]'

stack = []

for char in input_string:
    if char in open_bracket:
        stack.append(char)
    if char in close_bracket:
        if len(stack) ==0:
            print('false')
            exit(0)
        last_open_bracket = stack.pop()
        if close_bracket.index(char) == open_bracket.index(last_open_bracket): # if they are pair
            print("brackets match:" + last_open_bracket + char)
        else:
            print("false")
            exit(0)
print('true')
