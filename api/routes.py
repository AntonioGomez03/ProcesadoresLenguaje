""" Module for API routes"""

from fastapi import APIRouter
from pydantic import BaseModel
from antlr4 import CommonTokenStream, FileStream
import sys,os,uuid
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
print(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from python.src.lexer.gec_lexer import (gec_lexer as Lexer)
from python.src.parser.gec_parserParser import (gec_parserParser as Parser)
from python.src.semantic.gec_visitor import GecVisitor
from code_generator.generate_model import generate_model
from fastapi.responses import FileResponse

router = APIRouter()

class GenerateProjectRequest(BaseModel):
    code: str   

@router.post("/generate_project")
async def generate_project(code_request: GenerateProjectRequest):
    code = code_request.code
    temp_file = f"temp_{uuid.uuid4()}.gec"
    with open(temp_file, "w") as file:
        file.write(code)

    input_stream = FileStream(temp_file, encoding="utf-8")
    lexer = Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Parser(token_stream)
    tree = parser.program()
    visitor = GecVisitor()
    visitor.visit(tree)

    zip_path = generate_model("world.json")
    
    return FileResponse(
        zip_path,
        media_type="application/zip",
        filename="export.zip"
    )
