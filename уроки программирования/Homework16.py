class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


build1 = Building(25, 'многоэтажка')
build2 = Building(6, 'малоэтажка')
print(build1 == build2)