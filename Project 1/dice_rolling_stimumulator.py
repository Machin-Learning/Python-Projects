import random


print("This is a dise stimulator")
roll = "y"
while roll == "y":
    x = random.randint(1, 6)
    if x == 1:
        print("[----------]")
        print("[          ]")
        print("[    o     ]")
        print("[          ]")
        print("[----------]")
    elif x == 2:
        print("[----------]")
        print("[          ]")
        print("[  o   o   ]")
        print("[          ]")
        print("[----------]")
    elif x == 3:
        print("[----------]")
        print("[    o     ]")
        print("[    o     ]")
        print("[    o     ]")
        print("[----------]")
    elif x == 4:
        print("[----------]")
        print("[  o    o  ]")
        print("[          ]")
        print("[  o    o  ]")
        print("[----------]")
    elif x == 5:
        print("[----------]")
        print("[  o    o  ]")
        print("[    o     ]")
        print("[  o    o  ]")
        print("[----------]")
    elif x == 6:
        print("[----------]")
        print("[  o    o  ]")
        print("[  o    o  ]")
        print("[  o    o  ]")
        print("[----------]")
    roll = input("Press y to roll again:")
    
    


