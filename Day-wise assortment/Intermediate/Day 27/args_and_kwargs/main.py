# Unlimited arguments
# When we use *args as argument we take as many input as we want and,
# all the inputs are stored as a tuple thru which we can then loop
# def add(*args: object) -> object:
#     final_sum = 0
#     for n in args:
#         final_sum += n
#
#     return final_sum
#
#
# print(add(3, 42, 3, 1, 253, 5, 3))


# Unlimited positional arguments
# What **kwargs does is, it creates a dictionary with the key arguments that we provide
# Example
# One more way to key value of a key is .get()
# Using this we dont get any errors if the value is not present
# If value not present it gives NONE as output
def calculate(n, **calulations):
    if "add" in calulations:
        n += calulations.get("add")
    if "multiply" in calulations:
        n *= calulations.get("multiply")

    return n


result = calculate(2, add=5, multiply=8)
print(result)


# Another example
def send_message(name, message, **options):
    # Access parameters with explicit names
    print(f"Sending message to {name}: {message}")
    # Access optional arguments from kwargs based on keys
    if "subject" in options:
        print(f"Subject: {options['subject']}")
    if "urgent" in options and options["urgent"]:
        print("Marked as urgent!")


send_message("Alice", "Happy birthday!", subject="Birthday Wishes", urgent=True)
# Output: Sending message to Alice: Happy birthday!
#         Subject: Birthday Wishes
#         Marked as urgent!

