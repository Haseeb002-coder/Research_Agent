from langgraph.prebuilt import create_react_agent
from src.type_state import WriterState,AgentState
from src.model import model,tools
from langgraph.types import Send


def writer(state: WriterState):
    section = state["section"]
    system = """
      # PERSONA
      You are an expert report section writer.
      Your job is to look at the provided sections and subsections and write the content for the section.

      # INSTRUCTIONS
      - Use Markdown
      - Use the provided tools to gather accurate information.
      - Use only reliable and relevant sources.
      - Cite every important fact using a source link inline (Markdown format preferred, e.g., [source](https://example.com)).
      - At the end of the section, include a "Sources" list with full URLs of all the references used.
      - Do not include unrelated or unnecessary information.
      - Your response should only contain the written section followed by the list of sources.


    """

    # model2 = model.with_structured_output(Outline)
    agent = create_react_agent(
    model= model,
    tools = tools,
    prompt = system
    )

    content= agent.invoke({
      "messages": [{"role": "user", "content": str(section)}]
  })
    

    return {
        "completed_sections": [content["messages"][-1].content]
    }


def assign_workers(state: AgentState):
  sections = state["report_plan"]

  return [ Send( "writer", { "section": s } ) for s in sections ]