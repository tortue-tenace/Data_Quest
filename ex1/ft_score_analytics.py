import sys

int_list: list = []
print("=== Player Score Analytics ===")

if len(sys.argv) == 1:
    print("No scores provided.  Usage:  python3 ft_score_analytics.py"
          " <score1> <score2> ...")
    sys.exit(1)

for i in sys.argv[1:]:
    try:
        val = int(i)
        if val < 0:
            print(f"Invalid entry: {i} score can't be negative")
            continue
        int_list.append(val)
    except ValueError:
        print(f"Invalid parameter:  '{i}'")


if len(int_list) < 1:
    print("No scores provided.  Usage:  python3 ft_score_analytics.py"
          " <score1> <score2> ...")
    sys.exit(1)

print(f"Scores processed:  {int_list}")
print(f"Total players:  {len(int_list)}")
print(f"Total score:  {sum(int_list)}")
print(f"Average score:  {sum(int_list)/len(int_list)}")
print(f"High score:  {max(int_list)}")
print(f"Low score:  {min(int_list)}")
print(f"Score range:  {max(int_list) - min(int_list)}")
