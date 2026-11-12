# Stage 1 Plan: Getting Back into Shape (Day 1–15)

Focus: syntax, functions, containers, exceptions, small command-line tools.

This is a plan, not a contract. Swap topics freely; just keep each day small enough to finish
in 60–90 minutes.

## How to pick each day's topic

Before starting a day, ask:

1. **What does this stage need?** Check the roadmap in the root README.
2. **Where did I get stuck yesterday?** Read the "Improvements for Tomorrow" section of the
   previous day's README.
3. **Can I finish something runnable in 60–90 minutes?** If not, cut the scope.

A good daily topic is **one concrete small tool + one or two key concepts**, e.g.
"word frequency counter (dicts, sorting)" rather than "learn dicts".

## Schedule

| Day | Tool | Key concepts |
| --- | ---- | ------------ |
| 001 | hello-cli: greet the user from the command line | `sys.argv` / `input`, f-strings |
| 002 | number-guess: number guessing game | `while`, `random`, type conversion |
| 003 | unit-converter: unit converter | functions, parameters, return values |
| 004 | word-count: word frequency in a text | dicts, `sorted` with `key` |
| 005 | todo-list: in-memory to-do list | list CRUD, menu loop |
| 006 | safe-calculator: calculator | `try` / `except`, input validation |
| 007 | password-generator: password generator | `string`, `random.choice`, list comprehensions |
| 008 | grade-stats: grade statistics | tuples, sets, `min` / `max` / `sum` |
| 009 | argparse-tool: turn an earlier script into a real CLI | `argparse` |
| 010 | **Retrospective** + refactor one earlier script | write `notes/retro-day010.md` |
| 011 | text-search: find keywords in a text file | string methods, `enumerate` |
| 012 | dedupe-lines: remove duplicate lines | sets, preserving order |
| 013 | quiz-game: multiple-choice quiz | nested data (list of dicts) |
| 014 | expense-log: in-memory expense tracker | splitting into functions, exceptions, containers |
| 015 | stage1-mini-project: combine 2–3 tools into one menu-driven CLI | modular thinking, lead-in to stage 2 |

## Commands

Day 001 already exists. For the rest:

```bash
python scripts/new_day.py 2 "number-guess" --topic "Number guessing game"
python scripts/new_day.py 3 "unit-converter" --topic "Unit converter"
python scripts/new_day.py 4 "word-count" --topic "Word frequency counter"
python scripts/new_day.py 5 "todo-list" --topic "In-memory to-do list"
python scripts/new_day.py 6 "safe-calculator" --topic "Calculator with input validation"
python scripts/new_day.py 7 "password-generator" --topic "Password generator"
python scripts/new_day.py 8 "grade-stats" --topic "Grade statistics"
python scripts/new_day.py 9 "argparse-tool" --topic "Rebuild an earlier script with argparse"
python scripts/new_day.py 10 "retro-and-refactor" --topic "Retrospective and refactor"
python scripts/new_day.py 11 "text-search" --topic "Keyword search in text files"
python scripts/new_day.py 12 "dedupe-lines" --topic "Remove duplicate lines"
python scripts/new_day.py 13 "quiz-game" --topic "Multiple-choice quiz"
python scripts/new_day.py 14 "expense-log" --topic "Expense tracker"
python scripts/new_day.py 15 "stage1-mini-project" --topic "Stage 1 menu-driven CLI"
```

## Looking ahead

- **Stage 2:** add tests to earlier tools. Day 004's word counter is a natural first pytest
  exercise.
- **Stage 3:** pick the website to scrape before stage 2 ends. Stage 4 analyzes your own
  scraped data, so choose something you actually care about.
