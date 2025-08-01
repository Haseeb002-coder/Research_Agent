from typing import TypedDict, List, Annotated ,Optional
from operator import add
from pydantic import BaseModel

class Section(BaseModel):
  title: str
  description: Optional[str]
  sub_sections : Optional[List[str]]

class Sections(BaseModel):
  sections: List[Section]

class Outline(BaseModel):
  outline: str

class AgentState(TypedDict):
  input: str
  report_plan: list[Section]
  outline: str
  completed_sections: Annotated[list, add]
  report: str


class WriterState(TypedDict):
  section: Section
  completed_sections: Annotated[list, add]