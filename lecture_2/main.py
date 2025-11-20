def generate_profile(age: int):
    """Returns the user's life stage based on age."""
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"

# Get User Input
user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")

birth_year = int(birth_year_str)

current_age = 2025 - birth_year  # Calculate age

hobbies = []

# Ask for hobbies
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    hobbies.append(hobby)

# Process and Generate the Profile
life_stage = generate_profile(current_age)

user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

# Display Output
print("\n---")
print("Profile Summary:")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['stage']}")

if len(hobbies) == 0:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(hobbies)}):")
    for hobby in user_profile['hobbies']:
        print(f"- {hobby}")

print("---")