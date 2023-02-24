import json
from TuringMachine import TuringMachine


def tape_detail(tape_file: str):
    file = open(tape_file, "r")
    json_data = json.load(file)
    return json_data["metadata"]


def runner(tape_file: str, input_str: str, debug: bool = False):
    file = open(tape_file, "r")
    json_data = json.load(file)
    sigma, start_character, end_character, blank_character, start_state, end_state, tape = parse_tape(json_data)
    tm = TuringMachine(tape, sigma, start_character, end_character, blank_character, start_state, end_state)
    return tm.run(input_str, debug)


def tape_template_generator(path: str, name: str, author: str, description: str, sigma: str, start_character: str,
                            end_character: str, blank_character: str, start_state: str, end_state: str):
    json_data = {
        "metadata": {
            "name": name,
            "author": author,
            "description": description,
            "sigma": list(set(sigma)),
            "start_character": start_character,
            "end_character": end_character,
            "start_state": start_state,
            "end_state": end_state,
            "blank_character": blank_character
        },
        "tape": {
            start_state: {
            }
        }
    }
    for item in list(set(sigma)) + [blank_character,start_character]:
        json_data["tape"][start_state][item] = {
            "write": str(item),
            "move": +1,
            "state": str(start_state)
        }
    json_data["tape"][start_state][end_character] = {
        "write": end_character,
        "move": 0,
        "state": end_state
    }
    with open(path, "w") as file:
        json.dump(json_data, file, indent=2)


def parse_tape(tape: dict):
    try:
        metadata = tape["metadata"]
        tape = tape["tape"]
        start_character = metadata["start_character"]
        end_character = metadata["end_character"]
        blank_character = metadata["blank_character"]
        sigma = list(dict.fromkeys(metadata["sigma"] + [start_character, end_character, blank_character]))
        start_state = metadata["start_state"]
        end_state = metadata["end_state"]

        if start_state not in tape.keys():
            raise Exception(start_state, ": start_state not in", tape.keys())
        for i in tape.keys():
            for j in sigma:
                func = tape[i][j]
                if func.keys() != {"write", "move", "state"}:
                    raise Exception(i, ":", func, ": func keys not in {'write', 'move', 'state'}")
                if func["write"] not in sigma:
                    raise Exception(i, ":", func, ": write not in", sigma)
                if func["move"] not in [-1, 0, 1]:
                    raise Exception(i, ":", func, ": move not in [-1, 0, 1]")
                if func["state"] not in tape.keys() and func["state"] != end_state:
                    raise Exception(i, ":", func, ": state not in", tape.keys())
        return sigma, start_character, end_character, blank_character, start_state, end_state, tape
    except KeyError:
        raise Exception("Invalid tape file")


def tape_to_md(tape_file: str):
    file = open(tape_file, "r")
    json_data = json.load(file)
    sigma, start_character, end_character, blank_character, start_state, end_state, tape = parse_tape(json_data)
    print("K =", set(list(tape.keys())+[end_state]), start_state, "- start,", end_state, "- halt")
    print("Sigma =", sigma, start_character, "- begin,", end_character, "- end,", blank_character, "- blank")
    print("Table of transition functions delta:\n")
    print("|Index|t|k|delta(t,k)|")
    print("|:---:|:---:|:---:|:---|")
    i = 0
    for state in tape.keys():
        for character in sigma:
            i += 1
            write = tape[state][character]["write"]
            move = tape[state][character]["move"]
            next_state = tape[state][character]["state"]
            print("|", i, "|", state, "|", character, "|(", write, ",", next_state, ",", move, ")|")
