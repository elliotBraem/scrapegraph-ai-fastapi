from fastapi import APIRouter, Body
from typing import Optional
from app.modules import ScrapeGraphAiEngine
from pydantic import BaseModel

router = APIRouter(
    prefix="/crawl"
)

class CrawlRequest(BaseModel):
    prompt: str
    url: str
    provider: str
    llm_model: str
    temperature: Optional[float] = 0.0

@router.post("/scraper_graph")
async def scraper_graph(request: CrawlRequest):
    engine = ScrapeGraphAiEngine(
        model_provider=request.provider,
        model_name=request.llm_model,
        temperature=request.temperature
    )
    return await engine.crawl(prompt=request.prompt, source=request.url)

@router.post("/search_graph")
async def search_graph(
    prompt: str = Body(embed=True),
    provider: str = Body(embed=True),
    llm_model: str = Body(embed=True),
    temperature: float = Body(default=0.0, embed=False)
):
    engine = ScrapeGraphAiEngine(
        model_provider=provider,
        model_name=llm_model,
        temperature=temperature
    )
    return await engine.search(prompt=prompt)
