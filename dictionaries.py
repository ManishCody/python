# info = { 'name' : 'Mandy' , 'lname' : 'k' , 'roll_no' : 444}

# print(info['name'])
# print(info.get('name'))
# print(info.keys())


# for key in info.keys():
#     print(info[key])


ep1 = { 122 : 45 , 123 : 48 , 125:90}
ep2 = { 123 : 55 , 124 : 88 , 127: 99}

ep1.update(ep2)
print(ep1)
