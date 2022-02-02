PLACEHOLDER = "[name]"

with open("./input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./input/letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        striped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, striped_name)
        with open(f"./output/ready_to_send/letter_for_{striped_name}.txt", mode="w") as compeleted_letter:
            compeleted_letter.write(new_letter)

