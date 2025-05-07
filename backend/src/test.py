from src.resumes.orm import ResumeORM
import asyncio


async def main():
    print(await ResumeORM.get_resumes_for_filter(words_list=["python", "fastapi"]))


asyncio.run(main())