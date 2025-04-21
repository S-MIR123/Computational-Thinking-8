# beginning
extro_p = 0
intro_p = 0


# Middle
answer = input("Do you eat lunch with friends (A) or alone (B)?  ")
if answer == "A":
    extro_p += 1
elif answer == "B":
    intro_p += 1


answer = input("Do you talk with friends during class? Yes (A) or No (B)?  ")
if answer == "A":
    extro_p += 1
elif answer == "B":
    intro_p += 1


answer = input("Being around others makes me feel: Energized (A) or Exhausted (B)  ")
if answer == "A":
    extro_p += 1
elif answer == "B":
    intro_p += 1


answer = input("During social gatherings I tend to: Talk to others (A) or Keep to myself (B)  ")
if answer == "A":
    extro_p += 1
elif answer == "B":
    intro_p += 1


answer = input("When I am dealing with a problem I will: Talk to others about it (A) or keep to myself (B)  ")
if answer == "A":
    extro_p += 1
elif answer == "B":
    intro_p += 1


# end
if extro_p > intro_p:
    print("You are a extrovert!")
elif extro_p < intro_p:
    print("You are a introvert!")