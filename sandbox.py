def towers(n, m): 
    if n % 2 == 0 or m == 1: 
        return 2 
    else:
        return 1 

def grid_order(grid): 
    n_rows = len(grid)
    n_cols = len(grid[0]) 
    result = "YES"

    sorted_grid = []
    for row in grid: 
        sorted_grid.append(sorted(list(row)))

    # print(sorted_grid)
    for i in range(1, n_rows):
        for j in range(n_cols):
            if sorted_grid[i][j] < sorted_grid[i-1][j]: 
                result = "NO" 

    return result

def caeser_cipher(s, k): 
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    rotated = [alphabet[(i+k) % 26] for i in range(26)]
    ss = [rotated[alphabet.index(ch.lower())] if ch.isalpha() else ch for ch in s]

    for ch in s: 
        if ch.isupper(): 
            idx = s.index(ch)
            ss[idx] = ss[idx].upper()

    return "".join(ss)
    
def bribes(q): 
    n = len(q) 
    correct = [i + 1 for i in range(n)]
    q = list(q)
    bribes = 0
    diffs = [abs(q[j] - correct[j]) for j in range(n)]
    print(diffs)

    for i in range(n): 
        if q[i] > correct[i]: 
            bribes += (q[i] - correct[i])

    if max(diffs) > 5:
        print("Too chaotic")
    else:
        print(bribes)

def balanced(s): 
    o = list("({[")
    c = list(")}]")
    result = "YES"
    stack = []
    for p in list(s): 
        # print(stack, "incoming -> ", p)
        if p in o: 
            stack.append(p)
        else:
            if not stack:
                result = "NO"
            else:
                idx = c.index(p)
                if stack[-1] != o[idx]: 
                    result = "NO"
                else:
                    stack.pop()

    if stack: 
        result = "NO"

    return result

def text_editor(): 
    Q = int(input())
    S = ""
    log_adds_dels = []
    for i in range(Q): 
        print(f"S = {S} | log = {log_adds_dels}")
        opcode = input()
        if opcode != "4":
            op, arg = opcode.split()
            if op == "1": 
                S = S + arg
                log_adds_dels.append(["1", arg])
            elif op == "2":
                removed = S[-int(arg):]
                log_adds_dels.append(("2", removed))
                S = S[:-int(arg)]
            elif op == "3":
                print(S[int(arg)-1])
        elif opcode == "4":
            prev_op = log_adds_dels[-1]
            print(prev_op)
            if prev_op[0] == "2": 
                S = S + prev_op[1]
            elif prev_op[0] == "1": 
                S = S.replace(prev_op[1], "")
            log_adds_dels.pop() 
        else:
            print("Invalid operation") 

def time_conversion(s): 
    suffix = s[-2:]
    hr, mins, sec = s[:2], s[3:5], s[6:-2]
    if suffix == "AM":
        if hr == "12":
            return f"00:{mins}:{sec}" 
        else:
            return f"{hr}:{mins}:{sec}"
    else:
        if hr == "12":
            return f"{hr}:{mins}:{sec}" 
        else:
            return f"{int(hr) + 12}:{mins}:{sec}"

def lonely(a): 
    d = {}
    for x in a: 
        if x not in d:
            d[x] = 1 
        else:
            d[x] += 1 
    
    for k, v in d.items():
        if v == 1:
            return k 
        
    return -1 

def diag_diff(n, M): 
    a, b = 0, 0 
    for i in range(n): 
        a += M[i][i]
        b += M[n-1-i][i]
    return abs(a - b)


def main(): 
    # print(towers(2, 2))
    # print(towers(1, 4))
    # print(grid_order(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']))
    # print(grid_order(['fghij', 'ebacd', 'olmkn', 'trpqs', 'xywuv']))
    # print(caeser_cipher("There's-a-starman-waiting-in-the-sky", 3))
    # print(caeser_cipher("middle-Outz", 2))
    # (bribes([2,1,5,3,4]))
    # (bribes([2,5,1,3,4]))
    # (bribes([1,2,5,3,4]))
    # bribes([1,2,5,3,7,8,6,4])
    # print(balanced("{[()]}"))
    # print(balanced("{[(])}"))
    # print(balanced("{{[[(())]]}}"))
    # print(balanced("{"))
    # text_editor() 
    # print(time_conversion("07:05:45PM"))
    # print(time_conversion("12:18:25PM"))
    # print(time_conversion("12:18:25AM"))
    # print(lonely([1,2,3,4,3,2,1]))
    # print(lonely([1,1,1,3,5,5,5,3]))
    print(diag_diff(3, [[11,2,4], [4,5,6], [10,8,-12]]))
    print(diag_diff(3, [[1,2,3], [4,5,6], [9,8,9]]))


if __name__ == "__main__": 
    main() 