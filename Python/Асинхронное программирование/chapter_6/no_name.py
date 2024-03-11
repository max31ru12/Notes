from multiprocessing import Value, Process, Array


def increment_value(shared_int: Value):
    shared_int.value = shared_int.value + 1


def increment_array(shared_array: Array):
    for index, integer in enumerate(shared_array):
        shared_array[index] = integer + 1


if __name__ == "__main__":
    integer = Value('i', 0)
    integer_array = Array('i', [0, 0])

    # Это пример, когда образуется состяоние гонки
    # первый процесс сначала читает переменную, затем увеличивает
    # в это время второй процесс может считать то значение, которое было до того, как
    # первый процесс его увеличил
    procs = [Process(target=increment_value, args=(integer,)),
             Process(target=increment_array, args=(integer_array, )),
             Process(target=increment_value, args=(integer, ))]

    [p.start() for p in procs]
    [p.join() for p in procs]

    print(integer.value)
    print(integer_array[:])
    assert(integer.value == 2)





