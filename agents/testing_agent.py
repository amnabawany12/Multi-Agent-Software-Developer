from agents.llm import ask_ai


def create_tests(requirement, code):

    system_prompt = """
    You are a Python Software Testing Engineer.

    Your job is to create pytest test cases for the
    generated Python code.

    Requirements:
    1. Generate valid Python pytest code.
    2. Test normal functionality.
    3. Test edge cases.
    4. Test invalid inputs where relevant.
    5. Use clear test function names.
    6. Do not execute the generated code.
    7. Do not invent functions that are not present in the code.
    8. If the code cannot be tested clearly, explain why.
    9. Output Python test code only.
    """

    user_prompt = f"""
    SOFTWARE REQUIREMENT:

    {requirement}

    GENERATED PYTHON CODE:

    {code}

    Create suitable pytest test cases.
    """

    result = ask_ai(system_prompt, user_prompt)

    return result