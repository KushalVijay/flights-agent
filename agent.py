from phi.agent import Agent
from dotenv import load_dotenv
from phi.model.groq import Groq
from skyscanner import Skyscanner

load_dotenv()

skyscanner_tool = Skyscanner()
skyscanner_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[skyscanner_tool.get_cheapest_flight],
    instructions=["Use origin and destination codes for the tools like San Francisco code is SFO, Delhi is DEL","Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

def main():

    try:
        while True:
            user_input = input("Chat with AI (q to quit): ").strip()

            if user_input.lower() == 'q':
                break

            skyscanner_agent.print_response(user_input, stream=True)
    except Exception as e:
        print(e)
    
    


if __name__ == '__main__':
    main()