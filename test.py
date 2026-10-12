from Tools.hotel import tavily_search
from Tools.flight import search_flights
from backend import run_travel_agent


user_input= input("Enter travel request: ")


response = run_travel_agent(user_input=user_input,thread_id="test_user")

print("\nFinal Response:\n")
print(response["answer"])


# res= search_flights("Plan a 4 day trip to USA from Bangladesh")
# print(res)


# # res = tavily_search("Best Hotels in Srilanka")

# # print(res)
