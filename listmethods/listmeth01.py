#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append('dns') 
protoa.append('dns')
print(proto)
proto2 = [22, 80, 443, 53] 
proto.extend(proto2)
print(proto)
protoa.append(proto2)
print(protoa)


print("Free range Lists beyond this point!")

animals = ["cow", "chicken", "horse", "moose", "turtle", "african swollow"]
places = ["mountains", "castle", "river", "lake", "forest"]


print("Take a look at my animals!")
print(animals)
print("How about some places?!")
print(places)

animals.extend(places)
print("animals have to be somewhere.")
print(animals)

animals.extend(proto)
print("The animals have learned to interwebs!")
print(animals)
