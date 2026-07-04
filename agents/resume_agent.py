from pathlib import Path


def resume_agent(state):
    """
    Resume Agent

    Input:
        state["resume_folder"]

    Output:
        state["resumes"]
    """

    # ✅ get folder safely
    folder = Path(state.get("resume_folder", "data/resumes"))

    resumes = []

    # Read every txt file
    for file in folder.glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            resumes.append({
                "filename": file.name,
                "text": f.read()
            })

    state["resumes"] = resumes

    return state