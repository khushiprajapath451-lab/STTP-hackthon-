def response_agent(state):
    """
    Final response formatter

    Input:
        state (entire workflow output)

    Output:
        Prints final recruiter-friendly report
    """

    print("\n\n====================================")
    print("📊 FINAL RECRUITMENT REPORT")
    print("====================================\n")

    # Approval check
    if not state.get("approval", False):
        print("❌ Shortlist NOT approved by recruiter.")
        return state

    # Ranked candidates
    print("🏆 TOP CANDIDATES:\n")

    for c in state.get("ranked_candidates", []):
        print(f"- {c['name']} | Score: {c['score']}%")
        print(f"  Matched: {c.get('matched_skills', [])}")
        print(f"  Missing: {c.get('missing_skills', [])}\n")

    # Salary info
    print("💰 SALARY INSIGHTS:\n")
    salary = state.get("salary_data", {})

    print(f"Role: {salary.get('role')}")
    print(f"Location: {salary.get('location')}")
    print(f"Source: {salary.get('source')}\n")

    # Interview questions
    print("🎤 INTERVIEW QUESTIONS:\n")

    iq = state.get("interview_questions", {})

    if isinstance(iq, dict):
        print("Technical:")
        for q in iq.get("technical", []):
            print(f"- {q}")

        print("\nBehavioral:")
        for q in iq.get("behavioral", []):
            print(f"- {q}")
    else:
        print(iq)

    print("\n====================================")
    print("✅ PROCESS COMPLETED SUCCESSFULLY")
    print("====================================")

    return state