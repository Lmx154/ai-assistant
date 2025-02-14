from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from services.memories_service import memories_service

router = APIRouter(prefix="/memories", tags=["memories"])

class Memory(BaseModel):
    text: str

@router.get("/", response_model=List[str])
async def get_memories():
    return memories_service.get_memories()

@router.post("/")
async def add_memory(memory: Memory):
    memories_service.add_memory(memory.text)
    return {"status": "success"}

@router.delete("/{memory}")
async def remove_memory(memory: str):
    memories_service.remove_memory(memory)
    return {"status": "success"}

@router.delete("/")
async def clear_memories():
    memories_service.clear_memories()
    return {"status": "success"}
