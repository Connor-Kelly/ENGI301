import subprocess
import os

class Mocp():
    #  class vars
    # music_dir = "/home/vboxuser/ENGI301/project_01/sample_music"
    music_dir = None
    config_path = "/var/lib/cloud9/engi301/moc_config"

    def __init__(self, music_dir = "/var/lib/cloud9/engi301/project_01/sample_music") -> None:
        self.music_dir = music_dir

    def start_server(self):
        os.system("mocp -S -F -C %s"%self.config_path) # run server in headless mode

    def get_state(self):
        states = {"STOP\n": 0, "PLAY\n": 1, "PAUSE\n": 2}
        cmd = ["mocp", "-Q", "%state"]
        state = subprocess.run(cmd, capture_output=True, text=True).stdout
        print("Process in state_id: %d | state: %s"%(states[state],state))
        return states[state];

    def add(self, path = "/var/lib/cloud9/engi301/project_01/sample_music"):
        if (type(path)!=type("")):
            print("mocp_add | ERROR: nonstring path")
            return -1
        return os.system("mocp -a %s"%path)

    def toggle(self):
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