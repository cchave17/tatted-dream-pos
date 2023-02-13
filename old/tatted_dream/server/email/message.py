import json


class Message(object):

    def __init__(self, user_info):
        msg_info = json.dumps(user_info)
        load_msg = json.loads(msg_info)

        # form information
        self.name = load_msg["f_name"]
        self.last_name = load_msg["l_name"]
        self.travel_from = load_msg["travel_from"]
        self.email = load_msg["email"]
        self.phone = load_msg["phone"]
        self.instagram = load_msg['instagram']
        # self.description = load_msg['description']
        self.plans_to_cont = print_plans_to_cont(load_msg['plans-to-continue'])
        self.cover_up = print_cover_up(load_msg['cover-up'])
        self.rough_size = load_msg['rough-size']
        self.budget = load_msg['budget']
        # Change the availability
        # availability = load_msg['availability']

    def get_msg_parts(self):
        # form information
        name = self.name
        last_name = self.last_name
        travel_from = self.travel_from
        email = self.email
        phone = self.phone
        instagram = self.instagram
        # description = self.description
        plans_to_cont = self.plans_to_cont
        cover_up = self.cover_up
        rough_size = self.rough_size
        budget = self.budget
        # Change the availability
        # availability = load_msg['availability']
        return self

    def get_msg(self):
        msg_parts = self.get_msg_parts()
        msg = {
            "First Name: ": msg_parts.name,
            "Last Name: ": msg_parts.last_name,
            "Travel From: ": msg_parts.travel_from,
            "Email: ": msg_parts.email,
            "Phone: ": msg_parts.phone,
            "Instagram: ": msg_parts.instagram,
            # "Description: ": msg_parts.description,
            "Plans to continue: ": msg_parts.plans_to_cont,
            "Cover up: ": msg_parts.cover_up,
            "Rough size: ": msg_parts.rough_size,
            "Budget: ": msg_parts.budget
        }
        return msg


def print_plans_to_cont(plans_to_cont):
    if plans_to_cont == "1":
        return "Will want to continue in future"
    elif plans_to_cont == "2":
        return "I DO NOT WANT TO CONTINUE"
    else:
        return "I maybe continue this in the future (undecided) "


def print_cover_up(plans_to_cont):
    if plans_to_cont == "1":
        return "YES"
    elif plans_to_cont == "2":
        return "NO"
    # Get rid of this??
    else:
        return "Maybe"


def construct_email(msg):
    message = ""
    for part in msg:
        message += part
        message += msg[part]
        message += '\n'

    return message

