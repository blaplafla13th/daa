import json


class TuringMachine:

    def __init__(self, tape: dict, sigma: list, start_character: str = "s", end_character: str = "e",
                 blank_character: str = " ", start_state: str = "start", end_state: str = "end"):
        self.start_character = start_character
        self.end_character = end_character
        self.start_state = start_state
        self.end_state = end_state
        self.blank_character = blank_character
        self.sigma = sigma
        self.tape = tape

    def check_input(self, input_str: str):
        for i in input_str:
            if i not in self.sigma:
                raise Exception(i, ": not in", self.sigma)
        return True

    def run(self, input_str: str, debug=False):
        if input_str == "":
            return ""
        if input_str[-1] != self.end_character:
            input_str += self.end_character
        if input_str[0] != self.start_character:
            input_str = self.start_character + input_str
        self.check_input(input_str)
        state = self.start_state
        index = 0
        if debug:
            print("View in markdown mode for better view \n")
            print("|input|index|state|change|")
            print("|:---|:---:|:---|:---|")
        while state != self.end_state:
            func = self.tape[state][input_str[index]]
            if index < 0:
                input_str = self.start_state + input_str
                index = 0
            elif index >= len(input_str):
                input_str += self.end_character
            print("|", input_str, "|", index, "|", state, "->", func["state"], "|", input_str[index], "->",
                  func["write"], "|") if debug else None
            input_str = input_str[:index] + func["write"] + input_str[index + 1:]
            index += func["move"]
            state = func["state"]
        input_str = input_str.replace(self.start_character, " ")
        input_str = input_str.replace(self.end_character, " ")
        input_str = input_str.replace(self.blank_character, " ")
        input_str = input_str.strip()
        if debug:
            print("\nOutput =", input_str)
        return input_str
