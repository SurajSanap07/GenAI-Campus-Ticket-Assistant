
from agents.ticket_analyzer import analyze_ticket
from agents.risk_agent import predict_risk
from agents.policy_agent import get_relevant_policy


def process_ticket(ticket, question):

    # Agent 1: Ticket Analyzer
    analysis = analyze_ticket(ticket)

    # Agent 2: Risk Prediction Agent
    risk = predict_risk(ticket)

    # Agent 3: Policy/RAG Agent
    policy = get_relevant_policy(
        question,
        top_k=3
    )

    return {
        "ticket": ticket,
        "analysis": analysis,
        "risk": risk,
        "policy": policy
    }
