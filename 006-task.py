#Завдання.На кожну сходинку можна стати з попередньої або переступивши через одну. Визначте, скількома способами можна піднятися на задану сходинку.#
def count_ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return count_ways(n - 1) + count_ways(n - 2)

result_for_4 = count_ways(4)
print(result_for_4)
