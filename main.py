from jsonutils.merJson import MerJson

merjson = MerJson()
merjson.merge_by_filename_prefix(
    input_base_name='data',
    output_base_name='merged',
    max_file_size=50000, dir='out')
