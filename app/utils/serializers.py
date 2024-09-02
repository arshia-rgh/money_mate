from datetime import datetime

from pydantic import BaseModel


def serialize_item(item):
    if isinstance(item, BaseModel):
        item_dict = item.model_dump()
    else:
        item_dict = item

    for k, v in item_dict.items():
        if isinstance(v, datetime):
            item_dict[k] = v.isoformat()
    return item_dict
