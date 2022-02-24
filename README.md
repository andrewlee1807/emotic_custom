# emotic_custom

Emotion Recognition base on context

# Requirements

#### Python  3.8

```
torch==1.10.2
tensorboardX==2.4.1
scipy==1.8.0
scikit-learn==1.0.2
scikit-image==0.19.2
matplotlib==3.5.1
opencv-python==4.5.5.62
```

More detauil, please see _requirements.yml_ (This environment was build from windowsOS)

## Dataset

Download the [Emotic dataset](https://drive.google.com/open?id=0B7sjGeF4f3FYQUVlZ3ZOai1ieEU) and
[annotations](https://1drv.ms/u/s!AkYHbdGNmIVCgbYJxp1EtUplH6BhSw?e=VUP26u) and prepare the directory following the below
structure:

```
.
├── data
│   ├── Annotations
│   ├── emotic
│   ├── emotic_pre
│   └── inference.txt
├── emotic_dataset.py
├── emotic.py
├── inference.py
├── loss.py
├── main.py
├── mat2py.py
├── prepare_models.py
├── README.md
├── test.py
└── train.py
```

# Run experiments

1. To convert annotations from mat object to csv files and preprocess the data:

```
python mat2py.py --data_dir data --generate_npy
```

2. To train the model:

```
python main.py --mode train --data_path data/emotic_pre --experiment_path proj/debug_exp
```

3. To test the model:

```
python main.py --mode test --data_path data/emotic_pre --experiment_path proj/debug_exp
```

# Performance

We trained on 4 different scenarios: <br>

- ResNet-18 used in entire space extraction module, ResNet-18 used in body feature extraction module, denoted by Rl;
- ResNet-50 is used in the entire space extraction module, ResNet-18 is used in the body feature extraction module,
  denoted by R2;
- ResNet-18 is used in the entire space extraction module, ResNet-50 is used in the body feature extraction module,
  denoted by R3;
- ResNet-50 is used in the entire space extraction module, ResNet-50 is used in the body feature extraction module,
  denoted by R4.
- Efficientnet B4 is used in the entire space extraction module, Efficientnet B5 is used in the body feature extraction
  module, (B4 and B5 were pre-trained on ImageNet) denoted by R5. (last committed)

**_Note:_** The backbone models can modify the ```prepare_models.py```

While discrete categories are compared using AP per category (the higher, the better), the continuous dimensions use
AAE (the lower, the better), the results are shown in Table 1 and Table 2.

* Table 1:

| Category        | R1    | R2    | R3    | R4    | R5    |
|-----------------|-------|-------|-------|-------|-------|
| Affection       | 0.15  | 0.18  | 0.16  | 0.2   | 0.2   |
| Anger           | 0.05  | 0.07  | 0.05  | 0.04  | 0.04  |
| Annoyance       | 0.09  | 0.09  | 0.09  | 0.07  | 0.07  |
| Anticipation    | 0.5   | 0.52  | 0.52  | 0.51  | 0.51  |
| Aversion        | 0.04  | 0.05  | 0.05  | 0.05  | 0.05  |
| Confidence      | 0.57  | 0.64  | 0.64  | 0.63  | 0.63  |
| Disapproval     | 0.08  | 0.08  | 0.09  | 0.07  | 0.07  |
| Disconnection   | 0.18  | 0.19  | 0.2   | 0.2   | 0.2   |
| Disquietment    | 0.13  | 0.13  | 0.14  | 0.12  | 0.12  |
| Doubt/Confusion | 0.17  | 0.17  | 0.18  | 0.16  | 0.16  |
| Embarrassment   | 0.03  | 0.03  | 0.03  | 0.03  | 0.03  |
| Engagement      | 0.74  | 0.77  | 0.76  | 0.76  | 0.76  |
| Esteem          | 0.14  | 0.12  | 0.12  | 0.12  | 0.12  |
| Excitement      | 0.54  | 0.56  | 0.56  | 0.54  | 0.54  |
| Fatigue         | 0.07  | 0.07  | 0.07  | 0.07  | 0.07  |
| Fear            | 0.05  | 0.04  | 0.05  | 0.04  | 0.04  |
| Happiness       | 0.53  | 0.55  | 0.55  | 0.57  | 0.57  |
| Pain            | 0.04  | 0.03  | 0.03  | 0.03  | 0.03  |
| Peace           | 0.14  | 0.15  | 0.15  | 0.15  | 0.15  |
| Pleasure        | 0.29  | 0.31  | 0.32  | 0.33  | 0.33  |
| Sadness         | 0.11  | 0.09  | 0.11  | 0.09  | 0.09  |
| Sensitivity     | 0.05  | 0.04  | 0.04  | 0.04  | 0.04  |
| Suffering       | 0.07  | 0.07  | 0.08  | 0.05  | 0.05  |
| Surprise        | 0.07  | 0.07  | 0.08  | 0.06  | 0.06  |
| Sympathy        | 0.09  | 0.09  | 0.09  | 0.1   | 0.1   |
| Yearning        | 0.07  | 0.08  | 0.08  | 0.08  | 0.08  |
| mAP             | 0.191 | 0.199 | 0.202 | 0.196 | 0.196 |

* Table 2:

| Continuous Dimensions | R1   | R2   | R3   | R4   | R5   |
|-----------------------|------|------|------|------|------|
| Valence               | 0.96 | 0.95 | 1.02 | 0.94 | 0.94 |
| Arousal               | 1.15 | 1.08 | 1.11 | 1.08 | 1.07 |
| Dominance             | 1.02 | 1.01 | 1.03 | 1.03 | 1.03 |
| Mean                  | 1.04 | 1.02 | 1.05 | 1.02 | 1.01 |

Last experiment was
running: ```python main.py --gpu 0 --mode train --data_path data/emotic_pre --experiment_path proj/debug_exp_effici4-5 --epochs 50 --body_model resnet50 --context_model resnet50 --batch_size 28```
(Because of Models is huge, so batch_size is just 28 to adapt with environment.)


# References

[EMOTIC](https://github.com/Tandon-A/emotic)





