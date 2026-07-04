from dotenv import load_dotenv
import os

load_dotenv()


def screening_agent(state):
    """
    Screening Agent (RAG + Scoring)

    Input:
        state["parsed_jd"]
        state["retrieved_resumes"]

    Output:
        state["ranked_candidates"]
    """

    jd = state["parsed_jd"]
    resumes = state["retrieved_resumes"]

    required_skills = jd.get("skills", [])

    ranked_candidates = []

    for resume in resumes:

        text = resume["text"].lower()

        matched_skills = []
        missing_skills = []

        # simple keyword match (hackathon-friendly, fast)
        for skill in required_skills:

            if skill.lower() in text:
                matched_skills.append(skill)
            else:
                missing_skills.append(skill)

        # scoring logic
        if len(required_skills) > 0:
            score = int((len(matched_skills) / len(required_skills)) * 100)
        else:
            score = 0

        ranked_candidates.append({
            "name": resume["filename"],
            "score": score,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills
        })

    # sort by score (VERY IMPORTANT for demo)
    ranked_candidates = sorted(
        ranked_candidates,
        key=lambda x: x["score"],
        reverse=True
    )

    state["ranked_candidates"] = ranked_candidates

    return state