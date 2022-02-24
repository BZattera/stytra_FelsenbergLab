from stytra import Stytra, Protocol
from stytra.stimulation.stimuli.visual import Pause, FullFieldVisualStimulus
from stytra.triggering import NIBoard


class FlashProtocol(Protocol):
    name = "flash protocol"

    def __init__(self):
        super().__init__()
        self.period_sec = 3.0
        self.flash_duration = 2.0

    def get_stim_sequence(self):
        # This is the method we need to write to create a new stimulus list.
        # In this case, the protocol is simply a 1 second flash on the entire screen
        # after a pause of 4 seconds:
        stimuli = [
            Pause(duration=4.0),
            FullFieldVisualStimulus(duration=1.0, color=(255, 255, 255)),
        ]
        return stimuli


if __name__ == "__main__":

    trigger = NIBoard(chan="Dev1/ai0")

    st = Stytra(protocol=FlashProtocol(), scope_triggering=trigger)
