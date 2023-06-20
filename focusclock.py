import time

def focus_timer(minutes):
    seconds = minutes *  while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # 在同一行打印
        time.sleep(1)
        seconds -= 1
    print("Focus complete!")

# 设置专注时间为25分钟
focus_timer(25)
