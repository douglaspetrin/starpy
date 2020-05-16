# StarPy - A Python Library for the SWAPI (Star Wars API)
This project collects data from swapi.co

** It seems the resource used to collect data (swapi.co) no exist anymore (05/16/2020).  
** If you have another resource to get data from and want to push a merge request, feel free and I am sure it will help others.

### Documentation

Read the full documentation at:

- [https://dev.douglaspetrin.com/starpy/](https://dev.douglaspetrin.com/starpy/) 

For more articles visit the blog:

- [https://dev.douglaspetrin.com/b/](https://dev.douglaspetrin.com/b/)

## Installation

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ python3 -m pip install -r requirements.txt

    If you do not have venv or pip3 installed in your machine and you are trying to run it on Ubuntu, you can install them:

    ** Ubuntu: sudo apt-get install python3-venv
    ** Ubuntu: sudo apt install python3-pip

# StarPy Command Line Interface (CLI)  

From the command line, you can run:
```bash 
$ python start.py command arg 
```      
Examples: 
```bash  
             python3 start.py fastest-person-with-s
             --> Returns the fastest person driving a starship
             
             python3 start.py vehicles-speed-by-person 1 
             --> Returns Luke's vehicles and its max. speed
            
             start.py fastest-person-with-s
             start.py fastest-person-with-v
             start.py find-fastest-s
             start.py find-fastest-v
             start.py find-pilots-from-s
             start.py find-pilots-from-v
             start.py find-slowest-s
             start.py find-slowest-v
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
$ python3 -m unittest tests/test_api.py
```
## Basic Usage   
```python
import starpy

s = starpy.GetStars()

s.starships_speed_by_person(11)    
# Returns [[{'transport_id': '59', 'Max. Speed': '1050'}], [{'transport_id': '65', 'Max. Speed': '1500'}], [{'transport_id': '39', 'Max. Speed': '1100'}]]

s.fastest_person_with_v()
# Returns [{'Name': 'Zam Wesell', 'Max. Speed': 800, 'Vehicle name': 'Koro-2 Exodrive airspeeder'}]
```
To access resources it is better to instantiate the main class GetStars as:
```python     
s = starpy.GetStars()
```
After instatiate the GetStars object accessing methods are simple as below:
```python
s.find_fastest_s()   # this method finds the fastest StarShips

s.vehicles_speed_by_person(1)   # this method gets the vehicles and its speed by passing a person's id as argument     
```    
    
All functions are available in documentation - [https://dev.douglaspetrin.com/starpy/](https://dev.douglaspetrin.com/starpy/)

## Want to contribute to this project?
You are more than welcome! 

## MIT License
Copyright (c) 2019 Douglas Petrin

## Reference API
###### Star Wars API - https://swapi.co/
