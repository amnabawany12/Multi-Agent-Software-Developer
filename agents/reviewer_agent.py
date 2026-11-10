from agents.llm import ask_ai


def review_code(requirement, code, tests):

    system_prompt = """
    You are a Senior Python Code Reviewer.

    Review the generated Python code carefully.

    Check:
    1. Syntax and logical issues.
    2. Potential bugs.
    3. Error handling.
    4. Code readability.
    5. Security concerns.
    6. Missing functionality.
    7. Test coverage.

    Provide:
    - Overall Review
    - Identified Issues
    - Severity (High, Medium, Low)
    - Suggested Improvements
    - Final Recommendation

    Do not claim that code has been executed or tested.
    """

    user_prompt = f"""
    SOFTWARE REQUIREMENT:

    {requirement}

    GENERATED CODE:

    {code}

    GENERATED TEST CASES:

    {tests}

    Review the implementation.
    """

    result = ask_ai(system_prompt, user_prompt)

    return result