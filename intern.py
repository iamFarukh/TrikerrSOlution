def solv(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.values()

    
keys = ["idea", "idae", "bsnl", "nsbl", "grasim", "bata"]
solv(keys)
