"""Callback system for monitoring agent execution."""

from typing import Callable, Dict, List

class CallbackManager:
    def __init__(self):
        self._callbacks: Dict[str, List[Callable]] = {}
    
    def on(self, event: str, callback: Callable):
        self._callbacks.setdefault(event, []).append(callback)
    
    def emit(self, event: str, data=None):
        for cb in self._callbacks.get(event, []):
            cb(data)
