from send_email import send_email


def construct_email(msg):
    message = ""
    for part in msg:
        message += part
        message += msg[part]
        message += '\n'

    return message
