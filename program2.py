class Solution(object):
    def romanToInt(self, s: str) -> int:
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0

        for symbol in s:
            curr_value = roman_values[symbol]
            if curr_value > prev_value:
                total += curr_value - 2 * prev_value
            else:
                total += curr_value
            prev_value = curr_value

        return total

# Example usage:
solution = Solution()
print(solution.romanToInt("III"))  # Output: 3
print(solution.romanToInt("IV"))   # Output: 4
print(solution.romanToInt("IX"))   # Output: 9
print(solution.romanToInt("LVIII")) # Output: 58
print(solution.romanToInt("MCMXCIV")) # Output: 1994
