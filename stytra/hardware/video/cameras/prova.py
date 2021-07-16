import pyspin as PySpin
import cv2

serial = '19432971' #Probably different for you although I also use a BlackFly USB3.0

system = PySpin.System.GetInstance()

blackFly_list = system.GetCameras()

blackFly = blackFly_list.GetBySerial(serial)

height = blackFly.Height()
width = blackFly.Width()
channels = 1

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('test_vid.avi',fourcc, blackFly.AcquisitionFrameRate(), (blackFly.Width(), blackFly.Height()), False) #The last argument should be True if you are recording in color.


blackFly.Init()
blackFly.AcquisitionMode.SetValue(PySpin.AcquisitionMode_Continuous)
blackFly.BeginAcquisition()

nFrames = 1000

for _ in range(nFrames):
    im = blackFly.GetNextImage()

    im_cv2_format = im.GetData().reshape(height,width,channels)

    # Here I am writing the image to a Video, but once you could save the image as something and just do whatever you want with it.
    out.write(im_cv2_format)
    im.release()

out.release()