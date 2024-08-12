import plyer as no
import time
import pyttsx3 as tts

if __name__ == '__main__':
    while True:
        no.notification.notify(
            title='Time to drink water....',
            message="Now you should drink water and take rest for a few seconds......",
            app_icon='glassofwater_84019.ico',
            timeout=10

        )
        tts.speak('Now you should drink water and take rest for a few seconds')
        time.sleep(3600)
