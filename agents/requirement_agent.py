from agents.llm import ask_ai


def analyze_requirement(requirement):

    system_prompt = """
    You are a professional Software Requirement Analyst.

    Your job is to analyze software requirements and prepare
    a clear implementation plan.

    Include:
    1. Project Overview
    2. Main Features
    3. Functional Requirements
    4. Technical Requirements
    5. Implementation Steps
    6. Expected Outcome

    Use simple professional language.
    Do not generate code.
    """

    user_prompt = f"""
    Analyze the following software requirement:

    {requirement}
    """

    result = ask_ai(system_prompt, user_prompt)

    return result