print("---SECONDS TO TIME---")

seconds = int(input("Enter the seconds: "))

if 0 <= seconds:
    hours = seconds // 3600
    minuts = (seconds % 3600) // 60
    segs = seconds % 60

    print(f"{hours:02d}:{minuts:02d}:{segs:02d}")
else:
    print("negative time?")