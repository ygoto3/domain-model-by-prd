from fastapi import FastAPI, Depends
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from markupsafe import escape
from pydantic import BaseModel

from .config import ALLOWED_ORIGIN
from .prd import Prd
from .domain_model import DomainModel
from .ai import Ai
from .settings import SessionLocal


app = FastAPI()

origins = [ALLOWED_ORIGIN]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class PrdPost(BaseModel):
    title: str
    body: str

@app.get("/ok")
async def healthcheck():
    return Response(content="OK", status_code=200)

@app.get("/v1/prds")
async def get_prds(db = Depends(get_db)):
    prds = db.query(Prd).all()
    return prds

@app.get("/v1/prds/{prd_id}")
async def get_prds(prd_id: int, db = Depends(get_db)):
    result = db.query(Prd, DomainModel).filter(Prd.id == DomainModel.prd_id).first()
    if not result:
        return Response(content="Not Found", status_code=404)
    prd, domain_model = result
    return {
        "id": prd.id,
        "title": prd.title,
        "body": prd.body,
        "mermaid": domain_model.mermaid
    }

@app.post("/v1/prds")
async def post_prd(prd_post: PrdPost, db = Depends(get_db)):
    if not prd_post.title:
        return Response(content="Title is required", status_code=400)
    elif not prd_post.body:
        return Response(content="Body is required", status_code=400)
    
    ai = Ai()
    domain_model = ai.generate_domain_model(prd_post.body)

    valid_string_prefix = '```mermaid\n'

    if not domain_model.startswith(valid_string_prefix + 'classDiagram\n'):
        return Response(content="Failed to convert PRD into mermaid format", status_code=400)

    domain_model = domain_model[len(valid_string_prefix):]
    escaped_body = escape(prd_post.body)
    
    prd = Prd(title = prd_post.title, body = escaped_body)
    db.add(prd)
    db.commit()
    domain_model = DomainModel(prd_id = prd.id, mermaid = domain_model)
    db.add(domain_model)
    db.commit()

    return {
        "id": prd.id,
        "title": prd_post.title,
        "body": escaped_body,
        "mermaid": domain_model.mermaid
    }
