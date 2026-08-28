import sys
 
def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        nums = sorted([int(data[idx]), int(data[idx+1]), int(data[idx+2])])
        idx += 3
        ans = min(nums[2] - nums[0], nums[1])
        out.append(str(ans))
    print('
'.join(out))
 
if __name__ == '__main__':
    solve()