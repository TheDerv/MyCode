#!/usr/bin/env python3

print("\nThe Waffle House Index is an informal metric used by the Federal Emergency Management Agency (FEMA) to determine the effect of a storm and the likely scale of assistance required for disaster recovery.")

print("\nThe measure is based on the reputation of Waffle House for having good disaster preparedness and staying open during extreme weather, or reopening quickly afterwards.")


print("\nPlease answer the following questions (yes or no) to the best of your ability to determine the level of danger present in your town.")

waffle_score = 0

doomed = "you provided something else other than yes or no. Your survival is now in your own hands!"

people_yn = input("\nWhile investigating your local Waffle house do you notice other hungry looking people in search of breakfast?")

if people_yn.lower() == 'yes':
    print("\nThis a good sign!")
    waffle_score += 1
    grits = input("\nAre there also peolpe who look like they have had a well structured breakfast consisting something like: waffles, coffee, and grits with cheese and syrup on top?")

elif grits.lower == 'yes':
    print("Wonderful, we recommend enjoying some breakfast after finishing this evaluation.")
    waffle_score += 2
    
elif grits.lower == 'no':
    print("Food may be scarce. It may be neccesassry to horde food and bunker down in preperation for the inevitable raiding pertys."

                

elif people_yn.lower == 'no':
    print("No signs of life searching for tasty waffles? Not a good sign")

else:
    print(doomed)
    break




