import json
import argparse
import numpy as np
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('--model_output', type=str, default='./demo_model_output.json')
parser.add_argument("--output_path", type=str, default="./demo_score.json")

args = parser.parse_args()

def cal_score(model_outputs):
    triplets = defaultdict(list)
    for item in model_outputs:
        triplets[item['triplet_id']].append(item)

    # Genuine Accuracy
    correct_triplets = 0
    total_triplets = len(triplets)
    for _, entries in triplets.items():
        if all(entry['answer'] == entry['model_output'] for entry in entries):
            correct_triplets += 1
    genuine_accuracy_score = correct_triplets / total_triplets

    # Average accuracy
    average_score = sum([output['answer'] == output['model_output'] for output in model_outputs]) / len(model_outputs)

    # Origin accuracy
    o_score = sum([output['answer'] == output['model_output'] for output in model_outputs \
        if output['eval_type'] == 'Origin']) / len([output for output in model_outputs if output['eval_type'] == 'Origin'])

    # Perception accuracy
    p_score = sum([output['answer'] == output['model_output'] for output in model_outputs \
        if output['eval_type'] == 'Perception']) / len([output for output in model_outputs if output['eval_type'] == 'Perception'])

    # Knowledge accuracy
    k_score = sum([output['answer'] == output['model_output'] for output in model_outputs \
        if output['eval_type'] == 'Knowledge']) / len([output for output in model_outputs if output['eval_type'] == 'Knowledge'])

    scores = {
        "genuine_accuracy_score": round(genuine_accuracy_score * 100, 2), 
        "average_score": round(average_score * 100, 2),
        "origin_score": round(o_score * 100, 2),
        "perception_score": round(p_score * 100, 2),
        "knowledge_score": round(k_score * 100, 2)
    }
    return scores


if __name__ == '__main__':
    model_outputs = json.load(open(args.model_output, 'r'))
    data = {}
    for source in ["MMMU", "MathVista", "ScienceQA"]:
        data[source] = cal_score([output for output in model_outputs if output["source"] == source])
    data['Macro_Average'] = {
        k: round(
            np.mean([
                data[source][k] for source in ["MMMU", "MathVista", "ScienceQA"]
            ]),
            2
        ) for k in data["MMMU"]
    }
    data["Micro_Average"] = cal_score(model_outputs)

    json.dump(obj=data, fp=open(args.output_path, 'w'), indent=4)