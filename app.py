
import streamlit as st

from agents.access_control import verify_ticket_access
from agents.orchestrator import process_ticket
from agents.response_agent import generate_response


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="CampusGenAI",
    page_icon="🎓",
    layout="wide"
)


# ==========================================
# HEADER
# ==========================================

st.title("🎓 CampusGenAI")

st.subheader(
    "Smart Campus Ticket & Information Access Assistant"
)

st.write(
    "Securely access authorized campus ticket information "
    "and interact with the AI assistant."
)

st.divider()


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.header("🔐 Ticket Verification")

    ticket_id = st.text_input(
        "🎫 Ticket ID",
        placeholder="Example: CAMP-1001"
    )

    user_id = st.text_input(
        "👤 User ID",
        placeholder="Example: STU001"
    )

    verify_button = st.button(
        "🔍 Verify Ticket",
        use_container_width=True
    )


# ==========================================
# SESSION STATE
# ==========================================

if "authorized" not in st.session_state:
    st.session_state.authorized = False

if "ticket" not in st.session_state:
    st.session_state.ticket = None


# ==========================================
# VERIFY ACCESS
# ==========================================

if verify_button:

    if not ticket_id or not user_id:

        st.warning(
            "⚠️ Please enter both Ticket ID and User ID."
        )

    else:

        authorized, ticket = verify_ticket_access(
            ticket_id,
            user_id
        )

        if authorized:

            st.session_state.authorized = True
            st.session_state.ticket = ticket

            st.success(
                "✅ Access Granted"
            )

        else:

            st.session_state.authorized = False
            st.session_state.ticket = None

            st.error(
                "❌ Access Denied. "
                "Invalid Ticket ID or User ID."
            )


# ==========================================
# AUTHORIZED CONTENT
# ==========================================

if st.session_state.authorized:

    ticket = st.session_state.ticket

    st.success(
        f"Authorized access for {ticket['ticket_id']}"
    )

    st.header("📋 Ticket Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Ticket ID",
            ticket["ticket_id"]
        )

    with col2:

        st.metric(
            "Priority",
            ticket["priority"]
        )

    with col3:

        st.metric(
            "Status",
            ticket["status"]
        )


    st.write("### Ticket Details")

    st.write(
        "**Department:**",
        ticket["department"]
    )

    st.write(
        "**Issue:**",
        ticket["issue"]
    )

    st.write(
        "**Previous Incidents:**",
        ticket["previous_incidents"]
    )

    st.write(
        "**Ticket Age:**",
        ticket["ticket_age_days"],
        "days"
    )


    st.divider()


    # ==========================================
    # USER QUESTION
    # ==========================================

    st.header("💬 Ask CampusGenAI")

    question = st.text_area(
        "Enter your question:",
        placeholder=(
            "Example: What should I do about this issue?"
        )
    )


    ask_button = st.button(
        "🤖 Ask CampusGenAI",
        use_container_width=True
    )


    # ==========================================
    # AI PROCESSING
    # ==========================================

    if ask_button:

        if not question.strip():

            st.warning(
                "⚠️ Please enter a question."
            )

        else:

            with st.spinner(
                "🤖 CampusGenAI is analyzing your ticket..."
            ):

                result = process_ticket(
                    ticket,
                    question
                )


            # ==================================
            # TICKET ANALYSIS
            # ==================================

            st.header("🤖 AI Ticket Analysis")

            col1, col2 = st.columns(2)

            with col1:

                st.info(
                    f"**Issue Type:** "
                    f"{result['analysis']['issue_type']}"
                )

            with col2:

                st.info(
                    f"**Affected Area:** "
                    f"{result['analysis']['affected_area']}"
                )


            # ==================================
            # RISK PREDICTION
            # ==================================

            st.header("⚠️ Risk Prediction")

            risk = result["risk"]

            if risk == "HIGH":

                st.error(
                    f"🔴 Escalation Risk: {risk}"
                )

            elif risk == "MEDIUM":

                st.warning(
                    f"🟠 Escalation Risk: {risk}"
                )

            else:

                st.success(
                    f"🟢 Escalation Risk: {risk}"
                )


            # ==================================
            # POLICY RESULTS
            # ==================================

            st.header("📚 Relevant Campus Policy")

            for i, policy in enumerate(
                result["policy"]
            ):

                with st.expander(
                    f"Policy Result {i + 1}"
                ):

                    st.write(policy)


            # ==================================
            # LLM RESPONSE
            # ==================================

            with st.spinner(
                "🧠 Generating secure AI response..."
            ):

                answer = generate_response(

                    ticket=result["ticket"],

                    analysis=result["analysis"],

                    risk=result["risk"],

                    policy_chunks=result["policy"],

                    question=question
                )


            st.header("💡 CampusGenAI Response")

            st.success(answer)


# ==========================================
# NO AUTHORIZATION
# ==========================================

else:

    st.info(
        "🔐 Enter a valid Ticket ID and User ID "
        "from the sidebar to access the system."
    )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "CampusGenAI | GenAI-Powered Smart Campus "
    "Ticket & Information Access Assistant"
)
