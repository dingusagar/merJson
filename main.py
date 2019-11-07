from jsonutils.merJson import MerJson

merjson = MerJson()
merjson.merge_by_filename_prefix('data','merged',10000, 'out')