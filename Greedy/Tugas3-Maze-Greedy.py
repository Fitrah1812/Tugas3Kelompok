import math
from time import time

goal_x=5
goal_y=0

maze=[
    ['#','#','#','#','#','G','#','#'],
    ['#','#','#','#',' ',' ',' ','#'],
    [' ',' ',' ',' ',' ','#',' ',' '],
    [' ','#','#','#','#','#','#',' '],
    [' ','S',' ',' ',' ',' ',' ',' ']
]

maze_width=8
maze_height=5

class Node:
    def __init__(self,x,y,cost,actions):
        self.x=x
        self.y=y
        self.cost=cost
        self.heuristic=self.euclidean_distance()
        self.actions=actions

    def euclidean_distance(self):
        return math.sqrt(math.pow(self.x-goal_x,2)+math.pow(self.y-goal_y,2))


action=['LEFT','RIGHT','UP','DOWN']
ctr_x=[-1,1,0,0]
ctr_y=[0,0,-1,1]


fringe=list()

init_x=1
init_y=4
initial_state=Node(init_x,init_y,0,list())
fringe.append(initial_state)
count_expansion=1

closed = list()

while len(fringe) > 0:
    node_now=fringe.pop(0)

    if(node_now.x == goal_x and node_now.y == goal_y):
        waktu = time()
        print("Ditemukan setelah melakukan ekspansi sebanyak",count_expansion,"node")
        print("dengan",len(node_now.actions), "langkah:",node_now.actions)
        waktu1 = time()-waktu
        print("Waktunya adalah ", waktu1)
        break

    is_closed=False
    for i in closed:
        if i[0]==node_now.x and i[1]==node_now.y:
            is_closed=True
    
    if not is_closed:
        closed.append((node_now.x,node_now.y))
        zero_x=node_now.x
        zero_y=node_now.y
        
        for i in range(len(action)): #coba semua aksi
            new_x=zero_x+ctr_x[i] #calon posisi x yang baru 
            new_y=zero_y+ctr_y[i] #calon posisi y yang baru
            if(new_x >= 0 and new_x < maze_width and new_y >= 0 and new_y < maze_height and maze[new_y][new_x]!='#'): #validasi perpindahan posisi
                successor_in_fringe=False
                for k in fringe:
                    if k.x == new_x and k.y == new_y:
                        successor_in_fringe=True
                        break

                successor_in_closed=False
                for k in closed:
                    if k[0] == new_x and k[1] == new_y:
                        successor_in_fringe=True
                        break

                if not successor_in_fringe and not successor_in_closed:
                    copy_actions=node_now.actions.copy()
                    copy_actions.append(action[i])
                    new_node=Node(new_x,new_y,node_now.cost+1,copy_actions)
                    fringe.append(new_node)
                    fringe.sort(key=lambda x: x.heuristic)
        count_expansion+=1
