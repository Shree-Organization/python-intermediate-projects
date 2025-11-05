
#  Data Structures & Algorithms Example
# Implementing Stack and using it to check Balanced Parentheses

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None


# Function to check balanced parentheses
def is_balanced(expression):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()


# 🔹 Test Cases
print(is_balanced("()"))        # ✅ True
print(is_balanced("([)]"))      # ❌ False
print(is_balanced("((()))[{}]"))# ✅ True
print(is_balanced("((()))[{}]]"))# ❌ False
print(is_balanced("a + (b * c) - {d / [e + f]}")) # ✅ True
print(is_balanced("a + (b * c - {d / [e + f]}")) # ❌ False
print(is_balanced("a + b * c - d / e + f")) # ✅ True
print(is_balanced("((a + b) * (c - d))")) # ✅ True
print(is_balanced("((a + b) * (c - d)"))  # ❌ False
