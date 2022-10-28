# from collections import deque



def path_cost(hub: dict[dict], path:list[str]) -> int:
    cost:int = 0
    for i, leg in enumerate(path):
        cost += hub[leg][path[i+1]] if i+1 < len(path) else 0
    return cost


def find_cheapest_path(hub: dict[dict], start:str, end:str, path:list = [] ) -> list[str]:
    working_path = path.copy()
    working_path.append(start)
    if start == end:
        return working_path
    if start not in hub:
        return None
    cheapest = None
    for leg in hub[start]:
        if leg not in working_path:
            new_path = find_cheapest_path(hub, leg, end, working_path)
            if new_path:
                if not cheapest or path_cost(hub, new_path) < path_cost(hub, cheapest):
                    cheapest = new_path
    return cheapest


def shortest_path(hub: dict[dict], start:str, end:str ) -> tuple[int, list]:
    path:list = find_cheapest_path(hub,start,end)
    return (path_cost(hub,path), path)


hub = { 
          'a': {'b': 2, 'c': 4, 'e': 1},
          'b': {'a': 2, 'd': 3},
          'c': {'a': 4, 'd': 6},
          'd': {'c': 6, 'b': 3, 'e': 2},
          'e': {'a': 1, 'd': 2},
        }

"""
>>> shortest_path(hub, 'a', 'd')
        
Expected result: cost and path:
  (3, ['a', 'e', 'd'])
"""
print(shortest_path(hub, 'a', 'd'))
