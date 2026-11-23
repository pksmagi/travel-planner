import os

from crewai import Agent, Crew, Task


def main():
    city = input("Which city? ").strip()
    if not city:
        raise SystemExit("Please enter a city.")

    planner = Agent(
        role="You are a knowledgeable travel planner.",
        goal="Recommend memorable places that visitors can explore in their chosen city.",
        backstory=(
            "You help first-time visitors make the most of a short trip. "
            "You choose real, distinctive attractions and give concise, practical "
            "descriptions rather than long itineraries."
        ),
        llm=os.getenv("MODEL", "openai/gpt-4o-mini"),
        verbose=True,
    )
    task = Task(
        description=(
            "Recommend exactly 3 distinct places to visit in {city}. "
            "For each place, include a brief reason to visit or a practical tip."
        ),
        expected_output=(
            "Exactly three numbered lines, each in the format "
            "'1. Place name - brief reason or tip'. No introduction or conclusion."
        ),
        agent=planner,
    )
    crew = Crew(agents=[planner], tasks=[task])
    print(crew.kickoff(inputs={"city": city}))


if __name__ == "__main__":
    main()
