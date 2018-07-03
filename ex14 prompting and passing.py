from sys import argv

script, user_name = argv

prompt = '> '

print(f"Hi {user_name}, I'm the {script} script")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name } ?")
likes = input()

print(f"where do you live {user_name} ?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

nums = [1, 2, 3]

print(for n in nums print(n))
