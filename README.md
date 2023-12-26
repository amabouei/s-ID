# s-ID: Causal Effect Identification in a Sub-Population
This repository implements the s-ID algorithm in "s-ID: Causal Effect Identification in a Sub-Population."

## Abstract
 Causal inference in a sub-population involves identifying the causal effect of an intervention on a specific subgroup, which is distinguished from the whole population through the influence of systematic biases in the sampling process.
    However, ignoring the subtleties introduced by sub-populations can either lead to erroneous inference or limit the applicability of existing methods. We introduce and advocate for a causal inference problem in sub-populations (henceforth called s-ID), in which we merely have access to observational data of the targeted sub-population (as opposed to the entire population). Existing inference problems in sub-populations operate on the premise that the given data distributions originate from the entire population, thus, cannot tackle the s-ID problem. To address this gap, we provide necessary and sufficient conditions that must hold in the causal graph for a causal effect in a sub-population to be identifiable from the observational distribution of that sub-population. Given these conditions, we present a sound and complete algorithm for the s-ID problem.

## Contents
* ```main.py```: This file consists of the main algorithm and utils for working with graphs.

* ```examples.py```: This file includes some examples in the paper.

* ```requirements.txt```: Requirements packages for running the code.



## Install

For installing the dependencies, run the following code
```sh
pip install -r requirements.txt
```
## How to use the algorithm

* First, you need to create a dag using the function ```create_dag```.
* Then, call ```s-ID``` to identify your desired causal effect.



**Cite
If you find this code useful in your research, please consider citing:

```
@misc{abouei2023sid,
      title={s-ID: Causal Effect Identification in a Sub-Population}, 
      author={Amir Mohammad Abouei and Ehsan Mokhtarian and Negar Kiyavash},
      year={2023},
      eprint={2309.02281},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```


Contact
Please get in touch with amir.abouei@epfl.ch in case you have questions regarding the code.
