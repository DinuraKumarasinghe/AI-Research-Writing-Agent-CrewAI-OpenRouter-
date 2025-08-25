from crewai import Agent, Task, Crew
import os

# Set your OpenRouter API key
os.environ["OPENROUTER_API_KEY"] = "your_openrouter_api_key_here"

# --- Define Agents ---
researcher = Agent(
    role="AI Researcher",
    goal="Find the most relevant and accurate information for any given topic.",
    backstory="You are a highly skilled research assistant who extracts facts from reliable sources.",
    verbose=True,
    llm="openrouter/meta-llama/llama-3.1-70b-instruct"
)

writer = Agent(
    role="Content Writer",
    goal="Write engaging blog articles based on researched content.",
    backstory="You are a professional content writer who explains complex ideas in simple language.",
    verbose=True,
    llm="openrouter/openai/gpt-4"
)

# --- Define Tasks ---
task1 = Task(
    description="Research the topic: 'How AI agents are changing the future of work.'",
    agent=researcher
)

task2 = Task(
    description="Based on the research, write a 500-word blog post that is clear and engaging.",
    agent=writer
)

# --- Assemble the Crew ---
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2]
)

# --- Run the Crew ---
if __name__ == "__main__":
    result = crew.kickoff()
    print("\n=== Final Blog Post ===\n")
    print(result)
