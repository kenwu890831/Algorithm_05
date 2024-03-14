#演算法分析機側
#學號 : 10724128
#姓名 : 吳宇哲
#中原大學資訊工程系
from collections import deque
import time
def pushing_box_game(graph):
    x_num = len(graph[0])
    y_num = len(graph)
    box_x = 0
    box_y = 0
    person_x = 0
    person_y = 0 
    target_x = 0
    target_y = 0 
    box_count = 0 
    person_count = 0
    target_count = 0
    for i in range(x_num) :
       for j in range(y_num) :
          if graph[j][i] == 'S' :
             person_x = i
             person_y = j
             person_count =  person_count +1
          elif graph[j][i] == 'B' :
             box_x = i
             box_y = j
             box_count = box_count +1
          elif graph[j][i] == 'T' :
             target_x = i
             target_y = j
             target_count = target_count +1
    if target_count != 1 or box_count != 1 or person_count != 1 :
       print ( "error graph ")
       return False
    visited = []
    visited.append([person_x,person_y,box_x,box_y] )
    queue = deque()
    path = []
    queue.appendleft([person_x,person_y,box_x,box_y,path]) # pop
    while queue :
       now = []
       now = queue.pop() #NEXT STEP
       run_dir = [[0,1],[0,-1],[1,0],[-1,0]] # r l u d
       if ( now[2] == target_x and now[3] == target_y) : # ON TARGET
          print(now[4])
          return True
       for i in range(4) :
          next_person_x = now[0] + run_dir[i][0]
          next_person_y = now[1] + run_dir[i][1]
          next_box_x = now[2]
          next_box_y = now[3]
          box_moved = False
          if ( next_person_x == now[2] and next_person_y == now[3]) : # BOX MOVED
             box_moved = True
             next_box_x = next_box_x + run_dir[i][0]
             next_box_y = next_box_y + run_dir[i][1]
          if ( next_person_x < 0 or next_person_x >= x_num or next_person_y < 0 or next_person_y >= y_num or next_box_x < 0 or next_box_x >= x_num or next_box_y < 0 or next_box_y >= y_num or graph[next_person_y][next_person_x] == '#' or graph[next_box_y][next_box_x] == '#') : # out of range
             continue # ERROR
          if check_visited( visited , next_person_x,next_person_y,next_box_x,next_box_y) == False:
             path_temp = []
             path_temp = now[4][:]
             if i == 1 and box_moved ==  True:
                path_temp.append('N')
             elif i == 2 and box_moved ==  True :
                path_temp.append('E')
             elif i == 3 and box_moved ==  True :
                path_temp.append('W')
             elif i == 0 and box_moved ==  True :
                path_temp.append('S')
             elif i == 1 :
                path_temp.append('n')
             elif i == 2  :
                path_temp.append('e')
             elif i == 3  :
                path_temp.append('w')
             elif i == 0  :
                path_temp.append('s')
             visited.append([next_person_x,next_person_y,next_box_x,next_box_y])
             queue.appendleft([next_person_x,next_person_y,next_box_x,next_box_y,path_temp])
    print( "not have result")


       
def check_visited( visited , next_person_x,next_person_y,next_box_x,next_box_y) :
   for i in range(len(visited)) :
      if ( next_person_x == visited[i][0] and next_person_y == visited[i][1] and next_box_x == visited[i][2] and next_box_y == visited[i][3]) :
         return True
   return False

             




   
print("推箱子遊戲(Pushing Box  Game)")
y_axis, x_axis = map( int , input("請輸入x,y大小 : ").split())
graph = []
count = 1 
while (x_axis != 0) | ( y_axis != 0) :
 start_time = time.time()
 print("Maze #", count)
 for i in range(y_axis) :
    input_temp = []
    input_temp = input()
    char_temp = []
    if len(input_temp) != x_axis :
       print("error")
       break 
    else :
       for i in range(x_axis) :
          char_temp.append(input_temp[i])
    graph.append(char_temp)
 pushing_box_game(graph)
 total_time = time.time() - start_time
 print ( "run time : ",total_time )
 count = count +1
 y_axis, x_axis = map( int , input("請輸入x,y大小 : ").split())
 del graph
 graph = []
"""
1 8
T...B..S
1 7
SB..#.T
8 10
##########
#S.......#
#......B.#
#........#
#........#
#........#
#.......T#
##########
8 10
##########
#S.......#
#......B.#
#........#
#...B....#
#........#
#.......T#
##########
8 10
##########
#S.......#
#......B.#
#........#
#..S.....#
#........#
#.......T#
##########
8 10
##########
#S.......#
#......B.#
#........#
#........#
#....T...#
#.......T#
##########
8 10
##########
#.......S#
#........#
#...B....#
#........#
#........#
#T.......#
##########
7 11
###########
#T##......#
#.#.#..####
#....B....#
#.######..#
#.....S...#
###########
0 0

"""
