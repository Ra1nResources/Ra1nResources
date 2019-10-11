import dfu
device = dfu.acquire_device()
dfu.release_device(device)
