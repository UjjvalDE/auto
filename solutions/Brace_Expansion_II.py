def expand括号(s):
    def backtrack(i, j, path):
        if i > j:
            res.append(path)
        for k in range(i, j + 1):
            if s[k] == '{':
                j = s.find('}', k)
                if j != -1:
                    backtrack(i, j, path + s[i:k+1] + "{*}" + s[k+1:j])
            elif s[k] == '}':
                continue
            elif s[k] == ',':
                j = s.find('{', k)
                if j != -1:
                    backtrack(i, j-1, path + s[i:k] + "{*}")
            else:
                backtrack(i, j, path + s[i:k+1])

    res = []
    backtrack(0, len(s) - 1, "")
    return [x.replace("{*}", "**") for x in res]