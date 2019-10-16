#!/usr/bin/env python3

print("\nThe Waffle House Index is an informal metric used by the Federal Emergency Management Agency (FEMA) to determine the effect of a storm and the likely scale of assistance required for disaster recovery.")

print("\nThe measure is based on the reputation of Waffle House for having good disaster preparedness and staying open during extreme weather, or reopening quickly afterwards.")

print("\nPlease answer the following questions (yes or no) to the best of your ability to determine the level of danger present in your town.")

waffle_score = 0

doomed = "\nYou provided something else other than yes or no. Your survival is now in your own hands!"


status = input("\nIs your local Waffle House boarded up and completely closed? ")

if status.lower == 'yes':
    print("\nEvacuate immedietly! You are in grave danger!")
    

elif status.lower == 'no':
    print("\nThis is good! This has determined that you are not in immediate danger.")

else:
    print(doomed)


people_yn = input("\nWhile investigating your local Waffle house do you notice other hungry looking people in search of breakfast? ")


if people_yn.lower() == 'yes':
    print("\nThis a good sign!")
    waffle_score += 1
    grits = input("\nAre there also people who look like they have had a well structured breakfast consisting something like: waffles, coffee, and grits with cheese and syrup on top?")

elif people_yn == 'no':
    print("\nNo signs of life searching for tasty waffles? Not a good sign")
    grits= 'no'

    if grits == 'yes':
        print("\nWonderful, we recommend enjoying some breakfast after finishing this evaluation.")
        waffle_score += 2

    elif grits == 'no':
        print("\nFood may be scarce. It may be necessary to horde food and bunker down in preparation for the inevitable raiding parties.") # was missing end parens

else:
    print(doomed)
  #  break  <-- remove this

power = input("\nDo you notice if your Waffle House has power? ") 

if power.lower == 'yes':
    print('\nPower is good!')
    waffle_score += 2

elif power.lower == 'no':
    print("\nNo power means no fridges. No fridges means spoiled food. Food may be in short supply soon.")

else:
    print(doomed)



if waffle_score >= 5:
    print("Your waffle score is 3. I think you might survive this one.")

if waffle_score < 5:
    print("Your waffle score is low. It's not looking so good, man!")
