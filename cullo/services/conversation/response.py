from cullo.rules.cullo_rules import culo_rules
from cullo.services.language.rule_matcher import match_rule
from cullo.services.language.pronoun_replacer import replace_pronouns
import json
from cullo.rules import bot_rules
from cullo.services.language.Interpreter import interpret

# Define conversate_response()
def conversate_response(message):
    print("conversate_response")
    """This method calls the function match_rule().
    This returns a response if the message matched
    a culo template, and otherwise, None"""

    # Call match_rule()
    response, phrase = match_rule(culo_rules, message)
    # Return none is response is "default"
    if response == "default":
        return None
    if '{0}' in response:
        # Replace the pronouns of phrase
        phrase = replace_pronouns(phrase)
        # Calculate the response
        response = response.format(phrase)
    return response

temp_bot_resp = ""
tmp_pending = None
# Define send_message()
def send_message(state, pending, message):

    """The method takes current state, tuple of pending state & intent and message
        as input and returns the next state and tuple of pending state & intent"""

    global temp_bot_resp
    global tmp_pending
    bot_response = ""
    print(message)
    print("send_message")
    response = conversate_response(message)

    if response is not None:
        tmp_r = json.dumps({'state': state, 'pending': None, 'return_message': response})
        print("inside 1 " + str(state) + "," + str(response) + ",")
        response = ""
        return tmp_r

    # Calculate the new_state, response, and pending_state
    print("send_message before interept")
    next_state, response, pending_state = bot_rules.get_bot_rules()[(state, interpret(message))]
    print("inside 1 " + str(next_state) + "," + str(response) + "," + str(pending_state))
    temp_bot_resp = response

    if pending is not None:
        next_state, response, pending_state = bot_rules.get_bot_rules()[pending]
        print("inside 2 " + str(next_state) + "," + str(response) + "," + str(pending_state))
        bot_response = response
    if pending_state is not None:
        pending = (pending_state, interpret(message))
        tmp_pending = pending

    return_msg = json.dumps({'state': next_state, 'pending': tmp_pending, 'return_message': temp_bot_resp + bot_response})
    temp_bot_resp = ""
    tmp_pending = None
    return return_msg