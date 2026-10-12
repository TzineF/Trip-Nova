# TripNova

TripNova is an AI travel planner. You describe a trip in plain language. The app searches flights, looks up hotels, then writes a practical itinerary you can copy or download as a PDF.

The web UI is a FastAPI app. Planning is a LangGraph pipeline. Conversation state is stored in Postgres.

## Features

- Flight search via Aviationstack
- Hotel search via Tavily
- Itinerary and final plan written with Gemini
- Threaded conversations (reuse a `thread_id`)
- Copy plan or download PDF from the browser

## How it works

Four agents run in order:

1. **Flight agent** — finds flights from the user request
2. **Hotel agent** — searches hotels for the destination
3. **Itinerary agent** — builds a day-by-day plan
4. **Final agent** — formats the response (summary, flights, hotels, itinerary, budget, recommendations)

## Setup

Python 3.13+ is required.

```bash
python -m venv .venv
```

Activate the virtual environment, then:

```bash
pip install -r requirements.txt
```

Or with uv:

```bash
uv sync
```

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=
DATABASE_URL="postgresql://USER:PASSWORD@HOST/DBNAME?sslmode=require"
AVIATIONSTACK_API_KEY=
TAVILY_API_KEY=
DEFAULT_ORIGIN_IATA=DAC
```

Optional LangSmith tracing:

```env
LANGCHAIN_TRACING=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=
LANGCHAIN_PROJECT=Travel-Nova
```

`DATABASE_URL` must be reachable from your machine. If you use Render Postgres, use the **external** URL, keep `sslmode=require`, and allow your IP if an access list is enabled.

Do not commit `.env`.

## Run

Web app:

```bash
python app.py
```

Open http://127.0.0.1:8000

Health check: http://127.0.0.1:8000/health

Command line:

```bash
python test.py
```

## API

`POST /api/travel`

```json
{
  "message": "Plan a 4 day trip to Japan from Bangladesh",
  "thread_id": "optional-thread-id"
}
```

Reuse `thread_id` to continue the same conversation. The UI stores it in `localStorage`.

## Project layout

```
app.py              FastAPI server
backend.py         LangGraph agents and Postgres checkpointer
test.py             Command-line runner
Tools/flight.py     Flight search
Tools/hotel.py      Hotel search
templates/          HTML
Static/             CSS and JavaScript
```

## Notes

- Live flight APIs often omit ticket prices. The planner should say so when prices are missing.
- Default origin airport is `DEFAULT_ORIGIN_IATA` (DAC unless you change it).
- Ctrl+Enter sends the request from the textarea.
