from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.requirement_agent import analyze_requirement
from agents.code_agent import generate_code
from agents.testing_agent import create_tests
from agents.reviewer_agent import review_code


class DeveloperState(TypedDict):
    requirement: str
    plan: str
    code: str
    tests: str
    review: str
    report: str


# Agent 1: Requirement Analyst
def requirement_node(state: DeveloperState):

    plan = analyze_requirement(state["requirement"])

    return {"plan": plan}


# Agent 2: Code Generator
def code_node(state: DeveloperState):

    code = generate_code(
        state["requirement"],
        state["plan"]
    )

    return {"code": code}


# Agent 3: Testing Engineer
def testing_node(state: DeveloperState):

    tests = create_tests(
        state["requirement"],
        state["code"]
    )

    return {"tests": tests}


# Agent 4: Code Reviewer
def reviewer_node(state: DeveloperState):

    review = review_code(
        state["requirement"],
        state["code"],
        state["tests"]
    )

    return {"review": review}


# Final Development Report
def report_node(state: DeveloperState):

    report = f"""
    SOFTWARE DEVELOPMENT REPORT

    PROJECT REQUIREMENT:
    {state['requirement']}

    IMPLEMENTATION PLAN:
    {state['plan']}

    GENERATED PYTHON CODE:
    {state['code']}

    GENERATED TEST CASES:
    {state['tests']}

    CODE REVIEW:
    {state['review']}

    TEST EXECUTION STATUS:
    Test cases generated but not executed automatically.

    DEVELOPMENT STATUS:
    AI development workflow completed.
    """

    return {"report": report}


# Build LangGraph
builder = StateGraph(DeveloperState)

builder.add_node("requirement_analyst", requirement_node)
builder.add_node("code_generator", code_node)
builder.add_node("testing_agent", testing_node)
builder.add_node("code_reviewer", reviewer_node)
builder.add_node("report_generator", report_node)

# Connect agents
builder.set_entry_point("requirement_analyst")

builder.add_edge("requirement_analyst", "code_generator")
builder.add_edge("code_generator", "testing_agent")
builder.add_edge("testing_agent", "code_reviewer")
builder.add_edge("code_reviewer", "report_generator")
builder.add_edge("report_generator", END)

# Compile workflow
developer_graph = builder.compile()


def run_development(requirement):

    initial_state = {
        "requirement": requirement,
        "plan": "",
        "code": "",
        "tests": "",
        "review": "",
        "report": ""
    }

    result = developer_graph.invoke(initial_state)

    return result