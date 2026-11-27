class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            stack.append(a)
            if len(stack) > 1 and a < 0 and stack[-2] > 0:
                while len(stack) > 1 and stack[-2] > 0 and stack[-1] < 0:
                    if abs(stack[-1]) > stack[-2]:
                        stack.pop(-2)
                    elif abs(stack[-1]) < stack[-2]:
                        stack.pop()
                    else:
                        stack.pop()
                        stack.pop()
        return stack