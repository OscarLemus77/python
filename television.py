class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Initialize the Television instance with default values."""
        self.__status = False
        self.__muted = False
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME

    def power(self) -> None:
        """Toggle the power status of the TV."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggle the mute status of the TV. Muting stores the current volume."""
        if self.__status:
            self.__muted = not self.__muted


    def channel_up(self) -> None:
        """Increase the TV channel, cycling back to the minimum at the maximum."""
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel +=1

    def channel_down(self) -> None:
        """Decrease the TV channel, cycling back to the maximum at the minimum."""
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -=1

    def volume_up(self) -> None:
        """Increase the volume, respecting mute and maximum constraints."""
        if self.__status:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                 self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume, respecting mute and minimum constraints."""
        if self.__status:
            self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1


    def __str__  (self):
        """
        """Return the TV's current status, channel, and volume."""
        :return: tv status
        """""
        if self.__muted:
            return f"Power = {self.__status},Channel = {self.__channel},Volume = {0}"
        else:
            return f"Power = {self.__status},Channel = {self.__channel},Volume = {self.__volume}"
