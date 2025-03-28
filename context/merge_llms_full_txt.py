import os
import yaml


def load_config():
    with open("config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def read_file(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        print(f"⚠ Warning: {path} not found.")
        return ""


def main():
    config = load_config()
    master_config = config.get("llms_full_txt_file", {})

    input_files = master_config.get("input_files", [])
    layout = master_config.get("layout")

    # Handle both single output_file and multiple output_files
    output_file_single = master_config.get("output_file")
    output_files_list = master_config.get("output_files")

    print("output_files_single", output_file_single)
    print("output_files", output_files_list)

    # If output_files is defined, use that; otherwise fall back to output_file
    if output_files_list:
        output_files = output_files_list
    elif output_file_single:
        output_files = [output_file_single]
    else:
        print("Error: No output file(s) specified in config.yaml under master_file.")
        exit(1)

    # Read and combine the content from each input file
    contents = [read_file(f.get("file_path")) for f in input_files]

    if layout:
        # Replace placeholders {{FILE1}}, {{FILE2}}, etc. with respective file content
        result = layout
        for i, content in enumerate(contents, start=1):
            placeholder = f"{{{{FILE{i}}}}}"
            result = result.replace(placeholder, content)
    else:
        # Simply join the files with a separator
        result = "\n\n---\n\n".join(contents)

    # Write the combined result to each output file
    for out_file in output_files:
        os.makedirs(os.path.dirname(out_file.get("file_path")), exist_ok=True)
        with open(out_file.get("file_path"), "w", encoding="utf-8") as f:
            f.write(result)
        print(f"✔ Master file updated at {out_file.get('file_path')}")


if __name__ == "__main__":
    main()