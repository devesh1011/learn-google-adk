from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from .utils import load_instruction_from_file

scriptwriter_agent = LlmAgent(
    name="ShortsScriptWriter",
    model="gemini-2.5-pro-03-25",
    tools=[google_search],
    output_key="generated_script",
    instruction=load_instruction_from_file("youtube_shorts_assistant/scriptwriter_instruction.txt"),
)

visualizer_agent = LlmAgent(
    name="ShortsVisualizer",
    model="gemini-2.5-pro-03-25",
    description="Generates visual concepts based on a provided script.",
    output_key="visual_concepts",
    instruction=load_instruction_from_file("youtube_shorts_assistant/visualizer_agent_instruction.txt"),
)

formatter_agent = LlmAgent(
    name="ConceptFormatter",
    model="gemini-2.5-pro-03-25",
    instruction="""Combine the script from state["generated_script"] and the visual concepts from state["visual_concepts"] into the final markdown format""",
    description="Formats the final Short concept",
    output_key="final_short_concept",
)

youtube_shorts_agent = LlmAgent(
    name="youtube_shorts_agent",
    model="gemini-2.5-pro-03-25",
    description="You are shortform genius, an AI specialized in crafting engaging Youtube Shorts content. Your expertise lies in generating c",
    instruction=load_instruction_from_file("youtube_shorts_assistant/shorts_agent_instruction.txt"),
    sub_agents=[scriptwriter_agent, visualizer_agent, formatter_agent],
)

root_agent = youtube_shorts_agent
