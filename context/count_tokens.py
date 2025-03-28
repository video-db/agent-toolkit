import tiktoken
import yaml
import matplotlib.pyplot as plt
import json


def load_config_yaml():
    with open("config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def format_k(num):
    if num >= 1000:
        return f"{num / 1000:.1f}k"
    else:
        return str(num)


yml = load_config_yaml()
master_config = yml.get("llms_full_txt_file")
tkn_config = yml.get("token_count")

tkn_encoding_model = tkn_config.get("tiktoken_encoding_model")
sub_component_files = master_config.get("input_files")
final_files = master_config.get("output_files")
final_file = next((obj for obj in final_files if obj["name"] == "llms_full_txt"), None)


sub_component_files_result = []
final_file_result = {}


def count_token(text, model="gpt-4"):
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))


for file in sub_component_files:
    with open(file.get("file_path"), "r") as f:
        num_tokens = count_token(f.read(), tkn_encoding_model)
        sub_component_files_result.append(
            {"name": file.get("name"), "tokens": num_tokens}
        )


# Prepare data for plotting
labels = [item["name"] for item in sub_component_files_result]
tokens = [item["tokens"] for item in sub_component_files_result]

# Build custom labels with k-format
custom_labels = [
    f"{item['name']} ({format_k(item['tokens'])})"
    for item in sub_component_files_result
]

# Choose some distinct colors for each slice (adjust as needed)
colors = ["#db6430", "#46729F", "#C678DD", "#98C379"]

# Create figure and axes with transparent background
fig, ax = plt.subplots(figsize=(6, 6), facecolor="none")
ax.set_facecolor("none")  # Transparent Axes background

# Plot the pie chart
wedges, text_labels, pct_texts = ax.pie(
    tokens,
    colors=colors,
    startangle=140,
    # Move labels slightly away from the center to reduce overlap
    labeldistance=1.1,
    # Show % inside slices
    autopct="%1.1f%%",
    pctdistance=0.7,
    wedgeprops={"edgecolor": "white"},  # White edge lines
)

# Update label text and color
for i, txt in enumerate(text_labels):
    txt.set_text(custom_labels[i])
    # Use a neutral gray so text shows up on both dark & light backgrounds
    txt.set_color("#999")

# Update the color of the percentage text inside slices
for pct in pct_texts:
    pct.set_color("white")  # or a different color if you prefer

# Ensure the pie is a circle
ax.axis("equal")

# Tight layout to reduce clipping
plt.tight_layout()

# Save the figure with a transparent background
plt.savefig(tkn_config.get("token_breakdown_file"), transparent=True, dpi=300)

with open(final_file.get("file_path"), "r") as f:
    final_token_count = count_token(f.read())

shields_data = {
    "schemaVersion": 1,
    "label": "llms-full.txt token length",
    "message": str(format_k(final_token_count)),
    "color": "blue",
}

with open(tkn_config.get("readme_shields_file"), "w") as json_file:
    json.dump(shields_data, json_file, indent=4)
