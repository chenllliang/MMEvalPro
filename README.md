<h1 align="center">MMEvalPro</h1>

<p align="center">

<a href="https://mmevalpro.github.io/">
<img alt="Static Badge" src="https://img.shields.io/badge/Homepage-MMEvalPro-blue">
</a>

<a href="">
<img alt="Static Badge" src="https://img.shields.io/badge/ArXiv-2407.xxxxx-red">

<a href="https://huggingface.co/datasets/MM-Diagnose/MMEvalPro">
<img alt="Static Badge" src="https://img.shields.io/badge/HuggingFace Dataset-MMEvalPro-yellow">
</a>

</p>



We create **MMEvalPro** for more accurate and efficent evaluation for Large Multimodal Models. It is designed to avoid Type-I errors through a **trilogy** evaluation pipeline and more rigorous metrics. For each original question from existing benchmarks, human annotators augment it by creating one **perception** question and one **knowledge** anchor question through a meticulous annotation process. It comprises **2,138** question triplets, totaling **6,414** distinct questions.

## Trilogy Evaluation

For each original question from ScienceQA, MathVista, or MMMU, MMEvalPro annotates an additional perception question and a knowledge question. Only if a multimodal model can simultaneously answer all three questions, we regard it demonstrates a true understanding of the problem rather than merely exploiting shortcuts. We introduce a new metric called **Genuine Accuracy** to evaluate the performance of models in MMEvalPro.

<div align=center>
<img src="./assets/examples.png"/>
Trilogy Evaluation Examples in MMEvalPro
</div>



## Automatic Evaluation

🔔 To automatically evaluate a model on the dataset and compute the genuine accuracy, average accuracy and different analysis metric, we provide an example code to compute the scores given model output and groundtruth labels.

First, download the dataset from <a href="https://huggingface.co/datasets/MM-Diagnose/MMEvalPro">
<img alt="Static Badge" src="https://img.shields.io/badge/HuggingFace Dataset-MMEvalPro-yellow">
</a>.

The output for **all questions** should be saved in json file, following `./demo_model_output.json`
```json
[
    {
        "index": 0,
        "model_output": "A",
        "answer": "B",
        "triplet_id": 1,
        "eval_type": "Origin"
    },
    {
        "index": 1,
        "model_output": "A",
        "answer": "B",
        "triplet_id": 1,
        "eval_type": "Perception"
    },
    {
        "index": 2,
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
    --model_output  ./demo_model_output.json \  # model output file in json format
    --output_path  ./demo_score.json \  # path to save the result
```

The overall score file looks like below:

```json
{
    "MMMU": {
        "genuine_accuracy_score": 17.11,
        "average_score": 52.7,
        "origin_score": 45.13,
        "perception_score": 62.24,
        "knowledge_score": 50.74
    },
    "MathVista": {
        "genuine_accuracy_score": 15.37,
        "average_score": 51.67,
        "origin_score": 55.93,
        "perception_score": 50.37,
        "knowledge_score": 48.7
    },
    "ScienceQA": {
        "genuine_accuracy_score": 44.96,
        "average_score": 74.61,
        "origin_score": 80.54,
        "perception_score": 72.2,
        "knowledge_score": 71.09
    },
    "Macro_Average": {
        "genuine_accuracy_score": 25.81,
        "average_score": 59.66,
        "origin_score": 60.53,
        "perception_score": 61.6,
        "knowledge_score": 56.84
    },
    "Micro_Average": {
        "genuine_accuracy_score": 33.07,
        "average_score": 65.34,
        "origin_score": 68.71,
        "perception_score": 65.11,
        "knowledge_score": 62.21
    }
}
```

## Leaderboard
<div align=center>
<img src="./assets/results.png"/>
All LLMs perform poorly in the benchmark due to the rigorous metric. Best performing LMM (Qwen-VL-Max, GPT4-o) still lag behind human by 30% in average Genuine Accuracy of MMEvalPro. 
</div>


## Acknowledgements

We thank the creators of ScienceQA, MathVista and MMMU for providing the excellent evaluation resources!

## License

The new contributions to our dataset are distributed under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license, including

The copyright of the images and the original questions belongs to the authors of MMMU, ScienceQA and MathVista

- **Purpose:** The dataset was primarily designed for use as a test set. 
- **Commercial Use:** The dataset can be used commercially as a test set, but using it as a training set is prohibited. By accessing or using this dataset, you acknowledge and agree to abide by these terms in conjunction with the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

## Citation

Coming Soon~
