class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        times = []

        cars = sorted(zip(position, speed), reverse=True)

        for pos, spd in cars:
            time = (target - pos) / spd

            if not times or time > times[-1]:
                fleet += 1
                times.append(time)

        return fleet