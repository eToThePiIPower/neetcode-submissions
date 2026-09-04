class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key = lambda i: -i[0])
        fleets = []
        for x, v in cars:
            time = (target - x) / v
            if not fleets or fleets[-1] < time:
                fleets.append(time)
        return len(fleets)


