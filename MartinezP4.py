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
for phrase in english2spanish: 
  print(phrase)

# Get user input
user_input = input("\nPlease type out the phrase you want translated(case-sensitive and sensitive to symbols): ")

# Process user input
user_input = user_input.strip()
translation = english2spanish.get(user_input, "Phrase not found in list. Please restart program and try again.")
# Display Translation

print(f"\nThe translation of {user_input} is {translation}")
