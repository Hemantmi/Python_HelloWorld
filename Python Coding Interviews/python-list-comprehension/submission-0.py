from typing import List

odds_list=[]
def create_list_of_odds(n: int) -> List[int]:
    for i in range(n+1):
        if i % 2 != 0 and i not in odds_list:
            odds_list.append(i)
    return odds_list
    



# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))
