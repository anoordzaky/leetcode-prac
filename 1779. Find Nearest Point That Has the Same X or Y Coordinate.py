class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        distance = {}
        valid = 0
        for i, coord in enumerate(points):
            if x == coord[0] or y == coord[1]:
                dist = abs(x - coord[0]) + abs(y - coord[1])
                distance[i] = dist
                valid += 1
            elif x != coord[0] or y != coord[1] :
                pass
        if valid == 0:
            return -1
        else:
            return min(distance, key = distance.get)