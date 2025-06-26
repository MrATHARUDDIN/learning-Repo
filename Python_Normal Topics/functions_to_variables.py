def hello():
    print("Hello")

print(hello)  # This prints the memory address of the function 'hello'
hi = hello    # Assigns the function object 'hello' to the variable 'hi'

hi()          # This calls the function via the new variable 'hi'
