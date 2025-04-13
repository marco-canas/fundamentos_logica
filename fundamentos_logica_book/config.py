import asyncio
import sys
import os
os.environ["JUPYTER_PLATFORM_DIRS"] = "1"

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())