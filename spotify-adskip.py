import spotipy, pyautogui, os, win32gui, win32con, time, psutil
import spotipy.util as util
from dotenv import load_dotenv

load_dotenv()
#input your spotify credentials here (Available at https://developer.spotify.com/dashboard/login):
cid = os.getenv('cid')
secret = os.getenv('secret')
username = os.getenv('name')
location = os.getenv('location')    #location of spotify.exe in your computer

#Authorization (your browser will pop-up for a second)
scope = "user-read-currently-playing"
redirect_uri = "http://localhost:8888/callback"
token = util.prompt_for_user_token(username, scope, cid, secret, redirect_uri)
sp = spotipy.Spotify(auth=token)

while "Spotify.exe" in (i.name() for i in psutil.process_iter()):    #code will stop running after you exit spotify
    time.sleep(1)
    try:
        if sp.current_user_playing_track()['currently_playing_type'] == 'ad':   #if advert is detected
            os.system("TASKKILL /F /IM Spotify.exe")    #exit spotify
            os.startfile(location)                      #start spotify
            time.sleep(3)                               #wait for 3 seconds for spotify to open (change accordingly)
            pyautogui.press('nexttrack')                #play next song in queue
            Minimize = win32gui.GetForegroundWindow()   #minimize the window in front (which should be spotify as it opened it again and waited for 3 seconds to let it come on the front screen)
            win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
    except:
        pass
