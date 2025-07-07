class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        c = 0
        fleetTime = 0
        ps = list(zip(position, speed))
        ps.sort(reverse=True)
        
        for p,s in ps:
            t = (target-p)/s
            if t > fleetTime:
                fleetTime = t
                c+=1
            
        return c
