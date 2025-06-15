"""Prompt template management."""

AGENT_SYSTEM_PROMPT = '''You are {role}. Your goal is: {goal}.
You have access to the following tools: {tools}.
Think step by step before acting.'''

REFLECTION_PROMPT = '''Review your previous output:
{output}

Was this satisfactory for the task: {task}?
If not, improve it.'''
