import re


# Define replace_pronouns()
def replace_pronouns(message):


    """This method will swap pronouns where it will
    map "me" and "my" to "you" and "your" (and vice versa)
    in a string."""


    message = message.lower()
    print("proper noun " + message)
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub(' me ', ' you ', message)
    if 'my' in message:
        # Replace 'my' with 'your'
        return re.sub(' my ', ' your ', message)
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub(' your ', ' my ', message)
    if 'you' in message:
        # Replace 'you' with 'me'
        return re.sub(' you ', ' me ', message)
    if 'i' in message:
        return re.sub(' i ',' you ', message)
