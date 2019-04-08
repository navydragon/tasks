def SynchronizingTables(N, ids, salary):
    n_ids = sorted (ids)
    n_salary = sorted (salary)
    result = [];
    for i in range(len(ids)):
        ind = n_ids.index(ids[i]);
        result.append(n_salary[ind])
        n_salary[ind] = -1
    return result