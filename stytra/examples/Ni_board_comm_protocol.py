from stytra import Stytra, Protocol
from stytra.stimulation.stimuli.visual import Pause, FullFieldVisualStimulus
from stytra.stimulation.stimuli import Stimulus
from stytra.triggering import NIBoard
import nidaqmx

task = nidaqmx.Task()
class NICommStimulus(Stimulus):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def start(self):
        """ """
        task.ao_channels.add_ao_voltage_chan('Dev1/ao0', 'mychannel', 0, 5)
        task.start()
        task.write(5)  # send blinking command at stimulus start
        #self.shock +=1


    def stop(self):
        """ """
        task.write(0)  # send blinking command at stimulus start
        task.stop()
        task.close()


class FlashProtocol(Protocol):
    name = "flash protocol"

    def __init__(self):
        super().__init__()
        self.ITI= 30.0
        self.odor_duration = 5.0

    def get_stim_sequence(self):
        # This is the method we need to write to create a new stimulus list.
        # In this case, the protocol is simply a 1 second flash on the entire screen
        # after a pause of 4 seconds:
        stimuli = []
        stimuli.append(Pause(duration=self.ITI))
        stimuli.append(NICommStimulus(duration = self.odor_duration))
        stimuli.append(Pause(duration=self.ITI))
        stimuli.append(NICommStimulus(duration=self.odor_duration))
        stimuli.append(Pause(duration=self.ITI))

        return stimuli


if __name__ == "__main__":

    trigger = NIBoard(chan="Dev1/ai0")

    st = Stytra(protocol=FlashProtocol(), scope_triggering=trigger)
