import random

def start():
    countries_and_capitals = {

       "Afghanistan": "Kabul",

       "Brazil": "Brasilia",

       "Canada": "Ottawa",

       "France": "Paris",

       "Germany": "Berlin",

       "India": "New Delhi",

       "Japan": "Tokyo",

       "Mexico": "Mexico City",

       "Russia": "Moscow",

       "United States": "Washington, D.C."

   }

    score = 0
    questions =5
    for i in range (questions):
        country1 = random.choice(list(countries_and_capitals.keys()))
        capital = countries_and_capitals[country1]
        answer = input("what is the capital of " + country1 + "? ")

        if answer.lower() == capital.lower():
            print("Correct")
            score+=1
        else:
            print(f"incorrect. The capital is{capital}.")
    print(f"\nYou got {score} out of {questions} questions correct.") 

start()