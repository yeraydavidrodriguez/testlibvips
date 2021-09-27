import pyvips

image = pyvips.Image.new_from_file('raw/test.tif', access='sequential')
result = image.resize(0.5, kernel='lanczos2')
result.write_to_file("out.tif")
