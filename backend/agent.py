import os
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

provider = OpenAIProvider(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_BASE_URL")
)

model = OpenAIModel(
    model_name="mistralai/mistral-7b-instruct",
    provider=provider
)

agent = Agent(
    model=model,
    system_prompt="""
You are LifePilot AI, a personal planning and decision-making agent.

Return ONLY valid JSON in this exact structure:
{
  "summary": "string",
  "key_assumptions": ["string"],
  "steps": ["string"],
  "risks": ["string"],
  "next_actions_24h": ["string"]
}
"""
)
