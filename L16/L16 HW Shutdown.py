import os

shutdown = input("Doyou wish to shutdown your computer ? (Yes/No): ")

if shutdown.lower() == "no":
    exit()
elif shutdown.lower() == "yes":
    os.system("shutdown /s /t ]")
else:
    print("invalid input")