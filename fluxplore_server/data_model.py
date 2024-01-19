import json
import uuid
from typing import List, Dict

# Defaults
DATA_FOLDER = "./fluxplore_server/data"
SERIES_DATA_FILE = f"{DATA_FOLDER}/series_data.jsonl"
TEST_IMPLEMENTATION_FILE = f"{DATA_FOLDER}/test_implementation.jsonl"

# Load JSON configuration
with open(f"{DATA_FOLDER}/test_config.json", "r") as file:
    config = json.load(file)


class Classification:
    def __init__(self, test_type: List[str], test_methods: List[str], abilities_tested: List[str], areas_tested: List[str]):
        self.test_type = test_type
        self.test_methods = test_methods
        self.abilities_tested = abilities_tested
        self.areas_tested = areas_tested


class TestProvisionStrategy:
    def __init__(self, general_instructions: List[str], tester_action: List[str], subject_action: List[str]):
        self.general_instructions = general_instructions
        self.tester_action = tester_action
        self.subject_action = subject_action

    @staticmethod
    def create_default():
        return TestProvisionStrategy(general_instructions=[], tester_action=[], subject_action=[])


class Model:
    def __init__(
        self,
        version: str,
        description: str,
        classification: Classification,
        test_creation_instructions: List[str],
        test_provision_strategy: TestProvisionStrategy,
        result_requirements: Dict,
    ):
        self.version = version
        self.description = description
        self.classification = classification
        self.test_creation_instructions = test_creation_instructions
        self.test_provision_strategy = test_provision_strategy
        self.result_requirements = result_requirements


class TestImplementation:
    def __init__(
        self,
        implementation_id: str = None,
        test_series: str = "",
        test_date: str = "",
        tester_ai_version: str = "",
        subject_ai_version: str = "",
        obtained_biases: str = "",
        tester_runtime_parameters: str = "",
        subject_runtime_parameters: str = "",
        result: str = "",
        test_log: str = "",
    ):
        self.implementation_id = implementation_id if implementation_id else str(uuid.uuid4())
        self.implementation_id = implementation_id
        self.test_series = test_series
        self.test_date = test_date
        self.tester_ai_version = tester_ai_version
        self.subject_ai_version = subject_ai_version
        self.obtained_biases = obtained_biases
        self.tester_runtime_parameters = tester_runtime_parameters
        self.subject_runtime_parameters = subject_runtime_parameters
        self.result = result
        self.test_log = test_log

    @staticmethod
    def create_default():
        return TestImplementation(
            implementation_id=str(uuid.uuid4()),
            # Default values for other attributes
        )

    def save(self, file_name=TEST_IMPLEMENTATION_FILE):
        with open(file_name, "a") as file:
            json_record = json.dumps(self, default=lambda o: o.__dict__)
            file.write(json_record + "\n")

    @staticmethod
    def load(file_name=TEST_IMPLEMENTATION_FILE):
        with open(file_name, "r") as file:
            return [json.loads(line) for line in file]


class TestSeries:
    def __init__(self, series_id: str, models: List[Model], test_provision_strategy: TestProvisionStrategy, test_implementations: List[TestImplementation]):
        self.series_id = series_id
        self.models = models
        self.test_provision_strategy = test_provision_strategy
        self.test_implementations = test_implementations

    @staticmethod
    def create_default():
        return TestSeries(
            series_id=str(uuid.uuid4()),
            models=[],  # Default empty list or predefined models
            test_provision_strategy=TestProvisionStrategy.create_default(),
            test_implementations=[TestImplementation.create_default()],
        )

    def add_implementation(self, implementation: TestImplementation = None):
        if implementation is None:
            implementation = TestImplementation.create_default()
        self.test_implementations.append(implementation)
        self.save()  # Save the updated TestSeries

    def save(self, file_name=SERIES_DATA_FILE):
        with open(file_name, "a") as file:
            json_record = json.dumps(self, default=lambda o: o.__dict__)
            file.write(json_record + "\n")

    @staticmethod
    def load(file_name=SERIES_DATA_FILE):
        loaded_data = []
        with open(file_name, "r") as file:
            for line in file:
                data_dict = json.loads(line)
                test_data = TestSeries(
                    series_id=data_dict["series_id"],
                    models=[Model(**model) for model in data_dict["models"]],
                    test_provision_strategy=TestProvisionStrategy(**data_dict["test_provision_strategy"]),
                    test_implementations=[TestImplementation(**impl) for impl in data_dict["test_implementations"]],
                )
                loaded_data.append(test_data)
        return loaded_data


class TestSeriesList:
    def __init__(self):
        self.series_list = []

    def load(self, file_name=SERIES_DATA_FILE):
        with open(file_name, "r") as file:
            self.series_list = [
                TestSeries(
                    series_id=data_dict["series_id"],
                    models=[Model(**model) for model in data_dict["models"]],
                    test_provision_strategy=TestProvisionStrategy(**data_dict["test_provision_strategy"]),
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

    def get_series_by_id(self, series_id: str):
        return next((series for series in self.series_list if series.series_id == series_id), None)

    def add_implementation_to_series(self, series_id: str, implementation: TestImplementation):
        series = self.get_series_by_id(series_id)
        if series:
            series.add_implementation(implementation)
            self.save()


""" default_test_series = TestSeries.create_default()
default_test_series.save() """

# Create or load TestSeriesList
series_list = TestSeriesList()
series_list.load()

# Add a new TestSeries
""" new_series = TestSeries.create_default()
series_list.add_series(new_series) """

# Add a new TestImplementation to a specific TestSeries by ID
series_id = "87e9c719-2633-4daa-ab49-0bd9c9ff6a04"
new_implementation = TestImplementation.create_default()
series_list.add_implementation_to_series(series_id, new_implementation)

# You can also retrieve a specific series by ID
specific_series = series_list.get_series_by_id(series_id)
