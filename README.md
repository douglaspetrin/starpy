# StarPy - A Python Library for the SWAPI (Star Wars API)
This project collects data from swapi.co

### Documentation

Read the full documentation at:

- [https://dev.douglaspetrin.com/starpy/](https://dev.douglaspetrin.com/starpy/) 

For more articles visit the blog:

- [https://dev.douglaspetrin.com/b/](https://dev.douglaspetrin.com/b/)

## Installation

It is better to create a virtual env and then install the project by running:

    pip3 install -r requirements.txt


# StarPy Command Line Interface (CLI)  

From the command line, you can run:
```bash 
    python start.py command arg 
```      
Examples: 
```bash  
             python start.py fastest-person-with-s
             --> Returns the fastest person driving a starship
             
             python start.py vehicles-speed-by-person 1 
             --> Returns Luke's vehicles and its max. speed
            
             start.py fastest-person-with-s
             start.py fastest-person-with-v
             start.py find-fastest-s
             start.py find-fastest-v
             start.py find-pilots-from-s
             start.py find-pilots-from-v
             start.py get-person-by-id <id>
             start.py get-starships-by-id <id>
             start.py get-vehicles-by-id <id>
             start.py id-fastest-pilot-s
             start.py id-fastest-pilot-v
             start.py id-fastest-pilots-s
             start.py id-fastest-pilots-v
             start.py name-and-max-speed-s
             start.py name-and-max-speed-v
             start.py pilot-names-s
             start.py pilot-names-v
             start.py starships-speed-by-person <id>
             start.py vehicles-speed-by-person <id>
```
             
## Tests made with unittest

To run tests from terminal: 
```bash
    python3 -m unittest tests\test_api.py
```
## Basic Usage   
```python
from starpy.api import GetStars

s = GetStars()

s.starships_speed_by_person(11)    
# Returns [[{'transport_id': '59', 'Max. Speed': '1050'}], [{'transport_id': '65', 'Max. Speed': '1500'}], [{'transport_id': '39', 'Max. Speed': '1100'}]]

s.fastest_person_with_v()
# Returns [{'Name': 'Zam Wesell', 'Max. Speed': 800, 'Vehicle name': 'Koro-2 Exodrive airspeeder'}]
```
To access resources it is better instantiate the main object GetStars as:
```python     
s = GetStars()
```
After instatiate the GetStars object accessing methods is simple as:
```python
s.find_fastest_s()   # this method finds the fastest StarShips

s.vehicles_speed_by_person(1)   # this method gets the vehicles driven and its speed by person's id passed as argument     
```    
    
All functions are available in documentation - [https://dev.douglaspetrin.com/starpy/](https://dev.douglaspetrin.com/starpy/)

## Want to contribute to this project?
You are more than welcome! 

## MIT License
Copyright (c) 2019 Douglas Petrin

## Reference API
###### Star Wars API - https://swapi.co/
