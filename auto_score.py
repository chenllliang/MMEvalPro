import json
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('--model_output', type=str, default='./demo_output.json')
parser.add_argument("--output_path", type=str, default="./demo_score.json")

args = parser.parse_args()



if __name__ == '__main__':
    model_outputs = json.load(open(args.model_output, 'r'))

    triplets = defaultdict(list)
    for item in model_outputs:
        triplets[item['triplet_id']].append(item)

    # Genuine Accuracy
    correct_triplets = 0
    total_triplets = len(triplets)
    for triplet_id, entries in triplets.items():
        if all(entry['answer'] in entry['model_output'] for entry in entries):
            correct_triplets += 1
    genuine_accuracy_score = correct_triplets / total_triplets

    # Average accuracy
    average_score = sum([output['answer'] in output['model_output'] for output in model_outputs]) / len(model_outputs)

    # Origin accuracy
    o_score = sum([output['answer'] in output['model_output'] for output in model_outputs \
        if output['eval_type'] == 'Origin']) / len(model_outputs)

    # Perception accuracy
    p_score = sum([output['answer'] in output['model_output'] for output in model_outputs \
        if output['eval_type'] == 'Perception']) / len(model_outputs)

    # Knowledge accuracy
    k_score = sum([output['answer'] in output['model_output'] for output in model_outputs \
        if output['eval_type'] == 'Knowledge']) / len(model_outputs)

    data = [{"genuine_accuracy_score": round(genuine_accuracy_score * 100, 2), 
            "average_score": round(average_score * 100, 2),
            "origin_score": round(o_score * 100, 2),
            "perception_score": round(p_score * 100, 2),
            "knowledge": round(k_score * 100, 2)
            }]
    json.dump(obj=data, fp=open(args.output_path, 'w'), indent=4)