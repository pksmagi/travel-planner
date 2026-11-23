# Travel Planner

A CrewAI agent recommends three places to visit in a city.

## Setup

Create and activate a Python virtual environment, then install CrewAI:

```sh
python -m venv venv
source venv/bin/activate
pip install crewai
```

On Windows PowerShell, activate it with `venv\Scripts\Activate.ps1` instead.

Set your OpenAI API key and, optionally, the model name in your shell:

```sh
export OPENAI_API_KEY="your-key"
export MODEL="openai/gpt-4o-mini"
```

In PowerShell, use `$env:OPENAI_API_KEY="your-key"` and
`$env:MODEL="openai/gpt-4o-mini"`. `MODEL` defaults to
`openai/gpt-4o-mini`; select another model your key can access if needed.
Never commit your API key.

## Run

```sh
python travel_planner.py
```

Enter a city at the prompt. The agent will return three numbered suggestions.
