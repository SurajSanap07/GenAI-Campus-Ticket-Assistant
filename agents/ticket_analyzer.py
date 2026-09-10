
def analyze_ticket(ticket):

    issue = ticket["issue"].lower()

    if "unauthorized" in issue or "suspicious" in issue:
        issue_type = "SECURITY"
        affected_area = "Campus Security"

    elif "wifi" in issue:
        issue_type = "NETWORK"
        affected_area = "Campus WiFi"

    elif "id card" in issue:
        issue_type = "IDENTITY"
        affected_area = "Student ID System"

    elif "library" in issue:
        issue_type = "ACCESS"
        affected_area = "Library System"

    elif "examination" in issue or "login" in issue:
        issue_type = "SYSTEM"
        affected_area = "Examination Portal"

    else:
        issue_type = "GENERAL"
        affected_area = "Campus Administration"

    return {
        "issue_type": issue_type,
        "affected_area": affected_area
    }
