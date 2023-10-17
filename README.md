## Preprocessing
Data preprocessing for direct question answering
```
python3 preprocessing_for_qa_long.py --context_dir /path/to/context.json --data_dir /path/to/data.json --output_dir /path/to/processed-data.json
```
Do the following to process the training and validation data
```
python3 preprocessing_for_qa_long.py --context_dir ntuadl2023hw1/context.json --data_dir ntuadl2023hw1/train.json --output_dir ntuadl2023hw1/train_qa_long.json
python3 preprocessing_for_qa_long.py --context_dir ntuadl2023hw1/context.json --data_dir ntuadl2023hw1/valid.json --output_dir ntuadl2023hw1/valid_qa_long.json
```

## Training
Model training for direct question-answering
```
python3 run_qa_no_trainer_long.py \
    --model_name_or_path severinsimmler/xlm-roberta-longformer-base-16384 \
    --train_file ntuadl2023hw1/train_qa_long.json \
    --validation_file ntuadl2023hw1/valid_qa_long.json \
    --max_seq_length 2048 \
    --pad_to_max_length \
    --num_train_epochs 3 \
    --per_device_train_batch_size 2 \
    --per_device_eval_batch_size 2 \
    --gradient_accumulation_steps 2 \
    --output_dir result_3
```

## Prediction
After data preprocessing and model training, simply run the following shell script
```
bash run.sh ntuadl2023hw1/context.json ntuadl2023hw1/test.json prediction.csv
```
After that, prediction.csv can be submitted to Kaggle 