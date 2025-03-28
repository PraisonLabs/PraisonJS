"""Streaming response handler for real-time agent output."""

from typing import AsyncGenerator

async def stream_response(agent, prompt: str) -> AsyncGenerator[str, None]:
    async for chunk in agent.run_stream(prompt):
        yield chunk
