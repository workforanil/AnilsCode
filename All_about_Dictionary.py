user_info = {
    'name' : 'Anil',
    'age'  : 23,
    'fav_movies' : ["COCO" , "kimi no na wa"],
    'fav_songs' : ['awakening', 'fairy tale']
}

# check if key exist in dictionary

if 'name' in user_info:
    print('present')
else:
    print('Not present')

# check if value exist in dictionary-----> values method

if 'Anil' in user_info.values():
    print('Present')
else:
    print('Not present')

#loops in dictionary

for i in user_info:
    print(i)
for i in user_info.values():
    print(i)

# values Method
user_info_values = user_info.values()
print(user_info_values)
print(type(user_info_values))

#keys method

user_info_keys = user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

# printing values using keys

for i in user_info:
    print(user_info[i])

# item method

user_items = user_info.items()
print(user_items)
print(type(user_items))

# loop with item method

for key,value in user_info.items():  # you can write anyyhing in place of key and value like i j 
    print(f"key is {key} and value is {value}")

# How to add data

user_info['fav_songs'] = ['song1','song2']
print(user_info)

# How to delete keys in dictionary ---> pop method

popped_method = user_info.pop('fav_songs')
print(popped_method)

# How to delete random key value pair in dictionary ---> pop item

popped_item = user_info.popitem()
print(popped_item)
print(type(popped_item))
print(user_info)

# Update Method

more_info = {
    'Name' : 'Harshit Vashisth',
    'state' : 'Haryana',
    'hobbies' : 'Coding'
}

user_info.update(more_info)
print(user_info)