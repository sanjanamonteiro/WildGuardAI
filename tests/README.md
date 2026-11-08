# Testing Guide

This folder contains automated tests for the WildGuard AI backend.

## Test File

- `test_api.py` – Tests the FastAPI backend endpoints.

## Prerequisites

Make sure the backend dependencies are installed in the project's virtual environment.

## Run Tests

Open a terminal in the project root directory and run:

```powershell
.\backend\venv\Scripts\python.exe -m pytest tests\test_api.py -v
```

## Expected Result

All five API endpoint tests should pass.

The tests cover:

- Root endpoint
- Health check endpoint
- Risk map endpoint
- Wildlife summary endpoint
- Weather summary endpoint

## Notes

- Run the tests from the project root directory.
- Ensure the required processed datasets are available.
- Warnings may appear due to dependency deprecations; check that there are no test failures.
