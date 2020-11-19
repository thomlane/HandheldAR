from ArModules import CameraModule

Cam = CameraModule()
assert (Cam != None),"Camera Module not initialized"
print("Camera Module Initialized")

Buf = Cam.readbuf()
assert (Buf.any() != None),"Buffer not returned"
print("Buffer returned")

Cam.resize((320, 240))
assert (Cam.dimensions == (320, 240)),"Dimensions not resized"
print("Dimensions resized")

Buf = Cam.readbuf()
assert (Buf.any() != None),"Buffer not returned"
assert (Buf.shape == (240, 320, 3)), "Buffer of incorrect dimensions"
print("Buffer correct dimensions")

print("Say Cheese!")
Cam.capture()