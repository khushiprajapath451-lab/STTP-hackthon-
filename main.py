from pathlib import Path
from graph.workflow import graph


def run_chatbot():
    print("\n===================================")
    print(" AI RECRUITMENT SYSTEM STARTED")
    print("===================================\n")

    jd_path = Path("data/jd/ai_engineer.txt")
    jd_text = jd_path.read_text(encoding="utf-8") if jd_path.exists() else ""

    state = {
        "query": "",
        "jd_text": jd_text,
        "parsed_jd": {},
        "resume_folder": "data/resumes",
        "resumes": [],
        "retrieved_resumes": [],
        "ranked_candidates": [],
        "selected_candidate": {},
        "interview_questions": {},
        "salary_data": {},
        "intent": "",
        "approval": False,
        "messages": []
    }

    while True:

        user_input = input("\n Recruiter: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting system...")
            break

        state["query"] = user_input

        state = graph.invoke(state)

        if state.get("messages"):
            for msg in state["messages"]:
                print("\n", msg)

        if state.get("ranked_candidates"):
            print("\n TOP CANDIDATES:")
            for c in state["ranked_candidates"]:
                print(f"- {c['name']} | Score: {c['score']}%")

        if state.get("salary_data"):
            print("\n SALARY INFO:")
            print(state["salary_data"])

        if state.get("interview_questions"):
            print("\n INTERVIEW QUESTIONS:")
            print(state["interview_questions"])

        # DEBUG (SAFE)
        print("\nDEBUG JD:", state.get("parsed_jd", {}))
        print("DEBUG RESUMES:", len(state.get("resumes", [])))

        print("\n-----------------------------------")


if __name__ == "__main__":
    run_chatbot()