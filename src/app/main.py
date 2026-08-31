
session_name = None
work_session = "Work session"
short_break_session = "Short break"
long_break_session = "Long break"

is_user_working = False

break_count = 0
work_minutes = 25
short_break_minutes = 5
long_break_minutes = 15

work_seconds = work_minutes * 60
short_break_seconds = short_break_minutes * 60
long_break_seconds = long_break_minutes * 60

print(session_name)
print(f"Work session: {work_minutes} minutes\n"
      f"Short break: {short_break_minutes} minutes\n"
      f"Long break: {long_break_minutes} minutes")

user_response = input("Ready to start work session? Y/N\n").lower()

if user_response == "y":
      session_name = work_session

      print("Work session started")
      print(f"{session_name}: {work_minutes} minutes or {work_seconds} seconds")

      is_user_working = True
elif user_response == "n":
      print("Work session not started")
else:
      print("Invalid input")
      print("Work session not started")

if session_name == work_session:
      user_response = input("Ready to start break? Y/N\n").lower()
      if user_response == "y":
            session_name = short_break_session

            break_count = break_count + 1

            print(f"{session_name}: {break_count} started")
            print(f"{session_name}: {short_break_minutes} minutes or {short_break_seconds} seconds\n")

            is_user_working = False
      elif user_response == "n":
            print("Short break not started")
