from crewai import Agent
from tools import yt_tool


from dotenv import load_dotenv
load_dotenv()


import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] ="gpt-4-0125-preview"



## create senior blog content resercher

blog_resercher = Agent(
    role='Blog resercher from youtube videos',
    goal = 'get the relevant video content for the topic{topic} from youtube channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in ai data science ,machine learning and Gen Ai and providing suggestion"
    ),
    tools=[yt_tool],
    allow_delegation=True
)

### create a senior blog writter agent  with youtube tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False


)