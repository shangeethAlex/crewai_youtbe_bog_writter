from crewai import Crew,Process
from agent import blog_resercher,blog_writer
from task import research_task,write_task

crew = Crew(
    agents=[blog_writer,blog_resercher],
    tasks=[research_task,write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

### start the task execution process 
result = crew.kickoff(inputs={'topic':'AI vs ML vs DL vs Datascience'})
print(result)
