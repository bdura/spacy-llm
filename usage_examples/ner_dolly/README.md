# Using open-source Dolly models hosted on Huggingface

This example shows how you can use the [open-source Dolly
models](https://github.com/databrickslabs/dolly) hosted on Huggingface in a
Named Entity Recognition (NER) task. We demonstrate how you can use large
language models in zero- or few-shot annotation settings. 

You can run the pipeline on a sample text via:

```sh
python run_ner_dolly_pipeline.py [TEXT] [PATH TO CONFIG]
```

For example:

```sh
python run_ner_dolly_pipeline.py \
    "Matthew and Maria went to Japan to visit the Nintendo headquarters" \
    ./dolly_ner_zeroshot.cfg
```

By default, the pipeline assigns `PERSON`, `ORGANIZATION` or `LOCATION` labels
for each entity. You can change these labels by updating the
`dolly_ner_zeroshot.cfg` configuration file.

You can also include examples to perform few-shot annotation. To do so, use the
`dolly_ner_fewshot.cfg` file instead. You can find the few-shot examples in the
`ner_examples.yml` file. Feel free to change and update it to your liking.
We also support other file formats, including `json` and `jsonl`.

Finally, you can update the Dolly model in the configuration file. We're using
[`dolly-v2-3b`](https://huggingface.co/databricks/dolly-v2-3b) by default, but
you can change it to a larger model size like
[`dolly-v2-7b`](https://huggingface.co/databricks/dolly-v2-7b) or
[`dolly-v2-12b`](https://huggingface.co/databricks/dolly-v2-12b).