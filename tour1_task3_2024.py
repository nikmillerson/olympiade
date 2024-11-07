n_t = (str(input())).split()
n = int(n_t[0])
t = int(n_t[1])
queue = str(input())

def change_places(some_queue ,n, t):
    new_queue = ''
    was_changed = False
    for z in range(t):
        for i in range(n):
            if (some_queue[i] == 'S' and some_queue[i+1] == 'O') and (was_changed == False):
                new_queue += 'OS'
                was_changed = True
            elif was_changed == False:
                new_queue += some_queue[i]
            else:
                was_changed = False
        final_queue = new_queue
        some_queue = new_queue + ' '
        new_queue = ''
        was_changed = False
    return final_queue

print(change_places(queue,n, t))