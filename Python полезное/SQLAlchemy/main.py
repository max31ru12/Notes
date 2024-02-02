import asyncio
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from queries.orm import SyncOrm, AsyncOrm


SyncOrm.select_workers_with_joined_relationship()
