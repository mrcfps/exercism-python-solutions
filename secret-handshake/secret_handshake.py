binary_to_action = {
    1: "wink",
    2: "double blink",
    4: "close your eyes",
    8: "jump",
}

action_to_binary = {
    "wink": 1,
    "double blink": 2,
    "close your eyes": 4,
    "jump": 8,
}


def handshake(code):
    actions = []
    for binary, action in binary_to_action.items():
        if binary & code:
            actions.append(action)
    if code & 16:
        actions.reverse()
    return actions


def secret_code(actions):
    binary_list = [action_to_binary[action] for action in actions]
    code = sum(binary_list)

    # Check if the order is reversed
    if len(binary_list) > 1 and binary_list[0] > binary_list[1]:
        code += 16

    return code
