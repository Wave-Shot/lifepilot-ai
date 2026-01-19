from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

model = OpenAIModel(
    model_name="mistralai/mistral-7b-instruct"
)

agent = Agent(
    model=model,
    system_prompt="""
You are LifePilot AI, a personal planning and decision-making agent.

You MUST respond in valid JSON with this exact structure:

{
  "summary": "...",
  "key_assumptions": ["..."],
  "steps": ["..."],
  "risks": ["..."],
  "next_actions_24h": ["..."]
}

Return ONLY JSON. No markdown. No explanation.
"""
)
