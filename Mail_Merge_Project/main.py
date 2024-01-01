
with open("Input/Letters/starting_letter.txt","r") as pismo:
    letter = pismo.read()
with open("Input/Names/invited_names.txt", "r") as names:
    list_names = names.readlines()

for i in list_names:
    i = i.strip()
    with open(f"../Mail Merge Project Start/Output/ReadyToSend/letter_for_{i}.txt", "w") as file:
        replaced = letter.replace("[name]",i)
        file.write(replaced)




