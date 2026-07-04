
# =========================
# JD PARSER PROMPT
# =========================
JD_PARSE_PROMPT = """
You are an HR assistant.

Extract structured job information from the JD.

Return ONLY valid structured output with:
- role
- skills
- experience
- location
- education

Job Description:
{jd_text}
"""


# =========================
# INTERVIEW GENERATION PROMPT
# =========================
INTERVIEW_PROMPT = """
You are an expert technical interviewer.

Generate interview questions ONLY based on:
1. Job Description
2. Candidate Resume

Rules:
- Do NOT ask generic questions
- Focus on real technical depth

Job Description:
{jd}

Candidate Resume:
{resume}

Return JSON:
{
  "technical": [],
  "behavioral": []
}
"""


# =========================
# JD REWRITE PROMPT
# =========================
REWRITE_JD_PROMPT = """
Rewrite the following Job Description for a startup.

Make it:
- concise
- attractive
- startup-friendly
- skill-focused

Original JD:
{jd_text}
"""


# =========================
# SCREENING EXPLANATION PROMPT (optional upgrade)
# =========================
SCREENING_PROMPT = """
You are an AI recruiter.

Given:
1. Job Description
2. Candidate Resume

Explain why this candidate is a good or bad fit.

JD:
{jd}

Resume:
{resume}
"""


# =========================
# SALARY ANALYSIS PROMPT (optional upgrade)
# =========================
SALARY_PROMPT = """
Extract structured salary insights from web search results.

Return:
- average salary
- salary range
- top companies
- market trend summary

Data:
{data}
"""