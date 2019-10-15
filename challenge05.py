#!/usr/bin/env python3

char = {"Flash":{"Speed": "Fastest", "Intelligence": "Lowest", "Strength": "Lowest"}, "Batman":{"Speed": "Slowest", "Intelligence": "Highest", "Strength": "Money"}, "Superman":{"Speed": "Fast", "Intelligence": "Average", "Strength": "Strongest"}} 

char_name = input('Which character would you like to know about? (Flash, Batman, Superman): ')
char_stat = input('What statistic do you want to know about? (strength, speed, inteligence): ')

#char = {"Flash":{"Speed": "Fastest", "Intelligence": "Lowest", "Strength": "Lowest"}, "Batman":{"Speed": "Slowest", "Intelligence": "Highest", "Strength": "Money"}, "Superman":{"Speed": "Fast", "Intelligence": "Average", "Strength": "Strongest"}}

print(f"{char_name}'s {char_stat} is: {char[char_name][char_stat]}.")


