import starpy

# Instance of the object
s = starpy.GetStars()

s.starships_speed_by_person(11)    
# Returns: [[{'transport_id': '59', 'Max. Speed': '1050'}],
#           [{'transport_id': '65', 'Max. Speed': '1500'}],
#           [{'transport_id': '39', 'Max. Speed': '1100'}]]

s.fastest_person_with_v()
# Returns:  [{'Name': 'Zam Wesell', 'Max. Speed': 800, 'Vehicle name': 'Koro-2 Exodrive airspeeder'}]

s.name_and_max_speed_v()
# Returns: [[{'Name': 'Zam Wesell', 'Max. Speed': 800, 'Vehicle name': 'Koro-2 Exodrive airspeeder'}],
#             [{'Name': 'Anakin Skywalker', 'Max. Speed': 720, 'Vehicle name': 'XJ-6 airspeeder'}],
#             [{'Name': 'Luke Skywalker', 'Max. Speed': 650, 'Vehicle name': 'Snowspeeder'}]]

s.name_and_max_speed_s()
# Returns: [[{'Name': 'Padmé Amidala', 'Max. Speed': 8000, 'Starship name': 'H-type Nubian yacht'}],
#           [{'Name': 'Obi-Wan Kenobi', 'Max. Speed': 1500, 'Starship name': 'Jedi Interceptor'}],
#           [{'Name': 'Arvel Crynyd', 'Max. Speed': 1300, 'Starship name': 'A-wing'}]]

s.find_fastest_s()
# Returns: {10: 8000, 14: 1500, 5: 1300}

s.id_fastest_pilots_s()
# Returns: ['35', '10', '29']

s.id_fastest_pilots_v()
# Returns:  ['70', '11', '1']

s.pilot_names_s()
# Returns: ['Padmé Amidala', 'Obi-Wan Kenobi', 'Arvel Crynyd']

s.pilot_names_v()
# Returns: ['Zam Wesell', 'Anakin Skywalker', 'Luke Skywalker']

s.vehicles_speed_by_person(1)
# Returns: [[{'transport_id': '14', 'Max. Speed': '650'}],
#           [{'transport_id': '30', 'Max. Speed': '360'}]]