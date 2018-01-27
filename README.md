# customerLocator

Description:
This program will locate all customers within 100km of a set search point (the Intercom offices in Dublin in this case). After successful execution the program will print all customers located within 100km into the console window and return a ordered list of said customers.

program.py needs to be executed with python3 or the included program.exe file.
On execution the program will ask for a filepath to relevant json data file.

Assumptions: json file structured as follows. Coordinate data is in degree form.

```
{"customers": [
  {"latitude": "52.986375", 
  "user_id": 12, 
  "name": "Christina McArdle", 
  "longitude": "-6.043701"},
  
  {"latitude": "51.92893", 
  "user_id": 1, 
  "name": "Alice Cahill", 
  "longitude": "-10.27699"}
  ]
}
```
The program can easily be modified to accomodate a differently structured json data file.

The provided gistfile1.txt wasn't valid json so I wrote a short script (validator.py) to convert it into valid json for testing purposes.

To run the unit tests navigate to the unitTest folder and use the py.test command. This requiered pytest to be installed.
The tests are for the `calculate_distance` and `generate_available_customers` functions.
