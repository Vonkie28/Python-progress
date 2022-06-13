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

