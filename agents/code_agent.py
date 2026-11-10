from agents.llm import ask_ai, clean_code


def generate_code(requirement, plan):

    system_prompt = """
    You are a Senior Python Developer.

    Generate complete, clean and functional Python code
    according to the provided software requirement and plan.

    Rules:
    1. Generate Python code only.
    2. Include necessary imports.
    3. Use meaningful variable names.
    4. Include error handling where appropriate.
    5. Add helpful comments.
    6. Avoid unnecessary dependencies.
    7. Do not use dangerous system commands.
    8. Do not include markdown explanations.
    """

    user_prompt = f"""
    SOFTWARE REQUIREMENT:

    {requirement}

    IMPLEMENTATION PLAN:

    {plan}

    Generate the complete Python implementation.
    """

    result = ask_ai(system_prompt, user_prompt)

    return clean_code(result)