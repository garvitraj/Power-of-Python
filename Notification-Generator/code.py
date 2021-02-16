import time
from plyer import notification
 if __name__ == '__main__':
 	while True:
 		notification.notify(
 			title = "**TILE THAT YOU WANT IN NOTIFICATON**",
 			message ="MESSAGE THAT YOU WANT TO DISPALY WITH NOTIFICATION",
 			app_icon = "path to your .ico file",
 			timeout= 10    #it tells the time till which the notification will be on screen
 			)
 		#	time.sleep(6)
 			time.sleep(60*60) #setting up notification with time
