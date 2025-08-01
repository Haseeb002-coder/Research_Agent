from src.type_state import AgentState

def report_compiler(state:AgentState):
  completed_sections = state["completed_sections"]
  outline = state["outline"]
  input = state["input"]
  report_conetnt = "\n\n---\n\n".join(completed_sections)
  report = f' # {input} \n\n---\n\n {outline}  \n\n---\n\n {report_conetnt} '
  print("report_compiler")
  return {
      "report": report
  }