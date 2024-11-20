Nmk = input()
N_input = int(Nmk.split()[0])
m_input = int(Nmk.split()[1])
k_input = int(Nmk.split()[2])


def seconds_for_copy(N, m, k):
    copies = 1
    seconds_passed = 0
    copies_long = max(m,k) // min(m,k) #столько копий сделает быстрый принтер, пока работает долгий
    if copies_long >= (N - 1):
        seconds_passed += (N - 1) * min(m, k)  # быстрее напечатать на быстром, чем ждать долгого
    else:
        while copies != N:
            seconds_passed += 1
            if seconds_passed % min(m,k) == 0:
                copies += 1
            if seconds_passed % max(m,k) == 0:
                copies += 1
    return (seconds_passed + min(m,k))


print(seconds_for_copy(N_input, m_input, k_input))