from jsonutils.merJson import MerJson

merjson = MerJson()
merjson.merge_by_filename_prefix('data','merged',192, 'out')