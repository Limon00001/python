# Stack & Queue

# ------------------------------------------------  Stack  ----------------------------------------------------
actresses = []

# append or add actresses
actresses.append("Ana De Armas")
actresses.append("Kat Dennings")
actresses.append("Emma Watson")
actresses.append("Gal Gadot")
actresses.append("Alexandra Daddario")
print (actresses)


# remove or pop actresses
actresses.pop()
actresses.pop()
print("Actresses: ",actresses)
print("Actresses: ",actresses[-1])        # This will show the last item.
# actresses.pop()
# actresses.pop()
# actresses.pop()
# if not actresses:
#     print("No one here. Sorry!!")

'''------------------------------------------------------------------------------------------------------------------------
Using pop(), the last element will be removed. Here using pop() first time "Alexandra Daddario" will be removed. And second time using pop(), it removes "Gal Gadot".
-------------------------------------------------------------------------------------------------------------------------'''




# -------------------------------------------------  Queue  -----------------------------------------------------------------
from collections import deque  # For queue

actors = deque(["Leonardo DiCaprio", "Tom Hanks", "Tom Hardy"])
print(actors)

# remove or pop actors
actors.popleft()
print(actors)
print("Actors: ",actors[-1])              # This will show the last item.
actors.popleft()
print(actors)
# actors.popleft()
# if not actors:
#     print("No one here. Sorry!!")

'''------------------------------------------------------------------------------------------------------------------------
Using popleft(), the first element will be removed. Here using popleft() first time "Leonardo DiCaprio" will be removed. And second time using popleft(), it removes "Tom Hanks".
-------------------------------------------------------------------------------------------------------------------------'''
