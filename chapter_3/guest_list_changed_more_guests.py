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

#Counting the guests with len
print(len(guests))