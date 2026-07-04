def approval_agent(state):
    """
    Human-in-the-loop approval agent

    Input:
        state["ranked_candidates"]

    Output:
        state["approval"] (True/False)
    """

    print("\n==============================")
    print("TOP CANDIDATES (FOR APPROVAL)")
    print("==============================\n")

    for idx, c in enumerate(state.get("ranked_candidates", []), 1):
        print(f"{idx}. {c['name']} - Score: {c['score']}")

    print("\n------------------------------")
    user_input = input("Do you want to finalize shortlist? (yes/no): ").strip().lower()

    if user_input in ["yes", "y"]:
        state["approval"] = True
    else:
        state["approval"] = False

    return state