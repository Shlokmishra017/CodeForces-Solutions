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
        n = int(data[idx])
        s = data[idx+1]
        idx += 2
        
       
        odd_p1_ok = True 
        odd_p2_ok = True 
        
        for i in range(0, n, 2):
            expected1 = (i // 2) % 2
            expected2 = 1 - expected1
            
            if s[i] != '?':
                val = int(s[i])
                if val != expected1:
                    odd_p1_ok = False
                if val != expected2:
                    odd_p2_ok = False
                    
        odd_ways = (1 if odd_p1_ok else 0) + (1 if odd_p2_ok else 0)
        
       
        even_p1_ok = True 
        even_p2_ok = True  
        
        for i in range(1, n, 2):
            expected1 = ((i - 1) // 2) % 2
            expected2 = 1 - expected1
            
            if s[i] != '?':
                val = int(s[i])
                if val != expected1:
                    even_p1_ok = False
                if val != expected2:
                    even_p2_ok = False
                    
        even_ways = (1 if even_p1_ok else 0) + (1 if even_p2_ok else 0)
        
       
        ans = (odd_ways * even_ways) % 998244353
        out.append(str(ans))
        
    print('
'.join(out))
 
if __name__ == '__main__':
    solve()