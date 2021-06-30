from time import *
import threading

score = 0
report = ["very poor","Poor", "Bad", "Good", "Strong", "Very Strong"]

def timer():
    global sw
    sw = 10
    for x in range(10):
        sw = sw - 1
        sleep(1)
    print("TIME UP!!!")

timer_thread = threading.Thread(target = timer)
timer_thread.start()

while sw > 0:
    levels = input("Choose Level - 1. EASY 2. MEDIUM 3. HARD \n level:")
    if levels == "1":
        if sw == 0:
            break
        Q1 = input("How many days do we have in a week? \na. 5 \nb. 6 \nc. 7 \nd. 8 \nAnswer: ")
        if Q1 == "c":
            score += 1
        if sw == 0:
            break
        Q2 = input("How many days are there in a year? \na. 364 \nb. 365 \nc. 367 \nd. 366 \nAnswer: ")
        if Q2 == "b":
            score += 1
        if sw == 0:
            break
        Q3 = input("How many colors are there in a rainbow? \na. 7 \nb. 5 \nc. 8 \nd. 6 \nAnswer: ")
        if Q3 == "a":
            score += 1
        if sw == 0:
            break
        Q4 = input("Which animal is known as the Ship of the Desert? \na. Horse \nb. Dog \nc. Camel \nd. Bull \nAnswer: ")
        if Q4 == "c":
            score += 1
        if sw == 0:
            break
        Q5 = input("How many consonants are there in the English alphabet? \na. 22  \nb. 23 \nc. 21 \nd. 25 \nAnswer: ")
        if Q5 == "c":
            score += 1
        if sw == 0:
            break
        print("Correct options Are-")
        print("1. c(7) \n2. b(365) \n3. a(7) \n4. c(Camel) \n5. c(21)")
    elif levels == "2":
        if sw == 0:
            break
        Q1 = input("Which one of the following river flows between Vindhyan and Satpura ranges? \na. Narmada \nb. Mahandi \nc. Son \nd. Netravati \nAnswer: ")
        if Q1 == "a":
            score += 1
        if sw == 0:
            break
        Q2 = input("The Central Rice Research Station is situated in? \na. Chennai \nb. Cuttack \nc. Bangalore \nd. Quilon \nAnswer: ")
        if Q2 == "b":
            score += 1
        if sw == 0:
            break
        Q3 = input("Who among the following wrote Sanskrit grammar? \na. Kalidasa \nb. Charak \nc. Panini \nd. Aryabhatt \nAnswer: ")
        if Q3 == "c":
            score += 1
        if sw == 0:
            break
        Q4 = input("Which among the following headstreams meets the Ganges in last? \na. Alaknanda \nb. Pindar \nc. Mandakini \nd. Bhahgirathi \nAnswer: ")
        if Q4 == "d":
            score += 1
        if sw == 0:
            break
        Q5 = input("The metal whose salts are sensitive to light is? \na. Zinc \nb. Silver \nc. Copper \nd. Aluminum \nAnswer: ")
        if Q5 == "b":
            score += 1
        if sw == 0:
            break
        print("Correct options Are-")
        print("1. a(Narmada) \n2. b(Cuttack) \n3. c(panini) \n4. d(Bhagirathi) \n5. b(silver)")
    elif levels == "3":
        if sw == 0:
            break
        Q1 = input("Patanjali is well known for the compilation of ? \na. Yoga Sutra \nb. Panchatantra \nc. Bhrahma Sutra \nd. Ayurvedh \nAnswer: ")
        if Q1 == "a":
            score += 1
        if sw == 0:
            break
        Q2 = input("The country that has the highest in Barley Production? \na. China \nb. India \nc. Russia \nd. France \nAnswer: ")
        if Q2 == "c":
            score += 1
        if sw == 0:
            break
        Q3 = input("Tsunamis are not caused by? \na. Hurricanes \nb. Earthquakes \nc. Undersea landslides \nd. Volcanic eruptions \nAnswer: ")
        if Q3 == "a":
            score += 1
        if sw == 0:
            break
        Q4 = input(" Chambal river is a part of? \na. Sabarmati basin \nb. Ganga basin \nc. Narmada basin \nd. Godavari basin \nAnswer: ")
        if Q4 == "c":
            score += 1
        if sw == 0:
            break
        Q5 = input("D.D.T. was invented by? \na. Mosley \nb. Rudolf \nc. Karl Benz \nd. Dalton \nAnswer: ")
        if Q5 == "a":
            score += 1
        if sw == 0:
            break
        print("Correct options Are-")
        print("1. a(Yoga Sutra) \n2. c(Russia) \n3. a(Hurricanes) \n4. c(Narmada basin) \n5. a(Mosely)")
    break
print("Score :",report[score])



