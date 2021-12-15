import nidaqmx

while (True):
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        input = task.read()

        print(bool(round(input)))