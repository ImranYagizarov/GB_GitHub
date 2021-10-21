#Part 2 (Seconds calculation for hh:mm:ss format)

s = int(input("Announce the amount of seconds:"))
if s < 60:
    print(f"00:00:{s:02}")
elif s < 3600:
    print(f"00:{s // 60:02}:{s % 60:02}")
else :
    print(f"{s // 3600:02}:{(s % 3600) // 60:02}:{s % 60:02}")

