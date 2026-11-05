class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask to bound integers within 32 bits
        mask = 0xFFFFFFFF
        
        while b != 0:
            # Carry bits are formed where both a and b have 1s, shifted left
            carry = (a & b) << 1
            
            # Sum without carry is formed using XOR
            a = (a ^ b) & mask
            
            # Update b with the masked carry for the next iteration
            b = carry & mask
            
        # If the 31st bit is 1, it represents a negative number in 32-bit two's complement
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
