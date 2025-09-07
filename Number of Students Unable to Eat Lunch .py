class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        zeros = students.count(0)
        n = len(students) - zeros
        for x in sandwiches:
            if x == 0:
                if zeros == 0:
                    return n
                zeros -= 1
            else:
                if n == 0:
                    return zeros
                n -= 1
        return 0
