# End_to_End

## workflows -- Ml Pipeline
1. Data Ingestion
2. Data validation
3. Data Transformation
4. Model Training
5. Model Evalution


## workflows
1. update config.yaml  
   - Stores static project settings like file paths, directory locations, and general setup configurations.

2. update schema.yaml  
   - Defines the expected structure and data types for your datasets, ensuring data quality and consistency.Related to data validation ex: schema of new test data for input in model

3. update params.yaml  
   - Holds tunable parameters and hyperparameters for data processing, feature engineering, and machine learning models.

4. update the entity   
   - Defines data structures/blueprints (e.g., using dataclasses) for configurations or data objects that flow through your pipeline. Ensures type safety, clarity, and consistency.

5. update the configuration manager in src config   
   - A class that reads YAML config files (config.yaml, params.yaml, schema.yaml), instantiates type-safe entity objects (from src/entity/config_entity.py), and provides centralized access to all project settings for pipeline components.

6. update the components
   -Contains individual, modular, and reusable units of work for specific tasks within the pipeline (e.g., a DataIngestion class, a ModelTrainer class). Each component performs a distinct operation.
   
7. update the pipeline
   -Defines the sequence of interconnected stages (e.g., data ingestion, validation, training, evaluation) that form your end-to-end data science workflow. It brings together various components.

8. update the main.py 
   -The entry point of your application. It orchestrates the execution of your data science pipeline, often by calling methods from the pipeline module.  

