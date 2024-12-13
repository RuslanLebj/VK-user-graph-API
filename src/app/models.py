from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class Node(BaseModel):
    id: int
    label: Optional[str] = None
    name: Optional[str] = None
    screen_name: Optional[str] = None
    sex: Optional[int] = None
    home_town: Optional[str] = None


class RelationshipType(str, Enum):
    FOLLOW = "Follow"
    SUBSCRIBE = "Subscribe"


class Relationship(BaseModel):
    id: Optional[int] = None
    type: RelationshipType
    end_node_id: int


class InsertRequest(BaseModel):
    node: Node
    relationships: List[Relationship]
