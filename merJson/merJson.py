import json
import glob
import os


class MerJson:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    output_file_seq_no = 0
    extension_name = '.json'

    def read_json_to_dic(self, filename):
        with open(filename) as json_file:
            data = json.load(json_file)

        return data

    def list_files(self, path_prefix):
        regex = path_prefix + '[0-9]*'
        files = sorted(glob.glob(regex), key=lambda x: int(x[len(path_prefix): -1 * len(self.extension_name)]))
        print(files)
        return files

    def merge(self, src_json, dest_json):

        for key in src_json:

            if key in dest_json:
                dest_json[key].extend(src_json[key])
            else:
                dest_json[key] = src_json[key]

        return dest_json

    def get_next_seq_number(self):
        self.output_file_seq_no = self.output_file_seq_no + 1
        return str(self.output_file_seq_no)

    def write_file(self, output_base_name, dir, json_data,indent = 0):
        path_prefix = os.path.join(dir, output_base_name)
        filename = path_prefix + self.get_next_seq_number() + self.extension_name

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False,indent=4)

    def merge_by_filename_prefix(self, dir, input_base_name, output_base_name, max_file_size):

        path_prefix = os.path.join(dir, input_base_name)
        files = self.list_files(path_prefix)

        total_size = 0
        dest_json_file = self.read_json_to_dic(files[0])
        for filename in files[1:]:
            total_size += os.path.getsize(filename)

            if total_size > max_file_size:
                print('Max file size reached !!..Merging no more..')
                break

            json_to_merge = self.read_json_to_dic(filename)

            dest_json_file = self.merge(src_json=json_to_merge, dest_json=dest_json_file)

        self.write_file(output_base_name,dir,dest_json_file)

