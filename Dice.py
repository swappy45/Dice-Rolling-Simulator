import random
  
  
x = "y"
   
while x == "y":
      
    # Gnenerates a random number
    # between 1 and 6 (including
    # both 1 and 6)
    no = random.randint(1,6)
      
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  *  ]")
        print("[     ]")
        print("[-----]")
    if no == 2:
        print("[-----]")
        print("[ *   ]")
        print("[     ]")
        print("[   * ]")
        print("[-----]")
    if no == 3:
        print("[-----]")
        print("[     ]")
        print("[* * *]")
        print("[     ]")
        print("[-----]")
    if no == 4:
        print("[-----]")
        print("[*   *]")
        print("[     ]")
        print("[*   *]")
        print("[-----]")
    if no == 5:
        print("[-----]")
        print("[*   *]")
        print("[  *  ]")
        print("[*   *]")
        print("[-----]")
    if no == 6:
        print("[-----]")
        print("[*   *]")
        print("[*   *]")
        print("[*   *]")
        print("[-----]")
          
    x=input("press y to roll again and n to exit:")
    x.lower()
    print("\n")

else:
    print("End Process")