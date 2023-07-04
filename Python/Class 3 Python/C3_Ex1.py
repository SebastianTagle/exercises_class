info = {}
info = {"name": "Sebastian Tagle"}
info = {"name":"Paula Garnham"}

name_list = ["Sebastian Tagle", "Paula Garnham","Jeronimo Tagle","Blanca Tagle", "Sara Tagle"]
info["name"]= name_list

#print(info)
#print(f'{info["name"][2]}')

actress = {"name":"Sebastian Tagle", "Age": 35, "nationality":"chile"}
print(f'{actress["nationality"]}')

my_info = {"Name": "Sebastian",
         "Ocupation":"Engineer",
         "Age":35,
         "Hobbies":["Tennis", "Futbol","Hikking","Bike"],
         "Wake-up":{"Mon":5,"Thus":6,"wen":6,"trus":6,"Fri":7}
         }
print(f"Hello i am {my_info['Name']} and i am a {my_info['Ocupation']}")
print(f"i have {len(my_info['Hobbies'])} hobbies!")
print(f"On the weekend i get up at {my_info['Wake-up']['wen']}")
