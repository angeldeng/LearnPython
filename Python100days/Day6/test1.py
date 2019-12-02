m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1, m + 1):
    fm *= num
print(fm)
fn = 1
for num in range(1, n + 1):
    fn *= num
print(fn)
fmn = 1
for num in range(1, m - n + 1):
    fmn *= num
print(fmn)
print(fm // fn // fmn)