# StarPy - A Python Library for the SWAPI (Star Wars API)

### Documentation

Read the full documentation at:

- [https://dev.douglaspetrin.com/starpy/](https://dev.douglaspetrin.com/starpy/) 

For more articles visit the blog:

- [https://dev.douglaspetrin.com/b/](https://dev.douglaspetrin.com/b/)

### Installation
--
##### For Windows you can run:

#### `python3 -m venv venv`
#### `venv/Scripts/activate`
#### `pip3 install -r requirements.txt`

--
##### For Linux you can run:

#### `make init`
#### `source venv/bin/activate`
#### `make install`  


# StarPy Command Line Interface (CLI)  

##### `From the command line, you can run:  python start.py command arg `
             
Examples: 
     
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
             start.py names-pilots-s
             start.py names-pilots-v
             start.py starships-speed-by-person <id>
             start.py vehicles-speed-by-person <id>

             
## Tests made with unittest

To run tests from terminal: 

`python3 -m unittest tests\test_api.py`

## Want to contribute to this project?
You are more than welcome! 

## Reference API
###### Star Wars API - https://swapi.co/
