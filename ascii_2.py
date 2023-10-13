start="a"
end="z"
for alphabet1 in range(ord(start),ord(end)+1):
    if chr(alphabet1) == 'e' or chr(alphabet1) == 'q':
        continue
    print(chr(alphabet1))
