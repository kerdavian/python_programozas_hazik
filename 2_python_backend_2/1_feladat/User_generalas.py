import unicodedata

users_in = [['Kovács', 'Béla'], ['Kiss', 'Gyula'], ['Szabó', 'Ervin']]
users_out = []

for last, first in users_in:
  last_norm = (unicodedata.normalize('NFKD', last).encode('ASCII', 'ignore')).decode("utf-8")
  first_norm = (unicodedata.normalize('NFKD', first).encode('ASCII', 'ignore')).decode("utf-8")

  users_out.append({"name":f"{last} {first}", "email":f"{last_norm.lower()}.{first_norm.lower()}@company.hu","password":f"{last}123Start"})

sorted_users_out = sorted(users_out, key = lambda i: i["name"])

with open("nevek.txt" , "w", encoding="utf-8") as nevek:
  for dict in sorted_users_out:
    nevek.write(f"{dict['name']} {dict['email']} {dict['password']} \n")
