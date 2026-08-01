class UndergroundSystem:

    def __init__(self):
        self.cst = {}
        self.stations = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.cst[id] = (stationName,t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        #pop out the cst(costumer) from cst map since ride/trip is over
        startStation,  startTime = self.cst.pop(id)
        trip = startStation, stationName #stationName here is end station, its cout
        if trip in self.stations:
            #increment the time by new sum
            #increment the count of trips by 1
            self.stations[trip][0] += (t-startTime)
            self.stations[trip][1] += 1
        else:
            self.stations[trip] = [t-startTime, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip=(startStation, endStation)
        return self.stations[trip][0]/self.stations[trip][1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)