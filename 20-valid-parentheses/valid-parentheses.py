class Solution:
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
        