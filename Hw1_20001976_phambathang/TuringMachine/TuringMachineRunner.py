from TuringMachineUtils import runner, tape_detail, tape_template_generator, tape_to_md

if __name__ == '__main__':
    end = False
    while not end:
        print("1. Run Turing Machine")
        print("2. Generate Turing Machine Tape Template")
        print("3. Export to MD")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                tape_file = input("Enter tape file: ")
                print(tape_detail(tape_file))
                debug = input("Debug mode (press Yes to enable): ")
                debug = True if debug == "Yes" else False
                input_str = input("Input: ")
                print(runner(tape_file, input_str, debug))
            except Exception as e:
                print(e)
        elif choice == "2":
            path = input("Enter path: ")
            name = input("Enter tape name: ")
            author = input("Enter author: ")
            description = input("Enter description: ")
            sigma = input("Enter sigma: ")
            start_state = input("Enter start state: ")
            end_state = input("Enter end state: ")
            start_character = input("Enter start character: ")
            end_character = input("Enter end character: ")
            blank_character = input("Enter blank character: ")
            tape_template_generator(path, name, author, description, sigma, start_character, end_character
                                    , blank_character, start_state, end_state)
        elif choice == "3":
            tape_file = input("Enter tape file: ")
            tape_to_md(tape_file)
        elif choice == "0":
            end = True
        else:
            print("Invalid choice")
        print("\n" * 3)
