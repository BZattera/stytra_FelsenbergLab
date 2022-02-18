from stytra import Stytra, Protocol
from stytra.stimulation.stimuli.visual import Pause, FullFieldVisualStimulus, CombinerStimulus, VisualCombinerStimulus, Stimulus
from lightparam import Param
import pyfirmata

board = pyfirmata.Arduino('COM8') # initialization of the ball



class ArduinoCommStimulus(Stimulus):

    def __init__(self, pin,**kwargs):
        super().__init__(**kwargs)
        self.pin = pin

    def start(self):
        """ """
        board.digital[int(self.pin)].write(1)  # send blinking command at stimulus start

    def stop(self):
        """ """
        board.digital[int(self.pin)].write(0)  # turn off the pin

class FlashProtocol(Protocol):
    name = "flash_protocol"  # every protocol must have a name.

    def __init__(self):
        super().__init__()
        # Here we define these attributes as Param s. This will automatically
        #  build a control for them and make them modifiable live from the
        # interface.
        self.shock_duration = 2 # duration of the shock (2 sec)
        self.flash_duration = 3 # duration of the visual stimulus without any shock (3 sec)
        self.test_duration = 60 # duration of the test
        self.one_trial_rep = 12
        self.color1 = (29, 138, 225) # put (0,0,0) for black
        self.color2 = (45, 153, 50) # put (255, 255, 255) for white
        self.n_rep = 4

    def get_stim_sequence(self):
        # This is the
        stimuli = []

        # pre-training phase
        stimuli.append(FullFieldVisualStimulus(duration=5, color=(255, 255, 255))) # 5 sec of white stimulus
        stimuli.append(FullFieldVisualStimulus(duration=55, color=(0, 0, 0))) # 55 sec of black stimulus

        ### visual stimulation, no shock
        # defining the quadrants for the first stimulation
        up_left_only_stim = FullFieldVisualStimulus(duration=self.flash_duration, color=self.color1, clip_mask=(0,0, 0.5, 0.5))
        up_right_only_stim = FullFieldVisualStimulus(duration=self.flash_duration, color=self.color2,
                                                    clip_mask=(0, 0.5, 0.5, 0.5))
        low_left_only_stim = FullFieldVisualStimulus(duration=self.flash_duration, color=self.color2,
                                                     clip_mask=(0.5, 0, 0.5, 0.5))
        low_right_only_stim = FullFieldVisualStimulus(duration=self.flash_duration, color=self.color1, clip_mask=(0.5, 0.5, 0.5, 0.5))

        # defining the quadrants for the second position (reversed)
        up_left_only_stim_r = FullFieldVisualStimulus(duration=self.flash_duration, color=self.color2,
                                                    clip_mask=(0, 0, 0.5, 0.5))
        up_right_only_stim_r = FullFieldVisualStimulus(duration=self.flash_duration, color=self.color1,
                                                     clip_mask=(0, 0.5, 0.5, 0.5))
        low_left_only_stim_r = FullFieldVisualStimulus(duration=self.flash_duration, color=self.color1,
                                                     clip_mask=(0.5, 0, 0.5, 0.5))
        low_right_only_stim_r = FullFieldVisualStimulus(duration=self.flash_duration, color=self.color2,
                                                      clip_mask=(0.5, 0.5, 0.5, 0.5))

        ### visual stimulation DURING the shock
        # defining the quadrants for the first stimulation
        up_left_only_stim_shock = FullFieldVisualStimulus(duration=self.shock_duration, color=self.color1,
                                                    clip_mask=(0, 0, 0.5, 0.5))
        up_right_only_stim_shock = FullFieldVisualStimulus(duration=self.shock_duration, color=self.color2,
                                                     clip_mask=(0, 0.5, 0.5, 0.5))
        low_left_only_stim_shock = FullFieldVisualStimulus(duration=self.shock_duration, color=self.color2,
                                                     clip_mask=(0.5, 0, 0.5, 0.5))
        low_right_only_stim_shock = FullFieldVisualStimulus(duration=self.shock_duration, color=self.color1,
                                                      clip_mask=(0.5, 0.5, 0.5, 0.5))

        # defining the quadrants for the second position (reversed)
        up_left_only_stim_shock_r = FullFieldVisualStimulus(duration=self.shock_duration, color=self.color2,
                                                      clip_mask=(0, 0, 0.5, 0.5))
        up_right_only_stim_shock_r = FullFieldVisualStimulus(duration=self.shock_duration, color=self.color1,
                                                       clip_mask=(0, 0.5, 0.5, 0.5))
        low_left_only_stim_shock_r = FullFieldVisualStimulus(duration=self.shock_duration, color=self.color1,
                                                       clip_mask=(0.5, 0, 0.5, 0.5))
        low_right_only_stim_shock_r = FullFieldVisualStimulus(duration=self.shock_duration, color=self.color2,
                                                        clip_mask=(0.5, 0.5, 0.5, 0.5))

        # call the Arduino protocol to turn the Pin on
        shock = ArduinoCommStimulus(pin=13, duration=self.shock_duration)
        shock_r = ArduinoCommStimulus(pin=12, duration=self.shock_duration)

        for i in range(self.n_rep):

            for i in range(self.one_trial_rep):
                stimuli.append(CombinerStimulus([up_left_only_stim_shock, up_right_only_stim_shock,
                                                       low_left_only_stim_shock, low_right_only_stim_shock, shock]), )
                stimuli.append(VisualCombinerStimulus([up_left_only_stim, up_right_only_stim, low_left_only_stim, low_right_only_stim]), )

            for i in range(self.one_trial_rep):
                stimuli.append(VisualCombinerStimulus([up_left_only_stim_shock_r, up_right_only_stim_shock_r,
                                                       low_left_only_stim_shock_r, low_right_only_stim_shock_r, shock_r]), )
                stimuli.append(VisualCombinerStimulus([up_left_only_stim_r, up_right_only_stim_r, low_left_only_stim_r, low_right_only_stim_r]), )

        stimuli.append(FullFieldVisualStimulus(duration=120, color=(0, 0, 0))) # no visual stimulation for 2 min before the test

        # test for quadrants 1 and 3
        stimuli.append(CombinerStimulus([
            FullFieldVisualStimulus(duration=self.test_duration, color=self.color1,clip_mask=(0, 0, 0.5, 0.5)),
        FullFieldVisualStimulus(duration=self.test_duration, color=self.color2,clip_mask=(0, 0.5, 0.5, 0.5)),
        FullFieldVisualStimulus(duration=self.test_duration, color=self.color2,clip_mask=(0, 0.5, 0.5, 0.5)),
        FullFieldVisualStimulus(duration=self.test_duration, color=self.color1,clip_mask=(0.5, 0.5, 0.5, 0.5)),]))

        # test for quadrants 2 and 4
        stimuli.append(CombinerStimulus([
            FullFieldVisualStimulus(duration=self.test_duration, color=self.color2, clip_mask=(0, 0, 0.5, 0.5)),
            FullFieldVisualStimulus(duration=self.test_duration, color=self.color1, clip_mask=(0, 0.5, 0.5, 0.5)),
            FullFieldVisualStimulus(duration=self.test_duration, color=self.color1, clip_mask=(0, 0.5, 0.5, 0.5)),
            FullFieldVisualStimulus(duration=self.test_duration, color=self.color2, clip_mask=(0.5, 0.5, 0.5, 0.5)), ]))




        return stimuli


if __name__ == "__main__":
    st = Stytra(protocol=FlashProtocol())
