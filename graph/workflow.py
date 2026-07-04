from langgraph.graph import StateGraph, END

from graph.state import RecruiterState
from graph.router import router
from graph.edges import route_decision

from agents.jd_agent import jd_agent
from agents.resume_agent import resume_agent
from agents.screening_agent import screening_agent
from agents.interview_agent import interview_agent
from agents.salary_agent import salary_agent
from agents.approval_agent import approval_agent
from agents.response_agent import response_agent

from tools.count_tool import count_applicants


# -------------------------
# BUILD GRAPH
# -------------------------

workflow = StateGraph(RecruiterState)

# nodes
workflow.add_node("router", router)
workflow.add_node("jd_agent", jd_agent)
workflow.add_node("resume_agent", resume_agent)
workflow.add_node("screening_agent", screening_agent)
workflow.add_node("interview_agent", interview_agent)
workflow.add_node("salary_agent", salary_agent)
workflow.add_node("approval_agent", approval_agent)
workflow.add_node("response_agent", response_agent)

# tool node
workflow.add_node(
    "count_agent",
    lambda state: {
        **state,
        "messages": [
            f"Total Applicants: {count_applicants(state.get('resumes', []))}"
        ],
    },
)

# -------------------------
# ENTRY
# -------------------------

workflow.set_entry_point("router")

# -------------------------
# CONDITIONAL ROUTING
# -------------------------

workflow.add_conditional_edges(
    "router",
    route_decision,
    {
        "jd_agent": "jd_agent",
        "count_agent": "count_agent",
        "screening_agent": "screening_agent",
        "interview_agent": "interview_agent",
        "salary_agent": "salary_agent",
        "response_agent": "response_agent",
    },
)

# -------------------------
# LINEAR FLOW
# -------------------------

workflow.add_edge("jd_agent", "resume_agent")
workflow.add_edge("resume_agent", "screening_agent")
workflow.add_edge("screening_agent", "approval_agent")

workflow.add_edge("approval_agent", "interview_agent")
workflow.add_edge("interview_agent", "salary_agent")
workflow.add_edge("salary_agent", "response_agent")

workflow.add_edge("count_agent", "response_agent")

workflow.add_edge("response_agent", END)

# compile
graph = workflow.compile()
from langgraph.graph import StateGraph, END

from graph.state import RecruiterState
from graph.router import router
from graph.edges import route_decision

# agents
from agents.jd_agent import jd_agent
from agents.resume_agent import resume_agent
from agents.screening_agent import screening_agent
from agents.interview_agent import interview_agent
from agents.salary_agent import salary_agent
from agents.approval_agent import approval_agent
from agents.response_agent import response_agent

from tools.count_tool import count_applicants


# -------------------------
# BUILD GRAPH
# -------------------------

workflow = StateGraph(RecruiterState)

# nodes
workflow.add_node("router", router)
workflow.add_node("jd_agent", jd_agent)
workflow.add_node("resume_agent", resume_agent)
workflow.add_node("screening_agent", screening_agent)
workflow.add_node("interview_agent", interview_agent)
workflow.add_node("salary_agent", salary_agent)
workflow.add_node("approval_agent", approval_agent)
workflow.add_node("response_agent", response_agent)

# tool node
workflow.add_node(
    "count_agent",
    lambda state: {
        **state,
        "messages": [
            f"Total Applicants: {count_applicants(state.get('resumes', []))}"
        ],
    },
)

# -------------------------
# ENTRY
# -------------------------

workflow.set_entry_point("router")

# -------------------------
# CONDITIONAL ROUTING
# -------------------------

workflow.add_conditional_edges(
    "router",
    route_decision,
    {
        "jd_agent": "jd_agent",
        "count_agent": "count_agent",
        "screening_agent": "screening_agent",
        "interview_agent": "interview_agent",
        "salary_agent": "salary_agent",
        "response_agent": "response_agent",
    },
)

# -------------------------
# LINEAR FLOW
# -------------------------

workflow.add_edge("jd_agent", "resume_agent")
workflow.add_edge("resume_agent", "screening_agent")
workflow.add_edge("screening_agent", "approval_agent")

workflow.add_edge("approval_agent", "interview_agent")
workflow.add_edge("interview_agent", "salary_agent")
workflow.add_edge("salary_agent", "response_agent")

workflow.add_edge("count_agent", "response_agent")

workflow.add_edge("response_agent", END)

# compile
graph = workflow.compile()
if __name__ == "__main__":
    print(graph.get_graph().draw_mermaid())

if __name__ == "__main__":
    img = graph.get_graph().draw_mermaid_png()

    with open("workflow.png", "wb") as f:
        f.write(img)

    print("workflow.png created")