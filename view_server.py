"""
view module for create massages to user
"""
import server_controller


def get_popular():
    """
    return the number that appeared the most in the bot history.
    :return: str with the number and count.
    """
    popular_num_count = server_controller.popular()
    return "The number that appeared the most is: " + popular_num_count[0] + ". Number of appearances: " + \
           popular_num_count[1].__str__()


def interpret_message(sender_name, msg_text):
    """
    Interpret the message received. The message contains a command.
    According to the command received, activate an appropriate function.
    The function will return the answer.

    If one of the orders is received "/prime", "/factorial", "/ palindrome", "/ sqrt"
    And then any number, run the appropriate function on the number.

    If the "/ popular" command is received Run the function to find the popular number.

    If another message is received, return "I do not understand you".

    :param sender_name: str of sender name
    :param msg_text: str of message
    :return: str of reply.
    """
    input_words = msg_text.lstrip().split()
    if input_words.__len__() == 1 and input_words[0] == "/popular":
        return get_popular()
    if input_words.__len__() == 2 and input_words[1].isnumeric():
        num = int(input_words[1])
        server_controller.num_appearance(num)
        switcher = {
            "/prime": is_prime_to_str(num),
            "/factorial": is_factorial_to_str(num),
            "/palindrome": is_palindrome_to_str(num),
            "/sqrt": have_sqrt_to_str(num)
        }
        return switcher.get(input_words[0], "I do not understand you.")
    else:
        return "I do not understand you."
