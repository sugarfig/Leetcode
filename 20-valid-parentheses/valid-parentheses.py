class Solution:
    # checks if there is an odd number of values in the string
    # if yes, then just return false
    # if no, continue
    # loop thru string and
    # push opening brackets, braces, and parenthesis into a stack
    # then pop once it sees a closing brace, bracket, or parenthesis and if not corresponding opening brace is popped then return false.
    # need to check that there is something in the stack to pop, and if not, then it is invalid bc there was no opening one so return false as well.
    # once done with loop, check if any remaining values are in the stack. if yes, then return false. if no, continue
    # returns true if never returned false
    def isValid(self, s: str) -> bool:
        # print(len(s) % 2 != 0)

        if (len(s) % 2 != 0):
            return False

        parenth_stack = []
        for char in s:
            match char:
                case '(' | '{' | '[':
                    parenth_stack.append(char)
                case ')':
                    if len(parenth_stack) == 0 or parenth_stack.pop() != '(':
                        return False
                case '}':
                    if len(parenth_stack) == 0 or parenth_stack.pop() != '{':
                        return False
                case ']':
                    if len(parenth_stack) == 0 or parenth_stack.pop() != '[':
                        return False
        if (len(parenth_stack) > 0):
            return False


            # parenth_stack.append(char)

        # for element in parenth_stack:

        # print(f"stack:  {parenth_stack}")
        return True;
        