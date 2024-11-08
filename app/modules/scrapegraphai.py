from scrapegraphai.graphs import SmartScraperMultiGraph, SearchGraph
import os
from typing import Optional, List
from pydantic import BaseModel
import asyncio
from functools import partial

class ScrapeGraphAiEngine:
    """
    You can find the model_provider by langchain website:
    https://api.python.langchain.com/en/latest/chat_models/langchain.chat_models.base.init_chat_model.html
    """
    def __init__(
            self,
            model_provider: str,
            model_name: str,
            temperature: float = 0
    ):
        self.model_provider = model_provider
        self.model_name = model_name
        self.temperature = temperature
        self.model_tokens = 128000
        self.graph_config = self.create_model_instance_config()
        self._lock = asyncio.Lock()

    async def crawl(
            self,
            prompt: str,
            sources: List[str],
            schema: Optional[BaseModel] = None
    ):
        # Create graph instance with proper configuration
        smart_scraper_graph = SmartScraperMultiGraph(
            prompt=prompt,
            source=sources,
            config=self.graph_config,
            schema=schema
        )

        # Run the graph in the default event loop
        async with self._lock:  # Ensure thread-safe access to shared resources
            loop = asyncio.get_running_loop()
            # Use partial to create a callable that doesn't require arguments
            func = partial(smart_scraper_graph.run)
            # Run the blocking operation in the default loop
            result = await loop.run_in_executor(None, func)
            
        return result

    async def search(
            self,
            prompt: str,
    ):
        # Create search graph instance
        search_graph = SearchGraph(
            prompt=prompt,
            config=self.graph_config
        )

        # Run the search in the default event loop
        async with self._lock:  # Ensure thread-safe access to shared resources
            loop = asyncio.get_running_loop()
            # Use partial to create a callable that doesn't require arguments
            func = partial(search_graph.run)
            # Run the blocking operation in the default loop
            result = await loop.run_in_executor(None, func)
            
        return result

    def create_model_instance_config(
            self
    ):
        graph_config = {
            "llm": {},
            "verbose": True,
        }

        # Include provider in the model string
        model_string = f"{self.model_provider}/{self.model_name}"

        if self.model_provider == "google_genai":
            graph_config["llm"] = {
                "model": model_string,
                "api_key": os.environ["GOOGLE_API_KEY"],
                "temperature": self.temperature
            }
            if os.getenv("GOOGLE_API_ENDPOINT"):
                graph_config["llm"]["transport"] = "rest"
                graph_config["llm"]["client_options"] = {"api_endpoint": os.environ['GOOGLE_API_ENDPOINT']}

        else:
            graph_config["llm"] = {
                "model": model_string,
                "api_key": os.getenv("API_KEY"),
                "temperature": self.temperature
            }
            if os.getenv("API_BASE_URL"):
                graph_config["llm"]["base_url"] = os.getenv("API_BASE_URL")

        return graph_config
