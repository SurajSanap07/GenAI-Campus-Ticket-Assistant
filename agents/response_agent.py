
import os

from openai import OpenAI


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)


def generate_response(
    ticket,
    analysis,
    risk,
    policy_chunks,
    question
):

    policy_context = "\n\n".join(
        policy_chunks
    )

    prompt = f"""
You are CampusGenAI, a secure campus administration AI assistant.

The user has already been authorized to access the following ticket.

AUTHORIZED TICKET INFORMATION:

Ticket ID: {ticket["ticket_id"]}
Department: {ticket["department"]}
Issue: {ticket["issue"]}
Priority: {ticket["priority"]}
Status: {ticket["status"]}
Previous Incidents: {ticket["previous_incidents"]}
Ticket Age: {ticket["ticket_age_days"]} days

TICKET ANALYSIS:

Issue Type: {analysis["issue_type"]}
Affected Area: {analysis["affected_area"]}

PREDICTED ESCALATION RISK:

{risk}

RELEVANT CAMPUS POLICY:

{policy_context}

USER QUESTION:

{question}

INSTRUCTIONS:

1. Answer only using the authorized ticket information and relevant campus policy.
2. Do not reveal information about other users or tickets.
3. Do not invent campus rules.
4. If the policy information is insufficient, clearly say that the available campus policy does not provide enough information.
5. Give a concise and helpful answer.
6. Explain the recommended next action when appropriate.
"""


    response = client.chat.completions.create(

        model="openrouter/free",

        messages=[

            {
                "role": "system",
                "content":
                "You are a secure campus administration assistant."
            },

            {
                "role": "user",
                "content": prompt
            }

        ]
    )


    return response.choices[0].message.content
