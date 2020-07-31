#!/usr/bin/env python3.6
def hint_username(username):
   if len(username) < 3:
      print("User: " + username + ", " +
            "Invalid username. Must be at least 3 characters long")
   elif len(username) > 15:
     print("User: " + username + ", " +
           "Invalid username. Must be at most 15 characters long")
   else:
      print("User: " + username + ", " + "valid username")
      
'''
   else:
      if len(username) > 15:
          print("User: " + username + ", " +
                "Invalid username. Must be at most 15 characters long")
      else:
          print("User: " + username + ", " + "valid username")
'''
   

hint_username("tutul")
hint_username("Md Iftikhar Hossain Tutul")
hint_username("tt")
