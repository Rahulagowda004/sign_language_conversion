from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataCreation:
    root_dir: Path
    local_data_file: Path
    number_of_classes: int
    
@dataclass(frozen=True)
class DataPickle:
    root_dir: Path
    data_raw: Path
    data_pickle: Path
    
@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    dataset_path: Path
    n_estimators: int