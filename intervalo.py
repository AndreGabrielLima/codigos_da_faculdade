N = int(input())
_in = _on = 0
for c in range(N):
    n = int(input())
    if 0 <= n <= 20:
        _in += 1
    else:
        _on += 1
print('{} in'.format(_in))
print('{} out'.format(_on))