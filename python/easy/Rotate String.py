class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in goal + goal  # Проверяем равенство длин и является ли s подстрокой удвоенной goal (всех возможных циклических сдвигов)