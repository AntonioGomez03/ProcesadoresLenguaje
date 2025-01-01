""" Module for API routes"""

from fastapi import APIRouter

router = APIRouter()


@router.post("/generate_project")
def generate_project(code: str):
    """Generates a project with the given code"""
    return {"message": "Project generated successfully!"}
