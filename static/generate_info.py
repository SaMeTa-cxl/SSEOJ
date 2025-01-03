import os
import hashlib
import json

def calculate_md5(file_path):
    with open(file_path, "r", encoding='utf-8') as f:
        content = f.read().strip()
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def generate_info_for_folder(folder_path):
    files = os.listdir(folder_path)
    in_files = sorted([f for f in files if f.endswith('.in')])
    out_files = sorted([f for f in files if f.endswith('.out')])
    out_id = [os.path.splitext(out_file)[0] for out_file in out_files]

    spj = len(out_files) == 0
    test_cases = {}

    for in_file in in_files:
        case_id = os.path.splitext(in_file)[0]
        case_id_int = int(case_id)
        input_path = os.path.join(folder_path, in_file)
        input_size = os.path.getsize(input_path)

        if spj:
            test_cases[str(case_id+1)] = {
                "input_name": in_file,
                "input_size": input_size
            }
        else:
            if case_id in out_id:
                case_id = out_id.index(case_id)
                output_path = os.path.join(folder_path, out_files[case_id])
                output_size = os.path.getsize(output_path)
                stripped_output_md5 = calculate_md5(output_path)
                test_cases[str(case_id+1)] = {
                    "input_name": in_file,
                    "input_size": input_size,
                    "output_name": out_files[case_id],
                    "output_size": output_size,
                    "stripped_output_md5": stripped_output_md5
                }
    return {
        "spj": spj,
        "test_cases": test_cases
    }

if __name__ == '__main__':
    base_path = "test_case"  # Root folder containing test_case_i subfolders
    for subfolder in os.listdir(base_path):
        subfolder_path = os.path.join(base_path, subfolder)
        if os.path.isdir(subfolder_path):
            info = generate_info_for_folder(subfolder_path)
            info_path = os.path.join(subfolder_path, "info")
            with open(info_path, 'w', encoding='utf-8') as f:
                json.dump(info, f, indent=4)
