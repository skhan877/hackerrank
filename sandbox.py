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

def counting_sort(a): 
    c = [0] * 100
    for x in a: 
        c[x] += 1 
    return c 

def median(a): 
    n = len(a) 
    mid = n // 2 
    a = sorted(a) 
    print(a) 
    return a[mid]

def palindrome(s):
    if s == s[::-1]:
        return -1
    
    else:
        for i in range(len(s)):
            temp_s = list(s) 
            temp_s.remove(s[i]) 
            if temp_s == temp_s[::-1]: 
                return i 
        return -1

def contig_sum(a): 
    max_ending = max_slice = 0 
    for x in a: 
        max_ending = max(0, max_ending + x)
        max_slice = max(max_slice, max_ending)
    return max_slice

def closest_nums(a): 
    a = sorted(a) 
    diffs = [abs(a[i]-a[i-1]) for i in range(1, len(a))]
    min_diff = min(diffs) 
    idxs = [i for i in range(len(diffs)) if diffs[i] == min_diff]
    res = []
    for idx in idxs: 
        print(a[idx], a[idx+1])

def updateTimes(sigOne, sigTwo): 
    n = len(sigOne)
    m = len(sigTwo)
    runtime = min(n, m) 
    print("runtime: ", runtime)
    updates = 0 
    max_equal = 0 
    for i in range(runtime): 
        if sigOne[i] == sigTwo[i]:
            print(sigOne[i], sigTwo[i]) 
            cur_equal = sigOne[i] 
            if cur_equal > max_equal:
                max_equal = cur_equal
                updates += 1
                print(i, cur_equal, max_equal, updates)
                print("")
    return updates 

def rot_left(a, d): 
    n = len(a) 
    return [a[(i+d)%n] for i in range(n)]

def picking_numbers(a):
    n = len(a) 
    p, q = 0, 0 
    count = 0 
    a = sorted(a)
    max_count = 0 
    cur_count = 0
    while q < n: 
        if abs(a[p] - a[q]) <= 1: 
            cur_count += 1
            # print(a[p], a[q], cur_count)
            q += 1
        else:
            # print(a[p], a[q], cur_count)
            p = q 
            cur_count = 0 
        max_count = max(max_count, cur_count)
    return max_count

def prisoner_sweet(n, m, s): 
    # candy_positions = []
    # for i in range(s, m+s): 
    #     position = i % n 
    #     candy_positions.append(position)
    # return candy_positions[-1]
    return (m - 1 + s - 1) % n + 1 

def minimum_distance(a): 
    d = {} 
    for i in range(len(a)): 
        if a[i] in d: 
            d[a[i]].append(i) 
        else:
            d[a[i]] = [i]
    
    distances = []
    for k, v in d.items(): 
        if len(v) == 2: 
            distances.append(v[1] - v[0]) 
    return -1 if not distances else min(distances)

def acm_team(topics): 
    # ans = [no of topics, no of teams that know these] 
    possible_teams = []
    best_teams = 0
    count_topics = []
    n_people = len(topics)
    for i in range(n_people - 1): 
        for j in range(i+1, n_people): 
            team = [i+1, j+1]
            possible_teams.append(team)
            # bitwise OR 
            a, b = topics[i], topics[j]
            bitor = str(bin(int(a, 2) | int(b, 2)))
            count = bitor.replace("0b", "").count("1")
            count_topics.append(count)

    max_count = max(count_topics)
    for counts in count_topics:
        if counts == max_count:
            best_teams += 1

    return [max_count, best_teams]



def main(): 

    print(acm_team(["10101","11110","00010"]))
    print(acm_team(["10101","11100","11010","00101"]))
    # a = "1100"
    # b = "1010"
    # print(a, b, str(bin(int(a, 2) | int(b, 2))).replace("0b", "").count("1"))
    # print(minimum_distance([3,2,1,2,3]))
    # print(minimum_distance([7,1,3,4,1,7]))
    # print(minimum_distance([7,7]))
    # print(minimum_distance([7,3]))
    # print(prisoner_sweet(4,6,2))
    # print(prisoner_sweet(5,2,1))
    # print(prisoner_sweet(5,2,2))
    # print(picking_numbers([1,1,2,2,4,4,5,5,5]))
    # print(picking_numbers([1,2,2,3,1,2]))
    # print(picking_numbers([4,6,5,3,3,1]))
    # print(rot_left([1,2,3,4,5], 4))
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
    # print(diag_diff(3, [[11,2,4], [4,5,6], [10,8,-12]]))
    # print(diag_diff(3, [[1,2,3], [4,5,6], [9,8,9]]))
    # arr = "63 25 73 1 98 73 56 84 86 57 16 83 8 25 81 56 9 53 98 67 99 12 83 89 80 91 39 86 76 85 74 39 25 90 59 10 94 32 44 3 89 30 27 79 46 96 27 32 18 21 92 69 81 40 40 34 68 78 24 87 42 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3 70 95 33 46 44 9 69 48 33 60 65 16 82 67 61 32 21 79 75 75 13 87 70 33 "
    # print(counting_sort([1,1,3,2,1]))
    # print(counting_sort(list(map(int, arr.split()))))
    # print(median([5,3,1,2,4]))
    # print(palindrome("hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh"))  #-1
    # print(palindrome("a")) # -1
    # print(palindrome("baab")) #-1
    # print(palindrome("aaa")) #-1
    # print(palindrome("adaxa")) #-1
    # print(palindrome("aaax")) #3
    # print(contig_sum([-1,3,4,-2,5,-7]))
    # print(contig_sum([-1,-3,-4,-2,-5,-7]))
    # print(closest_nums([6,2,4,10]))
    # print(updateTimes([1,2,3,3,3,5,4], [1,2,3,4,3,5,4]))


if __name__ == "__main__": 
    main() 