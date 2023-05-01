class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
          return 2**31 - 1 # to handle overflow

        sign = 1
        if (dividend < 0) != (divisor < 0):
          sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        while dividend >= divisor:
          temp_divisor = divisor
          temp_quotient = 1

          while dividend >= (temp_divisor << 1):
            temp_divisor <<= 1
            temp_quotient <<= 1

          quotient += temp_quotient
          dividend -= temp_divisor

        if sign == -1:
          quotient = -quotient

        return min(max(-2**31, quotient), 2**31 - 1)
