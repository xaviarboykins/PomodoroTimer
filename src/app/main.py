import session

current_session = None

sessions = ["Work session", "Short break", "Work session", "Short break", "Work session", "Short break", "Work session",
            "Long break"]

session_data = {"Work session":{"duration": 25, "count": 0},
                "Short break":{"duration": 5, "count": 0},
                "Long break":{"duration": 15, "count": 0},
}

if __name__ == "__main__":

    pomo_schedule = session.build_session_schedule(sessions)

    session.print_schedule(pomo_schedule)

    response = "y"

    while response == "y":
          for s in sessions:
              response = input("Start Session? y/n: ").lower()

              while response not in ["y", "n"]:
                  print("Invalid response!")
                  response = input("Start Session? y/n: ").lower()

              if response == "y":
                  session_data[s]["count"] += 1
                  session_time = session.get_session_duration(s, session_data)

                  print(f"{s}: {session_data[s]["count"]} / {session_time}")

              elif response == "n":
                  print("Goodbye!")
                  break
