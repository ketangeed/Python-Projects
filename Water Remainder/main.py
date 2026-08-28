
import time
from plyer import notification

# Keep the reminder running continuously
while True:

    # Show the reminder in the terminal
    print("Time to sip some water...")

    # Show a desktop notification
    notification.notify(
        title="Time to DRINK water",
        message="You need to drink some water."
    )

    # Wait for 1 hour before showing the next reminder
    time.sleep(60 * 60)




