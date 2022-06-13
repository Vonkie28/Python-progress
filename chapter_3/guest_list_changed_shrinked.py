#First set of invitations
guests = ['donny', 'dennis', 'justin']
print(f"Bij deze nodig ik je uit voor een etentje, {guests[0]}. ")
print(f"Bij deze nodig ik je uit voor een etentje, {guests[1]}. ")
print(f"Bij deze nodig ik je uit voor een etentje, {guests[2]}. ")

#Add guest
guests.append('nicky')
print(guests)

#Delete guest
del guests[1]
print(guests)

#Second set of invitation
print(f"Dit is de tweede uitnodiging voor het etentje, {guests[0]}. ")
print(f"Dit is de tweede uitnodiging voor het etentje, {guests[-1]}. ")
print(f"Dit is de tweede uitnodiging voor het etentje, {guests[-2]}. ")

#Insert beginning of the list
guests.insert(0, 'lars')
print(guests)

#Insert in the middle of the list
guests.insert(2, 'jarmin')
print(guests)

#insert at the end of the list
guests.append('levi')
print(guests)

#Third set of invitation
print(f"{guests[0]}, Hierbij de uitnodiging voor het etentje aankomend weekend. ")
print(f"{guests[1]}, Hierbij de uitnodiging voor het etentje aankomend weekend. ")
print(f"{guests[2]}, Hierbij de uitnodiging voor het etentje aankomend weekend. ")
print(f"{guests[3]}, Hierbij de uitnodiging voor het etentje aankomend weekend. ")
print(f"{guests[4]}, Hierbij de uitnodiging voor het etentje aankomend weekend. ")

#printing message that only two people can come
print("Er kunnen maar twee mensen komen dus ik zal uitnodigingen sturen naar diegene die mogen komen")

#Popping soms of the guests
first_rejected = guests.pop(0)
second_rejected = guests.pop(1)
third_rejected = guests.pop(2)
fourth_rejected = guests.pop(2)
print(f"Hierbij kan ik je niet uitnodigingen voor mijn etentje, {first_rejected.title()}. ")
print(f"Hierbij kan ik je niet uitnodigingen voor mijn etentje, {second_rejected.title()}. ")
print(f"Hierbij kan ik je niet uitnodigingen voor mijn etentje, {third_rejected.title()}. ")
print(f"Hierbij kan ik je niet uitnodigingen voor mijn etentje, {fourth_rejected.title()}. ")

#Letting the two guests know they are invited
print(guests)
print(f"Jullie zijn de twee uitgenodigd voor mijn etentje, {guests[0]}. ")
print(f"Jullie zijn de twee uitgenodigd voor mijn etentje, {guests[1]}. ")

#deleting the two guests from lists
del guests
print(guests)