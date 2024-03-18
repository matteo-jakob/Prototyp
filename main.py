from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(".env")
client = OpenAI()


def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)


def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()


system_content = """You are a professional coach for personalized workouts. You give short and concise answers and what workouts one should do. 
A workout might need to contain available equipment. You're going to receive inputs from a user in within the hashtags '#'. 
If no value is in the hastags, the user didn't send any values for that specific question/option. Make sure that at the end of each message you describe the each workout name u used."""

print("Prototype Cooach | Matteo Jakob I21a 2024")
print("\nHello! I'm your personal coach. To get started, take a minute to answer my questions and I will create a workout plan for you:")
workout_before = input("Did you have a workout before? [y|n]").lower()
if workout_before == "y":
    workout_name = input("Describe your last workout: ")
    workout_reps_sets = input(
        "Enter the amount of reps, sets and maybe weight of your last workout: ")
    workout_feedback = input(
        "Rate your last workout from 1 to 10, where one is too easy and 10 too hard: ")
    workout_equipment = input(
        "Do you have any equipment available you would like to use? (For example dumbbells and jumping rope)")
    workout_length = input("How long would you like your workout to be?")
    workout_preferences = input(
        "Are there any preferences you would like the coach to know? (upper body for example, any restrictions or questions)")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": f"he users last workout: #{workout_name}# The amount of reps, sets and maybe other relevant information: #{workout_reps_sets}#, Last workout difficulty from 1-10, where 10 is too hard and 1 is too easy: #{workout_feedback}#, equipment the user would like to have incoporated: #{workout_equipment}#, workout duration #{workout_length}#, Additional information from the user: #{workout_preferences}#. Create a workout plan for 7 days consider that the daily workout should not exceed 10 minutes more or less of the provided duration. You do not have to use the provided equipment, but if deemed of value make sure to use it. Your answer should be nicely formatted by seperating each day."}
        ]
    )
    print("[!] Here's your plan:")
    print(completion.choices[0].message)
else:
    workout_equipment = input(
        "Do you have any equipment (ex. dumbbells) available, which you would like to use?")
    workout_preferences = input(
        "Is there anything you would like the coach to know?")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": f"The user didn't do any workouts beforehand. Create a workout plan for 7 days including the following equipment if provided: #{workout_equipment}#.  Your answer should be nicely formatted by seperating each day. Make sure the workout is fit for the average male. Here is additional information the user may have provided: #{workout_preferences}#"}
        ]
    )
    print(completion.choices[0].message)
