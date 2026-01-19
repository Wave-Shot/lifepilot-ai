from pydantic import BaseModel
from typing import List

class ActionPlan(BaseModel):
    summary: str
    key_assumptions: List[str]
    steps: List[str]
    risks: List[str]
    next_actions_24h: List[str]
