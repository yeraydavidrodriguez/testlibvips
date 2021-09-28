import pyvips

image = pyvips.Image.new_from_file('raw/test.tif', access='sequential')
result = image.icc_transform("sRGB")
result.write_to_file("raw/test-srgb.tif")
