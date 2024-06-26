from pathlib import Path
import datetime

def assess_mood(): 
    date_today = str(datetime.date.today())
    mood_diary_file = 'data/mood_diary.txt'

    existing_entry = False

    f = open(mood_diary_file, 'r')
    for line in f:
        if date_today in line:
            print("Sorry, you have already entered your mood today.")
            existing_entry = True
            break

    if existing_entry is False:
        ask_again = False
        while not ask_again:
            current_mood = input("Please enter your current mood: ").lower()
            if current_mood in ['happy', 'relaxed', 'apathetic', 'sad', 'angry']:
                ask_again = True
                if current_mood == 'angry':
                    current_mood = -2
                elif current_mood == 'sad':
                    current_mood = -1
                elif current_mood == 'apathetic':
                    current_mood = 0
                elif current_mood == 'relaxed':
                    current_mood = 1
                elif current_mood == 'happy':
                    current_mood = 2
                else:
                    ask_again = False


        f = open(mood_diary_file, 'a')
        f.write(f'{date_today}: {current_mood}\n')
        f.close()

        f = open(mood_diary_file, 'r')
        lines = f.readlines()
        f.close()

        if len(lines) >= 7:
            recent_entries = lines[-7:]
            happy_counter = 0
            sad_counter = 0
            apathetic_counter = 0
            total_mood = 0

            for user_entry in recent_entries:
                mood_integer = int(user_entry.split(': ')[1])
                if mood_integer == 2:
                    happy_counter = happy_counter + 1
                elif mood_integer == -1:
                    sad_counter = sad_counter + 1
                elif mood_integer == 0:
                    apathetic_counter = apathetic_counter + 1
                total_mood = total_mood + mood_integer

            if happy_counter >= 5:
                diagnosis = 'manic'
            elif sad_counter >= 4:
                diagnosis = 'depressive'
            elif apathetic_counter >= 6:
                diagnosis = 'schizoid'
            else:
                mood_average = round(total_mood/7)
                if mood_average == -2:
                    diagnosis = 'angry'
                elif mood_average == -1:
                    diagnosis = 'sad'
                elif mood_average == 0:
                    diagnosis = 'apathetic'
                elif mood_average == 1:
                    diagnosis = 'relaxed'
                elif mood_average == 2:
                    diagnosis == 'happy'
            print(f'Your diagnosis: {diagnosis}!')
                
        
    


