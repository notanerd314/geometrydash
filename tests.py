import gd
from gd.objects import *
import asyncio
from loguru import logger
from json import dumps

@logger.catch
async def main():
    geometrydash = gd.GeometryDash()
    
    # response = await geometrydash.get_daily_level(weekly=True, get_time_left=True)
    
    # level = response[0]
    # time_left = response[1]

    # print(time_left)
    # print(level.NAME)
    # print(level.DIFFICULTY)
    # print(level.STARS)
    # print(level.RATING)
    # print(level.DAILY_ID)

    response = await geometrydash.get_user_comments_history(3935672, display_most_liked=True)
    for comment in response:
        print()
        print(comment.__dict__)

asyncio.run(main())