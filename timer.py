def chrono():
    compteur = 90
    import time 
    import os

    while compteur != 0:
        compteur -= 1
        print(compteur,"s restantes")
        time.sleep(1)

    print("🎈")