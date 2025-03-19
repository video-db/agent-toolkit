import argparse
import requests
from bs4 import BeautifulSoup
import json
import sys

# Constants
DEFAULT_URL = "https://docs.videodb.io"
HTML_PARSER = "html.parser"
DEFAULT_SELECTOR = "data-coda-ui-id"
DEFAULT_SELECTOR_VALUE = (
    "page-list"  # Default attribute value to locate the parent element
)


def find_a_tags_with_depth(parent_tag, depth=0):
    """
    Recursively find all <a> tags within a parent tag and track their depth level.
    """
    results = []
    for child in parent_tag.find_all(recursive=False):  # Iterate over direct children
        if child.name == "a":
            results.append((child, depth))  # Store <a> tag with its depth
        results.extend(find_a_tags_with_depth(child, depth + 1))  # Recurse deeper
    return results


def list_to_nested_json(data):
    """
    Convert a list of tuples (element, depth) into a nested JSON-like structure,
    where items with the smallest depth are at the top level and items of the same
    depth become siblings.

    Parameters:
        data (list of tuple): Each tuple is (element, depth)

    Returns:
        list: A list of nested dictionaries representing the JSON structure.
    """
    result = []
    stack = []

    for element, depth in data:
        node = {
            "element": element.get_text(strip=True),
            "href": element.get("href"),
            "children": [],
        }

        # Adjust the stack to match the current depth
        while stack and stack[-1][1] >= depth:
            stack.pop()

        if stack:
            parent_node, _ = stack[-1]
            parent_node["children"].append(node)
        else:
            result.append(node)

        stack.append((node, depth))

    return result


def fetch_and_parse(url):
    """
    Fetch the webpage content from the given URL and parse it with BeautifulSoup.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, HTML_PARSER)
    else:
        raise Exception(
            f"Failed to fetch the webpage. Status code: {response.status_code}"
        )


def scrape_and_save(
    output_file,
    url=DEFAULT_URL,
    selector=DEFAULT_SELECTOR,
    selector_value=DEFAULT_SELECTOR_VALUE,
):
    """
    Scrape the webpage, convert <a> tags into a nested JSON structure, and save it to a file.

    Parameters:
        output_file (str): Path to the output JSON file.
        url (str): URL of the docs page to scrape.
        selector (str): HTML attribute name to locate the parent element.
        selector_value (str): Value for the attribute selector.
    """
    soup = fetch_and_parse(url)
    parent_tag = soup.find(attrs={selector: selector_value})

    if not parent_tag:
        raise Exception(f"Element with {selector}='{selector_value}' not found.")

    a_tags_with_levels = find_a_tags_with_depth(parent_tag)
    nested_json = list_to_nested_json(a_tags_with_levels)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(nested_json, f, indent=4)


def main():
    parser = argparse.ArgumentParser(
        description="Scrape a webpage, convert <a> tags into a nested JSON structure, and save it to a file."
    )
    parser.add_argument("output", help="Path to the output JSON file")
    parser.add_argument(
        "--url", default=DEFAULT_URL, help="URL of the docs page (default: %(default)s)"
    )
    parser.add_argument(
        "--selector",
        default=DEFAULT_SELECTOR,
        help="Attribute selector to locate the parent element (default: %(default)s)",
    )
    parser.add_argument(
        "--selector-value",
        default=DEFAULT_SELECTOR_VALUE,
        help="Value for the attribute selector (default: %(default)s)",
    )
    args = parser.parse_args()

    try:
        scrape_and_save(
            args.output,
            url=args.url,
            selector=args.selector,
            selector_value=args.selector_value,
        )
    except Exception as e:
        sys.exit(str(e))


if __name__ == "__main__":
    main()
