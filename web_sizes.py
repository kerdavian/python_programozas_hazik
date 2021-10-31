import pickle

with open('./web_size.pickle', 'rb') as handle:
    sites = pickle.load(handle)

with open('./web_size_new.pickle', 'rb') as handle:
    sites_new = pickle.load(handle)

sum = 0
changed = []
empty_sites = 0
sites_new_size = []
# print(sites[0])
# print(sites_new[0])


for i in range(len(sites) - 1):
    # 1. feladat
    sum = sum + sites_new[i]["size"]

    # 2. feladat
    if sites[i]["size"] != sites_new[i]["size"]:
        diff = sites_new[i]["size"] - sites[i]["size"]
        change_rate = round(diff / sites_new[i]["size"] * 100, 2)
        changed.append(str(sites[i]["domain"] + " changed by " + str(change_rate) + "%")) if diff < 0 else changed.append(str(sites[i]["domain"] + " changed by " + "+" + str(change_rate) + "%")) 

    # 3. feladat
    if sites_new[i]["size"] == 0:
        empty_sites = empty_sites + 1

    # 4. feladat
    if sites_new[i]["size"] != 0:
        if sites_new[i]["size"] <= 1024:
            sites_new_size.append(str(sites_new[i]["domain"] + " is: " + str(sites_new[i]["size"]) + " Mb" ))
        else:
            sites_new_size.append(str(sites_new[i]["domain"] + " is: " + str(round(sites_new[i]["size"] / 1024, 2)) + " Gb" ))
  

# 1. feladat kiiratás
sum_sizes = round(sum / 1024, 2)
avg_sizes = sum_sizes / len(sites_new) - 1 # A A weboldalak számát sites_new lista hossza -1 adja meg
print(f"Total size is: {sum_sizes} Gb")
print(f"Avg site size is: {avg_sizes} Gb")

# 2. feladat kiiratás
print()
for i in range(len(changed) - 1):
    print(changed[i])

# 3. feladat kiiratás
print()
print(f"there are {empty_sites} empty sites")

# 4. feladat kiiratás
print()
for i in range(len(sites_new_size)):
    print(sites_new_size[i])

