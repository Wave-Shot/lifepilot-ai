from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

model = OpenAIModel(
    model_name="mistralai/mistral-7b-instruct"
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
