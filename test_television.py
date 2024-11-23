from television import Television


class TestTelevision:

    def set_up(self):
        """Set up a new Television instance for each test."""
        self.tv = Television()

    def test_initial_state(self):
        """Test the initial state of the Television object."""
        assert str(self.tv) == "Power = False,Channel = 0,Volume = 0"

    def test_power(self):
        """Test the power method."""
        self.tv.power()
        assert str(self.tv) == "Power = True,Channel = 0,Volume = 0"

        self.tv.power()
        assert str(self.tv) == "Power = False,Channel = 0,Volume = 0"

    def test_mute(self):
        """Test the mute method."""
        self.tv.power()
        self.tv.mute()
        assert str(self.tv) == "Power = True,Channel = 0,Volume = 0"

        self.tv.volume_up()
        assert str(self.tv) == "Power = True,Channel = 0,Volume = 1"

        self.tv.mute()
        assert str(self.tv) == "Power = True,Channel = 0,Volume = 0"

    def test_channel_up(self):
        """Test the channel_up method."""
        self.tv.power()
        self.tv.channel_up()
        assert str(self.tv) == "Power = True,Channel = 1,Volume = 0"

        self.tv.channel_up()
        assert str(self.tv) == "Power = True,Channel = 2,Volume = 0"

        self.tv.channel_up()
        assert str(self.tv) == "Power = True,Channel = 3,Volume = 0"

        self.tv.channel_up()
        assert str(self.tv) == "Power = True,Channel = 0,Volume = 0"

    def test_channel_down(self):
        """Test the channel_down method."""
        self.tv.power()
        self.tv.channel_up()
        self.tv.channel_down()
        assert str(self.tv) == "Power = True,Channel = 0,Volume = 0"

        self.tv.channel_down()
        assert str(self.tv) == "Power = True,Channel = 3,Volume = 0"

    def test_volume_up(self):
        """Test the volume_up method."""
        self.tv.power()
        self.tv.volume_up()
        assert str(self.tv) == "Power = True,Channel = 0,Volume = 1"

        self.tv.volume_up()
        assert str(self.tv) == "Power = True,Channel = 0,Volume = 2"

        self.tv.volume_up()
        assert str(self.tv) == "Power = True,Channel = 0,Volume = 2"

    def test_volume_down(self):
        """Test the volume_down method."""
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_down()
        assert str(self.tv) == "Power = True,Channel = 0,Volume = 0"

        self.tv.volume_down()
        assert str(self.tv) == "Power = True,Channel = 0,Volume = 0"
