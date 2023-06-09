#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    neas = dir(hidden_4)
    for t in range(len(neas)):
        for u in range(len(neas[t])):
            if(neas[t][u] == '_' and neas[t][u+1] == '_'):
                break
            else:
                print(neas[t])
                break
