import nidaqmx
import time

task = nidaqmx.Task()
task.ao_channels.add_ao_voltage_chan('Dev1/ao0','mychannel',0,5)
task.start()
task.write(0)
time.sleep(2)
task.write(5)
time.sleep(2)
task.write(0)
task.stop()
task.close()


