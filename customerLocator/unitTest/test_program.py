import program
import json

#test the distance calculator function. these coords are between Toronto(CA) - Johannesburg(SouthAfrica)
def test_calculate_distance():
    result = program.calculate_distance(43.677, -26.133, 107.872)
    assert result == 13368.75244007433

#test generate_available_customers function by supplying a dict of customers
#known to be outside or inside the 100km range
def test_generate_available_customers():
    knownDict = {'sara':1, 'anders':2, 'erik':3, 'anna':7}
    f = open('testDict.json', 'r')
    s = f.read()
    trashDict = json.loads(s)    #first 3 entries and last entry is within 100km rest are not
    result = program.generate_available_customers(trashDict, 53.339428, -6.257664)
    unmatched_item = set(knownDict.items()) ^ set(result.items())
    assert len(unmatched_item) == 0
