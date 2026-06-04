# ask_test.py
from ai import ask_about_todos

questions = [
    "What should I do tomorrow?",
    "Any health related tasks?",
    "What food tasks do I have?",
]

for question in questions:
    print(f"Q: {question}")
    print(f"A: {ask_about_todos(question)}")
    print()