import json
import uuid
from typing import List, Dict, Union

# Defaults
DATA_FOLDER = "./fluxplore_server/data"  #
SERIES_DATA_FILE = f"{DATA_FOLDER}/series_data.jsonl"
TEST_IMPLEMENTATION_FILE = f"{DATA_FOLDER}/test_implementation.jsonl"
TEST_SERIES_CONFIG = f"{DATA_FOLDER}/test_config.json"


class Classification:
    def __init__(
            self,
            test_type: List[str],
            test_methods: List[str],
            abilities_tested: List[str],
            areas_tested: List[str],
            series_description: str
    ):

        self.test_type = test_type
        self.test_methods = test_methods
        self.abilities_tested = abilities_tested
        self.areas_tested = areas_tested
        self.series_description = series_description

    def to_dict(self):
        return {
            "test_type": self.test_type,
            "test_methods": self.test_methods,
            "abilities_tested": self.abilities_tested,
            "areas_tested": self.areas_tested,
            "series_description": self.series_description,
        }

    @staticmethod
    def from_dict(data: Dict):
        return Classification(
            test_type=data.get("test_type", []),
            test_methods=data.get("test_methods", []),
            abilities_tested=data.get("abilities_tested", []),
            areas_tested=data.get("areas_tested", []),
            series_description=data.get("series_description", ''),
        )


class TestProvisionStrategy:
    def __init__(
            self,
            general_instructions: List[str],
            tester_action: List[str],
            subject_action: List[str] = None,
            subject_2_action: List[str] = None
    ):
        self.general_instructions = general_instructions
        self.tester_action = tester_action

        if subject_action:
            subject_action = []
        self.subject_action = subject_action

        if subject_2_action:
            subject_2_action = []
        self.subject_2_action = subject_2_action

    def to_dict(self):
        return {
            "general_instructions": self.general_instructions,
            "tester_action": self.tester_action,
            "subject_action": self.subject_action,
            "subject_2_action": self.subject_2_action
            # Include other fields if necessary
        }

    @staticmethod
    def from_dict(data: Dict):
        if data:
            res = TestProvisionStrategy(
                general_instructions=data.get("general_instructions", []),
                tester_action=data.get("tester_action", []),
                subject_action=data.get("subject_action", []),
                subject_2_action=data.get("subject_2_action", [])
                # Include other fields if necessary
            )
        else:
            res = TestProvisionStrategy.create_default()
        return res

    @staticmethod
    def create_default():
        return TestProvisionStrategy(
            general_instructions=[],
            tester_action=[],
            subject_action=[],
            subject_2_action=[]
        )


class Model:
    def __init__(
        self,
        version: str,
        description: str,
        classification: Classification,
        test_creation_instructions: List[str],
        test_provision_strategy: Union[TestProvisionStrategy, Dict],
        result_requirements: Dict,
        model_parameters: Dict = None,
    ):
        self.version = version
        self.description = description
        self.classification = classification
        self.test_creation_instructions = test_creation_instructions
        if type(test_provision_strategy) is dict:
            test_provision_strategy = TestProvisionStrategy(**test_provision_strategy)
        self.test_provision_strategy = test_provision_strategy
        self.result_requirements = result_requirements

        if model_parameters:
            model_parameters = {}
        self.model_parameters = model_parameters

    def to_dict(self):
        classification_dict = self.classification.to_dict() \
            if isinstance(self.classification, Classification) \
            else self.classification
        test_provision_strategy_dict = self.test_provision_strategy.to_dict() \
            if isinstance(self.test_provision_strategy, TestProvisionStrategy) \
            else self.test_provision_strategy
        return {
            "version": self.version,
            "description": self.description,
            "classification": classification_dict,  # Assuming Classification has a to_dict method
            "test_creation_instructions": self.test_creation_instructions,
            "test_provision_strategy": test_provision_strategy_dict,  # Assuming TestProvisionStrategy has a to_dict method
            "result_requirements": self.result_requirements,
            "model_parameters": self.model_parameters,
        }

    @staticmethod
    def from_dict(data):
        classification = Classification.from_dict(data["classification"])  # Assuming Classification has a from_dict method
        test_provision_strategy = TestProvisionStrategy.from_dict(getattr(data, "test_provision_strategy", False))  # Assuming TestProvisionStrategy has a from_dict method
        return Model(
            version=data["version"],
            description=data["description"],
            classification=classification,
            test_creation_instructions=data["test_creation_instructions"],
            test_provision_strategy=test_provision_strategy,
            result_requirements=data["result_requirements"],
            model_parameters=data["model_parameters"],
        )


class TestImplementation:
    def __init__(
        self,
        implementation_id: str = None,
        test_desc: str = "",
        test_date: str = "",
        tester_ai_version: str = "",
        subject_ai_version: str = "",
        subject_2_ai_version: str = "",
        obtained_biases: str = "",
        tester_runtime_parameters: str = "",
        subject_runtime_parameters: str = "",
        result: str = "",
        # TODO Extend log structure to store Q-A of each actor
        test_log: List[str] = None,
    ):
        self.implementation_id = implementation_id if implementation_id else str(uuid.uuid4())
        self.test_desc = test_desc
        self.test_date = test_date
        self.tester_ai_version = tester_ai_version
        self.subject_ai_version = subject_ai_version
        self.subject_2_ai_version = subject_2_ai_version
        self.tester_runtime_parameters = tester_runtime_parameters
        self.subject_runtime_parameters = subject_runtime_parameters
        self.result = result
        self.obtained_biases = obtained_biases

        if test_log:
            test_log = []
        self.test_log = test_log

    def to_dict(self):
        return {
            "implementation_id": self.implementation_id,
            "test_desc": self.test_desc,
            "test_date": self.test_date,
            # ... include all other relevant fields
        }

    @staticmethod
    def from_dict(data: Dict):
        return TestImplementation(
            implementation_id=data.get("implementation_id", ""),
            test_desc=data.get("test_desc", ""),
            test_date=data.get("test_date", ""),
            # ... include all other relevant fields
        )

    @staticmethod
    def create_default():
        return TestImplementation(
            implementation_id=str(uuid.uuid4()),
            # Default values for other attributes
        )

    def save(self, file_name=TEST_IMPLEMENTATION_FILE):
        # TODO: Try to make files workflow binary(for decrease system encode types)
        with open(file_name, "a") as file:
            json_record = json.dumps(self, default=lambda o: o.__dict__)
            file.write(json_record + "\n")

    @staticmethod
    def load(file_name=TEST_IMPLEMENTATION_FILE):
        # TODO: Try to make files workflow binary(for decrease system encode types)
        with open(file_name, "r") as file:
            return [json.loads(line) for line in file]


class TestSeries:
    def __init__(
            self,
            series_id: str,
            model: Union[Model, Dict],
            test_implementations: List[TestImplementation]
    ):
        self.series_id = series_id
        self.model = model
        self.test_implementations = test_implementations

    @staticmethod
    def create_default():
        return TestSeries(
            series_id=str(uuid.uuid4()),
            model={},  # Default empty list or predefined model
            test_implementations=[TestImplementation.create_default()],
        )

    def save(self, file_name=SERIES_DATA_FILE):
        # TODO: Try to make files workflow binary(for decrease system encode types)
        with open(file_name, "a") as file:
            json_record = json.dumps(self, default=lambda o: o.__dict__)
            file.write(json_record + "\n")

    def add_implementation(self, implementation: TestImplementation = None):
        if implementation is None:
            implementation = TestImplementation.create_default()
        self.test_implementations.append(implementation)
        self.save()  # Save the updated TestSeries

    def get_implementation_by_id(self, imp_id: str):
        return next((imp for imp in self.test_implementations if imp.implementation_id == imp_id), None)

    @staticmethod
    def load(file_name=SERIES_DATA_FILE):
        loaded_data = []
        with open(file_name, "r") as file:
            for line in file:
                data_dict = json.loads(line)
                test_data = TestSeries(
                    series_id=data_dict["series_id"],
                    model=Model(**data_dict["model"]),
                    test_implementations=[TestImplementation(**impl) for impl in data_dict["test_implementations"]],
                )
                loaded_data.append(test_data)
        return loaded_data

    def to_dict(self):
        return {
            "series_id": self.series_id,
            "model": self.model.to_dict(),  # Ensure Model has a to_dict method
            "test_implementations": [ti.to_dict() for ti in self.test_implementations],  # Ensure TestImplementation has a to_dict method
        }

    @staticmethod
    def from_dict(data: Dict):
        model = Model.from_dict(data["model"])
        test_implementations = [TestImplementation.from_dict(ti) for ti in data["test_implementations"]]

        return TestSeries(
            series_id=data["series_id"],
            model=model,
            test_implementations=test_implementations
        )


class TestSeriesList:
    def __init__(self):
        # Load JSON configuration
        # TODO: Try to make files workflow binary(for decrease system encode types)
        with open(TEST_SERIES_CONFIG, "r") as file:
            config = json.load(file)
        self.config = config
        self.series_list = []

    def load(self, file_name=SERIES_DATA_FILE):
        with open(file_name, "r") as file:
            self.series_list = [
                TestSeries(
                    series_id=data_dict["series_id"],
                    model=Model(**data_dict["model"]),
                    test_implementations=[TestImplementation(**impl) for impl in data_dict["test_implementations"]],
                )
                for data_dict in [json.loads(line) for line in file]
            ]

    def save(self, file_name=SERIES_DATA_FILE):
        with open(file_name, "w") as file:
            for series in self.series_list:
                json_record = json.dumps(series, default=lambda o: o.__dict__)
                file.write(json_record + "\n")

    def add_series(self, series: TestSeries):
        self.series_list.append(series)
        self.save()

    def update_series(self, index, series: TestSeries):
        if index < len(self.series_list):
            self.series_list[index] = series
        self.save()

    def get_series_by_id(self, series_id: str):
        return next((series for series in self.series_list if series.series_id == series_id), None)

    def add_implementation_to_series(self, series_id: str, implementation: TestImplementation) -> str:
        """
        Add implementation to selected series

        Args:
            series_id (str): ID of selected series
            implementation (TestImplementation): default values for implementation

        Returns:
            str: new implementation id
        """
        series = self.get_series_by_id(series_id)
        res = None
        if series:
            series.add_implementation(implementation)
            self.save()
            res = series.test_implementations[-1].implementation_id
        return res


""" 
default_test_series = TestSeries.create_default()
default_test_series.save() 
"""

""" 
# Create or load TestSeriesList
series_list = TestSeriesList()
series_list.load() 
"""

# Add a new TestSeries
""" 
new_series = TestSeries.create_default()
series_list.add_series(new_series) 
"""

""" 
# Add a new TestImplementation to a specific TestSeries by ID
series_id = "87e9c719-2633-4daa-ab49-0bd9c9ff6a04"
new_implementation = TestImplementation.create_default()
series_list.add_implementation_to_series(series_id, new_implementation)

# You can also retrieve a specific series by ID
specific_series = series_list.get_series_by_id(series_id) 
"""
