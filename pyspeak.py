import win32com.client

speaker = win32com.client.Dispatch("SAPI.SPVOICE")
speaker.Speak("Friend")
