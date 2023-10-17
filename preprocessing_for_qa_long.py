from argparse import ArgumentParser
import json


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--context_dir", default="ntuadl2023hw1/context.json", type=str)
    parser.add_argument("--data_dir", default="ntuadl2023hw1/valid.json", type=str)
    parser.add_argument(
        "--output_dir", default="ntuadl2023hw1/valid_qa_long.json", type=str
    )

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()

    with open(args.data_dir, 'r') as json_file:
        data_list = json.load(json_file)
    with open(args.context_dir, 'r') as json_file:
        context_list = json.load(json_file)

    ans = []
    for data in data_list:
        relevant = [data["paragraphs"].index(data["relevant"])]
        length = 0
        for index in range(relevant[0]):
            length += len(context_list[data["paragraphs"][index]])
        data["answers"] = {
            "answer_start": [length + [data["answer"]["start"]][0]],
            "text": [data["answer"]["text"]],
        }
        data["context"] = (
            context_list[data["paragraphs"][0]]
            + context_list[data["paragraphs"][1]]
            + context_list[data["paragraphs"][2]]
            + context_list[data["paragraphs"][3]]
        )
        data.pop("paragraphs")
        data.pop("relevant")
        data.pop("answer")
        ans.append(data)

    data_json = {"data": ans}
    json.dump(data_json, open(args.output_dir, "w"), indent=2, ensure_ascii=False)
