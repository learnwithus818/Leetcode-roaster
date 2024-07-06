# pip install crewai
from crewai import Agent, Task, Crew, Process
import os

os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] ='llama3-70b-8192'
os.environ["OPENAI_API_KEY"] ='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'

responder = Agent(
    role = "Programmer roaster",
    goal = "you have to roast the user in the worst possible way using the leetcode stats provided to you",
    backstory = "You are an roaster made by Anurag Upadhyay whose only job is to roast the coders and programmers in the worst possible way using the leetcode statistics provided to you. Roast in a very brutal way that affects the mental health of the user. Donot praise the user even if his stats are good just roast him.",
    # verbose = True,
    allow_delegation = False,
)
def analyse_query_user(query):
    analyse_query = Task(
        description = f"Analyse the stats {query} given by the user and provide the output for the same.",
        agent = responder,
        expected_output = "Roast the user in the worst possible way so that it affects his/her at a very emotional and mental level. You are required to provide the roast in maximum of 250 words. Donot praise the user even if his stats are good just roast him. Roast in a very brutal way that affects the mental health of the user."
    )
    return analyse_query


print("Press enter to search or type exit to quit the assistant")

def results(query):
    if query == "exit" or len(query) == 0:
        return "thanks for chatting with me."
    
    crew = Crew(
        agents = [responder],
        tasks = [analyse_query_user(query)],
        process = Process.sequential
    )

    output = crew.kickoff()
    # print(output)
    return output














# Getting the leetcode user stats
import requests

def leetcode(user_id):
    url = 'https://leetcode.com/graphql'
    headers = {
        'Content-Type': 'application/json',
        'Referer': 'https://leetcode.com'
    }
    query = """
    query userProblemsSolved($username: String!) {
        allQuestionsCount {
            difficulty
            count
        }
        matchedUser(username: $username) {
            problemsSolvedBeatsStats {
                difficulty
                percentage
            }
            submitStatsGlobal {
                acSubmissionNum {
                    difficulty
                    count
                }
            }
        }
    }
    """
    variables = {
        'username': user_id
    }
    body = {
        'query': query,
        'variables': variables
    }
    
    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        data = response.json()

        
        if 'errors' in data:
            return (data)
        else:
            return data['data']
            # return (data)

    except requests.exceptions.RequestException as err:
        print('Error:', err)
        return ({'error': str(err)})
    
    