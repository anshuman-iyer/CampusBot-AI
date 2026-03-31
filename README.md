# CampusBot: AI Powered College Enquiry System

## Project Overview
CampusBot is a Python based intelligent chatbot that answers common college queries. It uses fuzzy logic with difflib SequenceMatcher to understand natural language input, including spelling mistakes. The system runs in a command line interface and responds instantly.

## Features
Fuzzy logic intent detection

Typo tolerance using similarity scoring

Natural language input support

Help command

Greeting and normal conversation support

Context memory for follow up questions

Confidence score display

JSON based knowledge base

Chat logging to file

Suggestion system for unknown queries

Contact and timing information

Time based greeting

Analytics tracking of queries

## Technology Stack
Language: Python 3

Libraries: difflib, json, datetime, random, re

Interface: Command Line Interface

## Project Structure
chatbot.py, main chatbot logic
knowledge.json, responses database
chat_history.txt, conversation logs
README.md, project documentation

## How to Run

Install Python 3.8 or above

Download or clone the repository

Ensure chatbot.py and knowledge.json are in the same folder

Open terminal in project directory

Run command

python chatbot.py

## Sample Conversation

You: hi

Bot: Hello. How can I help you?

You: what do you do

Bot: I can help with Fees, Hostel, Library, Exam, Placement, Admission

You: tell me about fee

Bot: The fee is ₹100000 per semester. confidence 0.82

You: hostel available

Bot: Hostels are available. confidence 0.79

You: how much

Bot: Accommodation is provided in campus hostel.

## AI Concepts Used

Fuzzy logic based matching

Similarity scoring using SequenceMatcher

Keyword based intent classification

Context aware response handling

Natural language processing basics
