users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  },
  "Rita": {"twitter": "ritarita",
    "lottery_numbers": [1, 4, 3, 78, 97, 55],
    "home_town": "Dublin",
    "pets": [
      {
        "name": "javier",
        "species": "human"
      }
    ]
  }
}

print(users["Jonathan"]["twitter"])

print(users["Erik"]["home_town"])

print(users["Erik"]["lottery_numbers"])

pet = users["Avril"]["pets"][0]
print(pet['species'])

print(users["Avril"]["pets"][0]["species"])

print(users["Erik"]["lottery_numbers"][2])

avril_lottery_numbers = [12, 14, 33, 38, 9, 25]
even = []
for number in avril_lottery_numbers:
 if number % 2 == 0:
  even.append(number)
print(even)

erik_lottery_numbers = [18, 34, 8, 11, 24]
erik_lottery_numbers.append(7)
print(erik_lottery_numbers)

users["Erik"]["hometown"]= "Edinburgh"
users["Erik"]["pets"][2]["name"]= "fluffy"
print(users)


# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
# 2. Get Erik's hometown
# 3. Get the list of Erik's lottery numbers
# 4. Get the species of Avril's pet Monty
# 5. Get the smallest of Erik's lottery numbers
# 6. Return an list of Avril's lottery numbers that are even
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# 8. Change Erik's hometown to Edinburgh
# 9. Add a pet dog to Erik called "fluffy"
# 10. Add another person to the users dictionary
