# MartinezP4
# Programmer: Adelita Martinez
# Email: amartinez1013@cnm.edu
# Purpose: Translate common phrases
# Python version: 3.12.3

#http://www.learnspanishtoday.com/learning_module/grammar.htm
english2spanish={'Good morning.':'Buenos días.',
'Good afternoon.':'Buenas tardes.',
'Good evening. (greeting)':'Buenas noches.',
'Hello, my name is John.':'Hola, me llamo Juan.',
'What is your name?':'¿Cómo se llama usted?',
'How are you?':'¿Cómo está usted?',
'I am fine.':'Estoy bien.',
'Nice to meet you.':'Mucho gusto.',
'Goodbye.':'Adiós.',
'See you later.':'Hasta luego.',
'I am lost. Where is the restroom?':'Estoy perdido. ¿Dónde está el baño?',
'Excuse me.':'Con permiso. OR Perdóname',
'Please.':'Por favor.',
'Thank you.':'Gracías.',
'Bless you.':'Salud.',
'You are welcome (it was nothing).':'De nada.',
'How much does it cost?':'¿Cuánto cuesta?',
'How many are there?':'¿Cuántos hay?',
'There are many.':'Hay muchos.',
'Do you want to buy this?':'¿Quiere comprarlo usted?',
'What time is it?':'¿Qué hora es?',
'How do you say maybe in Spanish?':'¿Cómo se dice maybe en Español?',
'Yes.':'Sí.',
'No.':'No.',
'I do not understand.':'Yo no comprendo.',
'Would you speak slower, please.':'Por favor, habla mas despacio.',
'Who?':'¿Quièn?',
'Why?':'¿Por què?'}

# Welcome and explaination
print("\nWelcome!")
print("This program acts as a english to spanish translator of common phrases.")

# Display available phrases
print("\nHere are the available phrases to choose from: ")
index = 1
for phrase in english2spanish: 
  print(f'{index}. {phrase}')
  index += 1


# Get user input
user_input = input("\nPlease type the number corresponding to the phrase you want translated: ")

# Process user input
user_input = int(user_input)
english_phrase = list(english2spanish.keys())[user_input - 1]
translation = list(english2spanish.values())[user_input - 1]


# Display Translation

print(f"\nThe translation of {english_phrase} is {translation}")
