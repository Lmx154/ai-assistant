from typing import List, Dict
import json
import os

class MemoriesService:
    def __init__(self):
        self.memories_file = "memories.json"
        self.memories = self._load_memories()

    def _load_memories(self) -> List[str]:
        if os.path.exists(self.memories_file):
            with open(self.memories_file, 'r') as f:
                return json.load(f)
        return []

    def _save_memories(self):
        with open(self.memories_file, 'w') as f:
            json.dump(self.memories, f)

    def add_memory(self, memory: str):
        if memory not in self.memories:
            self.memories.append(memory)
            self._save_memories()

    def remove_memory(self, memory: str):
        if memory in self.memories:
            self.memories.remove(memory)
            self._save_memories()

    def get_memories(self) -> List[str]:
        return self.memories

    def clear_memories(self):
        self.memories = []
        self._save_memories()

memories_service = MemoriesService()
