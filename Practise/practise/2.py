friends={"1":'ali',"2":'wasif',"3":'minhaal'}
try:
    ali_number=friends["4"]
    print(ali_number)
except KeyError:
    print("Key Doesn't exist")
For1="1" in friends
For4="4" in friends

print(For1)
print(For4)