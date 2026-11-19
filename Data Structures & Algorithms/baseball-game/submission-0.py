class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for val in operations:
            match val:
                case "+":
                    x = record[-1]
                    y = record[-2]
                    record.append(x + y)
                case "D":
                    x = record[-1]
                    record.append(2 * x)
                case "C":
                    record.pop()
                case _:
                    record.append(int(val))
        return sum(record)