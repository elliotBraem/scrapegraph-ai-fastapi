<!-- markdownlint-disable MD014 -->
<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD041 -->
<!-- markdownlint-disable MD029 -->

<div align="center">

<h1 style="font-size: 2.5rem; font-weight: bold;">AI-rachnid (Web Scraper)</h1>

  <p>
    <strong><a href="https://fastapi.tiangolo.com/"  target="_blank">FastAPI</a> for efficient, AI-driven web scraping using <a href="https://github.com/ScrapeGraphAI/Scrapegraph-ai" target="_blank">Scrapegraph-ai</a></strong>
  </p>

</div>

<details>
  <summary>Table of Contents</summary>

- [Getting Started](#getting-started)
  - [Environment Setup](#environment-setup)
  - [Running with Docker](#running-with-docker)
  - [Available Models](#available-models)
- [Contributing](#contributing)

</details>

## Getting Started

### Environment Setup

Copy `.env.example` to `.env` and configure your API keys. Due to the special nature of the Gemini model, it is configured separately. Other models are configurable via `API_KEY` and `API_BASE_URL`.

```cmd
GOOGLE_API_KEY=
GOOGLE_API_ENDPOINT=
API_KEY=
API_BASE_URL=
```

### Running with Docker

Ensure you have a [Docker](https://www.docker.com/) instance running. For MacOS, I recommend using [OrbStack](https://orbstack.dev).

Available commands:

- `npm run docker:build` - Build the Docker image
- `npm run docker:dev` - Run the container in development mode
- `npm run dev` - Build and run in one command
- `npm run docker:stop` - Stop running containers
- `npm run docker:clean` - Clean up Docker resources

### Available Models

The API supports multiple model providers and models, using langchain's `init_chat_model`.

- Google Gemini
  - Provider: `google_genai`
  - Model: `google_genai/gemini-1.5-flash-latest` // or other model
  - Requires: `GOOGLE_API_KEY` or `GOOGLE_API_ENDPOINT` in `.env`

- OpenAI
  - Provider: `openai`
  - Model: `gpt-4o-mini` // or other model
  - Requires: `API_KEY` or `API_BASE_URL` in `.env`

- Ollama
  - Provider: `ollama`
  - Model: `ollama/llama3.1` // or other model

You can find more supported models on the langchain website [init_chat_model](https://api.python.langchain.com/en/latest/chat_models/langchain.chat_models.base.init_chat_model.html).

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you're interested in contributing to this project, please read the [contribution guide](./CONTRIBUTING).

<div align="right">
<a href="https://nearbuilders.org" target="_blank">
<img
  src="https://builders.mypinata.cloud/ipfs/QmWt1Nm47rypXFEamgeuadkvZendaUvAkcgJ3vtYf1rBFj"
  alt="Near Builders"
  height="40"
/>
</a>
</div>
