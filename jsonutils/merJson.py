import json
import glob
import os
import logging

logging.basicConfig(level=logging.INFO)


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
        return files

    def merge(self, src_json, dest_json):

        for key in src_json:

            if key in dest_json:
                dest_json[key].extend(src_json[key])
            else:
                dest_json[key] = src_json[key]

        return dest_json

    def get_output_filename(self,path_prefix):
        files = self.list_files(path_prefix)
        if len(files) > 0:

            last_file = files[-1]
            last_seq_no = last_file[len(path_prefix) : -1 * len(self.extension_name)]

            try:
                last_seq_no = int(last_seq_no)
            except Exception as e:
                last_seq_no = 0
        else:
            last_seq_no = 0

        filename = path_prefix + str(last_seq_no + 1) + self.extension_name
        return filename

    def write_file(self, output_base_name, dir, json_data,indent = 0):
        path_prefix = os.path.join(dir, output_base_name)
        filename = self.get_output_filename(path_prefix)

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False,indent= indent)
            logging.info(f' Writing merged file : {filename} ')

    def merge_by_filename_prefix(self, input_base_name, output_base_name, max_file_size , dir = current_dir):

        path_prefix = os.path.join(dir, input_base_name)
        files = self.list_files(path_prefix)
        logging.info(f'  Json Files to process : {files} ')


        total_size = 0
        filename = files[0]
        dest_json_file = self.read_json_to_dic(filename)
        logging.info(f' Processing file : {filename} ')

        for filename in files[1:]:
            total_size += os.path.getsize(filename)

            if total_size > max_file_size:
                logging.error(f' Exceeding Max File Size ({max_file_size} Bytes) ')
                break

            logging.info(f' Processing file : {filename} ')
            json_to_merge = self.read_json_to_dic(filename)
            dest_json_file = self.merge(src_json=json_to_merge, dest_json=dest_json_file)

        self.write_file(output_base_name,dir,dest_json_file)

