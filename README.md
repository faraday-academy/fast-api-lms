# Fast API LMS

This repo goes along with the video on our Faraday Academy YouTube channel: https://youtu.be/gQTRsZpR7Gw

You can follow along with the video and check out different branches for each step of the tutorial. More work will be done on this repo in future tutorials to finish building all of the features.

## Table of Contents

1. [Overview & Requirements](#overview-&-requirements)
1. [Running Locally](#running-the-app-locally)
1. [Tech Stack](#tech-stack)
1. [Schema](#schema)

## Overview & Requirements

This is a learning management system where teachers can manage student and students can see their courses.

## Running the App Locally

1. Make sure Python, Poetry, and Postgres are installed. Postgres must be running. *If you need help with this, please follow the instructions in the video linked at the top of this README.*
2. Create a virtual environment: `python -m venv venv`
3. Install packages: `poetry install`
4. Run the development server: `uvicorn main:app --reload`

## Tech Stack

- Fast API
- Python 3.9+
- Poetry
- Postgres
- SQL Alchemy
- Alembic
- Pydantic
- Black
- Flake8
- Pre-commit

## Schema


