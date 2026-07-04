def route_decision(state):

    intent = state.get("intent")

    if intent == "jd_upload":
        return "jd_agent"

    if intent == "resume_count":
        return "count_agent"

    if intent == "screening":
        return "screening_agent"

    if intent == "interview":
        return "interview_agent"

    if intent == "salary":
        return "salary_agent"

    if intent == "rewrite_jd":
        return "rewrite_agent"

    return "response_agent"