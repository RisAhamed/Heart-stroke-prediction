# Heart-stroke-prediction

# project Folder Structure 
```bash
root/
└── heart_stroke/
    ├── cloud_storage/
    │   ├── __init__.py
    │   └── aws_storage.py
    ├── components/
    │   ├── __init__.py
    │   ├── data_ingestion.py
    │   ├── data_transformation.py
    │   ├── data_validation.py
    │   ├── model_evaluation.py
    │   ├── model_pusher.py
    │   └── model_trainer.py
    ├── configuration/
    │   ├── __init__.py
    │   ├── aws_connection.py
    │   └── mongo_db_connection.py
    ├── constant/
    │   ├── __init__.py
    │   ├── training_pipeline/
    │   │   └── __init__.py
    │   ├── application.py
    │   ├── database.py
    │   ├── env_variables.py
    │   └── s3_bucket.py
    ├── data_access/
    │   ├── __init__.py
    │   └── heart_stroke_data.py
    ├── entity/
    │   ├── __init__.py
    │   ├── artifact_entity.py
    │   ├── config_entity.py
    │   ├── estimator.py
    │   └── s3_estimator.py
    ├── exception/
    │   └── __init__.py
    ├── logger/
    │   └── __init__.py
    ├── pipeline/
    │   ├── __init__.py
    │   ├── train_pipeline.py
    │   └── prediction_pipline.py
    └── utils/
        ├── __init__.py
        └── main_utils.py
```