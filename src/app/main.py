
current_session = None

sessions = ["Work session", "Short break", "Work session", "Short break", "Work session", "Short break", "Work session",
            "Long break"]

session_data = {sessions[0]:{"duration": 25, "count": 0},
                sessions[1]:{"duration": 5, "count": 0},
                sessions[7]:{"duration": 15, "count": 0},
}

response = "y"

print("Pomodoro Schedule:")

for session_num, session in enumerate(sessions, start=1):
      # Print schedule
      print(f"{session_num} - {session}")

while response == "y":
      for session in sessions:
          response = input("Start Session? y/n: ").lower()

          while response not in ["y", "n"]:
              print("Invalid response!")
              response = input("Start Session? y/n: ").lower()

          if response == "y":
              current_session = session
              session_data[current_session]["count"] += 1
              print(f"{current_session}: {session_data[current_session]["count"]} / {session_data[current_session]
              ['duration']} minutes or {session_data[current_session]['duration'] * 60} seconds")
          elif response == "n":
              print("Goodbye!")
              break
