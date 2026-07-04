from typing import TypedDict, List, Dict, Any


class RecruiterState(TypedDict):

    # user input
    query: str

    # JD
    jd_text: str
    parsed_jd: Dict[str, Any]

    # resumes
    resumes: List[Dict]
    retrieved_resumes: List[Dict]

    # screening
    ranked_candidates: List[Dict]
    selected_candidate: Dict

    # outputs
    interview_questions: Any
    salary_data: Dict

    # control
    intent: str
    approval: bool
    messages: List[str]