import os
import subprocess

class mocp_runner():
    #  class vars
    music_dir = "/home/vboxuser/ENGI301/project_01/sample_music"

    def __init__(self, music_dir = "/home/vboxuser/ENGI301/project_01/sample_music") -> None:
        self.music_dir = music_dir

    def mocp_start_server(self):
        os.system("mocp -S") # run server in headless mode
    
    def mocp_exit_server(self):
        os.system("mocp -x") # kill server

    def mocp_get_state(self):
        states = {"STOP\n": 0, "PLAY\n": 1, "PAUSE\n": 2}
        cmd = ["mocp", "-Q", "%state"]
        state = subprocess.run(cmd, capture_output=True, text=True).stdout
        print("Process in state_id: %d | state: %s"%(states[state],state))
        return states[state];

    def mocp_add(self, path = ""):
        if (type(path)!=type("")):
            print("mocp_add | ERROR: nonstring path")
            return -1
        return os.system("mocp -a %s"%path)

    def mocp_toggle(self):
        state = self.mocp_get_state()
        if (state == 0): # the player is stopped, attempt to run
            os.system("mocp -p")
        if (state == 1): # the player is playing
            os.system("mocp -G")
        if (state == 0): # the player is paused
            os.system("mocp -G")
        state = self.mocp_get_state()
        print("mocp_toggle: newState: d\n"%state)
        return state

    def run(self):

        # start the server
        self.mocp_start_server()

        # add all files in the music_dir
        self.mocp_add(self.music_dir)

        # attempt to run
        self.mocp_toggle()

        return 0