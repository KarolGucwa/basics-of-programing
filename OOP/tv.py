class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0  # Initial volume level is 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on:
            if 0 < self.channel_no <= len(self.channels):
                print(f"TV is on, channel {self.channel_no} ({self.channels[self.channel_no - 1]}), volume {self.volume}")
            else:
                print(f"TV is on, channel {self.channel_no} (Invalid channel), volume {self.volume}")
        else:
            print("TV is off")

    def set_channel(self, new_channel_no):
        if 0 < new_channel_no <= len(self.channels):
            self.channel_no = new_channel_no
            print(f"Channel changed to {self.channel_no} ({self.channels[self.channel_no - 1]})")
        else:
            print("Invalid channel number")

    def set_channels(self, channels_list):
        self.channels = channels_list
        print("Channels have been set.")

    def show_channels(self):
        if self.channels:
            print("Channel list:")
            for idx, channel in enumerate(self.channels, 1):
                print(f"{idx}. {channel}")
        else:
            print("No channels available.")

    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1
            print(f"Volume increased to {self.volume}")
        else:
            print("Maximum volume reached")

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume decreased to {self.volume}")
        else:
            print("Minimum volume reached")
