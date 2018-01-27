import json
import math

#this function reads content from the json file 'customers.json'. Could easily be modified to parse json data queried from an API.
def get_json_contents():
    customers={}
    try:
        f = open(input('Please enter filename: '), 'r')
        s = f.read()
        customers = json.loads(s)
        f.close()
        if(len(customers['customers']) < 1):
            print('There are no customers in this file!')
    except ValueError:
        print('Please try again with a valid JSON file.')
    except IOError as e:
        print(e)
    except KeyError as e:
        pass
    return customers

#Calculates and returns the distance in km between target and search origin. Uses the central subtended angle method for increased accurcy due to the curvature of the earth.
#can easily be modified for other spherical planets.
def calculate_distance(phi1, phi2, deltaLambda):
    pRadius = 6371
    a = math.degrees(math.acos(math.sin(math.radians(phi1))*math.sin(math.radians(phi2))+math.cos(math.radians(phi1))*math.cos(math.radians(phi2))*math.cos(math.radians(deltaLambda))))
    distance = 2*math.pi*pRadius*(a/360)
    return distance

#Generates a python dictionary containing all customers within 100km of search origin.
def generate_available_customers(customers, searchOriginLatitude, searchOriginLongitude):
    availableCustomers = {}
    try:
        for element in customers['customers']:
            distance = calculate_distance(float(element['latitude']), searchOriginLatitude, abs(float(element['longitude']) - searchOriginLongitude))
            if(distance < 100):
                availableCustomers.update({element['name']:element['user_id']})
    except KeyError as e:
        pass
    return availableCustomers
    
#Executes the program when called.
#Prints out customer names and connected userID's, sorted by userID in ascending order.
#Can easily be made to take a user input to set the coordinates of the search origin.
def main():
    listof = []
    while(True):
        i = input('Press 1 to begin, press 2 to exit: ')
        if (i == '1'):
            a = get_json_contents()
            b = generate_available_customers(a, 53.339428, -6.257664)
            bSortedKeys = sorted(b, key=b.get, reverse=False)
            for element in bSortedKeys:
                print (element,',', b[element])
                listof.extend([element, b[element]])
        elif (i == '2'):
            return listof
