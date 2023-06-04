class Classification {
    testType: string;
    testMethods: string[];
    abilitiesTested: string[];
    areasTested: string[];
}

class TestProvisionStrategy {
    generalInstructions: string[];
    testerAction: string[];
    subjectAction: string[];
}

class Model {
    version: string;
    description: string;
    classification: Classification;
    testCreationInstructions: string[];
    testProvisionStrategy: TestProvisionStrategy;
    resultRequirements: {};
}

class TestImplementation {
    implementationId: string;
    testSeries: string;
    testDate: string;
    testerAIversion: string;
    subjectAIversion: string;
    obtainedBiases: string;
    testerRuntimeParameters: string;
    subjectRuntimeParameters: string;
    result: string;
    testLog: string;
}

class TestData {
    testId: string;
    model: Model[];
    testImplementations: TestImplementation[];
}
