english=float(input('請輸入你的英文成績'))
math=float(input('請輸入你的數學成績'))
if math>=90 and english>=90:
    print("有獎品")
if math<60 and english<60:
    print("要處罰")
if (math<60 and english>=60) or (math>=60 and english<60):
    print("再加油")
