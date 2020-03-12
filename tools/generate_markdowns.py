import yaml

from pathlib import Path
from typing import Union, Dict, List, Tuple

doc_path = Path('docs')


def get_pages(nav: Union[List, Dict]) -> List[Tuple[str, str]]:
    ret = list()
    if type(nav) is list:
        for item in nav:
            ret.extend(get_pages(item))
    elif type(nav) is dict:
        for key, value in nav.items():
            if type(value) is str:
                ret.append((key, value))
            else:
                ret.extend(get_pages(value))
    return ret


def print_page(page: Tuple[str, str]):
    title = page[0]
    file_path = Path('docs') / page[1]
    if not file_path.exists():
        print(title, ', ', file_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open(mode='w') as f:
            f.write('# %s\n' % title)
            f.write('\n')
            f.write('## WIP\n')


if __name__ == '__main__':
    with open('mkdocs.yml') as f:
        mkdocs_config = yaml.safe_load(f)
        # print(mkdocs_config['nav'])
    pages = get_pages(mkdocs_config['nav'])
    for page in pages:
        print_page(page)
