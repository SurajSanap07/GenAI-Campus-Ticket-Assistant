
import pandas as pd


def verify_ticket_access(ticket_id, user_id):
    tickets = pd.read_csv("data/tickets.csv")

    ticket = tickets[
        (tickets["ticket_id"].str.upper() == ticket_id.upper()) &
        (tickets["user_id"].str.upper() == user_id.upper())
    ]

    if ticket.empty:
        return False, None

    return True, ticket.iloc[0].to_dict()
