from fastapi import APIRouter, Body
from typing import Optional, List
from app.modules import ScrapeGraphAiEngine
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/crawl"
)
class CrawlRequest(BaseModel):
    prompt: str
    urls: List[str]
    provider: str = Field(default="openai", description="AI model provider")
    llm_model: str = Field(default="gpt-4o-mini", description="Language model to use")
    temperature: Optional[float] = Field(default=0.0, description="Model temperature")
    schema: Optional[BaseModel] = None

@router.post("/scraper_graph")
async def scraper_graph(request: CrawlRequest):
    engine = ScrapeGraphAiEngine(
        model_provider=request.provider,
        model_name=request.llm_model,
        temperature=request.temperature
    )
    return await engine.crawl(
        prompt=request.prompt, 
        sources=request.urls,
        schema=request.schema
    )

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
