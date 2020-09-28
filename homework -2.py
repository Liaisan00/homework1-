class Album():
    name_album = "Artpop"
    group = "Lady Gaga"
    track_list1 = {"Venus":3, "Aura":4, "Guy":5}
    track_list2 = {"Artpop":4, "Swine":4, "Donatella":7}
    def get_tracks(self):
        new_track = track()
        new_track.show


    def get_track(self, new_track, new_duration):
        self.track_list1.update({new_track:new_duration})
        print(self.track_list1)



    def get_duration(self):
        print(f"Длительность альбома {sum(self.track_list1.values())} минут")



class Track():
    name_track = " "
    duration = int()
    def show(self):
        print(f"{sef.name_track} - {self.duration}")


