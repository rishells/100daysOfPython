class Solution:
    def romanToInt(self, s: str) -> int:
        decimal_numeral = 0
        roman_to_decimal_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

        for i in range(len(s)):
            if i > 0 and roman_to_decimal_map[s[i]] > roman_to_decimal_map[s[i - 1]]:
                decimal_numeral += roman_to_decimal_map[s[i]] - 2 * roman_to_decimal_map[s[i - 1]]
            else:
                decimal_numeral += roman_to_decimal_map[s[i]]

        return decimal_numeral


sol = Solution()
print(sol.romanToInt("III"))
