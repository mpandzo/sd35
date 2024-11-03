# https://github.com/huggingface/diffusers/tree/main/examples/text_to_image

export MODEL_NAME="stabilityai/stable-diffusion-3.5-medium"
export OUTPUT_DIR="/sddata/sd35-tattoo-lora"
export HUB_MODEL_ID="sd35-tattoo-lora"
export DATASET_NAME="Drozdik/tattoo_v0"

accelerate launch --mixed_precision="fp16"  train_text_to_image_lora.py \
  --pretrained_model_name_or_path=$MODEL_NAME \
  --dataset_name=$DATASET_NAME \
  --dataloader_num_workers=8 \
  --resolution=512 --center_crop --random_flip \
  --train_batch_size=1 \
  --gradient_accumulation_steps=4 \
  --max_train_steps=15000 \
  --learning_rate=1e-04 \
  --max_grad_norm=1 \
  --lr_scheduler="cosine" --lr_warmup_steps=0 \
  --output_dir=${OUTPUT_DIR} \
  --push_to_hub \
  --hub_model_id=${HUB_MODEL_ID} \
  --report_to=wandb \
  --checkpointing_steps=500 \
  --validation_prompt="Totoro" \
  --seed=1337