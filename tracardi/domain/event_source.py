from datetime import datetime
from typing import Optional, Union, List, Any
from tracardi.domain.value_object.storage_info import StorageInfo
from tracardi.domain.entity import Entity


class EventSource(Entity):
    type: str
    timestamp: datetime
    name: Optional[str] = "No name provided"
    description: Optional[str] = "No description provided"
    enabled: Optional[bool] = True
    transitional: Optional[bool] = False
    tags: Union[List[str], str] = ["general"]
    groups: Union[List[str], str] = []
    returns_profile: Optional[bool] = False
    permanent_profile_id: Optional[bool] = False
    requires_consent: Optional[bool] = False
    manual: Optional[str] = None
    locked: bool = False

    def __init__(self, **data: Any):
        data['timestamp'] = datetime.utcnow()
        super().__init__(**data)

    # Persistence

    @staticmethod
    def storage_info() -> StorageInfo:
        return StorageInfo(
            'event-source',
            EventSource
        )
