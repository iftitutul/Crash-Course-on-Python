#!/usr/bin/env python3.6
def hint_username(username):
   if len(username) <3:
      print ("User:" + username + ", " + "Invalid username. Must be at least 3 characters long")
   else:
      print("User:" + username + ", " + "valid username")


hint_username("tutul")

hint_username("tt")
