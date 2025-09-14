import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

from .tools import StockDataTool

stock_tool = StockDataTool()
serper_tool = SerperDevTool()

@CrewBase
class LatestAiDevelopmentCrew:
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    agents_config_path = os.path.join(BASE_DIR, 'config', 'agents.yaml')
    tasks_config_path = os.path.join(BASE_DIR, 'config', 'tasks.yaml')

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            tools=[serper_tool, stock_tool]
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True
        )
    
    @agent
    def financial_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_analyst'],
            verbose=True,
            tools=[]  # No ProphetForecastTool anymore
        )

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config['research_task'])

    @task
    def financial_task(self) -> Task:
        return Task(config=self.tasks_config['financial_task'])

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            context=[self.research_task(), self.financial_task()]
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            full_output=True,
            step_callback=lambda x: print(f"Step output: {x}")
        )
