from knowledge_base import get_response


def process_message(message):
    """
    Process the user's message and return NOVA's response.
    """

    if not message or not message.strip():
        return "Please enter a message."

    message = message.strip()

    return get_response(message)