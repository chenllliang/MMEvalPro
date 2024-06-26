# MMEvalPro

We create **MMEvalPro** for more accurate and efficent evaluation for Large Multimodal Models. It is designed to avoid Type-I errors through a **trilogy** evaluation pipeline and more rigorous metrics. For each original question from existing benchmarks, human annotators augment it by creating one **perception** question and one **knowledge** anchor question through a meticulous annotation process. It comprises **2,068** question triplets, totaling **6,204** distinct questions.


## Automatic Evaluation

🔔 To automatically evaluate a model on the dataset and compute the genuine accuracy, average accuracy and different analysis metric, we provide an example code to compute the scores given model output and groundtruth labels.

The output for each instance should be saved in json file, in the format of
```json
[
    {
        "index": 1,
        "model_output": "A",
        "answer": "B",
        "triplet_id": 1,
        "eval_type": "Origin"
    },
    {
        "index": 2,
        "model_output": "A",
        "answer": "B",
        "triplet_id": 1,
        "eval_type": "Perception"
    },
    {
        "index": 3,
        "model_output": "A",
        "answer": "B",
        "triplet_id": 1,
        "eval_type": "Knowledge"
    }
]
```

Then you can run the `./auto_score.py` to get the scores.


```bash
python auto_score.py \ 
    --model_output  ./demo_output.json \  # model output file in json format
    --output_path  ./demo_score.json \  # path to save the result
```


## License

The new contributions to our dataset are distributed under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license, including

The copyright of the images and the questions belongs to the original authors of MMMU, ScienceQA and MathVista

- **Purpose:** The dataset was primarily designed for use as a test set. 
- **Commercial Use:** The dataset can be used commercially as a test set, but using it as a training set is prohibited. By accessing or using this dataset, you acknowledge and agree to abide by these terms in conjunction with the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
