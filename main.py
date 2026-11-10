
from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from workflow.graph import run_development

app = FastAPI(
    title="Multi-Agent Software Developer",
    description="AI-powered software development team",
    version="1.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


class DevelopmentRequest(BaseModel):
    requirement: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/api/develop")
async def develop_software(data: DevelopmentRequest):

    requirement = data.requirement.strip()

    if not requirement:
        raise HTTPException(
            status_code=400,
            detail="Please enter a software requirement."
        )

    if len(requirement) > 10000:
        raise HTTPException(
            status_code=400,
            detail="Requirement is too long. Maximum 10000 characters."
        )

    try:
        result = run_development(requirement)

        return {
            "success": True,
            "plan": result["plan"],
            "code": result["code"],
            "tests": result["tests"],
            "review": result["review"],
            "report": result["report"]
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Development workflow failed: {str(e)}"
        )


@app.get("/api/health")
async def health():

    return {
        "status": "running",
        "application": "Multi-Agent Software Developer"
    }
