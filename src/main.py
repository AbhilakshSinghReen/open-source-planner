from tqdm import tqdm

from src.io_handler import load_inputs, write_outputs
from src.github_apis import get_repo_info

import json

def main():
    inputs = load_inputs()

    outputs = []
    for i, repo_meta in tqdm(enumerate(inputs)):
        if i < 18:
            continue
        
        print(repo_meta)
        repo_info = get_repo_info(repo_meta['endpoint'])
        repo_info = {
            **repo_meta,
            **repo_info,
        }
        print(json.dumps(repo_info, indent=4))
        outputs.append(repo_info)
        # break
    
    write_outputs(outputs)


if __name__ == "__main__":
    main()
