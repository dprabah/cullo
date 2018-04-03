import re
import random

# Define match_rule()
def match_rule(rules, message):
    print(match_rule)
    """Clever thing about CULO is the way the
    program appears to understand what you told it, by
    occasionally including phrases uttered by the user
    in its responses. This method will match messages
    against some common patterns from dictionary called
    culo_rules and extract phrases """

    response, phrase = "default", None

    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Return the response and phrase
    return response, phrase